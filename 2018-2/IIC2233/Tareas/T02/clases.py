from gui.entities import Game, Human, Building
from random import random, uniform, normalvariate, triangular, randint
from parameters import a, g, o, delay, n, k, e, X, Y, w, v, t
from collections import deque
from abc import ABC
from math import pi


class Personal(ABC):

    def __init__(self, id_, nombre, edad, instalacion,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id_ = id_
        self.nombre = nombre
        self.edad = edad
        self.horario_prox = 0
        self.instalacion = instalacion

    @property
    def tiempo_descanso(self):  # En horas
        return max(min(normalvariate(14, 5), 20), 8)

    def calcular_horario_prox(self, sim):
        descanso = self.tiempo_descanso * 360
        self.horario_prox = (sim.horario + descanso) - \
                            ((sim.horario + descanso) % 360)


class Cliente(Human):

    def __init__(self, id_, nombre, edad, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id_ = id_
        self.nombre = nombre
        self.edad = edad
        self.destino = None
        self.destino_trampa = None
        self.coord = None
        self._tiempo = 0
        self.tiempo_total = 0
        self.tiempo_conversar = 0
        self.tiempo_estudio = 0
        self.converso = False
        self.hablo_tini = False
        self.hizo_trampa = False
        self.trampas = 0
        self.retirada = 0  # 0 si no se retiran, 1 por decision y -1 echados

        if self.personality is "ludopata":
            self.dinero = max(min(uniform(0.3, 0.7), 1), 0)
            self.lucidez = max(min(uniform(0.3, 0.7), 1), 0)
            self._ansiedad = max(min(uniform(0.7, 1), 1), 0)
            self.suerte = max(min(uniform(0.3, 0.7), 1), 0)
            self.sociabilidad = max(min(uniform(0.3, 0.7), 1), 0)
            self._stamina = max(min(uniform(0.7, 1), 1), 0)
            self.deshonestidad = max(min(uniform(0.3, 0.7), 1), 0)

        elif self.personality is "kibitzer":
            self.dinero = max(min(uniform(0, 0.3), 1), 0)
            self.lucidez = max(min(uniform(0.3, 0.7), 1), 0)
            self._ansiedad = max(min(uniform(0, 0.3), 1), 0)
            self.suerte = max(min(uniform(0.3, 0.7), 1), 0)
            self.sociabilidad = max(min(uniform(0.7, 1), 1), 0)
            self._stamina = max(min(uniform(0, 0.3), 1), 0)
            self.deshonestidad = max(min(uniform(0.3, 0.7), 1), 0)

        elif self.personality is "dieciochero":
            self.dinero = max(min(uniform(0.3, 0.7), 1), 0)
            self.lucidez = max(min(uniform(0, 0.3), 1), 0)
            self._ansiedad = max(min(uniform(0.7, 1), 1), 0)
            self.suerte = max(min(uniform(0.3, 0.7), 1), 0)
            self.sociabilidad = max(min(uniform(0.7, 1), 1), 0)
            self._stamina = max(min(uniform(0.3, 0.7), 1), 0)
            self.deshonestidad = max(min(uniform(0, 0.3), 1), 0)

        elif self.personality is "ganador":
            self.dinero = max(min(uniform(0.3, 0.7), 1), 0)
            self.lucidez = max(min(uniform(0.3, 0.7), 1), 0)
            self._ansiedad = max(min(uniform(0.3, 0.7), 1), 0)
            self.suerte = max(min(uniform(0.7, 1), 1), 0)
            self.sociabilidad = max(min(uniform(0.7, 1), 1), 0)
            self._stamina = max(min(uniform(0.7, 1), 1), 0)
            self.deshonestidad = max(min(uniform(0.7, 1), 1), 0)

        elif self.personality is "millonario":
            self.dinero = max(min(uniform(0.7, 1), 1), 0)
            self.lucidez = max(min(uniform(0.3, 0.7), 1), 0)
            self._ansiedad = max(min(uniform(0.3, 0.7), 1), 0)
            self.suerte = max(min(uniform(0.3, 0.7), 1), 0)
            self.sociabilidad = max(min(uniform(0.3, 0.7), 1), 0)
            self._stamina = max(min(uniform(0.7, 1), 1), 0)
            self.deshonestidad = max(min(uniform(0.3, 0.7), 1), 0)

        self.dinero_inicial = int(self.dinero * 200 // 1)
        self.dinero_actual = self.dinero_inicial

    @property
    def stamina(self):
        if self.dinero_actual == 0:
            return 0
        return self._stamina

    @stamina.setter
    def stamina(self, value):
        self._stamina = max(min(value, 1), 0)

    @property
    def ansiedad(self):
        if self.dinero_actual > 2 * self.dinero_inicial or \
                self.dinero_actual < (1/5) * self.dinero_inicial:
            return self._ansiedad * 1.25
        return self._ansiedad

    @ansiedad.setter
    def ansiedad(self, value):
        self._ansiedad = max(min(value, 1), 0)

    @property
    def retirarse(self):
        return 1 - self.stamina

    @property
    def jugar(self):
        return min(self.ansiedad, 1 - self.retirarse)

    @property
    def actividad(self):
        return min(self.sociabilidad, 1 - self.retirarse - self.jugar)

    @property
    def instalacion(self):
        return 1 - (self.retirarse + self.jugar + self.actividad)

    @property
    def dinero_ganado(self):
        return self.dinero_actual - self.dinero_inicial

    @property
    def tiempo(self):
        return self._tiempo

    @tiempo.setter
    def tiempo(self, value):
        self._tiempo = max(value, 0)

    @property
    def tiempo_actividad(self):
        return max(self.lucidez + self.sociabilidad - self.ansiedad, 0.1
                   ) * pi**2

    def apuesta(self, costo):
        apuesta = (1 + o * self.ansiedad) * costo
        if self.dinero_actual >= apuesta:
            self.dinero_actual -= apuesta
            return apuesta
        self.dinero_actual = 0
        return self.dinero_actual

    def mover(self, x, y):
        if x > self.x:
            self.x += 1
        elif x < self.x:
            self.x -= 1
        if y > self.y:
            self.y += 1
        elif y < self.y:
            self.y -= 1
        if self.x == x and self.y == y:
                return True
        return False

    def decidir(self):
        decision = random()
        if decision < self.retirarse:
            return "retirarse"
        elif decision < (self.retirarse + self.jugar):
            return "jugar"
        elif decision < (self.retirarse + self.jugar + self.actividad):
            return "actividad"
        else:
            return "instalacion"

    def conversar(self, sim, c2):
        if c2 is not None:
            tiempo1 = self.tiempo_actividad
            tiempo2 = c2.tiempo_actividad
            tiempo_final = max(tiempo1, tiempo2) * (1000 / delay)
            self.tiempo_conversar = tiempo_final
            c2.tiempo_conversar = tiempo_final

        elif c2 is None and self.tiempo_conversar <= 0:
            if self not in sim.espera_conversar:
                sim.espera_conversar.append(self)
            else:
                self.tiempo -= 1
                if self.tiempo <= 0:
                    sim.espera_conversar.remove(self)
                    self.tiempo = 0
                    self.destino = None
                    self.coord = None
        else:
            self.tiempo_conversar -= 1
            if self.tiempo_conversar <= 0:
                self.ansiedad = max(min(self.ansiedad - self.ansiedad * (
                        e / 100), 1), 0)
                self.deshonestidad = max(min(self.deshonestidad + X, 1), 0)
                self.tiempo = 0
                self.tiempo_conversar = 0
                self.destino = None
                self.coord = None
                self.converso = True

    def hablar_tini(self):
        self.tiempo -= 1
        if self.tiempo <= 0:
            self.dinero_actual -= 20
            self.hablo_tini = True
            self.stamina -= n
            self.destino = None
            self.coord = None
            self.tiempo = 0

    def trampa(self, sim, ruleta):
        if self.tiempo_estudio > 0:
            self.tiempo_estudio -= 1
        else:
            if self.tiempo <= 0:
                if random() < self.deshonestidad:
                    self.trampas += 1
                    self.hizo_trampa = True
                    if random() < w:
                        self.retirada = -1
                        self.deleteLater()
                        sim.clientes.remove(self)
                    else:
                        ruleta.run_trampa(self)
                        if self.trampas >= v:
                            self.destino = None
                            self.coord = None
                            self.tiempo = 0
                            self.tiempo_estudio = 0
                            self.trampas = 0
                        else:
                            self.tiempo = ruleta.duracion
            else:
                self.tiempo -= 1


class Bartender(Personal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._tiempo_trabajo = triangular(360, 540, 490) * (1000 / delay)

    @property
    def tiempo_trabajo(self):
        return self._tiempo_trabajo

    @tiempo_trabajo.setter
    def tiempo_trabajo(self, value):
        self._tiempo_trabajo = max(value, 0)

    def tiempo_reset(self):
        self.tiempo_trabajo = triangular(360, 540, 490) * (1000 / delay)


class Dealer(Personal):
    def __init__(self, mafia, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mafia = mafia
        self._tiempo_trabajo = triangular(360, 540, 540) * (1000 / delay)

    @property
    def tiempo_trabajo(self):
        return self._tiempo_trabajo

    @tiempo_trabajo.setter
    def tiempo_trabajo(self, value):
        self._tiempo_trabajo = max(value, 0)

    def tiempo_reset(self):
        self.tiempo_trabajo = triangular(360, 540, 540) * (1000 / delay)


class MrT(Personal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._tiempo_trabajo = triangular(360, 500, 420) * (1000 / delay)

    @property
    def tiempo_trabajo(self):
        return self._tiempo_trabajo

    @tiempo_trabajo.setter
    def tiempo_trabajo(self, value):
        self._tiempo_trabajo = max(value, 0)

    def tiempo_reset(self):
        self.tiempo_trabajo = triangular(360, 500, 420) * (1000 / delay)


class Tragamonedas(Game):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.duracion = (250/delay)//1  # 4 juegos por minuto
        self.costo = 1
        self.prob_juego = a
        self.pozo = 0
        self.casino = 0
        self.personal = []
        self.clientes = []
        self.personas = 0

    def __str__(self):
        return f''' Tipo: Tragamonedas, Coordenadas: {(self.x, self.y)}'''

    def prob_ganar(self, cliente):
        return max(min(self.prob_juego + 0.2 * cliente.suerte - 0.1, 1), 0)

    def run(self):
        for cliente in self.clientes:
            if cliente.tiempo == 0:
                apuesta = cliente.apuesta(self.costo)
                self.casino += apuesta * 0.1
                self.pozo += apuesta * 0.9
                if random() < self.prob_ganar(cliente):
                    cliente.dinero_actual += self.pozo
                cliente.destino = None
                self.clientes.remove(cliente)
            else:
                cliente.tiempo -= 1


class Ruleta(Game):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.duracion = (1000 / delay) // 1  # 1 juego por minuto
        self.costo = 1
        self.casino = 0
        self.personal = []
        self.clientes = []
        self.tipos_apuestas = ("verde", "negro", "rojo", "numero")
        self.personas = 0

    def __str__(self):
        return f''' Tipo: Ruleta, Coordenadas: {(self.x, self.y)}'''

    def prob_juego(self, tipo_apuesta):
        if tipo_apuesta in ("negro", "rojo"):
            return max(min(g / (2 * (g + 1)), 1), 0)
        else:
            return max(min(1 / (g + 1), 1), 0)

    def prob_ganar(self, cliente, tipo_apuesta):
        prob = max(min(self.prob_juego(tipo_apuesta) + 0.2 * cliente.suerte -
                       0.1, 1), 0)
        if cliente.hablo_tini and self.hay_mafia() is True:
            prob += prob * (k / 100)
        elif cliente.hizo_trampa is True:
            prob += prob * (Y / 100)
        return prob

    def hay_mafia(self):
        for pers in self.personal:
            if pers.mafia is True:
                return True
        return False

    def run(self):
        for cliente in self.clientes:
            if cliente.tiempo == 0:
                apuesta = cliente.apuesta(self.costo)
                self.casino += apuesta
                tipo_apuesta = self.tipos_apuestas[randint(0, 3)]
                if random() < self.prob_ganar(cliente, tipo_apuesta):
                    if tipo_apuesta in ("negro", "rojo"):
                        cliente.dinero_actual += apuesta * 1.5
                        self.casino -= apuesta * 1.5
                    else:
                        cliente.dinero_actual += apuesta * 5
                        self.casino -= apuesta * 5

                cliente.destino = None
                self.clientes.remove(cliente)
            else:
                cliente.tiempo -= 1

    def run_trampa(self, cliente):
        apuesta = cliente.apuesta(self.costo)
        self.casino += apuesta
        tipo_apuesta = self.tipos_apuestas[randint(0, 3)]
        if random() < self.prob_ganar(cliente, tipo_apuesta):
            if tipo_apuesta in ("negro", "rojo"):
                cliente.dinero_actual += apuesta * 1.5
                self.casino -= apuesta * 1.5
            else:
                cliente.dinero_actual += apuesta * 5
                self.casino -= apuesta * 5


class Instalacion(Building):
    def __init__(self, id_, nombre, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id_ = id_
        self.ubicacion = (self.x, self.y)
        self.nombre = nombre
        self.casino = 0
        self.clientes = deque()
        self.personal = []
        self.tiempo_sf = 0

    @property
    def funcionando(self):
        if len(self.personal) >= self.req:
            return True
        return False

    def __str__(self):
        return f'''ID: {self.id_}, Nombre: {self.nombre}'''


class Restobar(Instalacion):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max = 20
        self.costo = 2
        self.req = 2

    @property
    def duracion(self):
        duracion = max(min(100/len(self.personal), 50), 10)
        return duracion

    @staticmethod
    def bebida(cliente):
        cliente.ansiedad = max(min(cliente.ansiedad - 0.15, 1), 0)
        cliente.lucidez = max(min(cliente.lucidez - 0.2, 1), 0)
        cliente.stamina = max(min(cliente.stamina - 0.3, 1), 0)

    @staticmethod
    def comida(cliente):
        cliente.lucidez = max(min(cliente.lucidez + 0.1, 1), 0)
        cliente.ansiedad = max(min(cliente.ansiedad - 0.2, 1), 0)

    def run(self):
        if self.funcionando:
            for i in range(self.max):
                if self.clientes and i < len(self.clientes):
                    if self.clientes[i].tiempo == 0:
                        cliente = self.clientes.popleft()
                        if cliente.dinero_actual >= self.costo:
                            cliente.dinero_actual -= self.costo
                            self.casino += self.costo
                            if cliente.lucidez > cliente.ansiedad:
                                self.bebida(cliente)
                            elif cliente.lucidez < cliente.ansiedad:
                                self.comida(cliente)
                            else:
                                if random() < 0.5:
                                    self.bebida(cliente)
                                else:
                                    self.comida(cliente)
                        cliente.destino = None
                    else:
                        self.clientes[i].tiempo -= 1
        else:
            self.tiempo_sf += 1
            if self.clientes:
                for c in self.clientes:
                    c.tiempo = 0
                    c.destino = None
                self.clientes = deque()


class Tarot(Instalacion):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max = 1
        self.costo = 10
        self.req = 1

    @property
    def duracion(self):
        return max(normalvariate(3, 5), 0)

    @staticmethod
    def mal_futuro(cliente):
        cliente.stamina = max(min(cliente.stamina + t, 1), 0)

    @staticmethod
    def buen_futuro(cliente):
        cliente.suerte = min(cliente.suerte + 0.2, 1)

    def run(self):
        if self.funcionando:
            for i in range(self.max):
                if self.clientes and i < len(self.clientes):
                    if self.clientes[i].tiempo == 0:
                        cliente = self.clientes.popleft()
                        if cliente.dinero_actual >= self.costo:
                            cliente.dinero_actual -= self.costo
                            self.casino += self.costo
                            if random() < 0.5:
                                self.mal_futuro(cliente)
                            else:
                                self.buen_futuro(cliente)
                        cliente.destino = None
                    else:
                        self.clientes[i].tiempo -= 1
        else:
            self.tiempo_sf += 1
            if self.clientes:
                for c in self.clientes:
                    c.tiempo = 0
                    c.destino = None
                self.clientes = deque()


class Banno(Instalacion):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max = 20
        self.costo = 0.2
        self.req = 0

    @staticmethod
    def duracion(cliente):
        return max(normalvariate(3 * (1 - cliente.lucidez), 2), 0)

    def run(self):
        for i in range(self.max):
            if self.clientes and i < len(self.clientes):
                if self.clientes[i].tiempo == 0:
                    cliente = self.clientes.popleft()
                    if cliente.dinero_actual >= self.costo:
                        cliente.dinero_actual -= self.costo
                        self.casino += self.costo
                        cliente.ansiedad = max(cliente.ansiedad - 0.1, 0)
                    cliente.destino = None
                else:
                    self.clientes[i].tiempo -= 1
