from clases import Cliente, Bartender, Dealer, MrT, Tragamonedas, Ruleta, \
    Restobar, Tarot, Banno
from sys import exit
from time import mktime
from faker import Faker
from parameters import p, d, mafioso, delay
from collections import deque
from random import random, randint


class Simulacion:
    def __init__(self, tiempo, gui):
        self.gui = gui
        self.tiempo_inicial = tiempo
        self.tiempo = tiempo * (1000 / delay)
        self.instalaciones = []
        self.clientes = []
        self.clientes_totales = []
        self.personal = []
        self.juegos = []
        self.espera_conversar = deque()
        self.actividades = ("conversar", "tini", "trampa")
        self.dinero_total = 0
        self.fake = Faker()   # Como atributo para no ralentizar la simulacion
        self.horario = mktime((2018, 10, 8, 12, 0, 0, 0, 281, 1))

    @property
    def llega_cliente(self):
        return random() <= p

    def cargar_personal(self):
        restos = [resto for resto in self.instalaciones if type(resto) is
                  Restobar]
        tarots = [tarot for tarot in self.instalaciones if type(tarot) is
                  Tarot]
        for i in range(55):
            bartender = Bartender(id_=len(self.personal) + 1,
                                  nombre=self.fake.name(), edad=randint(
                    21, 100), instalacion=restos[randint(0, len(restos) - 1)])
            self.personal.append(bartender)
            if i <= 30:
                bartender.instalacion.personal.append(bartender)
            else:
                bartender.tiempo_trabajo = 0
                bartender.calcular_horario_prox(self)
        for i in range(62):
            if random() < mafioso:
                mafia = True
            else:
                mafia = False
            dealer = Dealer(id_=len(self.personal) + 1, nombre=self.fake.name(),
                            mafia=mafia, edad=randint(21, 100),
                            instalacion=self.juegos[randint(0, len(self.juegos)
                                                            - 1)])
            self.personal.append(dealer)
            if i <= 31:
                dealer.instalacion.personal.append(dealer)
            else:
                dealer.tiempo_trabajo = 0
                dealer.calcular_horario_prox(self)

        for i in range(3):
            mr_t = MrT(id_=len(self.personal) + 1, nombre=self.fake.name(),
                       edad=randint(21, 100), instalacion=tarots[
                    randint(0, len(tarots) - 1)])
            self.personal.append(mr_t)
            if i < len(tarots):
                if not mr_t.instalacion.personal:
                    mr_t.instalacion.personal.append(mr_t)
            else:
                mr_t.tiempo_trabajo = 0
                mr_t.calcular_horario_prox(self)

    def poblar(self):
        tragamonedas = Tragamonedas(type_="tragamonedas", x=60, y=200)
        ruleta = Ruleta(type_="ruleta", x=550, y=240, parent=None)
        resto = Restobar(type_="restobar", id_=1, x=300, y=0,
                         nombre="RestoCool")
        tarot = Tarot(type_="tarot", id_=2, x=343, y=320, nombre="Tataroto")
        banno = Banno(type_="baños", id_=3, x=695, y=425, nombre="Toyquememe")
        self.juegos.append(tragamonedas)
        self.gui.add_entity(tragamonedas)
        tragamonedas.updatePixmap()
        self.juegos.append(ruleta)
        self.gui.add_entity(ruleta)
        ruleta.updatePixmap()
        self.instalaciones.append(resto)
        self.gui.add_entity(resto)
        resto.updatePixmap()
        self.instalaciones.append(tarot)
        self.gui.add_entity(tarot)
        tarot.updatePixmap()
        self.instalaciones.append(banno)
        self.gui.add_entity(banno)
        banno.updatePixmap()
        self.cargar_personal()

    def poblar2(self):
        tragamonedas = Tragamonedas(type_="tragamonedas", x=80, y=320)
        ruleta = Ruleta(type_="ruleta", x=550, y=220, parent=None)
        resto = Restobar(type_="restobar", id_=1, x=220, y=0,
                         nombre="MacLaren's")
        tarot = Tarot(type_="tarot", id_=2, x=343, y=200,
                      nombre="Ima-gina-cion")
        banno = Banno(type_="baños", id_=3, x=695, y=425, nombre="Toyquemeca")
        tragamonedas2 = Tragamonedas(type_="tragamonedas", x=80, y=180)
        ruleta2 = Ruleta(type_="ruleta", x=550, y=320, parent=None)
        resto2 = Restobar(type_="restobar", id_=4, x=380, y=0,
                          nombre="Puzzle")
        tarot2 = Tarot(type_="tarot", id_=5, x=343, y=340,
                       nombre="Kenosvaigabien")
        banno2 = Banno(type_="baños", id_=6, x=620, y=425,
                       nombre="Sueltaeljordan")

        self.juegos.append(tragamonedas)
        self.gui.add_entity(tragamonedas)
        tragamonedas.updatePixmap()
        self.juegos.append(ruleta)
        self.gui.add_entity(ruleta)
        ruleta.updatePixmap()
        self.instalaciones.append(resto)
        self.gui.add_entity(resto)
        resto.updatePixmap()
        self.instalaciones.append(tarot)
        self.gui.add_entity(tarot)
        tarot.updatePixmap()
        self.instalaciones.append(banno)
        self.gui.add_entity(banno)
        banno.updatePixmap()
        self.juegos.append(tragamonedas2)
        self.gui.add_entity(tragamonedas2)
        tragamonedas2.updatePixmap()
        self.juegos.append(ruleta2)
        self.gui.add_entity(ruleta2)
        ruleta2.updatePixmap()
        self.instalaciones.append(resto2)
        self.gui.add_entity(resto2)
        resto2.updatePixmap()
        self.instalaciones.append(tarot2)
        self.gui.add_entity(tarot2)
        tarot2.updatePixmap()
        self.instalaciones.append(banno2)
        self.gui.add_entity(banno2)
        banno2.updatePixmap()
        self.cargar_personal()

    @staticmethod
    def coordenadas_destino(destino):
        if type(destino) is Restobar:
            pos_y = (60, 108)
            y = pos_y[randint(0, 1)]
            if y == 60:
                pos_x = (17, 42, 66, 90, 114)
                x = pos_x[randint(0, 4)]
            else:
                pos_x = (-7, 30, 90, 117)
                x = pos_x[randint(0, 3)]
            return [destino.x + x, destino.y + y]
        elif type(destino) is Tarot:
            return [destino.x + 20, destino.y + 60]
        elif type(destino) is Banno:
            return [destino.x + 12, destino.y + 5]
        elif type(destino) is Tragamonedas:
            pos_x = [18, 91]
            x = pos_x[randint(0, 1)]
            pos_y = [15, 60, 110]
            y = pos_y[randint(0, 2)]
            return [destino.x + x, destino.y + y]
        else:
            pos_x = (25, 50, 75)
            x = pos_x[randint(0, 2)]
            return [destino.x + x, destino.y - 25]

    def dinero_promedio_final(self, personalidad=None):
        dinero = 0
        if personalidad is None:
            for cliente in self.clientes_totales:
                dinero += cliente.dinero_ganado
            if len(self.clientes_totales) > 0:
                return dinero / len(self.clientes_totales)
            return 0.0
        else:
            numero_clientes = 0
            for cliente in self.clientes_totales:
                if cliente.personality is personalidad:
                    dinero += cliente.dinero_ganado
                    numero_clientes += 1
            if numero_clientes == 0:
                return 0.0
            return dinero / numero_clientes

    def tiempo_estadia(self, personalidad=None):
        tiempo = 0
        if personalidad is None:
            for cliente in self.clientes_totales:
                tiempo += cliente.tiempo_total
            tiempo = tiempo * (delay / 1000)
            if len(self.clientes_totales) > 0:
                return tiempo / len(self.clientes_totales)
            return 0.0
        else:
            numero_clientes = 0
            for cliente in self.clientes_totales:
                if cliente.personality is personalidad:
                    tiempo += cliente.tiempo_total
                    numero_clientes += 1
            tiempo = tiempo * (delay / 1000)
            if numero_clientes == 0:
                return 0.0
            return tiempo / numero_clientes

    def ganancias(self):
        dinero = 0
        for juego in self.juegos:
            dinero += juego.casino
        for inst in self.instalaciones:
            dinero += inst.casino
        return dinero / (self.tiempo_inicial / 1440)

    def mejor_juego(self):
        mayor = None
        for juego in self.juegos:
            if mayor is None:
                mayor = juego
            elif mayor.casino < juego.casino:
                mayor = juego
        return f"{mayor}, Dinero recaudado: {mayor.casino}"

    def porcentaje_tramposos(self):
        tramposos = 0
        for cliente in self.clientes_totales:
            if cliente.hizo_trampa:
                tramposos += 1
        if len(self.clientes_totales) > 0:
            return tramposos * (100 / len(self.clientes_totales))
        return 0.0

    def razones_salida(self):
        retirados = 0
        echados = 0
        for cliente in self.clientes_totales:
            if cliente.retirada == 1:
                retirados += 1
            elif cliente.retirada == -1:
                echados += 1
        if len(self.clientes_totales) > 0:
            porc_retirados = retirados * (100 / len(self.clientes_totales))
            porc_echados = echados * (100 / len(self.clientes_totales))
            return [porc_retirados, porc_echados]
        return [0, 0]

    def print_estadisticas(self):
        print(f'''
    Estadisticas finales:

    1.  Dinero promedio ganado: {self.dinero_promedio_final()}

    2.  Dinero promedio ganado por personalidad:

          - Ludópata: {self.dinero_promedio_final("ludopata")}

          - Kibitzer: {self.dinero_promedio_final("kibitzer")}

          - Dieciochero: {self.dinero_promedio_final("dieciochero")}

          - Ganador: {self.dinero_promedio_final("ganador")}

          - Millonario: {self.dinero_promedio_final("millonario")}

    3.  Tiempo de estadía promedio: {self.tiempo_estadia()} minutos

    4.  Tiempo de estadía promedio por personalidad:

          - Ludópata: {self.tiempo_estadia("ludopata")} minutos

          - Kibitzer: {self.tiempo_estadia("kibitzer")} minutos

          - Dieciochero: {self.tiempo_estadia("dieciochero")} minutos

          - Ganador: {self.tiempo_estadia("ganador")} minutos

          - Millonario: {self.tiempo_estadia("millonario")} minutos

    5.  Ganancias del casino en promedio por día: {self.ganancias()}

    6.  Juego de mayor Ganancia: {self.mejor_juego()}

    7.  Porcentaje de personas que hizo trampa: {self.porcentaje_tramposos()}%

    8.  Razones de salida:

          - Decision: {self.razones_salida()[0]}%

          - Echados: {self.razones_salida()[1]}%

    9.  Tiempo sin funcionar por instalación:''')
        for inst in self.instalaciones:
            print(f'''
          - {inst}, Tiempo sin funcionar: {inst.tiempo_sf}''')
        print(f'''    
    10. Numero de personas que visitó cada juego:''')
        for juego in self.juegos:
            print(f'''
          -{juego}, Visitas: {juego.personas}''')

    def casino(self):

        if self.clientes:
            for c in self.clientes:
                if c.destino is None and c.tiempo_total > 500 / delay:
                    # Se demoran medio minuto de la simulacion en realizar la
                    # primera decision (Para poder visualizarlos si se retiran
                    # en la primera decision)
                    accion = c.decidir()
                    if accion == "retirarse":
                        c.destino = "retirarse"
                        c.coord = [33, 0]
                    elif accion == "jugar":
                        juego = self.juegos[randint(0, len(self.juegos) - 1)]
                        c.destino = juego
                        c.tiempo = juego.duracion
                        c.coord = self.coordenadas_destino(c.destino)
                    elif accion == "actividad":
                        actividad = self.actividades[
                            randint(0, len(self.actividades) - 1)]
                        if actividad == "conversar":
                            lista_destinos = [[550, 50], [550, 150], [600, 50],
                                              [600, 150], [650, 50], [650, 150],
                                              [700, 50], [700, 150]]
                            c.destino = "conversar"
                            c.coord = lista_destinos[randint(0, 7)]
                            c.tiempo = d * (1000 / delay)
                        elif actividad == "tini":
                            c.destino = "tini"
                            c.coord = [33, 420]
                            c.tiempo = c.tiempo_actividad * (1000 / delay)

                        else:
                            if c.converso and c.personality == "kibitzer":
                                c.destino = "trampa"
                                ruletas = [rul for rul in self.juegos if
                                           type(rul) is Ruleta]
                                c.destino_trampa = ruletas[randint(
                                    0, len(ruletas) - 1)]
                                c.coord = self.coordenadas_destino(
                                    c.destino_trampa)
                                c.trampas = 0
                                c.tiempo_estudio = c.tiempo_actividad * (
                                        1000 / delay)

                    else:
                        instalacion = self.instalaciones[
                            randint(0, len(self.instalaciones) - 1)]
                        if type(instalacion) == Banno:
                            c.tiempo = instalacion.duracion(c) * (1000 / delay)
                            c.destino = instalacion
                            c.coord = self.coordenadas_destino(c.destino)
                        else:
                            c.tiempo = instalacion.duracion * (1000 / delay)
                            c.destino = instalacion
                            c.coord = self.coordenadas_destino(c.destino)

                else:
                    if c.coord is not None:
                        if c.mover(c.coord[0], c.coord[1]):
                            if c.destino in self.juegos:
                                if c not in c.destino.clientes:
                                    c.destino.personas += 1
                                    c.destino.clientes.append(c)
                            elif c.destino in self.instalaciones:
                                if c not in c.destino.clientes:
                                    c.destino.clientes.append(c)
                            elif c.destino == "conversar":
                                if self.espera_conversar and \
                                        self.espera_conversar[0] != c:
                                    c2 = self.espera_conversar.popleft()
                                    c.conversar(self, c2)
                                else:
                                    c.conversar(self, None)
                            elif c.destino == "tini":
                                c.hablar_tini()
                            elif c.destino == "trampa":
                                self.clientes_totales.remove(c)
                                c.trampa(self, c.destino_trampa)
                                self.clientes_totales.append(c)
                            elif c.destino == "retirarse":
                                self.clientes_totales.remove(c)
                                c.retirada = 1
                                self.clientes_totales.append(c)
                                c.deleteLater()
                                self.clientes.remove(c)


        for juego in self.juegos:
            juego.run()
        for instalacion in self.instalaciones:
            instalacion.run()

    def tick(self):

        tupla_personalidades = ("ludopata", "kibitzer", "dieciochero",
                                "ganador", "millonario")

        if self.llega_cliente:
            cliente = Cliente(id_=len(self.clientes_totales) + 1,
                              nombre=self.fake.name(), edad=randint(18, 100),
                              personality=tupla_personalidades[
                                  randint(0, 4)], x=33)
            self.clientes.append(cliente)
            self.clientes_totales.append(cliente)
            self.gui.add_entity(cliente)
            cliente.setFixedSize(36, 36)
        self.casino()
        self.horario += (delay / 1000) * 60
        self.tiempo = self.tiempo - 1
        for c in self.clientes:
            c.tiempo_total += 1
        for pers in self.personal:
            if pers.tiempo_trabajo > 0:
                if pers not in pers.instalacion.personal:
                    pers.instalacion.personal.append(pers)
                pers.tiempo_trabajo -= 1
                if pers.tiempo_trabajo == 0:
                    pers.instalacion.personal.remove(pers)
                    pers.calcular_horario_prox(self)
            else:
                if self.horario >= pers.horario_prox:
                    restos = [resto for resto in self.instalaciones if
                              type(resto) is
                              Restobar]
                    tarots = [tarot for tarot in self.instalaciones if
                              type(tarot) is
                              Tarot]
                    if type(pers) is Bartender:
                        pers.instalacion = restos[randint(0, len(restos) - 1)]
                    elif type(pers) is MrT:
                        pers.instalacion = tarots[randint(0, len(tarots) - 1)]
                    else:
                        pers.instalacion = self.juegos[randint(0, len(
                            self.juegos) - 1)]
                    if type(pers) is MrT:
                        if pers.instalacion.personal:
                            pers.instalacion.personal[0].tiempo_trabajo = 0
                            pers.instalacion.personal[0].calcular_horario_prox(
                                self)
                            pers.instalacion.personal = []
                    pers.instalacion.personal.append(pers)
                    pers.tiempo_reset()
        if self.tiempo <= 0:
            self.horario += (delay / 1000) * 60
            print(f"\n {'-' * 20} La simulación ha terminado {'-' * 20}\n")
            with open("resultados_simulacion.txt", "w", encoding="utf-8"
                      ) as archivo:
                archivo.write(f'''
    Estadisticas finales:

    1.  Dinero promedio ganado: {self.dinero_promedio_final()} 
    2.  Dinero promedio ganado por personalidad:
          - Ludópata: {self.dinero_promedio_final("ludopata")}
          - Kibitzer: {self.dinero_promedio_final("kibitzer")}
          - Dieciochero: {self.dinero_promedio_final("dieciochero")}
          - Ganador: {self.dinero_promedio_final("ganador")}
          - Millonario: {self.dinero_promedio_final("millonario")}
    3.  Tiempo de estadía promedio: {self.tiempo_estadia()} minutos
    4.  Tiempo de estadía promedio por personalidad:
          - Ludópata: {self.tiempo_estadia("ludopata")} minutos
          - Kibitzer: {self.tiempo_estadia("kibitzer")} minutos
          - Dieciochero: {self.tiempo_estadia("dieciochero")} minutos
          - Ganador: {self.tiempo_estadia("ganador")} minutos
          - Millonario: {self.tiempo_estadia("millonario")} minutos
    5.  Ganancias del casino en promedio por día: {self.ganancias()}
    6.  Juego de mayor Ganancia: {self.mejor_juego()}
    7.  Porcentaje de personas que hizo trampa: {self.porcentaje_tramposos()}%
    8.  Razones de salida:
          - Decision: {self.razones_salida()[0]}%
          - Echados: {self.razones_salida()[1]}%
    9.  Tiempo sin funcionar por instalación:''')
                for inst in self.instalaciones:
                    archivo.write(f'''
          - {inst}, Tiempo sin funcionar: {inst.tiempo_sf}''')
                archivo.write(f'''    
    10. Numero de personas que visitó cada juego:''')
                for juego in self.juegos:
                    archivo.write(f'''
          -{juego}, Visitas: {juego.personas}''')
            self.print_estadisticas()
            exit()
