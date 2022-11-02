
from abc import ABC
from estructuras import Lista


class Central:

    def __init__(self, id, nombre, sist, prov, comuna, tipo, potencia):
        self.id = id.valor
        self.nombre = nombre.valor
        self.sist = sist.valor
        self.prov = prov.valor
        self.comuna = comuna.valor
        self.tipo = tipo.valor
        self.potencia = float(potencia.valor) * 1000
        self.hijos = Lista()
        self.padres = Lista()
        self.consumo = 0
        self.consumo_real = 0

    def __str__(self):
        return f'''
        Central {self.id}
        Nombre: {self.nombre}
        Tipo: {self.tipo}
        Sistema: {self.sist}
        Provincia: {self.prov}
        Comuna: {self.comuna}
        '''


class Subestacion(ABC):

    def __init__(self, id, nombre, sist, prov, comuna, consumo):
        super().__init__()
        self.id = id.valor
        self.nombre = nombre.valor
        self.sist = sist.valor
        self.prov = prov.valor
        self.comuna = comuna.valor
        self.consumo = float(consumo.valor) * 1000
        self.hijos = Lista()
        self.padres = Lista()
        self._consumo_real = 0
        self.potencia = 0

    @property
    def consumo_real(self):
        if self.potencia >= self.consumo:
            return self.consumo
        else:
            return self.potencia


class Elevadora(Subestacion):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'''
        Elevadora {self.id}
        Nombre: {self.nombre}
        Sistema: {self.sist}
        Provincia: {self.prov}
        Comuna: {self.comuna}
        '''


class Transmision(Subestacion):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'''
        Transmision {self.id}
        Nombre: {self.nombre}
        Sistema: {self.sist}
        Provincia: {self.prov}
        Comuna: {self.comuna}
        '''


class Distribucion(Subestacion):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'''
        Distribucion {self.id}
        Nombre: {self.nombre}
        Sistema: {self.sist}
        Provincia: {self.prov}
        Comuna: {self.comuna}
        '''


class Casa:

    def __init__(self, id, sist, prov, comuna, consumo):
        self.id = id.valor
        self.sist = sist.valor
        self.prov = prov.valor
        self.comuna = comuna.valor
        self.consumo = consumo.valor
        self.hijos = Lista()
        self.padres = Lista()
        self._consumo_real = 0
        self.potencia = 0

    @property
    def consumo_real(self):
        if float(self.potencia) >= float(self.consumo):
            return self.consumo
        else:
            return self.potencia

    def __str__(self):
        return f'''
        Casa {self.id}
        Sistema: {self.sist}
        Provincia: {self.prov}
        Comuna: {self.comuna}
        '''


class Conexion:

    def __init__(self, id1, id2, dist):
        self.id1 = id1
        self.id2 = id2
        self.dist = dist

    def __repr__(self):
        return f'''
        ({self.id1} -> {self.id2} ({self.dist, type(self.dist), type(
self.dist.valor)}km))'''


