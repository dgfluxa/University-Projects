from funciones import mostrar_menu, abrir_consulta, ingresar_consulta, \
    leer_output
from os import path

if __name__ == '__main__':
    try:
        print("Bienvenido a Cruncher Flights")
        if path.isfile("output.txt") is False:
            with open("output.txt", "w", encoding="utf-8") as archivo:
                archivo.write("Consultas:\n")
        while True:
            accion = mostrar_menu()
            if accion is "1":
                abrir_consulta()

            elif accion is "2":
                ingresar_consulta()

            elif accion is "3":
                leer_output()

    except KeyboardInterrupt():
        exit()
