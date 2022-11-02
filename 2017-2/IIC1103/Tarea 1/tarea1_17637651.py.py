from Tarea_1 import *

root = tk.Tk()
root.geometry('{}x{}'.format("550", "650"))
app = Application(master=root)


def partida():
    # cartones

    f = 0
    c = 0
    j = 1
    #Desmarcar cartones
    while True:
        app.marcar_numero(f,c,False,j)
        f+=1
        if f==5:
            f=0
            c+=1
            if c==5:
                f=0
                c=0
                j+=1
                if j==3:
                    break

    f = 0
    c = 0
    j = 1

    app.reiniciar_contador()
    while True:
        numero = random.randint(1 + (20 * c), 20 + (20 * c))
        if app.agregar(numero) == True:
            app.colocar_numero(f, c, numero, j)
            f += 1
        if f == 5:
            f = 0
            c += 1
        if c == 5:
            c = 0
            j += 1
            app.reiniciar_contador()
        if j == 3:
            break

    apuesta1 = 0
    while apuesta1 <= 0 or apuesta1 > app.preguntar_monto(1):
        apuesta1 = int(input("Apuesta Jugador 1: "))
        if apuesta1 > 0 and apuesta1 <= app.preguntar_monto(1):
            app.mostrar_dinero(1, app.preguntar_monto(1) - apuesta1)
            break
        elif app.preguntar_monto(1) < apuesta1:
            print("La apuesta debe ser menor o igual al monto disponible")
        elif apuesta1 <= 0:
            print("La apuesta debe ser un número positivo")

    apuesta2 = 0
    while apuesta2 <= 0 or apuesta2 > app.preguntar_monto(2):
        apuesta2 = int(input("Apuesta Jugador 2: "))
        if apuesta2 > 0 and apuesta2 <= app.preguntar_monto(2):
            app.mostrar_dinero(2, app.preguntar_monto(2) - apuesta2)
            break
        elif app.preguntar_monto(2) < apuesta2:
            print("La apuesta debe ser menor o igual al monto disponible")
        elif apuesta2 <= 0:
            print("La apuesta debe ser un número positivo")

    app.poner_apuesta(apuesta1 + apuesta2)
    app.mostrar_mensaje("Pozo: " + str(apuesta1 + apuesta2))
    app.mostrar_ventana(True)


def preguntar(x):
    while True:
        if app.preguntar_monto(1) > 0 and app.preguntar_monto(2) > 0:
            respuesta = input("¿Jugar otra partida? ")
            if respuesta.lower().strip() == "si":
                print("Monto actual Jugador 1:", app.preguntar_monto(1))
                print("Monto actual Jugador 2:", app.preguntar_monto(2))
                x = 1

            elif respuesta.lower().strip() == "no":
                x = -1
                if app.preguntar_monto(1) > app.preguntar_monto(2):
                    print("Monto final Jugador 1:", app.preguntar_monto(1))
                    print("Monto final Jugador 2:", app.preguntar_monto(2))
                    print("Ganador final: Jugador 1")
                    app.cerrar_ventana()
                    break
                elif app.preguntar_monto(2) > app.preguntar_monto(1):
                    print("Monto final Jugador 1:", app.preguntar_monto(1))
                    print("Monto final Jugador 2:", app.preguntar_monto(2))
                    print("Ganador final: Jugador 2")
                    app.cerrar_ventana()
                    break
                elif app.preguntar_monto(1) == app.preguntar_monto(2):
                    print("Monto final Jugador 1:", app.preguntar_monto(1))
                    print("Monto final Jugador 2:", app.preguntar_monto(2))
                    print("Los jugadores han empatado")
                    app.cerrar_ventana()
                    break
            else:
                print("Debe ingresar si o no")
            if x==1:
                partida()
                break

        elif app.preguntar_monto(1) > app.preguntar_monto(2):
            print("Monto final Jugador 1:", app.preguntar_monto(1))
            print("Monto final Jugador 2:", app.preguntar_monto(2))
            print("Ganador final: Jugador 1")
            print("El BINGO ha finalizado, hasta luego")
            app.cerrar_ventana()
            break
        elif app.preguntar_monto(2) > app.preguntar_monto(1):
            print("Monto final Jugador 1:", app.preguntar_monto(1))
            print("Monto final Jugador 2:", app.preguntar_monto(2))
            print("Ganador final: Jugador 2")
            print("El BINGO ha finalizado, hasta luego")
            app.cerrar_ventana()
            break
        elif app.preguntar_monto(1) == app.preguntar_monto(2):
            print("Monto final Jugador 1:", app.preguntar_monto(1))
            print("Monto final Jugador 2:", app.preguntar_monto(2))
            print("Los jugadores han empatado")
            print("El BINGO ha finalizado, hasta luego")
            app.cerrar_ventana()
            break



def turno():
    x=0
    n = 0
    while True:  # Bolita
        numero = random.randint(1, 100)
        if app.agregar(numero) == True:
            app.mostrar_mensaje("Número: " + str(numero))
            n += 1
        if n == 1:
            break
    n = 0
    m = 0
    while True:  # Marcar número
        if numero > 80 and numero == int(app.obtener_numero(m, 4, 1 + n)):
            app.marcar_numero(m, 4, True, 1 + n)
        elif numero > 60 and numero == int(app.obtener_numero(m, 3, 1 + n)):
            app.marcar_numero(m, 3, True, 1 + n)
        elif numero > 40 and numero == int(app.obtener_numero(m, 2, 1 + n)):
            app.marcar_numero(m, 2, True, 1 + n)
        elif numero > 20 and numero == int(app.obtener_numero(m, 1, 1 + n)):
            app.marcar_numero(m, 1, True, 1 + n)
        elif numero > 0 and numero == int(app.obtener_numero(m, 0, 1 + n)):
            app.marcar_numero(m, 0, True, 1 + n)
        m += 1
        if m == 5 and n != 1:
            n += 1
            m = 0
        elif m == 5 and n == 1:
            n = 0
            m = 0
            break
    # revisar si esta marcado
    entero = 1
    y = 1
    diag = 1
    j1 = 0
    j2 = 0
    j = 1
    if app.esta_marcado(0, 0, j) == True and app.esta_marcado(0, 1, j) == True and app.esta_marcado(0, 2,
                                                                                                    j) == True and app.esta_marcado(
            0, 3, j) == True and app.esta_marcado(0, 4, j) == True and app.esta_marcado(1, 0,
                                                                                        j) == True and app.esta_marcado(
            1, 1, j) == True and app.esta_marcado(1, 2, j) == True and app.esta_marcado(1, 3,
                                                                                        j) == True and app.esta_marcado(
            1, 4, j) == True and app.esta_marcado(2, 0, j) == True and app.esta_marcado(2, 1,
                                                                                        j) == True and app.esta_marcado(
            2, 2, j) == True and app.esta_marcado(2, 3, j) == True and app.esta_marcado(2, 4,
                                                                                        j) == True and app.esta_marcado(
            3, 0, j) == True and app.esta_marcado(3, 1, j) == True and app.esta_marcado(3, 2,
                                                                                        j) == True and app.esta_marcado(
            3, 3, j) == True and app.esta_marcado(3, 4, j) == True and app.esta_marcado(4, 0,
                                                                                        j) == True and app.esta_marcado(
            4, 1, j) == True and app.esta_marcado(4, 2, j) == True and app.esta_marcado(4, 3,
                                                                                        j) == True and app.esta_marcado(
            4, 4, j) == True:
        j1 += 1
    j = 2
    if app.esta_marcado(0, 0, j) == True and app.esta_marcado(0, 1, j) == True and app.esta_marcado(0, 2,
                                                                                                    j) == True and app.esta_marcado(
            0, 3, j) == True and app.esta_marcado(0, 4, j) == True and app.esta_marcado(1, 0,
                                                                                        j) == True and app.esta_marcado(
            1, 1, j) == True and app.esta_marcado(1, 2, j) == True and app.esta_marcado(1, 3,
                                                                                        j) == True and app.esta_marcado(
            1, 4, j) == True and app.esta_marcado(2, 0, j) == True and app.esta_marcado(2, 1,
                                                                                        j) == True and app.esta_marcado(
            2, 2, j) == True and app.esta_marcado(2, 3, j) == True and app.esta_marcado(2, 4,
                                                                                        j) == True and app.esta_marcado(
            3, 0, j) == True and app.esta_marcado(3, 1, j) == True and app.esta_marcado(3, 2,
                                                                                        j) == True and app.esta_marcado(
            3, 3, j) == True and app.esta_marcado(3, 4, j) == True and app.esta_marcado(4, 0,
                                                                                        j) == True and app.esta_marcado(
            4, 1, j) == True and app.esta_marcado(4, 2, j) == True and app.esta_marcado(4, 3,
                                                                                        j) == True and app.esta_marcado(
            4, 4, j) == True:
        j2 += 1
    j = 1
    if app.esta_marcado(0, 0, j) == True and app.esta_marcado(1, 1, j) == True and app.esta_marcado(2, 2,
                                                                                                    j) == True and app.esta_marcado(
            3, 3, j) == True and app.esta_marcado(4, 2, j) == True and app.esta_marcado(1, 3,
                                                                                        j) == True and app.esta_marcado(
            0, 4, j) == True:
        j1 += 1
    j = 2
    if app.esta_marcado(0, 0, j) == True and app.esta_marcado(1, 1, j) == True and app.esta_marcado(2, 2,
                                                                                                    j) == True and app.esta_marcado(
            3, 3, j) == True and app.esta_marcado(4, 2, j) == True and app.esta_marcado(1, 3,
                                                                                        j) == True and app.esta_marcado(
            0, 4, j) == True:
        j2 += 1
    j = 1
    if app.esta_marcado(0, 0, j) == True and app.esta_marcado(1, 1, j) == True and app.esta_marcado(2, 2,
                                                                                                    j) == True and app.esta_marcado(
            3, 3, j) == True and app.esta_marcado(4, 4, j) == True:
        j1 += 1
    j = 2
    if app.esta_marcado(0, 0, j) == True and app.esta_marcado(1, 1, j) == True and app.esta_marcado(2, 2,
                                                                                                    j) == True and app.esta_marcado(
            3, 3, j) == True and app.esta_marcado(4, 4, j) == True:
        j2 += 1

    if j1 == j2 and j1 > 0:
        j1 = 0
        j2 = 0
        app.mostrar_mensaje("*" * 10 + " Empate " + "*" * 10)
        print("*" * 10 + " Empate " + "*" * 10)
        app.mostrar_dinero(1, app.preguntar_monto(1) + apuesta1)
        app.mostrar_dinero(2, app.preguntar_monto(2) + apuesta2)
        app.mostrar_ventana(True)
        app.after(1500)
        app.mostrar_ventana(False)
        preguntar(x)


    if j1 > j2 and j1 > 0:
        j1 = 0
        j2 = 0
        app.mostrar_mensaje("*" * 10 + " Jugador 1 gana la partida " + "*" * 10)
        print("*" * 10 + " Jugador 1 gana la partida " + "*" * 10)
        app.mostrar_dinero(1, app.preguntar_monto(1) + app.obtener_apuesta())
        app.mostrar_ventana(True)
        app.after(1500)
        app.mostrar_ventana(False)
        preguntar(x)


    if j2 > j1 and j2 > 0:
        j1 = 0
        j2 = 0
        app.mostrar_mensaje("*" * 10 + " Jugador 2 gana la partida " + "*" * 10)
        print("*" * 10 + " Jugador 2 gana la partida" + "*" * 10)
        app.mostrar_dinero(2, app.preguntar_monto(2) + app.obtener_apuesta())
        app.mostrar_ventana(True)
        app.after(1500)
        app.mostrar_ventana(False)
        preguntar(x)



# Aqui empieza su programa

import random

x=0

print("Hola, para iniciar el BINGO debe ingresar el monto inicial para cada jugador.")

monto1 = 0
while monto1 <= 0:
    monto1 = int(input("Monto Jugador 1: "))
    if monto1 > 0:
        app.mostrar_dinero(1, monto1)
    else:
        print("El monto debe ser un número positivo")

monto2 = 0
while monto2 <= 0:
    monto2 = int(input("Monto Jugador 2: "))
    if monto2 > 0:
        app.mostrar_dinero(2, monto2)
    else:
        print("El monto debe ser un número positivo")

print("Ahora comenzará la partida")

partida()





# ESTO NO SE TOCA
app.button.config(command=turno)
app.mainloop()
