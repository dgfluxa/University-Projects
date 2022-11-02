import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QScrollArea, QPushButton
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, Qt, QPoint, QTimer
from PyQt5.QtGui import QImage, QPainter, QPen
from backend_cliente import Avanzar, Actualizador

nombre_inicio, clase_inicio = uic.loadUiType("archivos_ui/ventana_inicio.ui")
nombre_ingreso, clase_ingreso = uic.loadUiType("archivos_ui/ventana_ingreso.ui")
nombre_registro, clase_registro = uic.loadUiType(
    "archivos_ui/ventana_registro.ui")
nombre_espera, clase_espera = uic.loadUiType("archivos_ui/sala_espera.ui")
nombre_juego, clase_juego = uic.loadUiType("archivos_ui/sala_juego.ui")
nombre_eleccion, clase_eleccion = uic.loadUiType(
    "archivos_ui/eleccion_teclas.ui")


class VentanaInicio(nombre_inicio, clase_inicio):
    def __init__(self, cliente):
        super().__init__()
        self.setupUi(self)

        self.cliente = cliente

        self.ingreso = VentanaIngreso(self, cliente)
        self.registro = VentanaRegistro(self, cliente)

        self.boton_ingreso_2.clicked.connect(self.click_ingreso)
        self.boton_registro.clicked.connect(self.click_registro)

    def click_ingreso(self):
        self.close()
        self.ingreso.show()

    def click_registro(self):
        self.close()
        self.registro.show()


class VentanaIngreso(nombre_ingreso, clase_ingreso):
    boton_signal = pyqtSignal(str, str)

    servidor_signal = pyqtSignal(dict)

    def __init__(self, ventana_inicio, cliente):
        super().__init__()
        self.setupUi(self)

        self.cliente = cliente

        self.servidor_signal.connect(cliente.send)

        self.inicio = ventana_inicio

        self.eleccion = EleccionTeclas(self, self.cliente)

        self.sala_espera = SalaEspera(self.cliente, self.inicio)

        self.label_error.hide()

        self.boton_signal.connect(self.cliente.ingresar)
        self.boton_ingresar.clicked.connect(self.click_ingresar)
        self.boton_atras.clicked.connect(self.click_atras)

    def click_ingresar(self):
        self.boton_signal.emit(self.line_usuario.text(),
                               self.line_clave.text())

    def click_atras(self):
        self.close()
        self.inicio.show()
        self.line_usuario.setText("")
        self.line_clave.setText("")
        self.label_error.hide()

    def ingresar(self, boolean):
        if boolean:
            self.label_error.hide()
            self.sala_espera.nombre_usuario = self.line_usuario.text()
            self.eleccion.name = self.line_usuario.text()
            self.line_usuario.setText("")
            self.line_clave.setText("")
            self.hide()
            self.eleccion.show()
            mensaje = {"status": "nuevo_usuario",
                       "data": self.sala_espera.nombre_usuario}
            self.cliente.send(mensaje)
        else:
            self.label_error.show()


class VentanaRegistro(nombre_registro, clase_registro):
    boton_signal = pyqtSignal(str, str, str)

    def __init__(self, ventana_inicio, cliente):
        super().__init__()
        self.setupUi(self)

        self.inicio = ventana_inicio

        self.cliente = cliente

        self.boton_signal.connect(self.cliente.registrar)

        self.label_error_nombre.hide()
        self.label_error_clave.hide()
        self.label_exito.hide()

        self.boton_registrar.clicked.connect(self.click_registrar)
        self.boton_atras.clicked.connect(self.click_atras)

    def click_registrar(self):
        self.boton_signal.emit(self.line_usuario.text(), self.line_clave.text(),
                               self.line_conf_clave.text())

    def click_atras(self):
        self.close()
        self.inicio.show()
        self.label_error_nombre.hide()
        self.label_exito.hide()
        self.label_error_clave.hide()

    def registro(self, boolean, num):
        if boolean:
            self.line_usuario.setText("")
            self.line_clave.setText("")
            self.line_conf_clave.setText("")
            self.label_error_clave.hide()
            self.label_error_nombre.hide()
            self.label_exito.show()
        else:
            if num == 1:
                self.label_error_nombre.hide()
                self.label_exito.hide()
                self.label_error_clave.show()
            else:
                self.label_exito.hide()
                self.label_error_clave.hide()
                self.label_error_nombre.show()


class EleccionTeclas(nombre_eleccion, clase_eleccion):
    terminar_conexion_signal = pyqtSignal()

    def __init__(self, parent, cliente):
        super().__init__()
        self.setupUi(self)

        self.parent = parent
        self.cliente = cliente

        self.terminar_conexion_signal.connect(cliente.terminar_conexion)

        self.name = None

        self.der = False
        self.izq = False

        self.boton_der.clicked.connect(self.clicked_der)
        self.boton_izq.clicked.connect(self.clicked_izq)
        self.boton_comenzar.clicked.connect(self.comenzar)
        self.boton_comenzar.setEnabled(False)

        self.timer = QTimer()
        self.timer.timeout.connect(self.revisar_listo)
        self.timer.start(250)

        self.tecla_der = None
        self.tecla_izq = None

    def clicked_der(self):
        self.der = True
        self.izq = False

    def clicked_izq(self):
        self.izq = True
        self.der = False

    def keyPressEvent(self, event):
        if self.der and event.key() != Qt.Key_Space and\
                event.key() != self.tecla_izq:  # Tecla espacio y tecla mov contrario consideradas inválidas
            self.tecla_der = event.key()
            name = event.text() if event.text() else event.key()
            self.label_der.setText(str(name))
        if self.izq and event.key() != Qt.Key_Space and\
                event.key() != self.tecla_der:
            self.tecla_izq = event.key()
            name = event.text() if event.text() else event.key()
            self.label_izq.setText(str(name))

    def comenzar(self):
        self.parent.sala_espera.juego.der = self.tecla_der
        self.parent.sala_espera.juego.izq = self.tecla_izq
        self.hide()
        self.parent.sala_espera.show()
        msg = {"status": "display_jugador",
               "data": {"usuario": self.name,
                        "color": self.cliente.color,
                        "jefe": self.cliente.jefe}}
        self.cliente.send(msg)

    def revisar_listo(self):
        if self.tecla_der and self.tecla_izq:
            self.boton_comenzar.setEnabled(True)
            self.timer.stop()


class SalaEspera(nombre_espera, clase_espera):

    servidor_signal = pyqtSignal(dict)
    terminar_conexion_signal = pyqtSignal()
    iniciar_signal = pyqtSignal()

    def __init__(self, cliente, inicio, *args,
                 **kwargs):
        super().__init__(*args, **kwargs)

        self.servidor_signal.connect(cliente.send)
        self.terminar_conexion_signal.connect(cliente.terminar_conexion)

        self.inicio = inicio
        self.cliente = cliente
        self.juego = SalaJuego(self, cliente)

        self.setupUi(self)
        self.contador.hide()
        self.num_contador = 10

        self.boton_salir.clicked.connect(self.salir)
        self.boton_inicio.clicked.connect(cliente.boton_iniciar)

        self.colores = {"7": "Rojo", "9": "Azul", "8": "Verde",
                        "12": "Amarillo", "11": "Rosado",
                        "17": "Morado", "10": "Cyan",
                        "3": "Blanco"}

        self.label_par.hide()
        self.label_vel.hide()
        self.label_punt.hide()
        self.label_jefe.hide()
        self.label_poder.hide()
        self.grupo_poderes.hide()
        self.boton_inicio.hide()
        self.contador.hide()
        self.sel_punt.hide()
        self.sel_vel.hide()

        '''Código rescatado ayudantia 13 IIC2233 2018-2'''

        # Log
        self.chat_log = ""

        self.chat_log_label = QLabel("", self)
        chat_log_label_font = self.chat_log_label.font()
        chat_log_label_font.setPointSize(10)
        self.chat_log_label.setFont(chat_log_label_font)
        self.chat_log_label.setStyleSheet("color: black")

        self.users_scroll = QScrollArea(self)
        self.users_scroll.setWidgetResizable(True)
        self.users_scroll.setStyleSheet("background-color: white")

        self.usuario_line_edit = QLineEdit("", self)
        usuario_line_edit_font = self.usuario_line_edit.font()
        usuario_line_edit_font.setPointSize(8)
        self.usuario_line_edit.setFont(usuario_line_edit_font)

        self.boton_usuario = QPushButton("\t\tEnviar\t\t", self)
        boton_usuario_font = self.boton_usuario.font()
        boton_usuario_font.setBold(True)
        boton_usuario_font.setPointSize(10)
        self.boton_usuario.setFont(boton_usuario_font)
        self.boton_usuario.setStyleSheet(
            "QPushButton{color: black; background: transparent; border: 2px solid black}"
            "QPushButton:pressed{color: #fcf7e3; background-color: black}")
        self.boton_usuario.clicked.connect(self.manejo_boton)

        self.players_log = ""

        self.players_log_label = QLabel("", self)
        players_log_label_font = self.chat_log_label.font()
        players_log_label_font.setPointSize(10)
        self.players_log_label.setFont(chat_log_label_font)
        self.players_log_label.setStyleSheet("color: black")

        self.players_scroll = QScrollArea(self)
        self.players_scroll.setWidgetResizable(True)
        self.players_scroll.setStyleSheet("background-color: white")

        # Alineación de UI
        self.init_setUp()

    def init_setUp(self):

        self.chat_log_label.setGeometry(460, 55, 220, 320)
        self.users_scroll.setWidget(self.chat_log_label)
        self.users_scroll.setGeometry(460, 55, 220, 320)
        self.chat_log_label.setAlignment(Qt.AlignTop)
        self.usuario_line_edit.setGeometry(460, 380, 150, 20)
        self.usuario_line_edit.setFocus()
        self.boton_usuario.setGeometry(615, 380, 65, 20)

        self.players_log_label.setGeometry(10, 70, 190, 90)
        self.players_scroll.setWidget(self.players_log_label)
        self.players_scroll.setGeometry(10, 70, 190, 90)
        self.players_log_label.setAlignment(Qt.AlignTop)

    def manejo_boton(self):
        mensaje = {"status": "mensaje",
                   "data": {"usuario": self.nombre_usuario,
                            "contenido": self.usuario_line_edit.text()}}
        self.servidor_signal.emit(mensaje)
        self.usuario_line_edit.setText("")

    def actualizar_chat(self, contenido):
        print(contenido)
        self.chat_log += f"{contenido}\n"
        self.chat_log_label.setText(self.chat_log)

    def actualizar_display(self, usuario, color, jefe):
        if jefe:
            self.players_log += f"{self.colores['color']}: {usuario} (JEFE)\n"
        else:
            self.players_log += f"{self.colores[str(color)]}: {usuario}\n"
        self.players_log_label.setText(self.players_log)

    def salir(self):

        mensaje = {"status": "salir"}
        self.servidor_signal.emit(mensaje)
        self.close()
        self.inicio.show()

    def es_jefe(self, boolean):
        if boolean:
            self.label_par.show()
            self.label_vel.show()
            self.label_punt.show()
            self.label_jefe.show()
            self.label_poder.show()
            self.grupo_poderes.show()
            self.boton_inicio.show()
            self.sel_punt.show()
            self.sel_vel.show()
        else:
            self.label_par.hide()
            self.label_vel.hide()
            self.label_punt.hide()
            self.label_jefe.hide()
            self.label_poder.hide()
            self.grupo_poderes.hide()
            self.boton_inicio.hide()
            self.sel_punt.hide()
            self.sel_vel.hide()

    def timer_iniciar(self):
        self.num_contador -= 1
        self.contador.display(self.num_contador)
        if self.num_contador == 0:
            self.timer.stop()
            self.contador.hide()
            self.hide()
            self.juego.show()
            self.num_contador = 10
            self.contador.display(self.num_contador)
            self.juego.señal_comenzar()

    def iniciar(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_iniciar)
        self.boton_salir.setEnabled(False)
        self.contador.show()
        self.timer.start(1000)


class SalaJuego(nombre_juego, clase_juego):
    signal_choque = pyqtSignal()
    signal_o = pyqtSignal(float)
    servidor_signal = pyqtSignal(dict)

    def __init__(self, parent, cliente):

        super().__init__()
        self.setupUi(self)

        self.setFocusPolicy(Qt.StrongFocus)

        self.client = cliente
        self.parent = parent

        self.inicio = parent.inicio

        self.actualizador = Actualizador(self)

        self.colores = {"7": Qt.red, "9": Qt.blue, "8": Qt.green,
                        "12": Qt.yellow, "11": Qt.magenta,
                        "17": Qt.darkMagenta, "10": Qt.cyan,
                        "3": Qt.white, "2": Qt.black}

        self.image = QImage(750, 500, QImage.Format_RGB32)
        self.image.fill(Qt.black)

        self.label_ganar.hide()
        self.label_perder.hide()
        self.label_pausado.hide()

        self.der = None
        self.izq = None

        self.alive = True
        self.pausado = True
        self.pos = None

        self.x = None
        self.y = None
        self.o = None

        self.timer = QTimer()
        self.timer.timeout.connect(self.revisar_listo)
        self.timer.start(250)

        self.signal_o.connect(self.actualizador.actualizar_o)
        self.signal_choque.connect(self.actualizador.choque)
        self.servidor_signal.connect(cliente.send)

        self.boton_pausa.clicked.connect(self.pausar)
        self.boton_salir.clicked.connect(self.salir)
        self.boton_nuevo.clicked.connect(self.juego_nuevo)

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Space:
            if self.alive:
                msg = {"status": "pausa"}
                self.servidor_signal.emit(msg)

        if event.key() == self.izq and self.alive and not self.pausado:
            self.signal_o.emit(0.05)

        if event.key() == self.der and self.alive and not self.pausado:
            self.signal_o.emit(-0.05)

    def keyReleaseEvent(self, event):

        if event.key() == self.izq and self.alive and not self.pausado:
            self.signal_o.emit(0.05)

        if event.key() == self.der and self.alive and not self.pausado:
            self.signal_o.emit(-0.05)

    def move(self, x, y):
        self.x = x
        self.y = y

        self.last_pos = QPoint(self.x, self.y)

        if self.image.pixelColor(self.x, self.y) != Qt.black:
            self.signal_choque.emit()
        msg = {"status": "pintar", "data": {"pos1": [self.pos.x(),
                                                     self.pos.y()],
                                            "pos2": [self.last_pos.x(),
                                                     self.last_pos.y()],
                                            "color": self.client.color}}
        self.servidor_signal.emit(msg)
        self.pos = self.last_pos

    def pintar(self, pos1, pos2, color):
        painter = QPainter(self.image)
        painter.setPen(QPen(self.colores[color], 4, Qt.SolidLine, Qt.RoundCap,
                            Qt.RoundJoin))
        pos_inicial = QPoint(pos1[0], pos1[1])
        pos_final = QPoint(pos2[0], pos2[1])

        painter.drawLine(pos_inicial, pos_final)
        self.update()

    def pausar(self):
        if self.alive:
            if self.pausado:
                self.forward.start()
                self.label_pausado.hide()
                self.pausado = False
                return
            else:
                self.forward.terminate()
                self.label_pausado.show()
                self.pausado = True
                return

    def actualizar_o(self, o):
        self.o = o

    def is_alive(self, boolean):
        self.alive = boolean

    def paintEvent(self, event):
        canvas = QPainter(self)
        canvas.drawImage(QPoint(250, 0), self.image)

    def señal_comenzar(self):
        msg = {"status": "comenzar"}
        self.servidor_signal.emit(msg)

    def comenzar(self, x1, y1, x2, y2, o):
        self.x = x2
        self.y = y2
        self.pos = QPoint(self.x, self.y)
        self.o = o
        msg = {"status": "pintar", "data": {"pos1": [x1,
                                                     y1],
                                            "pos2": [self.x,
                                                     self.y],
                                            "color": self.client.color}}
        self.servidor_signal.emit(msg)

    def revisar_listo(self):
        if self.x and self.y and self.o:
            self.crear_thread()
            self.timer.stop()

    def crear_thread(self):
        self.forward = Avanzar(self)

    def salir(self):
        self.forward.terminate()
        self.x = None
        self.y = None
        self.o = None
        self.image.fill(Qt.black)
        mensaje = {"status": "salir"}
        self.servidor_signal.emit(mensaje)
        self.close()
        self.parent.inicio.show()

    def juego_nuevo(self):
        self.forward.terminate()
        self.x = None
        self.y = None
        self.o = None
        msg = {"status": "nuevo"}
        self.servidor_signal.emit(msg)
        msg = {"status": "jefe"}
        self.servidor_signal.emit(msg)
        self.image.fill(Qt.black)
        self.hide()
        self.parent.show()
        self.parent.boton_salir.setEnabled(True)



if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    mi_juego = SalaJuego()
    mi_juego.show()
    app.exec()
