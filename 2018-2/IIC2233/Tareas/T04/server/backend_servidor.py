from os import urandom
from hashlib import sha256
from math import sin, cos, pi
from random import randint, uniform
from binascii import hexlify

def generador_usuarios():
    with open("usuarios.txt", "r", encoding="UTF-8") as archivo:
        archivo.readline()
        for linea in archivo:
            lista = linea.strip().split(",")
            yield lista


def encriptar(clave, salt=None):
    if salt is None:
        salt = hexlify(urandom(8)).decode("UTF-8").encode("UTF-8")
    clave_bytes = clave.encode("UTF-8")
    concatenado = clave_bytes + salt
    hash = sha256()
    hash.update(concatenado)
    clave_encriptada = hash.digest()

    return clave_encriptada, salt


def generar_pos():
    x = randint(75, 675)
    y = randint(75, 425)
    o = uniform(0, 2 * pi)
    x2 = x - (4 * cos(o))
    y2 = y + (4 * sin(o))
    return x, y, o, x2, y2


def pos_valida(lista, x2, y2):
    if lista:
        for pos in lista:
            if (pos[0] - 75 < x2 < pos[0] + 75) or (
                    pos[1] - 75 < y2 < pos[1] + 75):
                return False
    return True
