from rest_framework.response import Response
import requests
from rest_framework import viewsets
from rest_framework.decorators import action
from ..hmac_sha1 import hmac_sha1_64
from django.views import View
from django.http import HttpResponse
from .utilities import get_almacenes, get_orden_de_compra, get_almacenes_aux
import json
from .ingredients import SKU_INGREDIENT_DICT
from proyectogrupo2_api.sftp import load_db
from proyectogrupo2.settings import env

DEV_O_PROD = env("DEV_O_PROD") # Puede ser "dev" o "prod"

ingredientes = SKU_INGREDIENT_DICT
skus = ingredientes.keys()

class StocksViewset(View):
    #/skusWithStock?almacenId=id
    def get(self, request, format=None):
        almacenes = get_almacenes()
        resp_aux = dict.fromkeys(skus, 0)
        for almacen in almacenes:
            almacen_id = almacen['_id']
            #print("Almacen",almacen_id)
            url = 'https://'
            if DEV_O_PROD == "dev":
                url += "dev."
            url += 'api-bodega.2021-2.tallerdeintegracion.cl/bodega/'
            url += 'skusWithStock?almacenId=' + str(almacen_id)
            auth = 'INTEGRACION grupo2:' + hmac_sha1_64('GET'+str(almacen_id))
            headers = {'Content-type': 'application/json', 'Authorization': auth}
            sku_total = requests.get(url, headers=headers)
            sku_total = json.loads(sku_total.content)
            for sku in sku_total:
                resp_aux[sku['_id']] += sku['total']
                #print("    SKU:",sku['_id'],"CANTIDAD:",sku["total"])
        resp = [{'sku': a, 'total': b} for a, b in list(resp_aux.items())]

        return HttpResponse(json.dumps(resp), status=200,headers={'Content-type': 'application/json'})


class AlmacenesListViewset(View):
    #/skusWithStock?almacenId=id
    def get(self, request, format=None):
        almacenes = get_almacenes_aux()
        resp_aux = list()
        for almacen in almacenes:
            almacen_id = almacen['_id']
            almacen_usedSpace = almacen['usedSpace']
            almacen_totalSpace= almacen['totalSpace']
            if almacen["recepcion"] == True:
                almacen_name = 'recepcion'
            elif almacen["despacho"] == True:
                almacen_name = 'despacho'
            elif almacen["pulmon"] == True:
                almacen_name = 'pulmon'
            elif almacen["cocina"] == True:
                almacen_name = 'cocina'
            else:
                almacen_name = 'general' 
            url = 'https://'
            if DEV_O_PROD == "dev":
                url += "dev."
            url += 'api-bodega.2021-2.tallerdeintegracion.cl/bodega/'
            url += 'skusWithStock?almacenId=' + str(almacen_id)
            auth = 'INTEGRACION grupo2:' + hmac_sha1_64('GET'+str(almacen_id))
            headers = {'Content-type': 'application/json', 'Authorization': auth}
            sku_total = requests.get(url, headers=headers)
            almacen_stock = json.loads(sku_total.content)
            not_null = []
            for sku in almacen_stock:
                sku['name'] = ingredientes[sku['_id']]
                not_null.append(sku['_id'])
            for sku in skus:
                if sku not in not_null:
                    almacen_stock.append({'_id': sku, 'total': 0, 'name': ingredientes[sku]})
            resp_aux.append({'_id': almacen_id, 'usedSpace': almacen_usedSpace, 'totalSpace': almacen_totalSpace, 
                             'almacen_name': almacen_name, 'stock': almacen_stock})

        return HttpResponse(json.dumps(resp_aux), status=200,headers={'Content-type': 'application/json'})

class GeneralStocksViewset(View):
    def get(self, request, format=None):
        totalSpace = 0
        spaceWP = 0
        usedSpace = 0
        usedSpaceWP = 0
        almacenes = get_almacenes_aux()
        resp_aux = dict.fromkeys(skus, 0)
        for almacen in almacenes:
            if not almacen['pulmon']:
                spaceWP += almacen["totalSpace"] 
                usedSpaceWP += almacen["usedSpace"]
            almacen_id = almacen['_id']
            totalSpace += almacen["totalSpace"]  
            usedSpace += almacen["usedSpace"]
            url = 'https://'
            if DEV_O_PROD == "dev":
                url += "dev."
            url += 'api-bodega.2021-2.tallerdeintegracion.cl/bodega/'
            url += 'skusWithStock?almacenId=' + str(almacen_id)
            auth = 'INTEGRACION grupo2:' + hmac_sha1_64('GET'+str(almacen_id))
            headers = {'Content-type': 'application/json', 'Authorization': auth}
            sku_total = requests.get(url, headers=headers)
            sku_total = json.loads(sku_total.content)
            for sku in sku_total:
                resp_aux[sku['_id']] += sku['total']

        sku_list = [{'sku': a, 'stock': b, 'name': ingredientes[a]} for a, b in list(resp_aux.items())]
        resp = {'skus': sku_list, 'totalUsedSpace': usedSpace, 'totalSpace': totalSpace, 'spaceWP': spaceWP, 'usedSpaceWP': usedSpaceWP }

        return HttpResponse(json.dumps(resp), status=200,headers={'Content-type': 'application/json'})


class OcsViewset(View):
    def get(self, request, format=None):
        conteo = { "pendientes": 0, "aceptadas": 0, "rechazadas": 0, "finalizadas": 0}
        database = load_db()
        db_out = []
        for oc in database:
            status = database[oc][3]
            if status == "PENDIENTE":
                conteo["pendientes"] += 1
            elif status == "RECHAZADA":
                conteo["rechazadas"] += 1
            elif status == "ACEPTADA":
                conteo["aceptadas"] += 1
            elif status == "FINALIZADA":
                conteo["finalizadas"] += 1

            db_out.append({
                "oc_id": database[oc][0],
                "sku": database[oc][1],
                "cantidad": database[oc][2],
                "estado": database[oc][3]
            })
        resp = {"estadisticas": conteo, "ordenes": db_out}
        return HttpResponse(json.dumps(resp), status=200,headers={'Content-type': 'application/json'})

class OCDetailViewset(View):
    def get(self, request, id, pk=None):
        oc_object = get_orden_de_compra(id)
        return HttpResponse(json.dumps(oc_object), status=200,headers={'Content-type': 'application/json'})