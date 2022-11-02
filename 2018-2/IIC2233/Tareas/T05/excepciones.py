class IngresoInvalido(Exception):
    def __init__(self, msg):
        super().__init__(f"Ingreso Invalido: {msg}")


class ConsultaInvalida(Exception):
    def __init__(self, msg):
        super().__init__(f"Consulta Invalida: {msg}")


class Salir(Exception):
    def __init__(self):
        super().__init__("Salir")


class ErrorBusqueda(Exception):
    def __init__(self, msg):
        super().__init__(f"Error de búsqueda: {msg}")

