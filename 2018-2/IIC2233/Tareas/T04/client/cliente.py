'''Código rescatado en parte de ayudantia 13 IIC2233 2018-2'''
'''Código rescatado en parte de contenidos semana 13 IIC2233 2018-2'''
import threading
import socket
import json
from datetime import datetime
from frontend import VentanaInicio
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from backend_cliente import Helper
from parametros import t, s
from random import uniform

HOST = "localhost"
PORT = 8081

class Client:
    """
    Maneja toda la comunicación desde el lado del cliente.

    Implementa el esquema de comunicación donde los primeros 4 bytes de cada
    mensaje indicarán el largo del mensaje enviado.
    """

    def __init__(self, HOST, PORT):
        super().__init__()
        print("Inicializando cliente...")

        self.host = HOST
        self.port = PORT
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.jefe = False
        self.frontend = VentanaInicio(self)
        self.frontend.show()

        self.colores = {"rojo": Qt.red, "azul": Qt.blue, "verde": Qt.green,
                        "amarillo": Qt.yellow, "rosado": Qt.magenta,
                        "morado": Qt.darkMagenta, "cyan": Qt.cyan,
                        "blanco": Qt.white}

        self.color = None
        self.time1 = None
        self.time2 = None
        self.T = uniform(0, t)
        self.S = uniform(0, s)

        self.funciones = {"ingreso": self.conf_ingreso,
                          "registro": self.conf_registro,
                          "mensaje": self.mensaje,
                          "jefe": self.es_jefe,
                          "color": self.elegir_color,
                          "iniciar": self.iniciar,
                          "pintar": self.pintar,
                          "pausa": self.pausa,
                          "comenzar": self.comenzar,
                          "display_jugador": self.display_jugador}

        self.helper = Helper(self)

        try:
            self.connect_to_server()
            self.conectado = True
            self.listen()
        except ConnectionError:
            print("Conexión terminada.")
            self.socket_client.close()
            exit()

    def connect_to_server(self):
        """Crea la conexión al servidor."""

        self.socket_client.connect((self.host, self.port))
        print("Cliente conectado exitosamente al servidor.")

    def listen(self):
        """
        Inicializa el thread que escuchará los mensajes del servidor.

        Es útil hacer un thread diferente para escuchar al servidor,
        ya que de esa forma podremos tener comunicación asíncrona con este.
        Luego, el servidor nos podrá enviar mensajes sin necesidad de
        iniciar una solicitud desde el lado del cliente.
        """

        thread = threading.Thread(target=self.listen_thread, daemon=True)
        thread.start()

    def send(self, msg):
        """
        Envía mensajes al servidor.

        Implementa el mismo protocolo de comunicación que mencionamos;
        es decir, agregar 4 bytes al principio de cada mensaje
        indicando el largo del mensaje enviado.
        """

        mensaje_codificado = json.dumps(msg)
        contenido_mensaje_bytes = mensaje_codificado.encode("utf-8")

        # Tomamos el largo del mensaje y creamos 4 bytes de esto
        tamano_mensaje_bytes = len(contenido_mensaje_bytes).to_bytes(4,
                                                                     byteorder="big")

        # Enviamos al servidor
        self.socket_client.send(tamano_mensaje_bytes + contenido_mensaje_bytes)

    def listen_thread(self):
        while True:
            response_bytes_length = self.socket_client.recv(4)
            response_length = int.from_bytes(
                response_bytes_length, byteorder='big')
            response = bytearray()

            # Recibimos datos hasta que alcancemos la totalidad de los datos
            # indicados en los primeros 4 bytes recibidos.
            while len(response) < response_length:
                read_length = min(4096, response_length - len(response))
                response.extend(self.socket_client.recv(read_length))

            self.handle_command(response)

    def ingresar(self, nombre, clave):
        msg = {"status": "ingresar",
               "data": {"nombre": nombre,
                        "clave": clave}}
        self.send(msg)

    def registrar(self, nombre, clave, conf_clave):
        msg = {"status": "registrar",
               "data": {"nombre": nombre,
                        "clave": clave,
                        "conf_clave": conf_clave}}
        self.send(msg)

    def conf_ingreso(self, recibido):
        # QObject para enviar la pyqtsignal al frontend
        self.helper.conf_ingreso(recibido["valido"])

    def conf_registro(self, recibido):
        # QObject para enviar la pyqtsignal al frontend
        boolean = recibido["data"]["valido"]
        num = recibido["data"]["razon"]
        self.helper.conf_registro(boolean, num)

    def mensaje(self, recibido):
        data = recibido["data"]
        usuario = data["usuario"]
        contenido = data["contenido"]
        usuario = f"({datetime.now().hour}:{datetime.now().minute}) {usuario}"
        self.frontend.ingreso.sala_espera.actualizar_chat(
            f"{usuario}: {contenido}")

    def display_jugador(self, recibido):
        data = recibido["data"]
        usuario = data["usuario"]
        color = data["color"]
        jefe = data["jefe"]
        self.frontend.ingreso.sala_espera.actualizar_display(
            usuario, color, jefe)

    def es_jefe(self, recibido):
        self.helper.jefe(recibido["data"])

    def elegir_color(self, recibido):
        self.color = self.colores[recibido["data"]]

    def boton_iniciar(self):
        msg = {"status": "boton_iniciar"}
        self.send(msg)

    def iniciar(self, recibido):
        self.helper.iniciar()

    def pintar(self, recibido):
        pos1 = recibido["data"]["pos1"]
        pos2 = recibido["data"]["pos2"]
        color = recibido["data"]["color"]
        if self.time1:
            if float((datetime.now() - self.time1).seconds) <= self.T:
                self.helper.pintar(pos1, pos2, str(color))
            else:
                self.time1 = None
                self.time2 = datetime.now()
                self.T = uniform(0, t)
        elif self.time2:
            if float((datetime.now() - self.time2).seconds) <= self.S:
                pass
            else:
                self.time2 = None
                self.time1 = datetime.now()
                self.S = uniform(0, s)

        else:
            self.helper.pintar(pos1, pos2, str(color))

    def pausa(self, recibido):
        if not self.time1:
            self.time1 = datetime.now()
        self.helper.pausa()

    def comenzar(self, recibido):
        x1 = recibido["data"]["pos1"][0]
        y1 = recibido["data"]["pos1"][1]
        x2 = recibido["data"]["pos2"][0]
        y2 = recibido["data"]["pos2"][1]
        o = recibido["data"]["o"]
        self.helper.comenzar(x1, y1, x2, y2, o)

    def handle_command(self, contenido_mensaje_bytes):
        contenido_mensaje = contenido_mensaje_bytes.decode("utf-8")
        recibido = json.loads(contenido_mensaje)
        accion = recibido["status"]

        self.funciones[accion](recibido)

    def terminar_conexion(self):
        print("Conexión terminada")
        self.conectado = False
        self.socket_client.close()
        exit()



    '''def repl(self):
        """
        Captura el input del usuario.

        Lee mensajes desde el terminal y después se pasan a `self.send()`.
        """

        print("------ Consola ------\n>>> ", end='')
        while True:
            msg = input()
            response = self.send(msg)'''

if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])
    cliente = Client(HOST, PORT)
    app.exec()
