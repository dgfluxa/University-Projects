from collections import namedtuple, defaultdict, deque

"""
Aquí están las estructuras de datos para guardar la información respectiva.

NO MODIFICAR.
"""

# Como se vio en la ayudantía, hay varias formas de declarar una namedtuple :)
Entrenador = namedtuple('Entrenador', 'nombre apellido')
Pokemon = namedtuple('Pokemon', ['nombre', 'tipo', 'max_solicitudes'])
Solicitud = namedtuple('Solicitud', ['id_entrenador', 'id_pokemon'])

################################################################################
"""
En esta sección debe completar las funciones para cargar los archivos al sistema.

Puedes crear funcionas auxiliar si tú quieres, ¡pero estas funciones DEBEN
retornar lo pedido en el enunciado!
"""

def cargar_entrenadores(ruta_archivo):
    """
    Esta función debería leer el archivo archivo_entrenadores y cargarlo usando
    las estructuras entregadas.
    """

    with open(ruta_archivo,"r", encoding="latin-1") as archivo:
        entrenadores = {}
        for line in archivo:
            line = line.strip()
            id, nombre, apellido = line.split(";")
            entrenadores[id] = Entrenador(nombre, apellido)

    return entrenadores



def cargar_pokemones(ruta_archivo):
    """
    Esta función debería leer el archivo archivo_pokemones y cargarlo usando las
    estructuras entregadas.
    """
    with open(ruta_archivo,"r", encoding="latin-1") as archivo:
        pokemones = {}
        for line in archivo:
            line = line.strip()
            id, nombre, tipo, max_solicitudes = line.split(";")
            pokemones[id] = Pokemon(nombre, tipo, max_solicitudes)

    return pokemones


def cargar_solicitudes(ruta_archivo):
    """
    Esta función debería leer el archivo archivo_solicitudes y cargarlo usando
    las estructuras entregadas.
    """

    with open(ruta_archivo, "r", encoding="latin-1") as archivo:
        solicitudes = defaultdict(deque)
        for line in archivo:
            line = line.strip()
            id_entrenador, id_pokemon = line.split(";")
            solicitudes_pokemon = deque()
            solicitud = Solicitud(id_entrenador, id_pokemon)
            solicitudes[id_pokemon].append(solicitud)

    return solicitudes



################################################################################

"""
Lógica del Sistema.
Debes completar esta función como se dice en el enunciado.
"""

def sistema(modo, entrenadores, pokemones, solicitudes):
    """
    Esta función se encarga de llevar a cabo la 'simulación', de acuerdo al modo
    entregado.
    """

    if modo == 1:
        pokemones_ganados = defaultdict(list)
        for id_pokemon in solicitudes:
            max_solicitudes = pokemones[id_pokemon].max_solicitudes
            contador = 0
            while contador <= int(max_solicitudes):
                id_entrenador = solicitudes[id_pokemon].popleft()
                contador += 1

            pokemones_ganados[id_entrenador].append(id_pokemon)

    elif modo == 2:
        pokemones_ganados = defaultdict(list)
        for id_pokemon in solicitudes:
            max_solicitudes = pokemones[id_pokemon].max_solicitudes
            contador = 0
            while contador <= int(max_solicitudes):
                id_entrenador = solicitudes[id_pokemon].pop()
                contador += 1

            pokemones_ganados[id_entrenador].append(id_pokemon)




################################################################################
"""
Funciones de consultas, deben rellenarlos como dice en el enunciado :D.
"""

def pokemones_por_entrenador(id_entrenador, resultado_simulacion):
    """
    Esta función debe retornar todos los pokemones que ganó el entrenador con el
    id entregado.

    Recuerda que esta función debe retornar una lista.
    """



    pass

def mismos_pokemones(id_entrenador1, id_entrenador2, resultado_simulacion):
    """
    Esta función debe retornar todos los pokemones que ganó tanto el entrenador
    con el id_entrenador1 como el entrenador con el id_entrenador2.

    Recuerda que esta función debe retornar una lista.
    """
    pass

def diferentes_pokemones(id_entrenador1, id_entrenador2, resultado_simulacion):
    """
    Esta función debe retornar todos los pokemones que ganó el entrenador con
    id_entrenador1 y que no ganó el entrenador con id_entrenador2.

    Recuerda que esta función debe retornar una lista.
    """
    pass


if __name__ == '__main__':

    ############################################################################
    """
    Poblando el sistema.
    Ya se hacen los llamados a las funciones, puedes imprimirlos para ver si se
    cargaron bien.
    """

    entrenadores = cargar_entrenadores('entrenadores.txt')
    pokemones = cargar_pokemones('pokemones.txt')
    solicitudes = cargar_solicitudes('solicitudes.txt')

    # print(entrenadores)
    # print(pokemones)
    # print(solicitudes)

    ################################   MENU   ##################################
    """
    Menú.
    ¡No debes cambiar nada! Simplemente nota que es un menú que pide input del
    usuario, y en el caso en que este responda con "1" ó "2", entonces se hace
    el llamado a la función. En otro caso, el programa termina.
    """

    eleccion = input('Ingrese el modo de lectura de solicitudes:\n'
                 '1: Orden de llegada\n'
                 '2: Orden Inverso de llegada\n'
                 '>\t')

    if eleccion in {"1", "2"}:
        resultados_simulacion = sistema(eleccion, entrenadores,
                                        pokemones, solicitudes)
    else:
        exit()

    ##############################   Pruebas   #################################
    """
    Casos de uso.

    Aquí pueden probar si sus consultas funcionan correctamente.
    """
