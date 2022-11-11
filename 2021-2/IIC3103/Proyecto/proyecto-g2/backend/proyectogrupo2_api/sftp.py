import paramiko
from bs4 import BeautifulSoup
from proyectogrupo2.settings import env
import os
import pickle
import threading
import time
import json
import requests
from proyectogrupo2_api.Views.utilities import *
from proyectogrupo2_api.Views.QueueLock import QLock

DEV_O_PROD = env("DEV_O_PROD") # Puede ser "dev" o "prod"

PORT = int(env("FTP_PORT"))
HOST = env("FTP_URL")

if DEV_O_PROD == "dev":
    USER = env('FTP_USER_DEV')
    PASSWORD = env('FTP_PASS_DEV')
else:
    USER = env('FTP_USER_PROD')
    PASSWORD = env('FTP_PASS_PROD')


MAX_THREADS = 5
DB_LOCK = QLock()
SFTP_LOCK = QLock()
# CONTADOR = 1

def rechazar_o_aceptar_orden(_id, modo):
    # Cambia el estado de una OC en la api
    url = 'https://'
    if DEV_O_PROD == "dev":
       url += "dev." 
    url += 'oc.2021-2.tallerdeintegracion.cl/oc/'
    headers = {'Content-type': 'application/json'}
    if modo == "aceptar":
        url += "recepcionar/" +_id
        data = {}
        req = requests.post(url, data=json.dumps(data),headers=headers)
    elif modo == "rechazar":
        url += "rechazar/" + _id
        data = {"rechazo": "Rechazada por tiempos de fabricacion"}
        req = requests.post(url, data=json.dumps(data), headers=headers)
    req = json.loads(req.content)
    return req

def anular_orden(_id):
    url = 'https://'
    if DEV_O_PROD == "dev":
       url += "dev." 
    url += 'oc.2021-2.tallerdeintegracion.cl/oc/'
    headers = {'Content-type': 'application/json'}
    url += "anular/" + _id
    data = {"anulacion": "anulada por tiempos de fabricacion"}
    req = requests.delete(url, data=json.dumps(data), headers=headers)
    req = json.loads(req.content)
    return req

def create_connection():
    transport = paramiko.Transport((HOST,PORT))
    transport.connect(None,USER,PASSWORD)
    sftp = paramiko.SFTPClient.from_transport(transport)
    return sftp

def close_connection():
    SFTP.close()

def parse_data(file_name):
    SFTP_LOCK.acquire()
    with SFTP.open(file_name) as file:
        data = file.read()
    SFTP_LOCK.release()

    #parse data with BS
    bs_data = BeautifulSoup(data,"xml")

    #relevent params
    order_id = bs_data.find('id')
    order_sku = bs_data.find('sku')
    order_quantity = bs_data.find('qty')

    return order_id.getText(), order_sku.getText(), order_quantity.getText()

def save_db():
    with open('ORDER_DATABASE.pickle', "wb") as f:
        pickle.dump(DATABASE, f, protocol=3)
    print("*** GUARDANDO BASE DE DATOS ***")
    

def load_db():
    with open('ORDER_DATABASE.pickle', "rb") as f:
        DATABASE = pickle.load(f)
    return DATABASE

def create_db():
    db = dict()
    SFTP_LOCK.acquire()
    ordered_orders = SFTP.listdir()
    SFTP_LOCK.release()
    ordered_orders.sort()
    for file in ordered_orders:
        if file.endswith(".xml"):
            # PROCESAR
            _id, sku, qty = parse_data(file)
            # RECHAZAR TODAS LAS ANTIGUAS O IMPOSIBLES DE HACER
            if not can_order_be_done(file,_id):
                # RECHAZAR EN LA API
                #db[file] = [_id, sku, qty, "RECHAZADA"]
                db[file] = [_id, sku, qty, "ACEPTADA"]
            else:
                # NO HACER NADA EN API
                db[file] = [_id, sku, qty, "PENDIENTE"]
                rechazar_o_aceptar_orden(_id,modo="aceptar")
    return db


def can_order_be_done(file,_id):
    # RETORNA TRUE SI SE PUEDE HACER
    ### QUIZA HARDCODEAR LAS 6 HORAS DESDE EL TIMESTAMP DEL FILENAME
    ### PERO VER SI ESO CAMBIA CON FUTURAS ENTREGAS
    timestamp = int(file.split('-')[0]) // 1000
    now = int(time.time())
    delta = now-timestamp
    max_time = 3600*2 # 2 horas
    if delta > max_time:
        #rechazar_o_aceptar_orden(_id,modo="rechazar")
        rechazar_o_aceptar_orden(_id,modo="aceptar")
        return False
    return True


def check_new_orders():
    # AGREGARA NUEVOS FILES EN FTP
    # A LA BDD
    # Y RECHAZARA O PONDRA PENDIENTE
    print("Check new orders:")
    SFTP_LOCK.acquire()
    ordered_orders = SFTP.listdir()
    SFTP_LOCK.release()
    ordered_orders.sort()

    DB_LOCK.acquire()
    for file in ordered_orders:
        if file.endswith(".xml"):
            if file in DATABASE:
                continue
            _id, sku, qty = parse_data(file)
            if not can_order_be_done(file,_id):
                DATABASE[file] = [_id, sku, qty, "ACEPTADA"]
            else:
                DATABASE[file] = [_id, sku, qty, "PENDIENTE"]
                rechazar_o_aceptar_orden(_id,modo="aceptar")
    DB_LOCK.release()
    print("\nTermino el check new orders")


def change_to_finalizada(file):
    print("Changing status to 'FINALIZADA'")
    DB_LOCK.acquire()
    DATABASE[file][3] = "FINALIZADA"
    DB_LOCK.release()
    print("Status changed to 'FINALIZADA'")



def update_old_orders():
    #####
    DB_LOCK.acquire()
    for file, info in DATABASE.items():
        _id,_,_, status = info
        if status == "ACEPTADA":
            req = get_orden_de_compra(_id)
            if req["estado"] in ["rechazada","anulada"]:
                DATABASE[file][3] = "RECHAZADA"
            elif req["estado"] in ["finalizada"]:
                DATABASE[file][3] = "FINALIZADA"
    DB_LOCK.release()




def order_manager(current_order_threads, func, lock):
    """
    VA A TENER UN LISTADO DE LOS THREADS CORRIENDO,
    SI TIENE MENOS THREADS QUE EL LIMITE MÁXIMO,
    VA A BUSCAR LA ORDEN MAS ANTIGUA QUE ESTE PENDIENTE
    CHECKEA SI ES POSIBLE REALIZARLA NUEVAMENTE
    SI SE PUEDE REALIZAR LA AGREGA AL THREAD Y ASI HASTA LLENAR EL LIMITE
    SINO LA RECHAZA
    """
    #print(current_order_threads)
    print("Entrando al ORDER MANAGER: ")
    _list = []
    lock.acquire()
    for i,thread in enumerate(current_order_threads):
        if not thread.is_alive():
            _list.append(i)
    for idx in _list:
        current_order_threads.pop(idx)
    lock.release()
        
    if len(current_order_threads) >= MAX_THREADS:
        return 
    threads_aux = []

    DB_LOCK.acquire()
    for file, info in DATABASE.items():
        _id, sku, qty, status = info
        if status == "PENDIENTE":
            _id, sku, qty = parse_data(file)
            if not can_order_be_done(file,_id):
                #DATABASE[file] = [_id, sku, qty, "RECHAZADA"]
                DATABASE[file] = [_id, sku, qty, "ACEPTADA"]
            else:
                # ACEPTAR EN API
                rechazar_o_aceptar_orden(_id,modo="aceptar")
                DATABASE[file] = [_id, sku, qty, "ACEPTADA"]
                # EMPEZAR A REALIZAR
                if str(sku) in ["5000", "5001", "5005", "5006", "5020", "5021"]:
                    thread = threading.Thread(target=func, args=(_id,qty,sku,file),name=_id, daemon=True)
                    threads_aux.append(thread)
                    
                    lock.acquire()
                    current_order_threads.append(thread)
                    lock.release()
                
                #thread.start()
                # AGREGAR A THREAD  
        if len(current_order_threads) >= MAX_THREADS:
            DB_LOCK.release()
            for thr in threads_aux:
                thr.start()
            print("Saliendo del order manager")
            return 
    DB_LOCK.release()
    for thr in threads_aux:
        thr.start()
    print("Saliendo del order manager")
    return 

SFTP = create_connection()
SFTP.chdir("pedidos")
if os.path.isfile("ORDER_DATABASE.pickle"):
    DATABASE = load_db()
else:
    DATABASE = create_db()
    save_db()


