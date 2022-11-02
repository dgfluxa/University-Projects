import requests
from regex_functions import revisar_usuario, revisar_clave
from parameters import CLIENT_ID, CLIENT_SECRET, access_key
import json
from random import randint
from excepciones import IngresoInvalido, ConsultaInvalida, Salir, ErrorBusqueda
from math import radians, sin, cos, asin, sqrt
import sys
from datetime import datetime


# Inicio de sesión
def obtener_dicc_categorias():
    url = 'https://api.foursquare.com/v2/venues/categories'
    params = dict(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        intent='browse',
        v='20180323',
    )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    lista = data["response"]["categories"]
    dicc = {}
    dicc_cat(lista, dicc)
    return dicc


def dicc_cat(lista, dicc):
    for cat in lista:
        dicc[str(cat["name"]).lower()] = cat["id"]
        dicc[str(cat["pluralName"]).lower()] = cat["id"]
        dicc[str(cat["shortName"]).lower()] = cat["id"]
        if "categories" in cat:
            dicc_cat(cat["categories"], dicc)


def inicio_sesion():
    print("Por favor ingrese su correo electrónico:")
    usuario = input()
    revisar_usuario(usuario)
    print("Por favor ingrese su contraseña:")
    clave = input()
    revisar_clave(clave)
    print()
    print(f"{'-'*34} INGRESO EXITOSO {'-'*33}")
    return


def realizar_consulta(dicc):
    while True:
        print("\n¿Deseas buscar por palabra clave(1) o por categoría(2)?")
        numero = input()
        if numero == "1":
            query = input("Ingrese una palabra clave a buscar: ")
            consulta = realizar_consulta_query(query)
            if consulta:
                return consulta
            else:
                print()
                raise ConsultaInvalida("La búsqueda no arrojó resultados")
        elif numero == "2":
            while True:
                while True:
                    print("¿Deseas ver ejemplos de categorias? Si(1), No(2) o "
                          "Ver Todas(3)")
                    num = input()
                    if num == "1":
                        lista_cat = list(dicc.keys())
                        print(f'''
Ejemplos de categorías: -{lista_cat[randint(0, len(dicc))]}
                        -{lista_cat[randint(0, len(dicc))]}
                        -{lista_cat[randint(0, len(dicc))]}
                        -{lista_cat[randint(0, len(dicc))]}
                        -{lista_cat[randint(0, len(dicc))]}
                       ''')
                    elif num == "3":
                        print("\nCategorías:")
                        for cat in dicc.keys():
                            print(cat)
                        print()
                        break
                    elif num == "2":
                        break
                    else:
                        print("Debes ingresar 1, 2 o 3")
                print("Ingrese el nombre de la categoría (En inglés y "
                      "separados por comas si son mas de uno)")
                lista_categorias = input().split(",")
                lista_ids = []
                for categoria in lista_categorias:
                    if categoria in dicc:
                        lista_ids.append(dicc[categoria.lower()])
                ids = ",".join(lista_ids)
                if ids:
                    return realizar_consulta_id(ids)
                else:
                    print()
                    raise ConsultaInvalida("La(s) categoria(s) ingresada(s)"
                                           " no existe(n)")
        else:
            print("Debes ingresar 1 o 2")


def realizar_consulta_query(query):
    url = 'https://api.foursquare.com/v2/venues/search'
    params = dict(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        intent='browse',
        v='20180323',
        ll='-33.4389493,-70.6323447',
        radius=17000,
        limit=50,
        query=query
    )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    return data["response"]["venues"]


def realizar_consulta_id(id_):
    url = 'https://api.foursquare.com/v2/venues/search'
    params = dict(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        intent='browse',
        v='20180323',
        ll='-33.4389493,-70.6323447',
        radius=17000,
        limit=50,
        categoryId=id_
    )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    if not data["response"]:
        print()
        raise ConsultaInvalida("No existen establecimientos de dicha categoría")
    elif not data["response"]["venues"]:
        print()
        raise ConsultaInvalida("No existen establecimientos de dicha categoría")
    else:
        return data["response"]["venues"]


def elegir_lugar(consulta):
    n = 0
    for lugar in consulta:
        n += 1
        address = f"{lugar['location']['address']}" \
                  if "address" in lugar['location'] else "Dirección desconocida"
        lista_categorias = []
        for cat in lugar["categories"]:
            lista_categorias.append(cat["name"])
        categorias = ",".join(lista_categorias)
        if categorias == "":
            categorias = "Sin categorías"
        print(f"{n}.- {lugar['name']} ({address}): {categorias}")
    while True:
        numero_lugar = input("Ingrese el número del lugar o -1 para salir: ")
        if numero_lugar == "-1":
            raise Salir
        elif numero_lugar.isnumeric():
            if 1 <= int(numero_lugar) <= (len(consulta) + 1):
                return consulta[int(numero_lugar) - 1]
            else:
                print("Debes ingresar un número válido")
        else:
            print("Debes ingresar un número válido")


def encontrar_paradero(lat, lon, limite):
    url = f'https://api.scltrans.it/v1/stops?limit={str(limite)}&' \
          f'center_lon={lon}&center_lat={lat}'
    resp = requests.get(url=url)
    data = json.loads(resp.text)
    if data["results"]:
        return data["results"]
    else:
        print()
        raise ErrorBusqueda("Paradero no encontrado")


def encontrar_paradero_cliente(lat, lon):
    paraderos = encontrar_paradero(lat, lon, 500)
    for p in paraderos:

        if haversine(float(lat), float(lon), float(p["stop_lat"]),
                     float(p["stop_lon"])) <= 10:
            yield p
    else:
        print()
        raise ErrorBusqueda("Paradero no encontrado a menos de 10km")


def seguir():
    while True:
        print("\n¿Deseas realizar otra consulta(1) o salir(-1)")
        num = input()
        if num == "1":
            return False
        elif num == "-1":
            return True
        else:
            print("\nDebes ingresar (1) o (-1)")


def obtener_ubicacion():
    url = f'http://api.ipstack.com/check?access_key={access_key}'
    resp = requests.get(url=url)
    data = json.loads(resp.text)
    return data["latitude"], data["longitude"]


# Recuperado de https://stackoverflow.com/questions/4913349/haversine-formula-in
# -python-bearing-and-distance-between-two-gps-points
def haversine(lat1, lon1, lat2, lon2):
    r = 6372.8

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return r * c


def obtener_bus(paradero1, ruta):
    url = f"https://api.scltrans.it/v2/stops/{paradero1['stop_id']}/next_arrivals"
    resp = requests.get(url=url)
    data = json.loads(resp.text)
    while True:
        if "results" in data.keys():
            buses = data["results"]
            for bus in buses:
                if bus["route_id"] == ruta["route"]["route_id"]:
                    return bus

'''
def transformar_a_datetime(fecha):  # Recuperado de T00 IIC2233, Diego Fluxá

    hora, min, seg = fecha.split(":")
    fecha_dt = datetime(hour=int(hora), minute=int(min), second=int(seg))
    return fecha_dt'''


def obtener_rutas(paradero1):
    url = f"https://api.scltrans.it/v3/stops/{paradero1['stop_id']}/stop_routes"
    resp = requests.get(url=url)
    data = json.loads(resp.text)
    return data["results"]

'''
def obtener_tiempo(ruta, paradero):
    url = f"https://api.scltrans.it/v2/routes/{ruta['route']['route_id']}" \
          f"/directions"

    while True:
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        if "results" in data:
            for stops in data["results"]:
                for stop in stops["stop_times"]:
                    if stop["stop"] == paradero["stop_id"]:
                        return stop["arrival_time"]'''


def obtener_ruta_comun(paradero1, gen_paraderos):
    lista_rutas = obtener_rutas(paradero1)
    listas_id = []
    rutas_visitadas = []
    for ruta in lista_rutas:
        if ruta["route"]["route_type"] == "3" and ruta["route"]["route_id"] not in listas_id:
            listas_id.append(ruta["route"]["route_id"])
    for paradero in gen_paraderos:
        lista2 = obtener_rutas(paradero)
        for ruta in lista2:
            if ruta["route"]["route_id"] not in rutas_visitadas:
                rutas_visitadas.append(ruta["route"]["route_id"])
                if ruta["route"]["route_id"] in listas_id:
                    return ruta, paradero
    raise ErrorBusqueda("Ruta no encontrada")


# 1 normal
# 2 prueba con coordenadas del campus san joaquin
mode = 1

if __name__ == "__main__":
    print(f"{'-'*30} Bienvenido a DCConnect {'-'*30}")

    while True:
        try:
            inicio_sesion()
            break
        except IngresoInvalido as err:
            print(err)
    if mode not in (1, 2):
        print("Mode debe ser 1 o 2")
        sys.exit()
    dicc = obtener_dicc_categorias()
    while True:
        try:
            consulta = realizar_consulta(dicc)
            lugar = elegir_lugar(consulta)
            print(f"Lugar seleccionado: {lugar['name']}")
            print("\nPor favor espere mientras procesamos la información\n")
            t1 = datetime.now()
            paradero_final = encontrar_paradero(lugar["location"]["lat"],
                                                lugar["location"]["lng"], 1)[0]
            lat_cliente, long_cliente = obtener_ubicacion()
            if mode == 1:
                paraderos_posibles = encontrar_paradero_cliente(lat_cliente,
                                                                long_cliente)
            elif mode == 2:
                paraderos_posibles = encontrar_paradero_cliente(str(-33.498526),
                                                                str(-70.615627))
            # print(paraderos_posibles)
            # print(paradero_final)
            ruta, paradero = obtener_ruta_comun(paradero_final,
                                                paraderos_posibles)
            bus = obtener_bus(paradero, ruta)
            print(f"¡Listo!, Hemos encontrado tu bus en "
                  f"{(datetime.now() - t1).total_seconds()} segundos")
            print(f'''
    Paradero inicial:{paradero["stop_name"]}
    Paradero final: {paradero_final["stop_name"]}
    Patente Bus: {bus["bus_plate_number"]}
    Tiempo de espera: {bus["arrival_estimation"]}
    Distancia de viaje: {haversine(float(paradero["stop_lat"]), 
float(paradero["stop_lon"]), float(paradero_final["stop_lat"]), 
float(paradero_final["stop_lon"]))} km
    Tiempo de viaje: ''')

        except ConsultaInvalida as err:
            print(err)
        except Salir:
            if seguir():
                print(f"\n{'-'*40} Adiós {'-'*40}\n")
                break
            else:
                pass
        except ErrorBusqueda as err:
            print(err)












