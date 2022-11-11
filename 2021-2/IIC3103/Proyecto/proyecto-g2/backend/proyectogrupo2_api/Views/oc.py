from django.views import View
from django.http import HttpResponse
from rest_framework.views import APIView
import json
from .. import models
from .. import serializers
from django.forms.models import model_to_dict
import requests
from proyectogrupo2_api import sftp
import time
from proyectogrupo2_api.Views import utilities
from dateutil import parser
from datetime import datetime
from proyectogrupo2_api.Views.ingredients import Ingredientes
import threading


class OrdenCompraViewset(APIView):

    def post(self, request, id, pk=None):
        #return HttpResponse(status=503)
        print("--COMENZANDO A PROCESAR OC:", id, "DE OTRO GRUPO")
        oc_object = models.OrdenCompra.objects.filter(pk=id).first()
        # obtener algo por id
        # objects.all() da todo algo asi
        if oc_object == None:
            # No existe la oc en nuestra BDD -> se crea
            try:
                oc_info = utilities.get_orden_de_compra(id)
                print(oc_info)
                # SACAMOS LOS DATOS CON GET_ORDEN_DE COMPRA
                cliente = oc_info["cliente"]
                sku = oc_info["sku"]
                fechaEntrega = int(datetime.timestamp(parser.parse(oc_info["fechaEntrega"]))*1000)
                cantidad = oc_info["cantidad"]
                urlNotificacion = request.data["urlNotificacion"]
                estado = "recibida"
                precio = oc_info["precioUnitario"]
                proveedor = oc_info["proveedor"]
                new_oc = models.OrdenCompra(
                    id, cliente, sku, fechaEntrega,cantidad, urlNotificacion, estado
                )
                new_oc_serializer = serializers.OrdenCompraSerializer(data=model_to_dict(new_oc))
                new_oc_serializer.is_valid(raise_exception=True)
                new_oc.save()
                resp = json.dumps(new_oc_serializer.data)
                ## ACEPTAR O RECHAZAR
                args = (id, sku, urlNotificacion, fechaEntrega, cantidad, precio, proveedor)
                thread = threading.Thread(target=process_received_order, args=args, daemon=True)
                thread.start()
                return HttpResponse(resp,status=201, headers={"Content-Type": "application/json"})
            except:
                print("--ALGO FALLÓ")
                return HttpResponse(status=404, headers={"Content-Type": "application/json"})
        else:
            # Ya existe la oc en nuestra BDD -> no se crea denuevo
            resp = json.dumps({"mensaje": "OC ya fue recibida"})
            return HttpResponse(resp, status=400, headers={"Content-Type": "application/json"})
    
    def patch(self, request, id, pk=None):
        oc_object = models.OrdenCompra.objects.filter(pk=id).first()
        if oc_object == None:
            # No existe la oc en nuestra BDD
            return HttpResponse(status=404)
        else:
            # Existe la oc en nuestra BDD -> la actualizamos
            oc_object.estado = request.data["estado"]
            oc_object.save()
            return HttpResponse(status=204)

    def get(self, request, id, pk=None):
        oc_object = models.OrdenCompra.objects.filter(pk=id).first()
        if oc_object == None:
            # No existe la oc en nuestra BDD
            return HttpResponse(status=404)
        else:
            # Existe la oc en nuestra BDD
            oc_serializer = serializers.OrdenCompraSerializer(data=model_to_dict(oc_object))
            oc_serializer.is_valid(raise_exception=False)
            resp = json.dumps(oc_serializer.data)
            return HttpResponse(resp, headers={"Content-Type": "application/json"})



def process_received_order(_id, sku, endpoint, fecha_end, cantidad, precio, proveedor):
    # Si no es ni pepperoni, ni jamón, ni piña => rechazamos
    # Si nos piden más de 20 de algo => rechazamos
    if cantidad > 20 or str(sku) not in ["60", "90", "100"]:
        reject_received_order(_id, endpoint)
    else:
        if can_received_order_be_done(sku, cantidad, fecha_end):
            # SE NOTIFICA ACEPTACION
            accept_received_order(_id, endpoint)

            """ Ingredientes.move_and_despachar_received_order(cantidad, proveedor, _id, precio, sku)
            # THREAD
            # MOVEMOS LOS PRODUCTOS A DESPACHO
            time.sleep(5)
            end_order(_id) """
 
        else:
            reject_received_order(_id, endpoint)

def end_order(_id):
    # Ver si el estado de la OC cambió a finalizada
    print("--FINALIZANDO OC",_id)
    oc_info = utilities.get_orden_de_compra(_id)
    if oc_info["estado"] == "finalizada":
        print("--OC",_id,"FINALIZADA")
        # Si cambió a finalizada, actualizar esto en nuestra BDD
        oc_object = models.OrdenCompra.objects.filter(pk=_id).first()
        oc_object.estado = "finalizada"
        oc_object.save()
     
def reject_received_order(_id, endpoint):
    print("--SE RECHAZO LA OC",_id, "DEBIDO A QUE PIDIERON MUCHA CANTIDAD O UN SKU QUE NO ENTREGAMOS")
    sftp.rechazar_o_aceptar_orden(_id, "rechazar")
    oc_object = models.OrdenCompra.objects.filter(pk=_id).first()
    oc_object.estado = "rechazada"
    oc_object.save()
    if endpoint != "":
        headers = {'Content-type': 'application/json'}
        data = {"estado":"rechazada"}
        req = requests.patch(endpoint, data=json.dumps(data), headers=headers)
        return req
    return

def accept_received_order(_id, endpoint):
    print("--SE ACEPTÓ LA OC",_id)
    sftp.rechazar_o_aceptar_orden(_id, "aceptar")
    oc_object = models.OrdenCompra.objects.filter(pk=_id).first()
    oc_object.estado = "aceptada"
    oc_object.save()
    if endpoint != "":
        headers = {'Content-type': 'application/json'}
        data = {"estado":"aceptada"}
        req = requests.patch(endpoint, data=json.dumps(data), headers=headers)
        return req
    return

def can_received_order_be_done(sku, cant, fecha_end):
    # CHECKEAR SI TENEMOS LA CANTIDAD DE PRODUCTO
    # Y QUE LA FECHA NO ES MUY ENCIMA
    ratio = 0.2    # % minimo que debe haber de un sku
    alpha = (ratio*4278)/134
    fecha_end = int(fecha_end/1000) # Pasar de milisegundos a segundos
    now = int(time.time()) # en segundos
    time_left = fecha_end - now
    max_time = 60*10 # que tengamos 10 minutos para hacerla

    skus = utilities.obtener_skus_in_almacen("general")
    cantidad_sku_in_storage = 0
    for sku_aux in skus:
        if sku_aux["_id"] == sku:
            cantidad_sku_in_storage = sku_aux["total"]

    if time_left > max_time and cant <= 20:
        if str(sku) == "60": # pepperoni
            if cantidad_sku_in_storage >= alpha*40:
                return True
            else:
                return False
        elif str(sku) == "90": # jamon
            if cantidad_sku_in_storage >= alpha*20:
                return True
            else:
                return False
        elif str(sku) == "100": # piña
            if cantidad_sku_in_storage >= alpha*20:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

class OrdenesCompraGeneralViewset(View):
    def get(self, request, format=None):
        #Retorna todas las ordenes de compra en la bdd
        ocs = models.OrdenCompra.objects.all()
        conteo = { "recibidas": 0, "aceptadas": 0, "rechazadas": 0, "finalizadas": 0}
        db_out = []
        for oc in ocs:
            status = oc.estado
            if status == "recibida":
                conteo["recibidas"] += 1
            elif status == "rechazada":
                conteo["rechazadas"] += 1
            elif status == "aceptada":
                conteo["aceptadas"] += 1
            elif status == "finalizada":
                conteo["finalizadas"] += 1

            db_out.append({
                "oc_id": oc.id,
                "sku": oc.sku,
                "cantidad": oc.cantidad,
                "estado": oc.estado
            })
        resp = {"estadisticas": conteo, "ordenes": db_out}
        return HttpResponse(json.dumps(resp), status=200,headers={'Content-type': 'application/json'})

""" 
GROUPS_SKU_DICT = {} # CREAR ESTE DICT CON LOS SKU: [GROUPS_URL]

def send_order(sku_to_get, cant):
    # QUEREMOS PEDIR INGREDIENTES A OTRO GRUPO
    # SKU_TO_GET: SKU DESEADO
    # CANTIDAD: CANTIDAD DESEADA (NO PUEDE SER MAYOR A 20)
    
    a_group_has_it = False
    # no especifica headers pero porsiacaso
    headers = {'Content-type': 'application/json'}
    # body vacio, quiza no sea necesario esto
    data = {} 
    margen = 3 # Tienen que tener 3 veces la cantidad solicitada
    for url_group in GROUPS_SKU_DICT[sku_to_get]:
        url_stock = url_group +  "/stocks"
        req = requests.get(url_stock, data=json.dumps(data), headers=headers)
        if req.status_code != 200:
            # GRUPOS NO TIENEN SERVICIO CONSULTA DE STOCK
            continue

        req = json.loads(req.content)
        total = 0
        for item in req:
            sku = item["sku"]
            if sku_to_get == sku:
                total = item["total"]
                break
        if total < cant*margen:
            continue
        a_group_has_it = True
        url_of_group = url_group
        break
            # el grupo no lo tiene

    if not a_group_has_it:
        return False # VER COMO MANEJAR ESTO
    else:
        # CREAR ORDEN
        proveedor_id = from_url_get_id(url_of_group) # CREAR ESTO CON DICT O FUNC
        our_id = "NOSECUALESNUESTRAID" # OBTENER
        url_notificacion = "www.example/ordenes-compra/" 
        oc_info = utilities.crear_orden_de_compra(our_id, proveedor_id, sku_to_get, cant, url_notificacion)
        data = {
            "cliente": oc_info["cliente"],
            "sku":int(oc_info["sku"]),
            "fechaEntrega": oc_info["fechaEntrega"],
            "cantidad": oc_info["cantidad"],
            "urlNotificacion": oc_info["urlNotificacion"]
        }
        req = requests.post(url_group, data=json.dumps(data), headers=headers)

        if req.status_code == 201:
            # SIGNIFICA Q FUNCIONO
            id = oc_info["id"]
            cliente = oc_info["cliente"]
            sku = oc_info["sku"]
            fechaEntrega = oc_info["fechaEntrega"]
            cantidad = oc_info["cantidad"]
            urlNotificacion = oc_info["urlNotificacion"]
            estado = "recibida"

            new_oc = models.OrdenCompra(
                id, cliente, sku, fechaEntrega,
                cantidad, urlNotificacion, estado
            )
            new_oc_serializer = serializers.OrdenCompraSerializer(data=model_to_dict(new_oc))
            new_oc_serializer.is_valid(raise_exception=True)
            new_oc.save()

            return True
    return False




def from_url_get_id(url):
    pass
 """


