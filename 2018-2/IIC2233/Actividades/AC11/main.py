import os


def buscar_archivo(nombre, cwd=os.getcwd()):
    for dirpath, dirnames, filenames in os.walk("."):
        if nombre in filenames:
            return dirpath + f"\{nombre}"


def leer_archivo(path):
    with open(path, "rb") as archivo:
        arch_b = bytearray(archivo.read())

    while arch_b:
        b = [arch_b[:1]]
        arch_b = arch_b[2:]



def decodificar(bits):
    pass


def escribir_archivo(ruta, chunks):
    pass


# Aquí puedes crear todas las funciones extra que requieras.


if __name__ == "__main__":
    nombre_archivo_de_pista = "himno.shrek"
    ruta_archivo_de_pista = buscar_archivo(nombre_archivo_de_pista)

    chunks_corruptos_himno = leer_archivo(ruta_archivo_de_pista)

    chunks_himno = [decodificar(chunk) for chunk in chunks_corruptos_himno]

    nombre_ubicacion_himno = "himno.png"
    escribir_archivo(nombre_ubicacion_himno, chunks_himno)
