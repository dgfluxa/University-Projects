
class ElectricalOverload(Exception):
    def __init__(self, sobre_carga, casa_id):
        super().__init__(f"ElectricalOverload: La casa de id {casa_id} se ha "
                         f"sobrecargado en {sobre_carga}kw")


class ForbiddenAction(Exception):
    def __init__(self, accion, mensaje):
        super().__init__(f"ForbiddenAction: Acción '{accion}' no esta "
                         f"permitida {mensaje}")


class InvalidQuery(Exception):
    def __init__(self, mensaje):
        super().__init__(f"InvalidQuery: {mensaje}")
