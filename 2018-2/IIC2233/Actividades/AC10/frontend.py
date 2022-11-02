# Acá va lo relacionado con la GUI.
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel,\
    QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, Qt
from backend import NameChecker, Character
from random import randint

# Existe codigo recuperado de ayudantia 10


class VentanaInicio(QWidget):

    boton_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_GUI()

    def init_GUI(self):
        self.setGeometry(200, 100, 300, 300)
        self.setWindowTitle("Ingreso usuario")

        self.juego = VentanaPrincipal()

        self.label = QLabel("Nombre Usuario:", self)
        self.label.move(10, 15)
        self.warning = QLabel("El nombre debe tener al menos 6 carácteres y "
                              "estar compuesto solo por letras", self)
        self.warning.move(10, 30)
        self.edit = QLineEdit("", self)
        self.edit.setGeometry(45, 15, 100, 20)
        self.boton = QPushButton("Ingresar", self)

        self.boton.clicked.connect(self.check_name)

        self.spell_checker = NameChecker(self)
        self.boton_signal.connect(self.spell_checker.check)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.label)
        hbox.addWidget(self.edit)
        hbox.addWidget(self.boton)
        hbox.addStretch(1)

        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        vbox.addWidget(self.warning)
        vbox.addStretch(1)
        self.setLayout(vbox)

        self.show()
        self.warning.hide()

    def check_name(self):
        self.boton_signal.emit(self.edit.text())

    def open_window(self, state):
        if state:
            self.close()

            self.juego.show()
        else:
            self.warning.show()


class VentanaPrincipal(QWidget):

    move_character_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_GUI()

    def init_GUI(self):
        self._frame = 1

        self.setGeometry(100, 100, 560, 615)

        self.background = QLabel(self)
        self.background.setPixmap(QPixmap('sprites/map.png'))

        self.backend_character = Character(self, 267, 295)
        self.move_character_signal.connect(self.backend_character.move)

        self.front_character = QLabel(self)
        self.front_character.setPixmap(QPixmap('sprites/pacman_R_2.png'))
        self.front_character.move(267, 295)

    @property
    def frame(self):
        return self._frame

    @frame.setter
    def frame(self, value):
        if value > 3:
            self._frame = 1
        else:
            self._frame = value

    def keyPressEvent(self, e):

        self.frame += 1
        if e.key() == Qt.Key_D:
            self.front_character.setPixmap(QPixmap(
                f'sprites/pacman_R_{self.frame}.png'))
            self.move_character_signal.emit('R')
        if e.key() == Qt.Key_A:
            self.front_character.setPixmap(QPixmap(
                f'sprites/pacman_L_{self.frame}.png'))
            self.move_character_signal.emit('L')
        if e.key() == Qt.Key_W:
            self.front_character.setPixmap(QPixmap(
                f'sprites/pacman_U_{self.frame}.png'))
            self.move_character_signal.emit('U')
        if e.key() == Qt.Key_S:
            self.front_character.setPixmap(QPixmap(
                f'sprites/pacman_D_{self.frame}.png'))
            self.move_character_signal.emit('D')

        if e.key() == Qt.Key_Space:
            x = randint(15, 535)
            y = randint(10, 590)
            guinda = QLabel(self)
            guinda.setPixmap(QPixmap('sprites/cherry.png'))
            guinda.move(x, y)
            guinda.show()

    def update_position(self, event):
        self.front_character.move(event['x'], event['y'])


if __name__ == '__main__':
    app = QApplication([])
    form = VentanaInicio()
    form.show()
    sys.exit(app.exec_())
