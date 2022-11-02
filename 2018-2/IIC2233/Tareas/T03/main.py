
from clase_grafo import RedElectrica
from funciones import mostrar_menu



if __name__ == '__main__':
    print(f'''
{'-' * 25} Bienvenido a Electromatic {'-' * 25}
''')
    while True:
        tamaño = input("¿Que tamaño de archivos deseas leer? ")
        if tamaño == "small" or tamaño == "large":
            print(f"\nSe leerán los archivos de tamaño {tamaño}\n")
            break
        else:
            print(f"\nEl tamaño {tamaño} es inválido, por favor "
                  f"ingresar (small) o (large) \n")
    print("Por favor espere mientras se cargan los archivos\n")

    red = RedElectrica(tamaño)

    print("¡Listo! Los archivos se han cargado")

    mostrar_menu(red)



