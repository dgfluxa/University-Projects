from collections import namedtuple
from statistics import mean


# NO MODIFICAR ESTA FUNCION
def foreach(function, iterable):
    for elem in iterable:
        function(elem)


# Named tuples para cada entidad
Ciudad = namedtuple("Ciudad", ["sigla_pais", "nombre"])
Pais = namedtuple("Pais", ["sigla", "nombre"])
Persona = namedtuple("Persona", [
    "nombre", "apellido", "edad", "sexo", "ciudad_residencia",
    "area_de_trabajo", "sueldo"
])

###########################


def leer_ciudades(ruta_archivo_ciudades):

    with open(ruta_archivo_ciudades, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            sigla, nombre = linea.strip().split(",")
            yield Ciudad(sigla, nombre)



def leer_paises(ruta_archivo_paises):
    with open(ruta_archivo_paises, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            sigla, nombre = linea.strip().split(",")
            yield Pais(sigla, nombre)


def leer_personas(ruta_archivo_personas):
    with open(ruta_archivo_personas, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            nombre, apellido, edad, sexo, ciudad_residencia, area_de_trabajo,\
            sueldo = linea.strip().split(",")

            yield Persona(nombre, apellido, edad, sexo, ciudad_residencia,
                          area_de_trabajo, sueldo)


def sigla_de_pais(nombre_pais, paises):

    generador = (pais.sigla for pais in paises if nombre_pais == pais.nombre)

    return next(generador)



def ciudades_por_pais(nombre_pais, paises, ciudades):

    generador = (ciudad_del_pais for ciudad in ciudades
                 if sigla_de_pais(nombre_pais, paises) == ciudad.sigla_pais)

    return generador


def personas_por_pais(nombre_pais, paises, ciudades, personas):

    generador_ciudades = ciudades_por_pais(nombre_pais, paises, ciudades)
    generador_personas = (persona_del_pais for persona in personas
                          if persona.ciudad_residencia ==
                          generador_ciudades.nombre)
    return generador_personas


def sueldo_promedio(personas):

    return mean(map(lambda x: float(x.sueldo), personas))


def cant_personas_por_area_de_trabajo(personas):





if __name__ == '__main__':
    RUTA_PAISES = "Paises.txt"
    RUTA_CIUDADES = "Ciudades.txt"
    RUTA_PERSONAS = "Personas.txt"

    # (1) Ciudades en Chile
    ciudades_chile = ciudades_por_pais('Chile', leer_paises(RUTA_PAISES),
                                       leer_ciudades(RUTA_CIUDADES))
    # foreach(ciudades_chile,
    #         lambda ciudad: print(ciudad.sigla_pais, ciudad.nombre))

    # (2) Personas en Chile
    personas_chile = personas_por_pais('Chile', leer_paises(RUTA_PAISES),
                                       leer_ciudades(RUTA_CIUDADES),
                                       leer_personas(RUTA_PERSONAS))
    # foreach(personas_chile, lambda p: print(p.nombre, p.ciudad_residencia))

    # (3) Sueldo promedio de personas del mundo
    sueldo_mundo = sueldo_promedio(leer_personas(RUTA_PERSONAS))
    # print('Sueldo promedio: ', sueldo_mundo)

    # (4) Cantidad de personas por profesion
    dicc = cant_personas_por_area_de_trabajo(leer_personas(RUTA_PERSONAS))
    # foreach(dicc.items(), lambda elem: print(f"{elem[0]}: {elem[1]}"))

