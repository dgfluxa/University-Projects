from datetime import datetime
from iic2233_utils import parse, foreach
from itertools import tee
from collections import namedtuple
from typing import Union, Generator
from math import sqrt, sin, cos, asin
from operator import eq, ne, lt, gt
from os import path

Persona = namedtuple("Persona", "id_ name clase age")
Aeropuerto = namedtuple("Aeropuerto", "icao tipo lat long iso_country")
Vuelo = namedtuple("Vuelo", "id_ airport_from airport_to date")
Viaje = namedtuple("Viaje", "flight_id passenger_id")


def mostrar_menu():
    print("\nMenú Principal:\n"
          "1.- Abrir archivo con consultas\n"
          "2.- Realizar una consulta\n"
          "3.- Leer el archivo output.txt\n"
          "\n"
          "Ingrese el número de la accion a realizar:")
    accion = input()
    if accion not in ("1", "2", "3"):
        print("Input inválido, ingrese un número válido\n")
        return mostrar_menu()
    return accion


def crear_path(archivo, carpeta="small"):
    return f"data/{carpeta}/{archivo}"
# Si se desea cambiar el tamaño de la carpeta se puede realizar aquí


def leer_archivo(path):
    with open(path, "r", encoding="UTF-8") as archivo:
        archivo.readline()
        for linea in archivo:
            yield linea.strip()


def display_posibilidades(iterable):
    foreach(printear_enumerado, enumerate(iterable, 1))


def printear_enumerado(iterable_enumerado):
    print(f"{iterable_enumerado[0]}.- {iterable_enumerado[1]}")


def seleccionar_numero(iterable):
    numero = input("Ingrese el número deseado: ")
    if numero.isnumeric() is False or \
            int(numero) not in range(1, len(iterable) + 1):
        print("Input inválido, ingrese un número válido\n")
        seleccionar_numero(iterable)
    return numero


def seleccionar_multiples_numeros(iterable):
    print("Ingrese los números deseados separados por (,) ")
    lista_numeros = input().split(",")
    set_numeros = set(num for num in lista_numeros if num.isnumeric()
                      and int(num) in range(1, len(iterable) + 1))
    if len(set_numeros) is 0:
        print("No has ingresado números válidos")
        return seleccionar_multiples_numeros(iterable)
    lista_numeros_final = sorted(set_numeros)
    numeros = ", ".join(lista_numeros_final)
    print(f"Los numeros válidos que has ingresado son: {numeros}")
    return lista_numeros_final


def abrir_consulta_posibilidades(iterable):
    # Devuelve solo los ingresados correctamente
    print("\nDeseas seleccionar una consulta (1), varias (2), todas (3) "
          "o ninguna (-1)")
    accion = input("Ingrese el número de la acción deseada: ")
    if accion not in ("1", "2", "3", "-1"):
        print("Input inválido, ingrese un número válido")
        return abrir_consulta_posibilidades(iterable)
    elif accion is "1":
        return seleccionar_una_consulta(iterable)
    elif accion is "2":
        return seleccionar_varias_consultas(iterable)
    elif accion is "3":
        return seleccionar_todas_consultas(iterable)
    else:
        return []


def seleccionar_una_consulta(iterable):
    numero = seleccionar_numero(iterable)
    return [iterable[int(numero)-1]]


def seleccionar_varias_consultas(iterable):
    lista_numeros = seleccionar_multiples_numeros(iterable)
    lista_consultas = [iterable[int(num) - 1] for num in lista_numeros]
    return lista_consultas


def seleccionar_todas_consultas(iterable):
    return iterable


def crear_dicc_funciones():
    dicc_funciones = {"load_database": load_database,
                      "filter_flights": filter_flights,
                      "filter_passengers": filter_passengers,
                      "filter_passengers_by_age": filter_passengers_by_age,
                      "filter_airports_by_country": filter_airports_by_country,
                      "filter_airports_by_distance":
                          filter_airports_by_distance,
                      "favourite_airport": favourite_airport,
                      "passenger_miles": passenger_miles,
                      "popular_airports": popular_airports,
                      "airport_passengers": airport_passengers,
                      "furthest_distance": furthest_distance}
    return dicc_funciones


def entregar_argumentos(lista):
    return[revisar_argumentos(arg) for arg in lista]


def revisar_argumentos(arg):
    if type(arg) is dict:
        return traducir_consulta(arg)
    elif type(arg) is list:
        return str(arg[0])
    else:
        return str(arg)


def traducir_consulta(consulta):
    dicc_funciones = crear_dicc_funciones()
    if type(consulta) is str:
        consulta_p = parse(str(consulta))
    else:
        consulta_p = consulta
    con = [con_key for con_key in consulta_p][0]
    lista = [arg for arg in entregar_argumentos(consulta_p[con])]
    return dicc_funciones[con](*lista)


def leer_consulta(consulta):
    print(f"\n{'-'*40}\n")
    print(f"Consulta: {consulta}\n")
    gen = traducir_consulta(consulta)
    print("Resultado: ")
    foreach(print, gen)
    print()
    with open("output.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{consulta}\n")


def abrir_consulta():
    archivo = input("Ingrese el nombre del archivo a leer: ")
    if path.isfile(archivo) is False:
        print(f"No existe el archivo {archivo}")
        return
    tupla = [parse(consulta) for consulta in leer_archivo(archivo)]
    display_posibilidades(tupla)
    consulta = abrir_consulta_posibilidades(tupla)
    foreach(leer_consulta, consulta)


def ingresar_consulta():
    print("\nIngrese su consulta: ((-1) para volver al menú)")
    consulta = input()
    if consulta == "-1":
        return
    elif parse(str(consulta)) is None:
        print(f"La consulta {consulta} es inválida")
        return
    leer_consulta(consulta)


def print_output(lista):
    print(f"\n{'-'*10} Consulta N°{lista[0]} {'-'*10}")
    print(f"Consulta: {lista[1][0]}")
    print(f"Resultados: ")
    foreach(print, lista[1][1])


def crear_output(consulta):
    with open("output.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{consulta}\n")


def eliminar_consulta():
    lista = [consulta for consulta in leer_archivo("output.txt")]
    if len(lista) == 0:
        print("No es posible dado a que output.txt está vacío")
        return
    display_posibilidades(lista)
    consulta = abrir_consulta_posibilidades(lista)
    if consulta == lista:
        with open("output.txt", "w", encoding="utf-8") as archivo:
            archivo.write("Consultas:\n")
    else:
        foreach(lista.remove, consulta)
        with open("output.txt", "w", encoding="utf-8") as archivo:
            archivo.write("Consultas:\n")
        foreach(crear_output, lista)


def leer_output():
    lista = [[linea, traducir_consulta(linea)] for linea in
             leer_archivo("output.txt")]
    foreach(print_output, enumerate(lista, 1))
    print("\n¿Deseas borrar alguna consulta de output.txt?")
    accion = input("Si (1) o No (-1): ")
    if accion == "1":
        eliminar_consulta()
        return
    elif accion == "-1":
        return
    else:
        print("Debes ingresar un numero válido")
        return leer_output()


def transformar_a_datetime(fecha):  # Recuperado de Tarea00 IIC2233, Diego Fluxá
    lista = fecha.split(" ")
    lista[0] = lista[0].split("-")
    lista[1] = lista[1].split(":")
    fecha_dt = datetime(int(lista[0][0]), int(lista[0][1]), int(lista[0][2]),
                        int(lista[1][0]), int(lista[1][1]), int(lista[1][2]))
    return fecha_dt


def transformar_a_millas_nauticas(lat1, lat2, long1, long2):
    return 2*3440*asin(sqrt(sin((lat2 - lat1) / 2)**2 +
                            cos(lat1)*cos(lat2)*sin((long2 - long1) / 2)**2))


def transformar_simbolo(string):
    diccionario_operadores = {"<": lt, ">": gt, "==": eq, "!=": ne, "AND": and_,
                              "OR": or_, "XOR": xor_, "DIFF": diff_}
    return diccionario_operadores[string]


def distancia_entre_aeropuertos(generador_aeropuertos, icao_aeropt1,
                                icao_aeropt2):
    lista = [aeropuerto for aeropuerto in generador_aeropuertos if
             aeropuerto.icao == icao_aeropt1 or aeropuerto.icao == icao_aeropt2]
    return transformar_a_millas_nauticas(lista[0].lat, lista[1].lat,
                                         lista[0].long, lista[1].long)


def load_database(db_type: str) -> Generator:
    gen = leer_archivo(crear_path(f"{db_type.lower()}.csv"
                                  if db_type != "Travels"
                                  else "flights-passengers2.csv"))
    for elemento in gen:
        if db_type == "Passengers":
            id_, name, clase, age = elemento.split(",")
            yield Persona(id_, name, clase, age)
        elif db_type == "Airports":
            icao, tipo, lat, long, iso_country = elemento.split(",")
            yield Aeropuerto(icao, tipo, float(lat), float(long), iso_country)
        elif db_type == "Flights":
            id_, airport_from, airport_to, date = elemento.split(",")
            yield Vuelo(id_, airport_from, airport_to, date)
        else:
            flight_id, passenger_id = elemento.split(",")
            yield Viaje(flight_id, passenger_id)


def filter_flights(flights: Generator, airports: Generator, attr: str,
                   symbol: str, value: Union[datetime, int, float]) \
        -> Generator:
    for vuelo in flights:
        if attr == "date":
            if transformar_simbolo(symbol)(vuelo.date, value):
                yield vuelo
        else:
            airports, gen = tee(airports)
            if transformar_simbolo(symbol)(
                    float(distancia_entre_aeropuertos(gen, vuelo.airport_from,
                                                      vuelo.airport_to)),
                    float(value)):
                yield vuelo


def filter_passengers(passengers: Generator, flights: Generator,
                      travels: Generator, icao: str, start: datetime,
                      end: datetime) -> Generator:
    for flight in flights:
        if flight.airport_to == icao and \
                transformar_a_datetime(flight.date) <= \
                transformar_a_datetime(end) and \
                transformar_a_datetime(flight.date) >= \
                transformar_a_datetime(start):
            travels, travels_copia = tee(travels)
            for travel in travels_copia:
                if travel.flight_id == flight.id_:
                    passengers, passengers_copia = tee(passengers)
                    for passenger in passengers_copia:
                        if int(passenger.id_) == int(travel.passenger_id):
                            yield passenger


def filter_passengers_by_age(passengers: Generator, age: int, lower: bool=True)\
        -> Generator:
    for passenger in passengers:
        if lower is True:
            if int(passenger.age) < int(age):
                yield passenger
        else:
            if int(passenger.age) >= int(age):
                yield passenger


def filter_airports_by_country(airports: Generator, iso: str) -> Generator:
    for airport in airports:
        if airport.iso_country == iso:
            yield airport


def filter_airports_by_distance(airports: Generator, icao: str,
                                distance: float, lower: bool=False) -> \
        Generator:
    airports, airports_copia = tee(airports)
    for airport in airports_copia:
        airports, airports_copia2 = tee(airports)
        dist = distancia_entre_aeropuertos(airports_copia2, airport.icao, icao)
        if lower is False:
            if float(dist) > float(distance):
                yield airport
        else:
            if float(dist) < float(distance):
                yield airport


def gen_passenger_airport_to(flights: Generator, travels: Generator)\
        -> Generator:
    gen_travels = ((travel.passenger_id, travel.flight_id) for travel in
                   travels)
    for flight in flights:
        gen_travels, gen_travels_copia = tee(gen_travels)
        for travel in gen_travels_copia:
            if travel[1] == flight.id_:
                yield [travel[0], flight.airport_to]


def gen_dicc_passenger_airports(passengers: Generator, flights: Generator,
                                travels: Generator) -> Generator:
    gen = gen_passenger_airport_to(flights, travels)
    for passenger in passengers:
        gen, gen_copia = tee(gen)
        lista = [passenger.id_]
        for j in gen_copia:
            if j[0] == passenger.id_:
                lista.append(j[1])
        yield {lista[0]: lista[1:]}


def moda_lista(lista):
    lista_ordenada = sorted(lista, key=lista.count, reverse=True)
    return lista_ordenada[0]


def favourite_airport(passengers: Generator, flights: Generator,
                      travels: Generator) -> dict:
    gen = gen_dicc_passenger_airports(passengers, flights, travels)
    dicc = {pid: moda_lista(vuelos) for d in gen for pid in d.keys() for vuelos
            in d.values()}
    return dicc
# De haber 2 o mas aeropuertos que se hayan visitado la misma cantidad de
# veces, se retorna el cual esta relacionado al cual aparece mas arriba en el
# archivo flights-passengers2.csv


def gen_passenger_af_at(flights: Generator, travels: Generator)\
        -> Generator:
    gen_travels = ((travel.passenger_id, travel.flight_id) for travel in
                   travels)
    for flight in flights:
        gen_travels, gen_travels_copia = tee(gen_travels)
        for travel in gen_travels_copia:
            if travel[1] == flight.id_:
                yield [travel[0], [flight.airport_from, flight.airport_to]]


def gen_dicc_passenger_dist(passengers: Generator, airports: Generator,
                            flights: Generator, travels: Generator) -> \
        Generator:
    gen = gen_passenger_af_at(flights, travels)
    for passenger in passengers:
        gen, gen_copia = tee(gen)
        lista = [passenger.id_]
        for j in gen_copia:
            airports, airports_copia = tee(airports)
            if j[0] == passenger.id_:
                if len(lista) == 1:
                    lista.append(distancia_entre_aeropuertos(airports_copia,
                                                             j[1][0], j[1][1]))
                else:
                    lista[1] = lista[1] + distancia_entre_aeropuertos(
                        airports_copia, j[1][0], j[1][1])
        yield {passenger: lista[1]}


def passenger_miles(passengers: Generator,  airports: Generator,
                    flights: Generator, travels: Generator) -> dict:
    gen = gen_dicc_passenger_dist(passengers, airports, flights, travels)
    dicc = {passenger: dist for d in gen for passenger in d.keys() for dist
            in d.values()}
    return dicc


def gen_airport_passengers(airports: Generator, flights: Generator,
                           travels: Generator) -> Generator:
    gen = gen_passenger_airport_to(flights, travels)
    for airport in airports:
        gen, gen_copia = tee(gen)
        lista = [airport.icao]
        for j in gen_copia:
            if j[1] == airport.icao:
                lista.append(j[0])
        yield tuple(i for i in lista)


def gen_flight_passengers(flights: Generator, travels: Generator) -> Generator:
    gen_travels = ((travel.flight_id, travel.passenger_id) for travel in
                   travels)
    for flight in flights:
        gen_travels, gen_travels_c1 = tee(gen_travels)
        lista = [flight.airport_to]
        for tupla in gen_travels_c1:
            if tupla[0] == flight.id_:
                lista.append(tupla[1])
        yield tuple(i for i in lista)


def gen_airport_prom(airports: Generator, flights: Generator,
                     travels: Generator) -> Generator:
    gen = gen_flight_passengers(flights, travels)
    for airport in airports:
        gen, gen_copia = tee(gen)
        num_passengers = 0
        num_flights = 0
        for tupla in gen_copia:
            if tupla[0] == airport.icao:
                num_passengers += len(tupla[1:])
                num_flights += 1
        if num_flights != 0:
            yield (airport.icao, num_passengers/num_flights)
        else:
            yield (airport.icao, 0)


def gen_mayor(gen: Generator) -> Generator:
    gen, gen_copia1 = tee(gen)
    lista = []
    for i in gen_copia1:
        mayor = ""
        gen, gen_copia2 = tee(gen)
        for j in gen_copia2:
            if mayor == "" and j not in lista:
                mayor = j
            elif len(mayor) > 1:
                if mayor[1] < j[1] and j not in lista:
                    mayor = j
        lista.append(mayor)
        yield mayor[0]


def popular_airports(flights: Generator, airports: Generator,
                     travels: Generator, topn: int, avg: bool=False) -> tuple:
    if not avg:
        gen = gen_airport_passengers(airports, flights, travels)
        tupla = tuple(tup for tup in gen)
        tupla_final = tuple(l[0] for l in sorted(tupla, key=len, reverse=True))
    else:
        gen = gen_mayor(gen_airport_prom(airports, flights, travels))
        tupla_final = tuple(icao for icao in gen)
    return tupla_final[0: int(topn)]


def gen_passenger_airports(passengers: Generator, flights: Generator,
                           travels: Generator) -> Generator:
    gen = gen_passenger_af_at(flights, travels)
    for passenger in passengers:
        gen, gen_copia = tee(gen)
        lista = [passenger]
        for j in gen_copia:
            if j[0] == passenger.id_:
                lista.extend([j[1][0], j[1][1]])
        yield tuple(lista)


def and_(iterable, a, b):
    if a in iterable and b in iterable:
        return True
    else:
        return False


def or_(iterable, a, b):
    if a in iterable or b in iterable:
        return True
    else:
        return False


def xor_(iterable, a, b):
    if a in iterable or b in iterable:
        if a in iterable and b in iterable:
            return False
        else:
            return True
    else:
        return False


def diff_(iterable, a, b):
    if a in iterable and b not in iterable:
        return True
    else:
        return False


def airport_passengers(passengers: Generator, flights: Generator,
                       travels: Generator, icao1: str, icao2: str,
                       operation: str) -> set:
    gen = gen_passenger_airports(passengers, flights, travels)
    operador = transformar_simbolo(operation)

    set_passengers = set()
    for tupla in gen:
        if operador(tupla, icao1, icao2):
            set_passengers.add(tupla[0])
    return set_passengers


def revisar_agregar(lista, d):
    lista_copia = lista  # Para no modificar el input y cumplir funcional
    if len(lista) == 1:
        lista_copia.append(d)
    else:
        if d > lista[1]:
            lista_copia[1] = d
    return lista_copia


def gen_passenger_max_from_icao(passengers: Generator, airports: Generator,
                                flights: Generator, travels: Generator,
                                icao: str) -> Generator:
    gen = ((travel.passenger_id, travel.flight_id) for travel in travels)
    for passenger in passengers:
        lista = [passenger]
        flights, flights_copia = tee(flights)
        for flight in flights_copia:
            gen, gen_copia = tee(gen)
            if flight.airport_from == icao:
                for travel in gen_copia:
                    if flight.id_ == travel[1] and passenger.id_ == travel[0]:
                        airports, airports_copia = tee(airports)
                        d = distancia_entre_aeropuertos(
                            airports_copia, flight.airport_from,
                            flight.airport_to)
                        lista = revisar_agregar(lista, d)
        yield tuple(lista if len(lista) > 1 else [lista[0], 0])


def furthest_distance(passengers: Generator, airports: Generator,
                      flights: Generator, travels: Generator, icao: str,
                      n: int) -> list:
    gen = gen_passenger_max_from_icao(passengers, airports, flights, travels,
                                      icao)
    return [passenger for passenger in gen_mayor(gen)][:int(n)]
