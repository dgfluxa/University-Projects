from .utilities import *
from dateutil import parser
from datetime import datetime
import time
from proyectogrupo2_api import sftp
from .QueueLock import QLock
from proyectogrupo2.settings import env

DEV_O_PROD = env("DEV_O_PROD") # Puede ser "dev" o "prod"

if DEV_O_PROD == "dev":
    PROOVEDOR_DIRECCION_DICT = {
        "6167730b4909ec0004ed32b2":	"6167752d51533a0004922312",
        "6167730b4909ec0004ed32b3":	"6167752d51533a0004922317",
        "6167730b4909ec0004ed32b4":	"6167752d51533a000492231c",
        "6167730b4909ec0004ed32b5":	"6167752d51533a0004922321",
        "6167730b4909ec0004ed32b6":	"6167752d51533a0004922326",
        "6167730b4909ec0004ed32b7":	"6167752d51533a000492232b",
        "6167730b4909ec0004ed32b8":	"6167752d51533a0004922330",
        "6167730b4909ec0004ed32b9":	"6167752d51533a0004922335",
        "6167730b4909ec0004ed32ba":	"6167752d51533a000492233a",
        "6167730b4909ec0004ed32bb":	"6167752d51533a000492233f",
        "6167730b4909ec0004ed32bc":	"6167752d51533a0004922344",
        "6167730b4909ec0004ed32bd":	"6167752d51533a0004922349",
        "6167730b4909ec0004ed32be":	"6167752d51533a000492234e",
        "6167730b4909ec0004ed32bf":	"6167752d51533a0004922353",
        "6167730b4909ec0004ed32c0":	"6167752d51533a0004922358",
        "6167730b4909ec0004ed32c1":	"6167752d51533a000492235d"
    }
else:
    PROOVEDOR_DIRECCION_DICT = {
        "61832ff3104b2400047de07a":	"618332b7736b2300048b2180",
        "61832ff3104b2400047de07b":	"618332b7736b2300048b2185",
        "61832ff3104b2400047de07c":	"618332b7736b2300048b218a",
        "61832ff3104b2400047de07d":	"618332b7736b2300048b218f",
        "61832ff3104b2400047de07e":	"618332b7736b2300048b2194",
        "61832ff3104b2400047de07f":	"618332b7736b2300048b2199",
        "61832ff3104b2400047de080":	"618332b7736b2300048b219e",
        "61832ff3104b2400047de081":	"618332b7736b2300048b21a3",
        "61832ff3104b2400047de082":	"618332b7736b2300048b21a8",
        "61832ff3104b2400047de083":	"618332b7736b2300048b21ad",
        "61832ff3104b2400047de084":	"618332b7736b2300048b21b2",
        "61832ff3104b2400047de085":	"618332b7736b2300048b21b7",
        "61832ff3104b2400047de086":	"618332b7736b2300048b21bc",
        "61832ff3104b2400047de087":	"618332b7736b2300048b21c1",
        "61832ff3104b2400047de088":	"618332b7736b2300048b21c6",
        "61832ff3104b2400047de089":	"618332b7736b2300048b21cb"
    }

SKU_INGREDIENT_DICT = {
    "5": "harina",
    "10": "sal",
    "15": "levadura",
    "50": "queso",
    "60": "pepperoni",
    "70": "aceituna completa",
    "80": "tomate entero",
    "90": "jamon",
    "100": "piña",
    "1000": "masa familiar",
    "1001": "masa mediana",
    "1070": "aceituna laminada",
    "1080": "tomate picado",
    "1090": "champiñon deshidratado",
    "1100": "piña picada",
    "5000": "pizza pepperoni familiar",
    "5001": "pizza pepperoni mediana",
    "5005": "pizza doble pepperoni familiar",
    "5006": "pizza doble pepperoni mediana",
    "5010": "pizza aceituna familiar",
    "5011": "pizza aceituna mediana",
    "5020": "pizza hawaiana familiar",
    "5021": "pizza hawaiana mediana",
    "5030": "pizza vegana familiar",
    "5031": "pizza vegana mediana"
}

INGREDIENT_SKU_DICT = {v:k for k,v in SKU_INGREDIENT_DICT.items()}

move_lock = QLock()
despachar_lock = QLock()
kill_thread_lock = QLock()

class Ingredientes:  

    def __init__(self):
        self.stock_cocina = {k:0 for k,_ in INGREDIENT_SKU_DICT.items()}
        self.stock_general = {k:0 for k,_ in INGREDIENT_SKU_DICT.items()}
        self.stock_on_the_way = {k:0 for k,_ in INGREDIENT_SKU_DICT.items()}
        self.pending_to_cook = {k:0 for k,_ in INGREDIENT_SKU_DICT.items()}
        self.order_threads = []

    def masas_available_to_cook(self):
        # CANTIDAD DE MASAS 
        # QUE PODEMOS PEDIR A GENERAL
        # RETORNA EN CANT DE MASAS
        self.update_stock_general()
        self.update_stock_cocina()
        max_cant = int(min(self.stock_general["harina"]/3,self.stock_general["sal"]/2,self.stock_general["levadura"]/3))
        return max_cant

    def pizzas_available_to_cook(self):
        # CANTIDAD DE PIZZAS
        # QUE PODEMOS PEDIR A GENERAL
        # RETORNA EN CANT DE PIZZAS
        self.update_stock_general()
        self.update_stock_cocina()
        max_cant = int(min(self.stock_cocina["masa"],self.stock_general["queso"]/3,self.stock_general["pepperoni"]/3))
        return max_cant

    def mover_ingredientes_masa_a_cocina(self, qty,sku):
        products_harina = get_products_in_almacen_with_sku("general", 5)
        for p in products_harina:
            p["vencimiento"] = datetime.timestamp(parser.parse(p["vencimiento"]))
        products_harina.sort(key = lambda x: x['vencimiento'])

        products_sal = get_products_in_almacen_with_sku("general", 10)
        for p in products_sal:
            p["vencimiento"] = datetime.timestamp(parser.parse(p["vencimiento"]))
        products_sal.sort(key = lambda x: x['vencimiento'])

        products_levadura = get_products_in_almacen_with_sku("general", 15)
        for p in products_levadura:
            p["vencimiento"] = datetime.timestamp(parser.parse(p["vencimiento"]))
        products_levadura.sort(key = lambda x: x['vencimiento'])

        #print("PRODUCTS", len(products_harina), len(products_sal), len(products_levadura))
        if sku == "1000": 
            # FAMILIAR
            ingredients_list = [products_harina[:qty*3], products_sal[:qty*2], products_levadura[:qty*3]]
        else:
            # MEDIANA
            ingredients_list = [products_harina[:qty*2], products_sal[:qty*1], products_levadura[:qty*2]]
    
        for _list in ingredients_list: 
            for item in _list:
                prod_id = item["_id"]
                aux = move_product_to_almacen(prod_id, "cocina")
                print(aux)
                time.sleep(1)

    def cocinar_masas(self, qty, sku):
        ## MOVER MASA
        
        print("MOVIENDO INGREDIENTES MASA A COCINA")
        
        ## EMPIEZA EL LOCK DE MASAS
        # ***asumiendo que estan todos los ingredientes en general
        move_lock.acquire()
        self.mover_ingredientes_masa_a_cocina(qty,sku)
        move_lock.release()
        print("SE MOVIERON LOS INGREDIENTES DE MASA A COCINA")
        ## TERMINA EL LOCK DE MASAS
        req = fabricar_sin_pago(sku, qty)
        print("fabricar sin pago masa:",req)


        ## COCINAR MASAS
        return int((unix_to_int(req["disponible"])-unix_to_int(req["created_at"]))) + 60


    def _mover_ingredientes_masa_a_cocina(self):
        print("MOVIENDO INGREDIENTES MASA A COCINA")
        limit_masas = 3
        max_masas = min(self.masas_available_to_cook(), limit_masas)
        total_space = self.stock_cocina["harina"] + self.stock_cocina["sal"] + self.stock_cocina["levadura"]
        if max_masas and 400 > total_space:
            # ORDENAR POR FECHA MAS CERCANA A VENCIMIENTO
            products_harina = get_products_in_almacen_with_sku("general", 5)
            for p in products_harina:
                p["vencimiento"] = datetime.timestamp(parser.parse(p["vencimiento"]))
            products_harina.sort(key = lambda x: x['vencimiento'])

            products_sal = get_products_in_almacen_with_sku("general", 10)
            for p in products_sal:
                p["vencimiento"] = datetime.timestamp(parser.parse(p["vencimiento"]))
            products_sal.sort(key = lambda x: x['vencimiento'])

            products_levadura = get_products_in_almacen_with_sku("general", 15)
            for p in products_levadura:
                p["vencimiento"] = datetime.timestamp(parser.parse(p["vencimiento"]))
            products_levadura.sort(key = lambda x: x['vencimiento'])

            ingredients_list = [products_harina[:max_masas*3], products_sal[:max_masas*2], products_levadura[:max_masas*3]]
            for _list in ingredients_list: 
                for item in _list:
                    prod_id = item["_id"]
                    move_product_to_almacen(prod_id, "cocina")
                    time.sleep(1)

    def mover_ingredientes_pizza_pepperoni(self, qty, sku):
        products_pepperoni = get_products_in_almacen_with_sku("general", 60)
        for p in products_pepperoni:
            p["vencimiento"] = datetime.timestamp(parser.parse(p["vencimiento"]))
        products_pepperoni.sort(key = lambda x: x['vencimiento'])

        products_queso = get_products_in_almacen_with_sku("general", 50)
        for p in products_queso:
            p["vencimiento"] = datetime.timestamp(parser.parse(p["vencimiento"]))
        products_queso.sort(key = lambda x: x['vencimiento'])

        if sku == "5000":
            # FAM SIMPLE PEP
            ingredients_list = [products_pepperoni[:qty*3], products_queso[:qty*3]]
        elif sku== "5001":
            # MED SIMPLE PEP
            ingredients_list = [products_pepperoni[:qty*2], products_queso[:qty*2]]
        elif sku == "5005":
            # FAM DOBLE PEP
            ingredients_list = [products_pepperoni[:qty*6], products_queso[:qty*6]]
        elif sku == "5006":
            # MED DOBLE PEP
            ingredients_list = [products_pepperoni[:qty*4], products_queso[:qty*4]]

        for _list in ingredients_list: 
            for item in _list:
                prod_id = item["_id"]
                move_product_to_almacen(prod_id, "cocina")
                time.sleep(1)



    def mover_ingredientes_pizza_aceituna(self, qty, sku_masa):
        products_aceituna_completa = get_products_in_almacen_with_sku("general", 70)
        for p in products_aceituna_completa:
            p["vencimiento"] = datetime.timestamp(parser.parse(p["vencimiento"]))
        products_aceituna_completa.sort(key = lambda x: x['vencimiento'])

        products_tomate_entero = get_products_in_almacen_with_sku("general", 80)
        for p in products_tomate_entero:
            p["vencimiento"] = datetime.timestamp(parser.parse(p["vencimiento"]))
        products_tomate_entero.sort(key = lambda x: x['vencimiento'])

        products_jamon = get_products_in_almacen_with_sku("general", 90)
        for p in products_jamon:
            p["vencimiento"] = datetime.timestamp(parser.parse(p["vencimiento"]))
        products_jamon.sort(key = lambda x: x['vencimiento'])

        products_queso = get_products_in_almacen_with_sku("general", 50)
        for p in products_queso:
            p["vencimiento"] = datetime.timestamp(parser.parse(p["vencimiento"]))
        products_queso.sort(key = lambda x: x['vencimiento'])

        if sku_masa == "1000":
            # FAM
            ingredients_list = [products_jamon[:qty*3], 
                products_queso[:qty*3],
                products_aceituna_completa[:qty*6],
                products_tomate_entero[:qty]
            ]
        else:
            # MED
            ingredients_list = [products_jamon[:qty*3], 
                products_queso[:qty*2],
                products_aceituna_completa[:qty*6],
                products_tomate_entero[:qty]
            ]

        for _list in ingredients_list: 
            for item in _list:
                prod_id = item["_id"]
                move_product_to_almacen(prod_id, "cocina")
                time.sleep(1)
        ## THREAD UNLOCK


    def mover_ingredientes_pizza_hawaiana(self, qty, sku):
        products_pina = get_products_in_almacen_with_sku("general", 100)
        for p in products_pina:
            p["vencimiento"] = datetime.timestamp(parser.parse(p["vencimiento"]))
        products_pina.sort(key = lambda x: x['vencimiento'])

        products_jamon = get_products_in_almacen_with_sku("general", 90)
        for p in products_jamon:
            p["vencimiento"] = datetime.timestamp(parser.parse(p["vencimiento"]))
        products_jamon.sort(key = lambda x: x['vencimiento'])

        if sku == "5020":
            ingredients_list = [products_jamon[:qty*2], products_pina[:qty*1]]
        elif sku == "5021":
            ingredients_list = [products_jamon[:qty*1], products_pina[:qty*1]]

        for _list in ingredients_list: 
            for item in _list:
                prod_id = item["_id"]
                move_product_to_almacen(prod_id, "cocina")
                time.sleep(1)


    def can_cook_masa(self):
        self.update_stock_cocina()
        if self.stock_cocina["harina"] >=3 and self.stock_cocina["sal"] >=2 and self.stock_cocina["levadura"] >=3:
            return True
        return False

    def can_cook_pizza(self):
        self.update_stock_cocina()
        if self.stock_cocina["masa"] >=1 and self.stock_cocina["queso"] >=3 and self.stock_cocina["pepperoni"] >=3:
            return True
        return False

    def cook_pizza(self):
        print("COCINANDO PIZZA")
        if self.can_cook_pizza():
            fabricar_sin_pago(INGREDIENT_SKU_DICT["pizza"],1)

    def cook_masa(self):
        print("COCINANDO MASA")
        if self.can_cook_masa():
            fabricar_sin_pago(INGREDIENT_SKU_DICT["masa"], 1)


    def update_stock_cocina(self):
        stocks = obtener_skus_in_almacen("cocina")
        for stock in stocks:
            sku = stock["_id"]
            qty = stock["total"]
            ingrediente = SKU_INGREDIENT_DICT[sku]
            self.stock_cocina[ingrediente] = qty

    def update_stock_general(self): 
        stocks = obtener_skus_in_almacen("general")
        for stock in stocks:
            sku = stock["_id"]
            qty = stock["total"]
            ingrediente = SKU_INGREDIENT_DICT[sku]
            self.stock_general[ingrediente] = qty

    def run_job_despachar_pizza(self):
        print("DESPACHANDO PISA")
        self.update_stock_cocina()
        limit = 3
        j = 0
        if self.stock_cocina["pizza"] > 0:
            prods = get_products_in_almacen_with_sku("cocina", INGREDIENT_SKU_DICT["pizza"])
            for prod in prods:
                if j > limit:
                    break
                prod_id = prod["_id"]
                stat = move_product_to_almacen(prod_id, "despacho")
                time.sleep(1)

    def from_recepcion_to_general(self):
        # Funcion para pasar todos los productos e ingredientes desde la recepción 
        # hacia el (almacen general).
        print("MOVIENDO DE RECEPCION A GENERAL")
        sku_total = obtener_skus_in_almacen("recepcion")
        limit = 30
        j = 0
        for sku in sku_total:
            if j > limit:
                break
            all_products = get_products_in_almacen_with_sku("recepcion", sku["_id"])
            
            for product in all_products:
                if j > limit:
                    break
                prod_id = product["_id"]
                status = move_product_to_almacen(prod_id, "general")
                if self.stock_on_the_way[SKU_INGREDIENT_DICT[sku["_id"]]] > 0:
                    self.stock_on_the_way[SKU_INGREDIENT_DICT[sku["_id"]]] -= 1
                j +=1 

    def _from_x_to_y(self):
        print("MOVIENDO DE X A Y")
        sku_total = obtener_skus_in_almacen("cocina")
        print(sku_total)
        #print(sum)
        _dict = {}
        for sku in sku_total:
            all_products = get_products_in_almacen_with_sku("cocina", sku["_id"])
            #print("ALL PRODUCTS", all_products)

            for product in all_products:
                prod_id = product["_id"]
                print("MOVIENDO SKU:", sku["_id"])
                status = move_product_to_almacen(prod_id, "general")
                print("   ",status)
                time.sleep(1)



    def order_ingredients_from_factory(self):
        self.update_stock_general()
        ratio = 0.87          # % A USAR DE CAP TOTAL
        alpha = (ratio*4278)/134
        # Harina
        if (self.stock_general["harina"] + self.stock_on_the_way["harina"]) < alpha*15:
            print("Pidiendo Harina")
            fabricar_sin_pago("5", 20)
            self.stock_on_the_way["harina"] += 20
        # Sal
        if (self.stock_general["sal"] + self.stock_on_the_way["sal"]) < alpha*9:
            print("Pidiendo Sal")
            fabricar_sin_pago("10", 24)
            self.stock_on_the_way["sal"] += 24
        # Levadura
        if (self.stock_general["levadura"] + self.stock_on_the_way["levadura"]) < alpha*15:
            print("Pidiendo Levadura")
            req = fabricar_sin_pago("15", 21)
            self.stock_on_the_way["levadura"] += 21
        # Queso
        if (self.stock_general["queso"] + self.stock_on_the_way["queso"]) < alpha*15:
            print("Pidiendo Queso")
            fabricar_sin_pago("50", 24)
            self.stock_on_the_way["queso"] += 24
        # Pepperoni
        if (self.stock_general["pepperoni"] + self.stock_on_the_way["pepperoni"]) < alpha*40:
            print("Pidiendo Pepperoni")
            fabricar_sin_pago("60", 24)
            self.stock_on_the_way["pepperoni"] += 24
        # Aceituna completa -> NUESTRO GRUPO NO PUEDE FABRICAR ESTO EN LA ENTREGA 3
        """ if (self.stock_general["aceituna completa"] + self.stock_on_the_way["aceituna completa"]) < alpha*12:
            print("Pidiendo Aceituna completa")
            fabricar_sin_pago("70", 20)
            self.stock_on_the_way["aceituna completa"] += 20 """
        # Tomate Entero -> NUESTRO GRUPO NO PUEDE FABRICAR ESTO EN LA ENTREGA 3
        """ if (self.stock_general["tomate entero"] + self.stock_on_the_way["tomate entero"]) < alpha*2:
            print("Pidiendo Tomate entero")
            fabricar_sin_pago("80", 20)
            self.stock_on_the_way["tomate entero"] += 20 """
        # Jamon
        if (self.stock_general["jamon"] + self.stock_on_the_way["jamon"]) < alpha*20:
            print("Pidiendo Jamón")
            fabricar_sin_pago("90", 24)
            self.stock_on_the_way["jamon"] += 24
        # Piña
        if (self.stock_general["piña"] + self.stock_on_the_way["piña"]) < alpha*20:
            print("Pidiendo Piña")
            fabricar_sin_pago("100", 21)
            self.stock_on_the_way["piña"] += 21

    def print_stocks(self):
        self.update_stock_general()
        self.update_stock_cocina()
        print("STOCK GENERAL:", self.stock_general)
        print("\nSTOCK COCINA:", self.stock_cocina)
        print("\nSTOCK EN CAMINO:", self.stock_on_the_way)


    def completar_orden_de_compra(self, _id, qty, sku, file):
        
        print("EMPEZANDO ORDEN ", _id, qty, sku)
        qty = int(qty)
        ### ASUMIENDO QUE SKU SIEMPRE CORRESPONDE A PIZZAS
        tipo = int(sku)%5
        if tipo:
            sku_masa = "1001"
        else:
            sku_masa = "1000"

        time_masa = self.cocinar_masas(qty, sku_masa) 
        print("TIEMPO COCINAR MASA:", time_masa)
        if int(sku) in range(5000,5007): 
            # PIZZAS PEPPERONI
            print("MOVIENDO INGREDIENTES PIZZA PEPPERONI")
            move_lock.acquire()
            self.mover_ingredientes_pizza_pepperoni(qty, sku)
            move_lock.release()
            print("SE TERMINO DE MOVER LOS INGREDIENTES")
            max_time = time_masa + 60
            print("MAX_TIME =",max_time)

        elif int(sku) in range(5010,5012):
            # PIZZAS ACEITUNEITOR
            print("MOVIENDO INGREDIENTES PIZZA ACEITUNEITOR")
            move_lock.acquire()
            self.mover_ingredientes_pizza_aceituna(qty, sku_masa)
            move_lock.release()
            print("SE TERMINO DE MOVER LOS INGREDIENTES")
            print("LAMINANDO ACEITUNAS")
            req = fabricar_sin_pago("1070",qty*2)
            print(req)
            time_1 = int((unix_to_int(req["disponible"])-unix_to_int(req["created_at"]))) + 60
            print("PICANDO TOMATE")
            req = fabricar_sin_pago("1080",qty)
            time_2 = int((unix_to_int(req["disponible"])-unix_to_int(req["created_at"]))) + 60
            max_time = max(time_masa, time_1, time_2)
            print("MAX_TIME =",max_time)

        elif sku == "5020" or sku == "5021":
            # PIZZAS HAWAI
            print("MOVIENDO INGREDIENTES PIZZA HAWAIANA")
            move_lock.acquire()
            self.mover_ingredientes_pizza_hawaiana(qty, sku)
            move_lock.release()
            print("SE TERMINO DE MOVER LOS INGREDIENTES")
            print("PICANDO PIÑA")
            req = fabricar_sin_pago("1100",qty)
            print(req)
            time_1 = int((unix_to_int(req["disponible"])-unix_to_int(req["created_at"]))) + 60
            max_time = max(time_masa, time_1)
            print("MAX_TIME =",max_time)
            
        time.sleep(max_time)
        
        print("FABRICAR PIZZA")
        req = fabricar_sin_pago(sku,qty)

        if "disponible" in req:
            print(req)
            time_pizza = int((unix_to_int(req["disponible"])-unix_to_int(req["created_at"]))) + 60
            print("TIEMPO EN FABRICAR PIZZA:", time_pizza )
            time.sleep(time_pizza)

            ### SEGUIR CON DESPACHO
            despachar_lock.acquire()
            self.mover_a_despacho_y_despachar(_id,sku,qty)
            despachar_lock.release()
        else:
            print("Error al fabricar pizza. Anulando.")
            print(req)
            sftp.anular_orden(_id)
            """ error_fabric = json.loads(requests.get("http://127.0.0.1:8000/almacenes").content)
            for almacen in error_fabric:
                if almacen["almacen_name"] == "cocina":
                    for sku_total in almacen["stock"]:
                        print("SKU:", sku_total["_id"], "| TOTAL:",sku_total["total"]) """

        ## ELIMINAR THREAD
        print("ELIMINANDO THREAD")
        print("Threads antes:",self.order_threads)
        sftp.change_to_finalizada(file)
        kill_thread_lock.acquire()
        print("pre delete thread")
        self.delete_thread(_id)
        print("Threads después:",self.order_threads)
        kill_thread_lock.release()

    
    def mover_a_despacho_y_despachar(self,_id,sku,qty):
        move_lock.acquire()
        products_pizza = get_products_in_almacen_with_sku("cocina", int(sku))

        for p in products_pizza:
            p["vencimiento"] = datetime.timestamp(parser.parse(p["vencimiento"]))
        products_pizza.sort(key = lambda x: x['vencimiento'])
        print("products pizza:", products_pizza)
        print("QTY:", qty)
        print("Moviendo pizzas a despacho")
        for item in products_pizza[:qty]: 
            prod_id = item["_id"]
            req_aux = move_product_to_almacen(prod_id, "despacho")
            print("Moviendo una pizza a despacho:",req_aux)
            time.sleep(2)
            despachar_pizza(prod_id,_id)
            time.sleep(2)
        move_lock.release()

    def delete_thread(self, _id):
        print("Deleting thread")
        for i,thread in enumerate(self.order_threads):
            if thread.name == _id:
                idx = i
                break
        self.order_threads.pop(idx)
        print("Thread deleted")
        

    def handler_order_manager(self):
        print("status threads antes de entrar a manager")
        print(self.order_threads)
        sftp.order_manager(self.order_threads, self.completar_orden_de_compra, kill_thread_lock)
        print("volviendo a handler")
        print(self.order_threads)

    @staticmethod
    def move_and_despachar_received_order(cantidad, proveedor, _id, precio, sku):
        direccion = PROOVEDOR_DIRECCION_DICT[proveedor]
        print("--proveedor:",proveedor,"direccion:",direccion)
        despachar_lock.acquire()
        move_lock.acquire()
        # MOVEMOS LOS INGREDIENTES
        print("--MOVIENDO Y DESPACHANDO INGREDIENTES DE OC", _id, "Y SKU:",sku)
        products = get_products_in_almacen_with_sku("general", sku)
        for p in products:
            p["vencimiento"] = datetime.timestamp(parser.parse(p["vencimiento"]))
        products.sort(key = lambda x: x['vencimiento'])

        for prod in products[:cantidad]:
            prod_id = prod["_id"]
            move_product_to_almacen(prod_id, "despacho")
            time.sleep(1)
            despachar_producto(prod["_id"], direccion, _id, precio)
        move_lock.release()
        despachar_lock.release()

        print("--PRODUCTOS DESPACHADOS DE OC",_id)


def unix_to_int(unix):
    return datetime.timestamp(parser.parse(unix))