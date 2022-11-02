from collections import namedtuple, defaultdict
from datetime import datetime

Correo = namedtuple("Correo", ["de", "para", "asunto", "cuerpo", "etiquetas"])
Evento = namedtuple("Evento", ["dueño", "nombre", "inicio", "final",
                               "descripcion", "invitados", "etiquetas"])


def cargar_usuarios(archivo_a_leer):

    diccionario_usuarios = {}
    path = "data/" + archivo_a_leer
    with open(path, "r", encoding="utf-8") as archivo:
        archivo.readline()
        for line in archivo:
            line = line.strip()
            user, password = line.split(",")
            diccionario_usuarios[user] = password

    return diccionario_usuarios


def cargar_correos(archivo_a_leer):
    lista_correos = []

    path = "data/" + archivo_a_leer
    with open(path, "r", encoding="utf-8") as archivo:
        archivo.readline()
        for line in archivo:
            line = line.strip()
            if line.count(",") == 4:
                de, para, asunto, cuerpo, etiquetas = line.split(",")
            else:
                lista = line.split(",")
                de = lista[0]
                para = lista[1]
                asunto = lista[2]
                if asunto.count("'") == 1:
                    for elemento in lista[3:]:
                        if elemento.count("'") == 1:
                            numero = lista.index(elemento)
                            asunto = ",".join(lista[2:numero + 1])
                            break
                        else:
                            pass
                else:
                    numero = 2
                    pass
                cuerpo = lista[numero + 1]

                if cuerpo.count("'") == 1:
                    for elemento in lista[numero + 2:]:
                        if elemento.count("'") == 1:
                            numero2 = lista.index(elemento)
                            cuerpo = ",".join(lista[numero + 1:numero2 + 1])
                            break
                        else:
                            pass
                else:
                    numero2 = numero + 1
                    pass
                etiquetas = lista[numero2 + 1]
            lista_para = para.split(";")
            lista_etiquetas = etiquetas.split(";")
            correo = Correo(de, lista_para, asunto, cuerpo, lista_etiquetas)
            lista_correos.append(correo)

    lista_correos = lista_correos[::-1]

    return lista_correos


def cargar_eventos(archivo_a_leer):  # Recuperado de función cargar_correos
    lista_eventos = []

    path = "data/" + archivo_a_leer
    with open(path, "r", encoding="utf-8") as archivo:
        archivo.readline()
        for line in archivo:
            line = line.strip()
            if line.count(",") == 6:
                dueño, nombre, inicio, final, descripcion, invitados, etiquetas\
                    = line.split(",")
                inicio_dt = transformar_a_datetime(inicio)
                final_dt = transformar_a_datetime(final)
            else:
                lista = line.split(",")
                dueño = lista[0]
                nombre = lista[1]
                if nombre.count("'") == 1:
                    for elemento in lista[2:]:
                        if elemento.count("'") == 1:
                            numero = lista.index(elemento)
                            nombre = ",".join(lista[1:numero + 1])
                            break
                        else:
                            pass
                else:
                    numero = 1
                    pass

                inicio = lista[numero + 1]
                inicio_dt = transformar_a_datetime(inicio)
                final = lista[numero + 2]
                final_dt = transformar_a_datetime(final)
                descripcion = lista[numero + 3]

                if descripcion.count("'") == 1:
                    for elemento in lista[numero + 4:]:
                        if elemento.count("'") == 1:
                            numero2 = lista.index(elemento)
                            descripcion = ",".join(lista[numero + 3:
                                                         numero2 + 1])
                            break
                        else:
                            pass
                else:
                    numero2 = numero + 3
                    pass
                invitados = lista[numero2 + 1]
                etiquetas = lista[numero2 + 2]

            lista_invitados = invitados.split(";")
            lista_etiquetas = etiquetas.split(";")
            evento = Evento(dueño, nombre, inicio_dt, final_dt,
                            descripcion, lista_invitados, lista_etiquetas)
            lista_eventos.append(evento)

    lista_eventos = lista_eventos[::-1]

    return lista_eventos


def crear_dicc_correos(lista_correos, usuarios):
    dicc_correos = defaultdict(list)

    for correo in lista_correos:
        for usuario in usuarios:
            if usuario in correo[1]:
                dicc_correos[usuario].append(correo)

    return dicc_correos


def crear_dicc_usuario_evento(lista_eventos, usuarios):
    # Recuperado de crear_dicc_correos
    dicc_usuario_evento = defaultdict(list)

    for evento in lista_eventos:
        for usuario in usuarios:
            if usuario in evento.dueño:
                dicc_usuario_evento[usuario].append(evento)
            elif usuario in evento.invitados:
                dicc_usuario_evento[usuario].append(evento)

    return dicc_usuario_evento


def transformar_a_datetime(fecha):

    lista = fecha.split(" ")
    lista[0] = lista[0].split("-")
    lista[1] = lista[1].split(":")
    fecha_dt = datetime(int(lista[0][0]), int(lista[0][1]), int(lista[0][2]),
                        int(lista[1][0]), int(lista[1][1]), int(lista[1][2]))
    return fecha_dt


def crear_numeros_bin(cadena_aleatoria):
    clave = "2233"
    lista_numeros = [str(numero) for numero in range(256)]

    cadena_inicio = []
    while len(cadena_inicio) < 256:
        for elemento in (clave + cadena_aleatoria):
            cadena_inicio.append(int(elemento))

    for i in range(256):
        j = i + cadena_inicio[i]
        k = lista_numeros[i]
        if j > 255:
            j = j - 256
        lista_numeros[i] = lista_numeros[j]
        lista_numeros[j] = k

    lista_numeros_bin = ['{0:08b}'.format(int(numero))
                         for numero in lista_numeros]
    # '{0:08b}'.format() recuperado de https://stackoverflow.com/questions/
    # 10411085/converting-integer-to-binary-in-python

    numeros_bin = "".join(lista_numeros_bin)

    return numeros_bin


def binario_a_numero(binario):
    # Recuperado de: https://stackoverflow.com/questions/47676424/
    # python-3-6-converting-8-bit-binary-to-decimal
    numero = 0
    for digito in binario:
        numero = numero*2 + int(digito)
    return numero
