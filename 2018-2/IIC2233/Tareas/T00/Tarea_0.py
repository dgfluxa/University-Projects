from crear import cargar_correos, cargar_eventos, cargar_usuarios, \
    crear_dicc_correos, crear_dicc_usuario_evento
from verificar import ingreso_usuario, revisar_usuario, revisar_contraseña
from correos import crear_usuario, crear_correo, bandeja_entrada
from eventos_2 import accion_calendario

# Funciones


def login(usuarios):

    while True:
        print()
        accion = input("¿Deseas ingresar a tu correo (1), crear uno "
                       "nuevo (2) o cerrar la página (-1)? ")

        if accion == "1":
            correo = input("Dirección de correo: ")
            contraseña = input("Contraseña: ")
            if ingreso_usuario(usuarios, correo, contraseña) is True:
                return correo
            else:
                pass

        elif accion == "2":

            while True:
                correo = input(
                    "Dirección de correo: ")
                if revisar_usuario(correo) is True:
                    break

            while True:
                contraseña = input("Contraseña: ")
                if revisar_contraseña(contraseña) is True:
                    break

            crear_usuario(usuarios, correo, contraseña)

        elif accion == "-1":
            print()
            print("-"*36, "Hasta luego", "-"*35)
            return False

        else:
            print("Debes ingresar (1), (2), o (-1) (sin paréntesis)")


def pantalla_principal(correo):
    while True:
        print()
        print("-"*84)
        print()
        print("Bienvenido al menú principal de DCCorreos", correo)
        print("Acciones disponibles: ")
        print("(1): Crear Correo")
        print("(2): Ingresar a la Bandeja de Entrada")
        print("(3): Ingresar a tu Calendario")
        print("(-1): Salir")
        accion = input("¿Que deseas hacer? ")
        if accion != "1" and accion != "2" and accion != "3" and accion != "-1":
            print("Debes ingresar (1), (2), (3), o (-1)")
        else:
            return accion


def mostrar_calendario(usuario, usuarios, dicc_usuario_eventos, lista_eventos,
                       archivo_a_leer):
    print()
    print("-"*84)
    print("Bienvenido a tu Calendario", usuario)
    print()
    print("Tus eventos en orden de creación (más reciente a más antiguo):")
    numero = 0
    lista_str_numeros = []
    for evento in dicc_usuario_eventos[usuario]:
        numero += 1
        lista_str_numeros.append(str(numero))
        print(str(numero) + ".-", evento.nombre)

    print()
    if accion_calendario(usuario, usuarios, dicc_usuario_eventos,
                         lista_eventos, archivo_a_leer, lista_str_numeros) \
            == "-1":
        return "-1"

# Programa


print()
print("-"*30, "Bienvenido a DCCorreos", "-"*30)
usuarios = cargar_usuarios("db_users.csv")
correos = cargar_correos("db_emails.csv")
eventos = cargar_eventos("db_events.csv")
dicc_correos = crear_dicc_correos(correos, usuarios)
dicc_usuario_evento = crear_dicc_usuario_evento(eventos, usuarios)


while True:

    usuario = login(usuarios)
    if usuario is False:
        break

    while True:

        accion = int(pantalla_principal(usuario))
        if accion == 1:
            dicc_correos = crear_correo(usuario, usuarios)
            correos = cargar_correos("db_emails.csv")

        elif accion == 2:
            while True:
                bandeja_entrada(dicc_correos, usuario)
                while True:
                    salir = input("Volver a la bandeja de entrada (1)"
                                  " o salir (-1) ")

                    if salir == "1":
                        break
                    elif salir == "-1":
                        break
                    else:
                        print("Solo puedes ingresar (1) o (-1)")
                if salir == "-1":
                    break

        elif accion == 3:
            while True:
                salir = mostrar_calendario(usuario, usuarios,
                                           dicc_usuario_evento, eventos,
                                           "db_events.csv")
                eventos = cargar_eventos("db_events.csv")
                dicc_usuario_evento = crear_dicc_usuario_evento(eventos,
                                                                usuarios)
                while True:
                    if salir == "-1":
                        break
                    print()
                    salir = input("Volver al calendario (1)"
                                  " o salir (-1) ")

                    if salir == "1":
                        break
                    elif salir == "-1":
                        break
                    else:
                        print("Solo puedes ingresar (1) o (-1)")
                if salir == "-1":
                    break

        elif accion == (-1):
            break
