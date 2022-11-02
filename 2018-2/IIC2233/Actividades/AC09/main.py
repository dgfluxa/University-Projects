import threading
import time
from itertools import chain
from random import randint, random
from queue import Queue


lock = threading.Lock()

cola_atacados = Queue()


class Hacker(threading.Thread):
    def __init__(self, nombre_equipo):
        super().__init__()
        self.tiempo = randint(4, 12)
        self.daemon = True
        self.desencriptado = False
        self.listo = threading.Event()
        self.equipo = nombre_equipo
        self.lock = threading.Lock()

    def run(self):
        while True:
            self.tiempo -= 1
            if self.tiempo == 0:
                with self.lock:
                    print(f"{self.equipo}: El hacker ha terminado "
                          f"la desencriptación")
                    self.desencriptado = True
                    self.listo.set()
                    break
            time.sleep(1)


class Cracker(threading.Thread):
    def __init__(self, nombre_equipo):
        super().__init__()
        self.velocidad = randint(5, 15)
        self.daemon = True
        self.listo = threading.Event()
        self.atacado = False
        self.lineas_codigo = 0
        self.equipo = nombre_equipo
        self.lock = threading.Lock()

    def run(self):
        while True:
            if self.atacado is False:
                if random() < 0.2:
                    with self.lock:
                        self.atacado = True
                        cola_atacados.put(self)
                else:
                    self.lineas_codigo += self.velocidad
                    if self.lineas_codigo >= 50:
                        with self.lock:
                            print(f"{self.equipo}: El cracker ha terminado "
                                  f"el código")
                            self.listo.set()
                            break
            time.sleep(1)


class Equipo(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.hacker = Hacker(nombre)
        self.cracker = Cracker(nombre)
        self.listo = False
        self.daemon = True
        self.termino = False

    def __str__(self):
        return f'''
        Equipo: {self.nombre}
        Lineas Cracker: {self.cracker.lineas_codigo}
        Desencriptado: {self.hacker.desencriptado}'''

    def run(self):
        self.hacker.start()
        self.cracker.start()
        self.hacker.listo.wait()
        self.cracker.listo.wait()
        self.termino = True


class Nebil(threading.Thread):
    def __init__(self):
        super().__init__()
        self.lock = threading.Lock()
        self.daemon = True

    @property
    def tiempo(self):
        return randint(1, 3)

    def run(self):
        while True:
            with self.lock:
                cracker = cola_atacados.get()
                print(
                    f"NebiLockbottom ha empezando a ayudar a {cracker.equipo}")
            for i in range(self.tiempo):
                time.sleep(1)
            with self.lock:
                print(
                    f"NebiLockbottom ha terminado de ayudar a {cracker.equipo}")
                cracker.atacado = False
                cola_atacados.task_done()



class Mision:
    def __init__(self):
        self.equipos = [Equipo("Equipo 1"), Equipo("Equipo 2"),
                        Equipo("Equipo 3")]
        self.nebil = Nebil()

    def run(self):
        for equipo in self.equipos:
            equipo.start()
        self.nebil.start()

        listo = False
        while not listo:
            for equipo in self.equipos:
                if equipo.termino:
                    print(f"Equipo Ganador: {equipo.nombre}")
                    listo = True
                    break

        print("Estadísticas equipos:")
        for equipo in self.equipos:
            print(f"{equipo}")

        return


def desencriptar(nombre_archivo):
    """
    Esta simple (pero útil) función te permite descifrar un archivo encriptado.
    Dado el path de un archivo, devuelve un string del contenido desencriptado.
    """

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        murcielago, numeros = "murcielago", "0123456789"
        dic = dict(chain(zip(murcielago, numeros), zip(numeros, murcielago)))
        return "".join(
            dic.get(char, char) for linea in archivo for char in linea.lower())


if __name__ == "__main__":
    mision = Mision()
    mision.run()

