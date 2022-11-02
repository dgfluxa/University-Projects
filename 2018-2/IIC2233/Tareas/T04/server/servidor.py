'''Código rescatado en parte de ayudantia 13 IIC2233 2018-2'''
'''Código rescatado en parte de contenidos semana 13 IIC2233 2018-2'''

import threading
import socket

from backend_servidor import generador_usuarios, encriptar, generar_pos, pos_valida

import json

HOST = "localhost"
PORT = 8081

class Server:
    def __init__(self, HOST, PORT):
        print("Inicializando servidor...")

        self.host = HOST
        self.port = PORT
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind_and_listen()
        self.accept_connections()

        self.funciones = {"nuevo_usuario": self.nuevo_usuario,
                          "mensaje": self.enviar_mensaje,
                          "cerrar_sesion": self.cerrar_sesion,
                          "salir": self.salir,
                          "ingresar": self.ingresar,
                          "registrar": self.registrar,
                          "boton_iniciar": self.iniciar,
                          "pintar": self.pintar,
                          "pausa": self.pausa,
                          "comenzar": self.comenzar,
                          "jefe": self.es_jefe,
                          "nuevo": self.nuevo,
                          "display_jugador": self.display_jugador}

        self.colores_predet = {"0": "rojo", "1": "azul", "2": "verde",
                               "3": "amarillo"}

        self.sockets = {}
        self.sockets_espera = []
        self.sockets_juego = []
        self.posiciones = []

    def bind_and_listen(self):
        """
        Enlaza el socket creado con el host y puerto indicado.

        Primero, se enlaza el socket y luego queda esperando
        por conexiones entrantes.
        """
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen(4)
        print(f"Servidor escuchando en {self.host}:{self.port}...")

    def accept_connections(self):
        """
        Inicia el thread que aceptará clientes.

        Aunque podríamos aceptar clientes en el thread principal de la
        instancia, es útil hacerlo en un thread aparte. Esto nos
        permitirá realizar la lógica en la parte del servidor sin dejar
        de aceptar clientes. Por ejemplo, seguir procesando archivos.
        """
        thread = threading.Thread(target=self.accept_connections_thread)
        thread.start()

    def accept_connections_thread(self):
        """
        Es arrancado como thread para aceptar clientes.

        Cada vez que aceptamos un nuevo cliente, iniciamos un
        thread nuevo encargado de manejar el socket para ese cliente.
        """
        print("Servidor aceptando conexiones...")

        while True:
            client_socket, _ = self.socket_server.accept()
            self.sockets[client_socket] = None
            listening_client_thread = threading.Thread(
                target=self.listen_client_thread,
                args=(client_socket, ),
                daemon=True)
            listening_client_thread.start()
            if len(self.sockets) > 4:
                break

    @staticmethod
    def send(valor, socket):
        """
        Envía mensajes hacia algún socket cliente.

        Debemos implementar en este método el protocolo de comunicación
        donde los primeros 4 bytes indicarán el largo del mensaje.
        """
        msg_json = json.dumps(valor)
        msg_bytes = msg_json.encode()

        # Luego tomamos el largo de los bytes y creamos 4 bytes de esto
        msg_length = len(msg_bytes).to_bytes(4, byteorder="big")

        # Finalmente, los enviamos al servidor
        socket.send(msg_length + msg_bytes)

    def listen_client_thread(self, client_socket):
        """
        Es ejecutado como thread que escuchará a un cliente en particular.

        Implementa las funcionalidades del protocolo de comunicación
        que permiten recuperar la informacion enviada.
        """
        print("Servidor conectado a un nuevo cliente...")

        while True:
            try:
                # Primero recibimos los 4 bytes del largo
                response_bytes_length = client_socket.recv(4)
                # Los decodificamos
                response_length = int.from_bytes(response_bytes_length,
                                                 byteorder="big")

                # Luego, creamos un bytearray vacío para juntar el mensaje
                response = bytearray()

                # Recibimos datos hasta que alcancemos la totalidad de los datos
                # indicados en los primeros 4 bytes recibidos.
                while len(response) < response_length:
                    response += client_socket.recv(256)

                # Una vez que tenemos todos los bytes, entonces ahí decodificamos
                response = response.decode()

                # Luego, debemos cargar lo anterior utilizando json
                decoded = json.loads(response)

                # Para evitar hacer muy largo este método, el manejo del mensaje se
                # realizará en otro método
                self.handle_command(decoded, client_socket)
            except ConnectionResetError:
                decoded_message = {"status": "cerrar_sesion"}
                self.handle_command(decoded_message, client_socket)
                break

    def enviar_mensaje(self, recibido, client_socket):
        msj = {"status": "mensaje",
               "data": {"usuario": self.sockets[client_socket],
                        "contenido": recibido["data"]["contenido"]}}
        for skt in self.sockets.keys():
            self.send(msj, skt)

    def es_jefe(self, recibido, client_socket):
        if len(self.sockets_espera) == 1:
            msg = {"status": "jefe", "data": True}
        else:
            msg = {"status": "jefe", "data": False}
        print(msg)
        self.send(msg, client_socket)

    def salir(self, recibido, client_socket):
        self.sockets[client_socket] = None
        if client_socket in self.sockets_espera:
            self.sockets_espera.remove(client_socket)
        elif client_socket in self.sockets_juego:
            self.sockets_juego.remove(client_socket)
        if self.sockets_espera:
            self.es_jefe(True, self.sockets_espera[0])

    def ingresar(self, recibido, client_socket):
        gen = generador_usuarios()
        usuario = recibido["data"]["nombre"]
        clave = recibido["data"]["clave"]
        for lista in gen:

            if str(lista[0]) == str(usuario):
                salt = lista[2].encode("utf-8")
                clave_encriptada, salt_basura = encriptar(clave, salt)
                if str(clave_encriptada) == str(lista[1]):
                    msj = {"status": "ingreso",
                           "valido": True}
                    self.sockets_espera.append(client_socket)
                    self.es_jefe(recibido, client_socket)
                    color = self.colores_predet[
                        str(self.sockets_espera.index(client_socket))]
                    self.color(color, client_socket)
                else:
                    msj = {"status": "ingreso",
                           "valido": False}
                self.send(msj, client_socket)
                return
        msj = {"status": "ingreso",
               "valido": False}
        self.send(msj, client_socket)
        return

    def registrar(self, recibido, client_socket):
        usuario = recibido["data"]["nombre"]
        clave = recibido["data"]["clave"]
        conf_clave = recibido["data"]["conf_clave"]
        if clave != conf_clave:
            msg = {"status": "registro", "data": {"valido": False, "razon": 1}}
            self.send(msg, client_socket)
            return

        gen = generador_usuarios()
        for lista in gen:
            if usuario == lista[0]:
                msg = {"status": "registro",
                       "data": {"valido": False, "razon": 2}}
                self.send(msg, client_socket)
                return
        clave_encriptada, salt = encriptar(clave)
        with open("usuarios.txt", "a", encoding="UTF-8") as archivo:
            archivo.write(
                f"\n{usuario},{clave_encriptada},{salt.decode('UTF-8')}")
            msg = {"status": "registro", "data": {"valido": True, "razon": 0}}
            self.send(msg, client_socket)
            return

    def nuevo_usuario(self, recibido, client_socket):
        self.sockets[client_socket] = recibido["data"]

    def cerrar_sesion(self, recibido, client_socket):
        if client_socket in self.sockets_espera:
            self.sockets_espera.remove(client_socket)
        elif client_socket in self.sockets_juego:
            self.sockets_juego.remove(client_socket)
        if self.sockets_espera:
            self.es_jefe(True, self.sockets_espera[0])
        del self.sockets[client_socket]

    def color(self, color, client_socket):
        msg = {"status": "color",
               "data": color}
        self.send(msg, client_socket)

    def iniciar(self, recibido, client_socket):
        msg = {"status": "iniciar"}
        for socket in self.sockets_espera:
            self.send(msg, socket)
        self.sockets_juego = self.sockets_espera
        self.sockets_espera = []

    def pintar(self, recibido, client_socket):
        for socket in self.sockets_juego:
            self.send(recibido, socket)

    def pausa(self, recibido, client_socket):
        if self.posiciones:
            self.posiciones = []
        for socket in self.sockets_juego:
            self.send(recibido, socket)

    def comenzar(self, recibido, client_socket):
        x, y, o, x2, y2 = generar_pos()
        if pos_valida(self.posiciones, x2, y2):
            self.posiciones.append([x2, y2])
            msg = {"status": "comenzar", "data": {"pos1": [x,
                                                           y],
                                                  "pos2": [x2,
                                                           y2],
                                                  "o": o}}
            self.send(msg, client_socket)
            return
        else:
            self.comenzar(recibido, client_socket)

    def nuevo(self, recibido, client_socket):
        self.sockets_juego.remove(client_socket)
        self.sockets_espera.append(client_socket)
        self.es_jefe(recibido, client_socket)

    def display_jugador(self, recibido, client_socket):
        msj = {"status": "display_jugador",
               "data": {"usuario": self.sockets[client_socket],
                        "color": recibido["data"]["color"],
                        "jefe": recibido["data"]["jefe"]}}
        for skt in self.sockets.keys():
            self.send(msj, skt)

    def handle_command(self, recibido, client_socket):
        print("Mensaje Recibido: {}".format(recibido))
        accion = recibido["status"]

        self.funciones[accion](recibido, client_socket)


if __name__ == "__main__":
    server = Server(HOST, PORT)
