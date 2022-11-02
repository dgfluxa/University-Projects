from collections import namedtuple
from datetime import timedelta
from crear import transformar_a_datetime
from verificar import comprobar_fecha, verificar_destinatarios

Evento = namedtuple("Evento", ["dueño", "nombre", "inicio", "final",
                               "descripcion", "invitados", "etiquetas"])


def crear_evento(usuario, usuarios, lista_eventos):
    print()
    print("-" * 84)
    print("Crear evento:")
    print()
    dueño = usuario

    while True:
        posible = "si"
        while True:
            nombre = input("Nombre: ")
            if len(nombre) < 6:
                print("El nombre debe tener al menos 6 carácteres")
            elif len(nombre) > 50:
                print("El nombre no puede exceder los 50 carácteres")
            else:
                break
        while True:
            print("Fecha de inicio (AÑO-MES-DÍA HORA:MINUTOS:SEGUNDOS): ")
            inicio = input()
            if comprobar_fecha(inicio) is True:
                inicio_dt = transformar_a_datetime(inicio)
                break
            else:
                pass
        while True:
            print("Fecha de término: (AÑO-MES-DÍA HORA:MINUTOS:SEGUNDOS)")
            print("(De no rellenar se establecerá como una hora después "
                  "de la hora de inicio) ")
            final = input()
            if final == "":
                final_dt = inicio_dt + timedelta(hours=1)
                final = final_dt.isoformat(" ")
                break

            elif comprobar_fecha(final) is True:
                final_dt = transformar_a_datetime(final)
                if final_dt > inicio_dt:
                    break
                else:
                    print("La fecha de término debe ser "
                          "posterior a la de inicio")

        for evento in lista_eventos:
            if evento.nombre.strip("'") == nombre and evento.inicio == inicio \
                    and evento.final == final:
                posible = "no"
            else:
                pass
        if posible == "si":
            break
        else:
            print("No se puede crear el evento debido a que ya existe uno "
                  "con el mismo nombre, fecha de inicio y fecha de término")
            while True:
                print()
                salir = input("Volver a creación de evento (1) o Salir (-1): ")
                print()
                if salir == "1" or salir == "-1":
                    break
                else:
                    print("Solo puedes ingresar (1) o (2)")
        if salir == "-1":
            break
        else:
            pass

    while True:
        descripcion = input("Descripcion: ")
        if descripcion == "":
            descripcion = "sin descripción"
            break
        else:
            break
    while True:
        invitados = input("Ingrese el o los invitados separandolos con (,): ")
        if invitados == "":
            invitados = "sin invitados"
            break
        elif verificar_destinatarios(invitados, usuarios) is True:
            break
        else:
            pass

    if invitados == "sin invitados":
        invitados_final = "sin invitados"
        pass
    else:
        lista_invitados = invitados.split(",")
        invitados_final = ""
        for invitado in lista_invitados:
            invitados_final = invitados_final + invitado + ";"

        invitados_final = invitados_final[0:len(invitados_final) - 1]

    while True:
        etiquetas = input("Ingrese la o las etiquetas separandolas con (,): ")

        if etiquetas == "":
            etiquetas = "sin etiquetas"
            break
        elif ";" in etiquetas:
            print("Las etiquetas deben estar separadas por (,)"
                  " y no pueden contener (;)")
        else:
            break

    if etiquetas == "sin etiquetas":
        etiquetas_final = "sin etiquetas"

    else:
        lista_etiquetas = etiquetas.split(",")
        etiquetas_final = ""
        for etiqueta in lista_etiquetas:
            etiquetas_final = etiquetas_final + etiqueta + ";"

        etiquetas_final = etiquetas_final[0:len(etiquetas_final) - 1]

    while True:
        print()
        print("¿Deseas ver una vista previa de tu evento? (1): Si (-1): No")
        preview = input()

        if preview == "1":
            print()
            print("-" * 84)
            print("Dueño:", dueño)
            print("Nombre:", nombre)
            print("Fecha inicio:", inicio_dt.isoformat(" "))
            print("Fecha término:", final_dt.isoformat(" "))
            print("Descripción:", descripcion)
            print("Invitados:", invitados_final)
            print("Etiquetas:", etiquetas_final)
            print("-" * 84)
            print()
            break
        elif preview == "-1":
            break
        else:
            print("Debes ingresar (1) o (-1)")

    while True:
        print()
        guardar = input("Guardar (1) o Borrar (-1): ")

        if guardar == "1":

            path = "data/db_events.csv"
            evento_final = str(dueño + "," + "'" + nombre + "'" + "," +
                               inicio + "," + final + "," +
                               "'" + descripcion + "'" + "," +
                               invitados_final + "," + etiquetas_final)
            with open(path, "a", encoding="utf-8") as archivo:
                archivo.write("\n")
                archivo.write(evento_final)

            print()
            print("Evento guardado exitosaamente")
            print()

            return

        elif guardar == "-1":

            print()
            print("Evento no guardado")
            print()

            return

        else:
            print("Debes ingresar (1) o (-1)")


def mostrar_evento(usuario, numero_evento, dicc_usuario_evento):
    evento = dicc_usuario_evento[usuario][int(numero_evento) - 1]
    print()
    print("-" * 84)
    print("Dueño:", evento.dueño)
    print("Nombre:", evento.nombre.strip("'"))
    print("Fecha inicio:", evento.inicio.isoformat(" "))
    print("Fecha término:", evento.final.isoformat(" "))
    print("Descripción:", evento.descripcion.strip("'"))
    print("Invitados:", ", ".join(evento.invitados))
    print("Etiquetas:", ", ".join(evento.etiquetas))
    print("-" * 84)
    print()


def ingresar_evento(lista_str_numeros):
    while True:
        numero_evento = input("Selecciona el número del evento deseado: ")

        if numero_evento not in lista_str_numeros:
            print("Debes introducir uno de los números habilitados ")

        else:
            print()
            return numero_evento


def editar_evento(usuario, usuarios, dicc_usuario_evento, numero_evento,
                  lista_eventos, archivo_a_sobreescribir):
    evento = dicc_usuario_evento[usuario][int(numero_evento) - 1]
    if evento.dueño != usuario:
        print("Solo el dueño de un evento puede editarlo")

    else:
        while True:
            mostrar_evento(usuario, numero_evento, dicc_usuario_evento)
            print("¿Que componente deseas editar? "
                  "(si deseas salir ingresa (-1))")
            print("Nombre (1), Inicio (2), Término (3), Descripción (4), "
                  "Invitados (5), Etiquetas (6)")
            componente = input("Ingresa el número: ")
            if componente == "-1":
                break
            elif componente == "1":
                nuevo_nombre = input("Introduce el nuevo nombre: ")
                nuevo_nombre = "'" + nuevo_nombre + "'"
                evento = dicc_usuario_evento[usuario][
                    int(numero_evento) - 1]
                nuevo_evento = Evento(evento.dueño, nuevo_nombre, evento.inicio,
                                      evento.final, evento.descripcion,
                                      evento.invitados, evento.etiquetas)

                posible = "si"
                for evento in lista_eventos:
                    if evento.nombre == nuevo_evento.nombre and\
                            evento.inicio == nuevo_evento.inicio and\
                            evento.final == nuevo_evento.final:
                        posible = "no"
                    else:
                        pass

                if posible == "no":
                    print("No se puede editar el evento debido a que ya existe "
                          "uno con el mismo nombre, fecha de inicio y fecha de "
                          "término")

                else:
                    evento = dicc_usuario_evento[usuario][
                        int(numero_evento) - 1]
                    lista_eventos2 = lista_eventos[::-1]
                    index_evento = lista_eventos2.index(evento)
                    lista_eventos2[index_evento] = nuevo_evento
                    path = "data/" + archivo_a_sobreescribir
                    with open(path, "w", encoding="utf-8") as archivo:
                        archivo.write("owner,name,start,finish,description,"
                                      "invited,tags")
                        for evento in lista_eventos2:
                            archivo.write("\n")
                            archivo.write(evento.dueño + "," +
                                          evento.nombre + "," +
                                          evento.inicio.isoformat(" ") + "," +
                                          evento.final.isoformat(" ") + "," +
                                          evento.descripcion + "," +
                                          ";".join(evento.invitados) + "," +
                                          ";".join(evento.etiquetas))
                    print()
                    print("Nombre cambiado exitosamente")
                break

            elif componente == "2":
                nuevo_inicio = input("Introduce la nueva fecha de inicio: ")
                if comprobar_fecha(nuevo_inicio) is True:
                    inicio_dt = transformar_a_datetime(nuevo_inicio)
                    if inicio_dt < evento.final:
                        evento = dicc_usuario_evento[usuario][
                            int(numero_evento) - 1]
                        nuevo_evento = Evento(evento.dueño, evento.nombre,
                                              inicio_dt, evento.final,
                                              evento.descripcion,
                                              evento.invitados,
                                              evento.etiquetas)
                        posible = "si"
                        for evento in lista_eventos:
                            if evento.nombre == nuevo_evento.nombre and \
                                    evento.inicio == nuevo_evento.inicio and \
                                    evento.final == nuevo_evento.final:
                                posible = "no"
                            else:
                                pass

                        if posible == "no":
                            print("No se puede editar el evento debido a que ya"
                                  " existe uno con el mismo nombre, fecha de "
                                  "inicio y fecha de término")

                        else:
                            evento = dicc_usuario_evento[usuario][
                                int(numero_evento) - 1]
                            lista_eventos2 = lista_eventos[::-1]
                            index_evento = lista_eventos2.index(evento)
                            lista_eventos2[index_evento] = nuevo_evento
                            path = "data/" + archivo_a_sobreescribir
                            with open(path, "w", encoding="utf-8") as archivo:
                                archivo.write(
                                    "owner,name,start,finish,description,"
                                    "invited,tags")
                                for evento in lista_eventos2:
                                    archivo.write("\n")
                                    archivo.write(evento.dueño + "," +
                                                  evento.nombre + "," +
                                                  evento.inicio.isoformat(" ")
                                                  + "," +
                                                  evento.final.isoformat(" ")
                                                  + "," +
                                                  evento.descripcion + "," +
                                                  ";".join(evento.invitados)
                                                  + "," +
                                                  ";".join(evento.etiquetas))
                            print()
                            print("Fecha de inicio cambiada exitosamente")
                    else:
                        print("La fecha de inicio debe ser "
                              "anterior a la de término")

                else:
                    pass

                break

            elif componente == "3":

                nuevo_final = input("Introduce la nueva fecha de término: ")
                if comprobar_fecha(nuevo_final) is True:
                    final_dt = transformar_a_datetime(nuevo_final)
                    if final_dt > evento.inicio:
                        evento = dicc_usuario_evento[usuario][
                            int(numero_evento) - 1]
                        nuevo_evento = Evento(evento.dueño, evento.nombre,
                                              evento.inicio, final_dt,
                                              evento.descripcion,
                                              evento.invitados,
                                              evento.etiquetas)
                        posible = "si"
                        for evento in lista_eventos:
                            if evento.nombre == nuevo_evento.nombre and \
                                    evento.inicio == nuevo_evento.inicio and \
                                    evento.final == nuevo_evento.final:
                                posible = "no"
                            else:
                                pass

                        if posible == "no":
                            print(
                                "No se puede editar el evento debido a que ya "
                                "existe uno con el mismo nombre, fecha de "
                                "inicio y fecha de término")

                        else:
                            evento = dicc_usuario_evento[usuario][
                                int(numero_evento) - 1]
                            lista_eventos2 = lista_eventos[::-1]
                            index_evento = lista_eventos2.index(evento)
                            lista_eventos2[index_evento] = nuevo_evento
                            path = "data/" + archivo_a_sobreescribir
                            with open(path, "w", encoding="utf-8") as archivo:
                                archivo.write(
                                    "owner,name,start,finish,description,"
                                    "invited,tags")
                                for evento in lista_eventos2:
                                    archivo.write("\n")
                                    archivo.write(evento.dueño + "," +
                                                  evento.nombre + "," +
                                                  evento.inicio.isoformat(" ")
                                                  + "," +
                                                  evento.final.isoformat(" ")
                                                  + "," +
                                                  evento.descripcion + "," +
                                                  ";".join(evento.invitados)
                                                  + "," +
                                                  ";".join(evento.etiquetas))
                            print()
                            print("Fecha de término cambiada exitosamente")

                    else:
                        print("La fecha de término debe ser "
                              "posterior a la de inicio")

                break
            elif componente == "4":
                nueva_descripcion = input("Introduzca la nueva descripción: ")
                nueva_descripcion = "'" + nueva_descripcion + "'"
                evento = dicc_usuario_evento[usuario][
                    int(numero_evento) - 1]
                nuevo_evento = Evento(evento.dueño, evento.nombre,
                                      evento.inicio, evento.final,
                                      nueva_descripcion, evento.invitados,
                                      evento.etiquetas)

                lista_eventos2 = lista_eventos[::-1]
                index_evento = lista_eventos2.index(evento)
                lista_eventos2[index_evento] = nuevo_evento
                path = "data/" + archivo_a_sobreescribir
                with open(path, "w", encoding="utf-8") as archivo:
                    archivo.write("owner,name,start,finish,description,"
                                  "invited,tags")
                    for evento in lista_eventos2:
                        archivo.write("\n")
                        archivo.write(evento.dueño + "," +
                                      evento.nombre + "," +
                                      evento.inicio.isoformat(" ") + "," +
                                      evento.final.isoformat(" ") + "," +
                                      evento.descripcion + "," +
                                      ";".join(evento.invitados) + "," +
                                      ";".join(evento.etiquetas))

                print()
                print("Descripción cambiada exitosamente")
                break
            elif componente == "5":
                while True:
                    print("Antiguos invitados:", evento.invitados)
                    print("Introduzca los nuevos invitados "
                          "(Separados por (,)): ")
                    nuevos_invitados = input()

                    if nuevos_invitados == "":
                        nuevos_invitados = "sin invitados"
                        break
                    elif verificar_destinatarios(nuevos_invitados, usuarios) \
                            is True:
                        break
                    else:
                        pass
                if nuevos_invitados == "sin invitados":
                    lista_invitados = ["sin invitados"]
                    pass
                else:
                    lista_invitados = nuevos_invitados.split(",")

                evento = dicc_usuario_evento[usuario][
                    int(numero_evento) - 1]
                nuevo_evento = Evento(evento.dueño, evento.nombre,
                                      evento.inicio, evento.final,
                                      evento.descripcion, lista_invitados,
                                      evento.etiquetas)
                lista_eventos2 = lista_eventos[::-1]
                index_evento = lista_eventos2.index(evento)
                lista_eventos2[index_evento] = nuevo_evento
                path = "data/" + archivo_a_sobreescribir
                with open(path, "w", encoding="utf-8") as archivo:
                    archivo.write("owner,name,start,finish,description,"
                                  "invited,tags")
                    for evento in lista_eventos2:
                        archivo.write("\n")
                        archivo.write(evento.dueño + "," +
                                      evento.nombre + "," +
                                      evento.inicio.isoformat(" ") + "," +
                                      evento.final.isoformat(" ") + "," +
                                      evento.descripcion + "," +
                                      ";".join(evento.invitados) + "," +
                                      ";".join(evento.etiquetas))

                print()
                print("Invitados cambiados exitosamente")
                break

            elif componente == "6":
                while True:
                    print("Introduzca las nuevas etiquetas (Separados por (,) ")
                    nuevas_etiquetas = input()
                    if nuevas_etiquetas == "":
                        nuevas_etiquetas = "sin etiquetas"
                        break
                    elif ";" in nuevas_etiquetas:
                        print("Las etiquetas deben estar separadas por (,)"
                              " y no pueden contener (;)")
                    else:
                        break

                if nuevas_etiquetas == "sin etiquetas":
                    etiquetas_final = "sin etiquetas"
                    lista_etiquetas = [etiquetas_final]

                else:
                    lista_etiquetas = nuevas_etiquetas.split(",")

                evento = dicc_usuario_evento[usuario][
                    int(numero_evento) - 1]
                nuevo_evento = Evento(evento.dueño, evento.nombre,
                                      evento.inicio, evento.final,
                                      evento.descripcion, evento.invitados,
                                      lista_etiquetas)
                lista_eventos2 = lista_eventos[::-1]
                index_evento = lista_eventos2.index(evento)
                lista_eventos2[index_evento] = nuevo_evento
                path = "data/" + archivo_a_sobreescribir
                with open(path, "w", encoding="utf-8") as archivo:
                    archivo.write("owner,name,start,finish,description,"
                                  "invited,tags")
                    for evento in lista_eventos2:
                        archivo.write("\n")
                        archivo.write(evento.dueño + "," +
                                      evento.nombre + "," +
                                      evento.inicio.isoformat(" ") + "," +
                                      evento.final.isoformat(" ") + "," +
                                      evento.descripcion + "," +
                                      ";".join(evento.invitados) + "," +
                                      ";".join(evento.etiquetas))

                print()
                print("Etiquetas cambiadas exitosamente")
                break

            else:
                print("Solo puedes ingresar (1), (2), (3), (4),"
                      " (5), (6), o (-1)")

    pass
