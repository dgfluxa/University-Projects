from collections import namedtuple, defaultdict
from verificar import verificar_destinatarios, año_bisiesto, revisar_etiquetas
from eventos_1 import ingresar_evento, mostrar_evento, crear_evento, \
    editar_evento
Evento = namedtuple("Evento", ["dueño", "nombre", "inicio", "final",
                               "descripcion", "invitados", "etiquetas"])


def accion_calendario(usuario, usuarios, dicc_usuario_eventos, lista_eventos,
                      archivo_a_leer, lista_str_numeros):
    while True:
        accion = input("Ingresar a evento (1), Crear nuevo evento (2), "
                       "Editar (3), Eliminar(4), Invitar (5), "
                       "Filtrar Eventos (6), o Salir (-1): ")
        if accion != "1" and accion != "2" and accion != "3" and accion != "4" \
                and accion != "5" and accion != "6" and accion != "-1":
            print()
            print("Debes ingresar (1), (2), (3), (4), (5), (6) o (-1) ")
            print()

        elif accion == "-1":
            return "-1"

        elif accion == "1":
            if len(lista_str_numeros) == 0:
                print("No tienes eventos disponibles")
                break
            else:
                numero_evento = ingresar_evento(lista_str_numeros)
                mostrar_evento(usuario, numero_evento, dicc_usuario_eventos)
                break
        elif accion == "2":
            crear_evento(usuario, usuarios, lista_eventos)
            break
        elif accion == "3":
            if len(lista_str_numeros) == 0:
                print("No tienes eventos disponibles")
                break
            else:
                numero_evento = ingresar_evento(lista_str_numeros)
                editar_evento(usuario, usuarios, dicc_usuario_eventos,
                              numero_evento, lista_eventos, archivo_a_leer)
                break
        elif accion == "4":
            if len(lista_str_numeros) == 0:
                print("No tienes eventos disponibles")
                break
            else:
                numero_evento = ingresar_evento(lista_str_numeros)
                eliminar_evento(usuario, dicc_usuario_eventos,
                                numero_evento, lista_eventos, archivo_a_leer)
                break
        elif accion == "5":
            if len(lista_str_numeros) == 0:
                print("No tienes eventos disponibles")
                break
            else:
                numero_evento = ingresar_evento(lista_str_numeros)
                invitar_a_evento(usuario, usuarios, dicc_usuario_eventos,
                                 numero_evento, lista_eventos, archivo_a_leer)
                break
        elif accion == "6":
            if len(lista_str_numeros) == 0:
                print("No tienes eventos disponibles para filtrar")
                break
            else:
                filtrar_eventos(usuario, usuarios, dicc_usuario_eventos,
                                lista_eventos, archivo_a_leer)
                break


def eliminar_evento(usuario, dicc_usuario_evento, numero_evento, lista_eventos,
                    archivo_a_sobreescribir):
    evento = dicc_usuario_evento[usuario][int(numero_evento) - 1]
    if evento.dueño != usuario:
        print("Solo el dueño de un evento puede eliminarlo")

    else:
        while True:
            print("¿Estas seguro de querer eliminar el evento",
                  str(evento.nombre) + "?")
            verificar = input("Si (1) No (-1): ")
            if verificar == "1":

                lista_eventos.remove(evento)

                path = "data/" + archivo_a_sobreescribir
                with open(path, "w", encoding="utf-8") as archivo:
                    archivo.write("owner,name,start,finish,"
                                  "description,invited,tags")
                    for evento in lista_eventos:
                        archivo.write("\n")
                        archivo.write(evento.dueño + "," + evento.nombre + "," +
                                      evento.inicio + "," + evento.final + "," +
                                      evento.descripcion + "," +
                                      evento.invitados + "," + evento.etiquetas)
                print("Evento eliminado exitosamente")
                return

            elif verificar == "-1":
                print("Evento no eliminado")
                return
            else:
                print("Solo puedes ingresar (1) o (-1)")


def invitar_a_evento(usuario, usuarios, dicc_usuario_evento, numero_evento,
                     lista_eventos, archivo_a_sobreescribir):
    evento = dicc_usuario_evento[usuario][int(numero_evento) - 1]
    if evento.dueño != usuario:
        print("Solo el dueño de un evento puede invitar más personas a este")
        return
    else:
        pass

    if evento.invitados != "sin invitados":
        lista_invitados = evento.invitados.split(";")
    else:
        lista_invitados = []

    while True:
        print("Invitados actuales:", evento.invitados)
        print("Ingresar nuevos invitados separados por (,): "
              "(Si desea salir ingrese (-1)")
        nuevos_invitados = input()
        if nuevos_invitados == "-1":
            return

        elif verificar_destinatarios(nuevos_invitados, usuarios) is True:
            lista_nuevos_invitados = nuevos_invitados.split(",")
            for nuevo_invitado in lista_nuevos_invitados:
                if nuevo_invitado in lista_invitados:
                    print("El usuario", nuevo_invitado, "ya estaba invitado")
                    print("Por favor vuelva a ingresar a los invitados")
                    print()
                    nuevos_invitados = ""
                else:
                    pass
            if nuevos_invitados != "":
                break
            else:
                pass
        else:
            pass

    while True:
        print()
        print("Nuevos invitados:", nuevos_invitados)
        invitar = input("Invitar (1) o Salir (-1) ")
        if invitar == "-1":
            print("Los usuarios ingresados no han sido invitados")
            return
        elif invitar == "1":

            lista_invitados_final = []
            lista_invitados_final.extend(lista_invitados)
            lista_invitados_final.extend(lista_nuevos_invitados)
            print(lista_invitados_final)

            invitados_final = ";".join(lista_invitados_final)

            index_evento = lista_eventos.index(evento)
            lista_eventos[index_evento] = Evento(evento.dueño, evento.nombre,
                                                 evento.inicio, evento.final,
                                                 evento.descripcion,
                                                 invitados_final,
                                                 evento.etiquetas)
            path = "data/" + archivo_a_sobreescribir
            with open(path, "w", encoding="utf-8") as archivo:
                archivo.write("owner,name,start,finish,"
                              "description,invited,tags")
                for evento in lista_eventos:
                    archivo.write("\n")
                    archivo.write(evento.dueño + "," + evento.nombre + "," +
                                  evento.inicio + "," + evento.final + "," +
                                  evento.descripcion + "," +
                                  evento.invitados + "," + evento.etiquetas)
            print("Usuarios invitados exitosamente")
            return
        else:
            print("Solo puedes ingresar (1) o (-1)")


def filtrar_eventos(usuario, usuarios, dicc_usuario_evento, lista_eventos,
                    archivo_a_leer):
    nombre = ""
    año = ""
    mes = ""
    dia = ""
    etiquetas = ""
    while True:
        print("¿De acuerdo a que atributo desea filtrar sus eventos?")
        print("Nombre (1), Fecha de inicio (2), o Etiquetas (3) "
              "((-1) para salir)")
        atributo = input()
        if atributo == "-1":
            break
        elif atributo == "1":
            nombre = input("Ingresa el nombre deseado: ")
            break

        elif atributo == "2":
            año = ""
            mes = ""
            dia = ""
            while True:
                print("Filtrar por año (1), año-mes (2), "
                      "año-mes-dia (3)")
                filtro_fecha = input()

                if filtro_fecha == "1":
                    while True:
                        año = input("Ingrese el año: ")
                        if año.isnumeric() is False:
                            print("Debes ingresar valores numéricos")

                        elif int(año) < 0 or int(año) > 9999:
                            print("Año inválido")

                        else:
                            año = int(año)
                            break
                    break

                elif filtro_fecha == "2":
                    while True:
                        año = input("Ingrese el año: ")
                        if año.isnumeric() is False:
                            print("Debes ingresar valores numéricos")

                        elif int(año) < 0 or int(año) > 9999:
                            print("Año inválido")

                        else:
                            año = int(año)
                            break

                    while True:
                        mes = input("Ingrese el mes: ")
                        if mes.isnumeric() is False:
                            print("Debes ingresar valores numéricos")

                        elif int(mes) < 1 or int(mes) > 12:
                            print("Mes inválido")

                        else:
                            mes = int(mes)
                            break
                    break

                elif filtro_fecha == "3":
                    meses_31_dias = (1, 3, 5, 7, 8, 10, 12)
                    while True:
                        año = input("Ingrese el año: ")
                        if año.isnumeric() is False:
                            print("Debes ingresar valores numéricos")

                        elif int(año) < 0 or int(año) > 9999:
                            print("Año inválido")

                        else:
                            año = int(año)
                            break
                    while True:
                        mes = input("Ingrese el mes: ")
                        if mes.isnumeric() is False:
                            print("Debes ingresar valores numéricos")

                        elif int(mes) < 1 or int(mes) > 12:
                            print("Mes inválido")

                        else:
                            mes = int(mes)
                            break
                    while True:
                        dia = input("Ingrese el dia: ")
                        if dia.isnumeric() is False:
                            print("Debes ingresar valores numéricos")

                        elif int(dia) < 1 or int(dia) > 31:
                            print("El día", dia, "no existe")

                        elif int(dia) > 30 and int(
                                mes) not in meses_31_dias:
                            print("El dia", dia, "no existe en el mes", mes)

                        elif int(dia) > 28 and int(mes) == 2:

                            if año_bisiesto(año) is False:
                                print("El dia", dia, "del mes", mes,
                                      "del año",
                                      año, "no existe")

                            else:
                                pass
                        else:
                            dia = int(dia)
                            break
                    break
                else:
                    print("Solo puedes ingresar (1), (2), o (3)")

            if filtro_fecha == "1" or filtro_fecha == "2" or \
                    filtro_fecha == "3":
                break

        elif atributo == "3":
            while True:
                print("Ingresa las etiquetas separadas por (,)")
                etiquetas = input()
                if ";" in etiquetas:
                    print("Las etiquetas deben estar separadas por (,)"
                          " y no pueden contener (;)")
                else:
                    lista_etiquetas = etiquetas.split(",")
                    etiquetas_final = ";".join(lista_etiquetas)
                    break
            break

        else:
            print("Solo puedes ingresar (1), (2), (3), o (-1)")
    lista_eventos_filtrados = []
    if nombre != "":
        for evento in dicc_usuario_evento[usuario]:
            if nombre == evento.nombre.strip("'") \
                    and evento not in lista_eventos_filtrados:
                lista_eventos_filtrados.append(evento)
            else:
                pass
    if año != "":
        if mes != "":
            if dia != "":
                for evento in dicc_usuario_evento[usuario]:
                    if año == evento.inicio.year and \
                            mes == evento.inicio.month and\
                            dia == evento.inicio.day and\
                            evento not in lista_eventos_filtrados:
                        lista_eventos_filtrados.append(evento)
            else:
                for evento in dicc_usuario_evento[usuario]:
                    if año == evento.inicio.year and mes == evento.inicio.month\
                            and evento not in lista_eventos_filtrados:
                        lista_eventos_filtrados.append(evento)
        else:
            for evento in dicc_usuario_evento[usuario]:
                if año == evento.inicio.year and evento \
                        not in lista_eventos_filtrados:
                    lista_eventos_filtrados.append(evento)

    if etiquetas != "":
        for evento in dicc_usuario_evento[usuario]:
            agregar = revisar_etiquetas(evento, etiquetas_final,
                                        lista_eventos_filtrados)
            if agregar is True:
                lista_eventos_filtrados.append(evento)
            else:
                pass

    if len(lista_eventos_filtrados) == 0:
        print("No existen eventos que cumplan con dichos filtros")
        return

    diccionario = defaultdict(list)

    for evento in lista_eventos_filtrados:
        diccionario[usuario].append(evento)

    numero = 0
    lista_str_numeros = []
    print()
    print("-"*84)
    print("Eventos filtrados:")
    print("(En caso de querer seguir filtrando se considerarán "
          "estos eventos ya filtrados)")
    print()
    for evento in diccionario[usuario]:
        numero += 1
        lista_str_numeros.append(str(numero))
        print(str(numero) + ".-", evento.nombre)

    print()
    if accion_calendario(usuario, usuarios, diccionario,
                         lista_eventos, archivo_a_leer,
                         lista_str_numeros) == "-1":
        return
