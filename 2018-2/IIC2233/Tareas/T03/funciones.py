from estructuras import Lista
from clases import Central, Elevadora, Transmision, Distribucion, Casa, Conexion
from csv import reader
from sys import exit
from excepciones import ElectricalOverload, ForbiddenAction, InvalidQuery
from consultas import energia_comuna, mayor_consumo, menor_consumo, \
    consumo_subestacion, potencia_perdida


def cargar_instalaciones(path, clase):
    lista = Lista()
    with open(path, "r", newline='', encoding="utf-8") as archivo:
        archivo.readline()
        archivo_csv = reader(archivo, dialect='excel')
        for row in archivo_csv:
            sub_lista = Lista(*row)
            instalacion = clase(*sub_lista)
            lista.append(instalacion)

    return lista


def poblar_nodos(tamaño="small"):
    lista_nodos = Lista()
    lista_nodos.extend(cargar_instalaciones(f"bd/{tamaño}/centrales.csv",
                                            Central))
    lista_nodos.extend(cargar_instalaciones(f"bd/{tamaño}/elevadoras.csv",
                                            Elevadora))
    lista_nodos.extend(cargar_instalaciones(f"bd/{tamaño}/transmision.csv",
                                            Transmision))
    lista_nodos.extend(cargar_instalaciones(f"bd/{tamaño}/distribucion.csv",
                                            Distribucion))
    lista_nodos.extend(cargar_instalaciones(f"bd/{tamaño}/casas.csv", Casa))

    return lista_nodos


def cargar_conexiones(path):
    lista = Lista()
    with open(path, "r", encoding="UTF-8") as archivo:
        archivo.readline()
        archivo_csv = reader(archivo, dialect='excel')
        for row in archivo_csv:
            if "casas_casas" not in path and "centrales" not in path:
                sub_lista = Lista(*row)
                conexion = Conexion(sub_lista[1], sub_lista[0], sub_lista[2])
            else:
                sub_lista = Lista(*row)
                conexion = Conexion(*sub_lista)
            lista.append(conexion)

    return lista


def poblar_conexiones(tamaño="small"):
    lista_1 = cargar_conexiones(
        f"bd/{tamaño}/centrales_elevadoras.csv")
    lista_2 = cargar_conexiones(
        f"bd/{tamaño}/transmision_elevadoras.csv")
    lista_3 = cargar_conexiones(
        f"bd/{tamaño}/distribucion_transmision.csv")
    lista_4 = cargar_conexiones(
        f"bd/{tamaño}/casas_distribucion.csv")
    lista_5 = cargar_conexiones(
        f"bd/{tamaño}/casas_casas.csv")
    return Lista(lista_1, lista_2, lista_3, lista_4, lista_5)


def nodo_en_lista(lista, id_, clase):
    for i in lista:
        if i.valor.id == id_ and type(i.valor) == clase:
            return True
    return False


def aplicar_conexiones(lista, lista_conexiones):
    lista_nodos = lista
    for conexion in lista_conexiones[0].valor:
        for nodo in lista_nodos:
            if str(nodo.valor.id) == str(conexion.valor.id1) and isinstance(
                    nodo.valor, Central):
                for n in lista_nodos:
                    if str(n.valor.id) == str(conexion.valor.id2) and \
                            isinstance(n.valor, Elevadora):
                        if nodo_en_lista(n.valor.padres, nodo.valor.id, type(
                                nodo.valor)) is False:
                            n.valor.padres.append(nodo.valor)
                        guardar = True
                        if len(nodo.valor.hijos) > 0:
                            for hijo in nodo.valor.hijos:
                                if str(hijo.valor[0].valor.id) == str(
                                        n.valor.id) and type(hijo.valor[0].valor
                                                             ) == type(n.valor):
                                    guardar = False
                        if guardar:
                            nodo.valor.hijos.append(Lista(n.valor,
                                                          conexion.valor.dist))
    for conexion in lista_conexiones[1].valor:
        for nodo in lista_nodos:
            if str(nodo.valor.id) == str(conexion.valor.id1) and isinstance(
                    nodo.valor, Elevadora):
                for n in lista_nodos:
                    if str(n.valor.id) == str(conexion.valor.id2) and \
                            isinstance(n.valor, Transmision):
                        if nodo_en_lista(n.valor.padres, nodo.valor.id, type(
                                nodo.valor)) is False:
                            n.valor.padres.append(nodo.valor)
                        guardar = True
                        for hijo in nodo.valor.hijos:
                            if hijo.valor[0].valor.id == n.valor.id and type(
                                    hijo.valor[0].valor) == type(n.valor):
                                guardar = False
                        if guardar:
                            nodo.valor.hijos.append(Lista(n.valor,
                                                          conexion.valor.dist))

    for conexion in lista_conexiones[2].valor:
        for nodo in lista_nodos:
            if str(nodo.valor.id) == str(conexion.valor.id1) and isinstance(
                    nodo.valor, Transmision):
                for n in lista_nodos:
                    if str(n.valor.id) == str(conexion.valor.id2) and \
                            isinstance(n.valor, Distribucion):
                        if nodo_en_lista(n.valor.padres, nodo.valor.id,
                                         type(nodo.valor)) is False:
                            n.valor.padres.append(nodo.valor)
                        guardar = True
                        for hijo in nodo.valor.hijos:
                            if hijo.valor[0].valor.id == n.valor.id and type(
                                    hijo.valor[0].valor) == type(n.valor):
                                guardar = False
                        if guardar:
                            nodo.valor.hijos.append(Lista(n.valor,
                                                          conexion.valor.dist))

    for conexion in lista_conexiones[3].valor:
        for nodo in lista_nodos:
            if str(nodo.valor.id) == str(conexion.valor.id1) and \
                    isinstance(nodo.valor, Distribucion):
                for n in lista_nodos:
                    if str(n.valor.id) == str(conexion.valor.id2) and \
                            isinstance(n.valor, Casa):
                        if nodo_en_lista(n.valor.padres, nodo.valor.id,
                                         type(nodo.valor)) is False:
                            n.valor.padres.append(nodo.valor)
                        guardar = True
                        for hijo in nodo.valor.hijos:
                            if hijo.valor[0].valor.id == n.valor.id and type(
                                    hijo.valor[0].valor) == type(n.valor):
                                guardar = False
                        if guardar:
                            nodo.valor.hijos.append(Lista(n.valor,
                                                          conexion.valor.dist))

    for conexion in lista_conexiones[4].valor:
        for nodo in lista_nodos:
            if str(nodo.valor.id) == str(conexion.valor.id1) and isinstance(
                    nodo.valor, Casa):
                for n in lista_nodos:
                    if str(n.valor.id) == str(conexion.valor.id2) and \
                            isinstance(n.valor, Casa):
                        if nodo_en_lista(n.valor.padres, nodo.valor.id,
                                         type(nodo.valor)) is False:
                            n.valor.padres.append(nodo.valor)
                        guardar = True
                        for hijo in nodo.valor.hijos:
                            if hijo.valor[0].valor.id == n.valor.id and type(
                                    hijo.valor[0].valor) == type(n.valor):
                                guardar = False
                        if guardar:
                            nodo.valor.hijos.append(Lista(n.valor,
                                                          conexion.valor.dist))

    return lista_nodos


def sist_valido(lista):
    for nodo in lista:
        if len(nodo.valor.padres) == 0 and isinstance(nodo.valor, Central) is \
                False:
            return False
        elif isinstance(nodo.valor, Central) and len(nodo.valor.hijos) == 0:
            return False
    return True


def crear_lista_sist(lista_nodos):
    '''
    Esta funcion existe por si existiera un nodo sin padres en el sistema, con
    el fin de que este no afecte el calculo de la demanda
    :param lista_nodos:
    :return:
    '''
    lista = lista_nodos
    while not sist_valido(lista):
        for nodo in lista:
            if not isinstance(nodo.valor, Central) and len(
                    nodo.valor.padres) == 0:
                for hijo in nodo.valor.hijos:
                    hijo.valor[0].valor.padres.remove(
                        hijo.valor[0].valor.padres.index(nodo.valor))
                lista.remove(lista.index(nodo.valor))
            elif isinstance(nodo.valor, Central) and len(nodo.valor.hijos) == 0:
                lista.remove(lista.index(nodo.valor))

    return lista


def mostrar_menu(red):
    lista_acciones = Lista("1", "2", "3", "-1")
    while True:
        print(f'''
MENÚ PRINCIPAL:
    1.- Realizar Consulta
    2.- Modificar Red Electrica
    3.- Realizar Prueba
            ''')
        print("¿Que acción deseas realizar? ((-1) para salir)")
        accion = str(input())
        if accion in lista_acciones:
            if accion == "-1":
                print(f'''
{'-' * 32} Hasta Luego {'-' * 32}
                    ''')
                exit()
            elif accion == "1":
                menu_consulta(red)
            elif accion == "2":
                red = menu_nodos(red)
            else:
                menu_prueba(red)
        else:
            print("\nSolo puedes ingresar los numeros 1, 2, 3 o -1\n")


def menu_consulta(red):
    lista_acciones = Lista("1", "2", "3", "4", "5", "-1")
    print(f'''
REALIZAR CONSULTA:
    1.- Energía total consumida en una comuna
    2.- Clientes con mayor consumo
    3.- Clientes con menor consumo
    4.- Potencia perdida en transmisión
    5.- Consumo de una subestación
    ''')
    while True:
        print("¿Que acción deseas realizar? ((-1) para volver al "
              "menú principal)")
        accion = str(input())
        if accion in lista_acciones:
            if accion == "1":
                comuna = input("Ingrese el nombre de la comuna: ").upper()
                try:
                    lista = energia_comuna(red, comuna)
                    print(f'''
    Energia comuna {comuna}: {lista[0].valor}
    Porcentaje consumo total: {lista[1].valor}%''')
                except InvalidQuery as err:
                    print(err)

            elif accion == "2":
                sigla = input(
                    "Ingrese la sigla del sistema eléctrico: ").upper()
                try:
                    print(mayor_consumo(red, sigla))
                except InvalidQuery as err:
                    print(err)
            elif accion == "3":
                sigla = input(
                    "Ingrese la sigla del sistema eléctrico: ").upper()
                try:
                    print(menor_consumo(red, sigla))
                except InvalidQuery as err:
                    print(err)
            elif accion == "4":
                id_ = input("Ingrese el id de la casa: ")
                try:
                    print(potencia_perdida(red, id_))
                except InvalidQuery as err:
                    print(err)
            elif accion == "5":
                id_ = input("Ingrese el id de la subestacion: ")
                print("1.- Transmisión\n2.- Distribución")
                num = input("Ingrese el numero deseado: ")
                try:
                    print(consumo_subestacion(red, id_, num))
                except InvalidQuery as err:
                    print(err)
            return
        else:
            print("\nSolo puedes ingresar los numeros 1, 2, 3, 4, 5 o -1\n")


def menu_nodos(red):
    lista_acciones = Lista("1", "2", "3", "4", "-1")
    print(f'''
EDITAR RED ELÉCTRICA:
    1.- Agregar Nodo
    2.- Remover Nodo
    3.- Agregar Conexión
    4.- Remover Conexión
        ''')
    while True:
        print("¿Que acción deseas realizar? ((-1) para volver al "
              "menú principal)")
        accion = str(input())
        if accion in lista_acciones:
            if accion == "1":
                red = menu_agregar_nodo(red)
            elif accion == "2":
                red = menu_remover_nodo(red)
            elif accion == "3":
                red = menu_agregar_conexion(red)
            elif accion == "4":
                red = menu_remover_conexion(red)
            return red
        else:
            print("\nSolo puedes ingresar los numeros 1, 2, 3, 4 o -1\n")


def menu_prueba(red):
    red_secundaria = red
    lista_acciones = Lista("1", "2", "3", "4", "5", "-1")
    while True:
        print(f'''
MENÚ DE PRUEBA:
    1.- Agregar Nodo
    2.- Remover Nodo
    3.- Agregar Conexión
    4.- Remover Conexión
    5.- Reiniciar Red de Prueba
                ''')
        print("¿Que acción deseas realizar? ((-1) para volver al "
              "menú principal)")
        accion = str(input())
        if accion in lista_acciones:
            if accion == "-1":
                return
            if accion == "1":
                red_secundaria = menu_agregar_nodo(red_secundaria)
            elif accion == "2":
                red_secundaria = menu_remover_nodo(red_secundaria)
            elif accion == "3":
                red_secundaria = menu_agregar_conexion(red_secundaria)
            elif accion == "4":
                red_secundaria = menu_remover_conexion(red_secundaria)
            elif accion == "5":
                red_secundaria = red
            # Printear estadísticas de la red secundaria
            if red_secundaria is not None:
                red_secundaria.print_estadisticas()
        else:
            print("\nSolo puedes ingresar los numeros 1, 2, 3, 4 o -1\n")


def menu_agregar_nodo(red):
    lista_acciones = Lista("1", "2", "3", "4", "5", "-1")
    print(f'''
AGREGAR NODO:
    1.- Central
    2.- Elevadora
    3.- Transmisión
    4.- Distribución
    5.- Casa
    ''')
    while True:
        print("¿Que tipo de nodo deseas agregar? ((-1) para volver al "
              "menú principal)")
        accion = str(input())
        if accion in lista_acciones:
            if accion == "-1":
                return
            else:
                if accion == "1":
                    clase = Central
                elif accion == "2":
                    clase = Elevadora
                elif accion == "3":
                    clase = Transmision
                elif accion == "4":
                    clase = Distribucion
                else:
                    clase = Casa
                try:
                    red.agregar_nodo(clase)
                except InvalidQuery as err:

                    print(err)
                except ElectricalOverload as err:
                    print(err)
                finally:
                    return red
        else:
            print("\nSolo puedes ingresar los numeros 1, 2, 3, 4, 5 o -1\n")


def menu_remover_nodo(red):
    lista_acciones = Lista("1", "2", "3", "4", "5", "-1")
    print(f'''
REMOVER NODO:
    1.- Central
    2.- Elevadora
    3.- Transmisión
    4.- Distribución
    5.- Casa
        ''')
    while True:
        print("¿Que tipo de nodo deseas remover? ((-1) para volver al "
              "menú principal)")
        accion = str(input())
        if accion in lista_acciones:
            if accion == "-1":
                return
            else:
                if accion == "1":
                    clase = Central
                elif accion == "2":
                    clase = Elevadora
                elif accion == "3":
                    clase = Transmision
                elif accion == "4":
                    clase = Distribucion
                else:
                    clase = Casa
                id_ = input("Ingrese el id del nodo a remover: ")
                try:
                    red.remover_nodo(clase, id_)
                except InvalidQuery as err:
                    print(err)
                except ElectricalOverload as err:
                    print(err)
                finally:
                    return red
        else:
            print("\nSolo puedes ingresar los numeros 1, 2, 3, 4, 5 o -1\n")


def menu_agregar_conexion(red):
    lista_acciones = Lista("1", "2", "3", "4", "5", "-1")
    print(f'''
AGREGAR CONEXIÓN:
    1.- Central -> Elevadora
    2.- Elevadora -> Transmisión
    3.- Transmisión -> Distribución
    4.- Distribución -> Casa
    5.- Casa -> Casa
        ''')
    while True:
        print("¿Que tipo de conexión deseas agregar? ((-1) para volver al "
              "menú principal)")
        accion = str(input())
        if accion in lista_acciones:
            if accion == "-1":
                return
            else:
                if accion == "1":
                    clase1 = Central
                    clase2 = Elevadora
                elif accion == "2":
                    clase1 = Elevadora
                    clase2 = Transmision
                elif accion == "3":
                    clase1 = Transmision
                    clase2 = Distribucion
                elif accion == "4":
                    clase1 = Distribucion
                    clase2 = Casa
                else:
                    clase1 = Casa
                    clase2 = Casa
                id1 = input("Ingrese el id del nodo inicial: ")
                id2 = input("Ingrese el id del nodo final: ")
                dist = input("Ingrese la distancia entre los nodos: ")
                try:
                    red.agregar_conexion(clase1, clase2, id1, id2, dist)
                except InvalidQuery as err:
                    print(err)
                except ForbiddenAction as err:
                    print(err)
                except ElectricalOverload as err:
                    print(err)
                except Exception as err:
                    print(err)
                finally:
                    return red
        else:
            print("\nSolo puedes ingresar los numeros 1, 2, 3, 4, 5 o -1\n")


def menu_remover_conexion(red):
    lista_acciones = Lista("1", "2", "3", "4", "5", "-1")
    print(f'''
REMOVER CONEXIÓN:
    1.- Central -> Elevadora
    2.- Elevadora -> Transmisión
    3.- Transmisión -> Distribución
    4.- Distribución -> Casa
    5.- Casa -> Casa
        ''')
    while True:
        print("¿Que tipo de conexión deseas remover? ((-1) para volver al "
              "menú principal)")
        accion = str(input())
        if accion in lista_acciones:
            if accion == "-1":
                return
            else:
                if accion == "1":
                    clase1 = Central
                    clase2 = Elevadora
                elif accion == "2":
                    clase1 = Elevadora
                    clase2 = Transmision
                elif accion == "3":
                    clase1 = Transmision
                    clase2 = Distribucion
                elif accion == "4":
                    clase1 = Distribucion
                    clase2 = Casa
                else:
                    clase1 = Casa
                    clase2 = Casa
                id1 = input("Ingrese el id del nodo inicial: ")
                id2 = input("Ingrese el id del nodo final: ")
                try:
                    red.remover_conexion(clase1, clase2, id1, id2)
                except InvalidQuery as err:
                    print(err)
                except ForbiddenAction as err:
                    print(err)
                except ElectricalOverload as err:
                    print(err)
                finally:
                    return red
        else:
            print("\nSolo puedes ingresar los numeros 1, 2, 3, 4, 5 o -1\n")
