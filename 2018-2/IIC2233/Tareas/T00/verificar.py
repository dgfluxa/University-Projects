

def ingreso_usuario(usuarios, correo, contraseña):

    if correo in usuarios:
        if usuarios[correo] == contraseña:
            return True

        else:
            print("*" * 10, "Contraseña incorrecta", "*" * 10)
            return False

    else:
        print("*" * 10, "Esta dirección de correo no existe", "*" * 10)
        return False


def revisar_usuario(correo):
    if "@" in correo:
        if "," not in correo:
            if ";" not in correo:
                lugar_arroba = correo.find("@")
                if "." in correo[lugar_arroba:]:
                    return True
                else:
                    print(
                        "Tu dirección de correo debe tener una "
                        "dirección de servicio a continuación de un (@)"
                        " y luego un (.algo). Tampoco puede poseero el "
                        "carácter (,) ni (;)")
            else:
                print(
                    "Tu dirección de correo debe tener una dirección de"
                    " servicio a continuación de un (@) y luego un"
                    " (.algo). Tampoco puede poseero el carácter (,) "
                    "ni (;)")
        else:
            print("Tu dirección de correo debe tener una dirección de "
                  "servicio a continuación de un (@) y luego un (.algo)"
                  ". Tampoco puede poseero el carácter (,) ni (;)")
    else:
        print("Tu dirección de correo debe tener una dirección de "
              "servicio a continuación de un (@) y luego un (.algo)."
              "Tampoco puede poseero el carácter (,) ni (;)")


def revisar_contraseña(contraseña):
    if len(contraseña) >= 6:
        if "," not in contraseña:
            if ";" not in contraseña:
                return True
            else:
                print(
                    "Tu contraseña debe tener al menos 6 carácteres, y"
                    " no puede contener los carácteres (,) ni (;)")

        else:
            print("Tu contraseña debe tener al menos 6 carácteres, y no"
                  "puede contener los carácteres (,) ni (;)")

    else:
        print("Tu contraseña debe tener al menos 6 carácteres, y no"
              "puede contener los carácteres (,) ni (;)")


def verificar_destinatarios(str_destinatarios, usuarios):
    numero_arrobas = str_destinatarios.count("@")
    numero_comas = str_destinatarios.count(",")
    if len(str_destinatarios) == 0:
        print("Debes ingresar destinatarios")
        return False
    elif numero_arrobas == 0:
        print("Debes ingresar destinatarios válidos (de_ejemplo@ejemplo.ej)")
        return False
    elif numero_comas == -1:
        pass
    elif numero_comas == (numero_arrobas - 1):
        pass
    else:
        print("Los destinatarios deben estar separados por (,)")
        return False

    lista_destinatarios = str_destinatarios.split(",")

    for destinatario in lista_destinatarios:
        if destinatario not in usuarios.keys():
            print("El destinatario", destinatario, "no existe")
            return False
        else:
            pass

    return True


def revisar_etiquetas(evento, etiquetas_final, lista_eventos_filtrados):
    lista_etiquetas = evento.etiquetas
    lista_etiquetas_final = etiquetas_final.split(";")
    for etiqueta_a_buscar in lista_etiquetas_final:
        if etiqueta_a_buscar not in lista_etiquetas:
            return False
    if evento not in lista_eventos_filtrados:
        return True


def año_bisiesto(año):
    # Recuperado de :
    # http://www.linuxhispano.net/2016/11/24/calcular-ano-bisiesto-python-3/

    if int(año) % 4 == 0:
        if int(año) % 100 == 0:
            if int(año) % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def comprobar_fecha(fecha):
    numero_guiones = fecha.count("-")
    numero_espacios = fecha.count(" ")
    numero_dobles_puntos = fecha.count(":")
    if numero_dobles_puntos != 2 or numero_espacios != 1 \
            or numero_guiones != 2:
        print("Debes seguir el formato "
              "(AÑO-MES-DÍA HORA:MINUTOS:SEGUNDOS)")

    else:
        numeros = ""
        lista_inicio = fecha.split(" ")
        lista_inicio[0] = lista_inicio[0].split("-")
        lista_inicio[1] = lista_inicio[1].split(":")
        for numero in lista_inicio[0]:
            numeros = numeros + numero
        for numero in lista_inicio[1]:
            numeros = numeros + numero

        if numeros.isnumeric() is False:
            print("Debes ingresar valores numericos")
        else:
            año = int(lista_inicio[0][0])
            mes = int(lista_inicio[0][1])
            dia = int(lista_inicio[0][2])
            hora = int(lista_inicio[1][0])
            minutos = int(lista_inicio[1][1])
            segundos = int(lista_inicio[1][2])
            meses_31_dias = (1, 3, 5, 7, 8, 10, 12)
            if año < 1 or año > 9999:
                print("El año", año, "no es válido")
                return False
            elif mes < 1 or mes > 12:
                print("El mes", mes, "no es válido")
                return False
            elif dia < 1 or dia > 31:
                print("El día", dia, "no existe")
                return False
            elif dia > 30 and mes not in meses_31_dias:
                print("El dia", dia, "no existe en el mes", mes)
                return False
            elif dia > 28 and mes == 2:
                if año_bisiesto(año) is False:
                    print("El dia", dia, "del mes", mes, "del año", año,
                          "no existe")
                    return False
                else:
                    pass
            elif hora < 0 or hora > 23:
                print("La hora", hora, "no existe")
                return False
            elif minutos < 0 or minutos > 59:
                print("No pueden existir", minutos, "minutos")
                return False
            elif segundos < 0 or segundos > 59:
                print("No pueden existir", segundos, "minutos")
                return False
            else:
                return True
