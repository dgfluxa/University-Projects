from PyQt5.QtCore import QObject, pyqtSignal, QThread, QMutex
from math import sin, cos
from time import sleep


class Helper(QObject):

    ingreso_signal = pyqtSignal(bool)
    registro_signal = pyqtSignal(bool, int)
    es_jefe_signal = pyqtSignal(bool)
    iniciar_signal = pyqtSignal()
    pintar_signal = pyqtSignal(list, list, str)
    pausa_signal = pyqtSignal()
    comenzar_signal = pyqtSignal(int, int, float, float, float)

    def __init__(self, parent):
        super().__init__()

        self.ingreso_signal.connect(parent.frontend.ingreso.ingresar)
        self.registro_signal.connect(parent.frontend.registro.registro)
        self.es_jefe_signal.connect(parent.frontend.ingreso.sala_espera.es_jefe)
        self.iniciar_signal.connect(parent.frontend.ingreso.sala_espera.iniciar)
        self.pintar_signal.connect(
            parent.frontend.ingreso.sala_espera.juego.pintar)
        self.pausa_signal.connect(
            parent.frontend.ingreso.sala_espera.juego.pausar)
        self.comenzar_signal.connect(
            parent.frontend.ingreso.sala_espera.juego.comenzar)

    def conf_ingreso(self, boolean):
        self.ingreso_signal.emit(boolean)

    def conf_registro(self, boolean, num):
        self.registro_signal.emit(boolean, num)

    def jefe(self, boolean):
        self.es_jefe_signal.emit(boolean)

    def iniciar(self):
        self.iniciar_signal.emit()

    def pintar(self, pos1, pos2, color):
        self.pintar_signal.emit(pos1, pos2, color)

    def pausa(self):
        self.pausa_signal.emit()

    def comenzar(self, x, y, x2, y2, o):
        self.comenzar_signal.emit(x, y, x2, y2, o)


class RegistroUsuario(QObject):

    exito_signal = pyqtSignal(bool, int)

    def __init__(self, parent):
        super().__init__()
        self.exito_signal.connect(parent.registro)

    def conf_registro(self, boolean, num):
        self.exito_signal.emit(boolean, num)



class Avanzar(QThread):

    signal_posiciones = pyqtSignal(float, float)
    signal_o = pyqtSignal(float)

    mutex = QMutex()

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.x = parent.x
        self.y = parent.y
        self.o = parent.o
        self.signal_posiciones.connect(parent.move)

    def run(self):
        while True:
            if self.parent.o != self.o:
                self.o = self.parent.o

            self.x -= (4 * cos(self.o))
            self.y += (4 * sin(self.o))

            self.signal_posiciones.emit(self.x, self.y)
            sleep(0.07)


class Actualizador(QObject):

    signal_o = pyqtSignal(float)
    signal_alive = pyqtSignal(bool)

    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.signal_o.connect(parent.actualizar_o)
        self.signal_alive.connect(parent.is_alive)

    def actualizar_o(self, valor):
        self.signal_o.emit(self.parent.o + valor)  # Aqui se le puede sumar la diferencia del sleep al cambiar la velocidad para radios consistentes

    def choque(self):
        self.parent.forward.terminate()
        print("PERDEDOOOOR")
        self.signal_alive.emit(False)





