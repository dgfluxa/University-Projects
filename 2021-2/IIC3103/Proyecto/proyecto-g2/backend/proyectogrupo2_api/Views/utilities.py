from ..hmac_sha1 import hmac_sha1_64
import json
import requests
import time
import random
from proyectogrupo2.settings import env
from dateutil import parser
from datetime import datetime

DEV_O_PROD = env("DEV_O_PROD") # Puede ser "dev" o "prod"

# OBTENER ALMACENES
url_aux = 'https://'
if DEV_O_PROD == "dev":
    url_aux += "dev."
url_aux += 'api-bodega.2021-2.tallerdeintegracion.cl/bodega/almacenes'
auth_aux = 'INTEGRACION grupo2:' + hmac_sha1_64('GET')
headers = {'Content-type': 'application/json', 'Authorization': auth_aux}
almacenes_global = json.loads(requests.get(url_aux, headers=headers).content)
 
def get_almacenes():
    return(almacenes_global)

def get_almacenes_aux():
    url = 'https://'
    if DEV_O_PROD == "dev":
        url += "dev."
    url += 'api-bodega.2021-2.tallerdeintegracion.cl/bodega/almacenes'
    auth_aux_ = 'INTEGRACION grupo2:' + hmac_sha1_64('GET')
    headers_ = {'Content-type': 'application/json', 'Authorization': auth_aux_}
    return json.loads(requests.get(url, headers=headers_).content)

def get_almacen(nombre):
    # DE UN NOMBRE DE ALMACEN OBTIENE SU ID
    almacenes = get_almacenes() 
    if nombre not in {"recepcion", "despacho", "pulmon", "cocina", "general"}:
        return False
    #print(almacenes)
    for almacen in almacenes:
        if nombre == "recepcion" and almacen["recepcion"] == True:
            return almacen
        elif nombre == "despacho" and almacen["despacho"] == True:
            return almacen
        elif nombre == "pulmon" and almacen["pulmon"] == True:
            return almacen
        elif nombre == "cocina" and almacen["cocina"] == True:
            return almacen
        elif nombre == "general" and almacen["cocina"] == False and almacen["pulmon"] == False and almacen["despacho"] == False and almacen["recepcion"] == False:
            return almacen


def move_product_to_almacen(productoId, nombreAlmacen):
    # MOVER PRODUCTOS ENTRE ALMACENES
    almacenId = get_almacen(nombreAlmacen)["_id"]
    url = 'https://'
    if DEV_O_PROD == "dev":
        url += "dev."
    url += 'api-bodega.2021-2.tallerdeintegracion.cl/bodega/moveStock'
    auth = 'INTEGRACION grupo2:' + hmac_sha1_64('POST'+str(productoId) +str(almacenId))
    headers = {'Content-type': 'application/json', 'Authorization': auth}
    data = {"productoId": productoId, "almacenId":almacenId}
    req = requests.post(url, data=json.dumps(data), headers=headers)
    if req.status_code != 200:
        print("ERROR AL MOVER ENTRE ALMACENES")
        print(json.loads(req.content))
        print("productoId:",productoId,"nombreAlmacen:",nombreAlmacen)
    req = json.loads(req.content)
    # RETORNAR ALGO SEGUN EL STATUS
    return req


def obtener_skus_in_almacen(nombreAlmacen):
    ## OBTENER SKUS CON STOCK
    almacen_id = get_almacen(nombreAlmacen)["_id"]
    url = 'https://'
    if DEV_O_PROD == "dev":
        url += "dev."
    url += 'api-bodega.2021-2.tallerdeintegracion.cl/bodega/'
    url += 'skusWithStock?almacenId=' + str(almacen_id)
    auth = 'INTEGRACION grupo2:' + hmac_sha1_64('GET'+str(almacen_id))
    headers = {'Content-type': 'application/json', 'Authorization': auth}
    req = requests.get(url, headers=headers)
    req = json.loads(req.content)
    return req

def get_products_in_almacen_with_sku(nombreAlmacen, sku, limit=200):
    ### OBTENER PRODUCTOS EN ALMACEN
    almacen_id = get_almacen(nombreAlmacen)["_id"]
    url = 'https://'
    if DEV_O_PROD == "dev":
        url += "dev."
    url += 'api-bodega.2021-2.tallerdeintegracion.cl/bodega/'
    url += 'stock?almacenId=' + str(almacen_id) +"&sku="+str(sku)+"&limit="+str(limit)
    auth = 'INTEGRACION grupo2:' + hmac_sha1_64('GET'+str(almacen_id)+str(sku))
    headers = {'Content-type': 'application/json', 'Authorization': auth}
    req = requests.get(url, headers=headers)
    
    req = json.loads(req.content)
    return req


def fabricar_sin_pago(sku, cantidad):
    # FABRICAR PRODUCTOS SIN PAGO
    url = 'https://'
    if DEV_O_PROD == "dev":
        url += "dev."
    url += 'api-bodega.2021-2.tallerdeintegracion.cl/bodega/fabrica/fabricarSinPago'
    auth = 'INTEGRACION grupo2:' + hmac_sha1_64('PUT'+str(sku) +str(cantidad))
    headers = {'Content-type': 'application/json', 'Authorization': auth}
    data = {"sku": str(sku), "cantidad": int(cantidad)}
    req = requests.put(url, data=json.dumps(data), headers=headers)
    req = json.loads(req.content)
    # RETORNAR ALGO SEGUN EL STATUS
    return req


def move_product_to_bodega(productoId, almacenId, oc, precio):
    # MOVER PRODUCTOS ENTRE BODEGAS (DESPACHO A OTRO GRUPO)
    url = 'https://'
    if DEV_O_PROD == "dev":
        url += "dev."
    url += 'api-bodega.2021-2.tallerdeintegracion.cl/bodega/moveStockBodega'
    auth = 'INTEGRACION grupo2:' + hmac_sha1_64('POST'+str(productoId) +str(almacenId))
    headers = {'Content-type': 'application/json', 'Authorization': auth}
    data = {"productoId": productoId, "almacenId":almacenId,
            "oc":oc, "precio":str(precio)}
    req = requests.post(url, data=json.dumps(data), headers=headers)
    req2 = json.loads(req.content)
    # RETORNAR ALGO SEGUN EL STATUS
    return req2


def despachar_producto(productoId, direccion, oc, precio):
    # DESPACHAR PRODUCTO A DIRECCION
    url = 'https://'
    if DEV_O_PROD == "dev":
        url += "dev."
    url += 'api-bodega.2021-2.tallerdeintegracion.cl/bodega/stock'
    auth = 'INTEGRACION grupo2:' + hmac_sha1_64('DELETE'+str(productoId) +str(direccion)+str(precio)+str(oc))
    headers = {'Content-type': 'application/json', 'Authorization': auth}
    data = {"productoId": productoId,
            "oc":oc, 
            "direccion":direccion,
            "precio":precio}
    req = requests.delete(url, data=json.dumps(data), headers=headers)
    return req


def get_orden_de_compra(_id):
    url = 'https://'
    if DEV_O_PROD == "dev":
        url += "dev."
    url += 'oc.2021-2.tallerdeintegracion.cl/oc/obtener/'
    headers = {'Content-type': 'application/json'}
    url += _id
    data = {}
    req = requests.get(url, data=json.dumps(data), headers=headers)
    req = json.loads(req.content)
    return req[0]

def crear_orden_de_compra(our_id, proveedor_id, sku, cantidad, url_notificacion):
    url = 'https://'
    if DEV_O_PROD == "dev":
        url += "dev."
    url += 'oc.2021-2.tallerdeintegracion.cl/oc/crear/'
    headers = {'Content-type': 'application/json'}
    due_date = 3600*5
    precio = random.randint(10,20)
    data = {
        "cliente":our_id,
        "proveedor": proveedor_id,
        "sku": int(sku),
        "fechaEntrega": int(time.time()) + due_date, # QUIZA ESTO PASARLO A DATETIME?
        "cantidad":int(cantidad),
        "precioUnitario":precio,
        "canal":"b2b", 
        "notas":"",
        "urlNotificacion":url_notificacion # NUESTRA URL DE NOTIFICACION
    }
    req = requests.put(url, data=json.dumps(data), headers=headers)
    req = json.loads(req.content)
    return req


def despachar_pizza(prod_id, oc_id):
    # DESPACHAR PRODUCTO A DIRECCION
    oc_info = get_orden_de_compra(oc_id)
    print(oc_info)
    precio = oc_info["precioUnitario"]
    direccion = oc_info["proveedor"]
    req = despachar_producto(prod_id,direccion,oc_id,precio)
    req = json.loads(req.content)
    print("Despachando pizza")
    print(req)
    return req