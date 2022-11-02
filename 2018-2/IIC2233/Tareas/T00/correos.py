from random import randint
from crear import crear_numeros_bin, binario_a_numero, cargar_correos, \
    crear_dicc_correos
from verificar import verificar_destinatarios


def codificar(cuerpo):

    lista_cuerpo_bin = ['{0:08b}'.format((ord(caracter) + 10))
                        for caracter in cuerpo]

    # ord() recuperado de: https://stackoverflow.com/questions/
    # 227459/ascii-value-of-a-character-in-python
    # '{0:08b}'.format() recuperado de: https://stackoverflow.com/questions/
    # 10411085/converting-integer-to-binary-in-python

    cuerpo_bin = "".join(lista_cuerpo_bin)

    cadena_aleatoria = ""
    while len(cadena_aleatoria) < 10:
        cadena_aleatoria = cadena_aleatoria + str(randint(0, 9))

    mensaje_codificado = cadena_aleatoria

    numeros_bin = crear_numeros_bin(cadena_aleatoria)

    for i in range(len(cuerpo_bin)):
        if cuerpo_bin[i] == numeros_bin[i]:
            mensaje_codificado = mensaje_codificado + "0"
        else:
            mensaje_codificado = mensaje_codificado + "1"

    return mensaje_codificado


def decodificar(mensaje_codificado):
    cadena_aleatoria = mensaje_codificado[0:10]
    mensaje_codificado = mensaje_codificado[10:]
    numeros_bin = crear_numeros_bin(cadena_aleatoria)
    mensaje_deco_bin = ""

    for numero in range(len(mensaje_codificado)):
        if mensaje_codificado[numero] == "0":
            mensaje_deco_bin = mensaje_deco_bin + str(numeros_bin[numero])
        else:
            if numeros_bin[numero] == "0":
                mensaje_deco_bin = mensaje_deco_bin + "1"
            else:
                mensaje_deco_bin = mensaje_deco_bin + "0"

    lista_mensaje_bin = [mensaje_deco_bin[i*8: (i + 1)*8]
                         for i in range(int(len(mensaje_deco_bin)/8))]

    lista_mensaje_ascii = [(int(binario_a_numero(binario)))
                           for binario in lista_mensaje_bin]

    lista_mensaje_deco = [(chr(int(numero_ascii)-10)) for
                          numero_ascii in lista_mensaje_ascii]
    # chr() recuperado de: https://stackoverflow.com/questions/227459/
    # ascii-value-of-a-character-in-python

    mensaje_decodificado = "".join(lista_mensaje_deco)

    return mensaje_decodificado


def bandeja_entrada(dicc_correos, usuario):
    numero = 0
    lista_numeros_str = []
    if len(dicc_correos[usuario]) == 0:
        print("Actualmente no tienes correos disponibles")
        return

    print()
    print("-"*84)
    print()
    print("Bandeja de Entrada: (Correos ordenados del más reciente"
          " al más antiguo)")
    print()
    for correo_recibido in dicc_correos[usuario]:

        numero += 1
        lista_numeros_str.append(str(numero))
        etiquetas_str = ""
        for etiqueta in correo_recibido.etiquetas:
            etiquetas_str = etiquetas_str + etiqueta + ","
        etiquetas_str = etiquetas_str[0:len(etiquetas_str)-1]

        print(str(numero) + ".-", etiquetas_str,
              " "*(48 - (len(etiquetas_str) + len(str(numero)))), "|",
              correo_recibido.asunto)

    while True:
        print("¿Que correo deseas leer? (Debes ingresar el número del correo o "
              "(-1) para salir)")
        numero_correo = input()

        if numero_correo == "-1":
            return

        elif numero_correo not in lista_numeros_str:
            print("Debes introducir uno de los números habilitados")

        else:
            break

    correo = dicc_correos[usuario][int(numero_correo)-1]
    correo_desencriptado = \
        decodificar(correo.cuerpo)
    print()
    print("-" * 84)
    print("De:", correo.de)
    print("Para:", ", ".join(correo.para))
    print("Asunto:", correo.asunto.strip("'"))
    print()
    print(correo_desencriptado)
    print()
    print("Etiquetas:", ", ".join(correo.etiquetas))
    print("-" * 84)
    print()


def crear_correo(usuario, usuarios):
    print()
    print("-"*84)
    print("Crear correo:")
    print()
    while True:
        para = input("Ingrese el o los destinatarios separandolos con (,): ")
        if verificar_destinatarios(para, usuarios) is True:
            break
        else:
            pass
    list_para = para.split(",")
    para_final = ""
    for destinatario in list_para:
        para_final = para_final + destinatario + ";"

    para_final = para_final[0:len(para_final)-1]

    while True:
        asunto = input("Asunto: ")
        if len(asunto) > 50:
            print("El asunto no puede exceder los 50 carácteres")
        else:
            break

    while True:
        print("A continuación escriba el cuerpo del correo: ")
        cuerpo = input()
        if len(cuerpo) > 256:
            print("El asunto no puede exceder los 256 carácteres")
        else:
            break

    lista_etiquetas = ["Importante", "Publicidad", "Destacado", "Newsletter"]
    etiquetas = ""
    while True:  # Recuperado en parte de Tarea 3 IIC1103, 2017, Diego Fluxá #
        numero = 0
        lista_numeros_str = []
        if len(lista_etiquetas) > 0:
            print()
            print("Seleccione las etiquetas: ")
            for etiqueta in lista_etiquetas:
                print(str(lista_etiquetas.index(etiqueta) + 1) + ".-", etiqueta)
                numero += 1
                lista_numeros_str.append(str(numero))
        else:
            etiquetas = etiquetas[0:len(etiquetas) - 1]
            print()
            print("*" * 40)
            print()
            print("No quedan etiquetas por agregar")
            print()
            print("*"*40)
            break

        print()
        print("Presione (-1) para terminar la selección")
        accion = input()

        if accion == "-1":
            if len(etiquetas) == 0:
                etiquetas = "sin clasificación"
                break
            else:
                etiquetas = etiquetas[0:len(etiquetas)-1]
            break
        elif accion in lista_numeros_str:
            etiquetas = etiquetas + str(lista_etiquetas[int(accion)-1]) + ";"
            lista_etiquetas.pop(int(accion) - 1)

        else:
            print("Debes ingresar un número permitido")

    while True:
        print()
        print("¿Deseas ver una vista previa de tu correo? (1): Si (-1): No")
        preview = input()
        if preview == "1":
            print()
            print("-"*84)
            print("De:", usuario)
            print("Para:", para)
            print("Asunto:", asunto)
            print()
            print(cuerpo)
            print()
            print("Etiquetas:", etiquetas)
            print("-"*84)
            print()
            break
        elif preview == "-1":
            break
        else:
            print("Debes ingresar (1) o (-1)")

    while True:
        enviar = input("¿Enviar (1) o Borrar (-1)? ")
        if enviar == "1":
            cuerpo_encriptado = codificar(cuerpo)
            path = "data/db_emails.csv"
            correo_final = str(usuario + "," + para_final + "," + asunto + ","
                               + cuerpo_encriptado + "," + etiquetas)
            with open(path, "a", encoding="utf-8") as archivo:
                archivo.write("\n")
                archivo.write(correo_final)

            correos = cargar_correos("db_emails.csv")
            dicc_correos = crear_dicc_correos(correos, usuarios)
            print()
            print("Correo enviado exitosaamente")
            print()

            return dicc_correos

        elif enviar == "-1":
            correos = cargar_correos("db_emails.csv")
            dicc_correos = crear_dicc_correos(correos, usuarios)
            print()
            print("Correo no enviado")
            print()

            return dicc_correos

        else:
            print("Debes ingresar (1) o (-1)")


def crear_usuario(usuarios, correo, contraseña):

    path = "data/db_users.csv"
    if correo not in usuarios:
        with open(path, "a", encoding="utf-8") as archivo:
            archivo.write("\n")
            archivo.write(correo + "," + contraseña)
            usuarios[correo] = contraseña
            return usuarios

    else:
        print("Esta dirección de correo ya existe")
        return usuarios
