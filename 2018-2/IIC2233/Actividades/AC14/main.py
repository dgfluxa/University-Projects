import re
import json
import requests
from time import sleep

from credenciales import API_KEY


API_URL = "https://api.nasa.gov/planetary/apod"
DIR_IMAGENES = 'imagenes'
PATH_RESULTADOS = 'resultados.txt'


def limpiar_fecha(linea):
    '''
    Esta función se encarga de limpiar el texto introducido a las fechas

    :param linea: str
    :return: str
    '''
    filtro = re.sub("</?(\w)+>", "", linea)

    return str(filtro)


def chequear_fecha(fecha):
    '''
    Esta función debe chequear si la fecha cumple el formato especificado

    :param fecha: str
    :return: bool
    '''
    return bool(re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", fecha))


def obtener_fechas(path):
    '''
    Esta función procesa las fechas para devolver aquellas que son útiles
    para realizar las consultas a la API

    :param path: str
    :return: iterable
    '''
    lista = []
    with open(path, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            filtrada = limpiar_fecha(linea.strip())
            if chequear_fecha(filtrada):
                lista.append(filtrada)

    return lista


def obtener_info(fecha):
    '''
    Recibe una fecha y retorna un diccionario
    con el título, la fecha y el url de la imagen
    :param fecha: str
    :return: dict
    '''
    parametros = {"date": fecha, "hd": False, "api_key": API_KEY}
    response = requests.get(API_URL, params=parametros)
    response = response.json()
    return response


def escribir_respuesta(datos):
    '''
    Esta función debe escribir las respuestas de la API en el archivo
    resultados.txt

    :param datos_respuesta: dict
    '''
    path = f"{DIR_IMAGENES}/resultados.txt"
    with open(path, "a", encoding="utf-8") as archivo:
        archivo.write(f"{datos['date']} --> {datos['title']}: {datos['url']}\n")
    lista_url = re.split("/", datos['url'])
    nombre_archivo_imagen = str(lista_url[len(lista_url) - 1])
    descargar_imagen(datos['url'], f"{DIR_IMAGENES}/{nombre_archivo_imagen}")


def descargar_imagen(url, path):
    '''
    Recibe la url de una imagen y guarda los datos en un archivo en path

    :param url: str
    :param path: str
    '''
    respuesta = requests.get(url, stream=True)
    if respuesta.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in respuesta:
                f.write(chunk)


if __name__ == "__main__":
    PATH_FECHAS = 'fechas_secretas.txt'

    for fecha in obtener_fechas(PATH_FECHAS):
        respuesta = obtener_info(fecha)
        escribir_respuesta(respuesta)
