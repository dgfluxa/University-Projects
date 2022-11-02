

class Aventurero:

    def __init__(self, nombre, vida, ataque, velocidad):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.velocidad = velocidad
        self.poder = self._vida + self.ataque + self.velocidad

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, v):
        if int(v) > 100:
            self._vida = 100
        elif int(v) < 0:
            self._vida = 0
        else:
            self._vida = v

    def grito_de_guerra(self):
        print('{}: "¡Gloria al gran Tini!"'.format(self.nombre))
        pass


class Guerrero(Aventurero):

    def __init__(self, defensa, **kwargs):
        super().__init__(**kwargs)
        self.defensa = defensa
        self.poder = 0.8*self.vida + 2.2*self.ataque + 1.5*self.defensa + \
                     0.5*self.velocidad


class Mago(Aventurero):
    def __init__(self, magia, **kwargs):
        super().__init__(**kwargs)
        self.magia = magia
        self.poder = self.vida + 0.1 * self.ataque + 2.5 * self.magia + \
                     1.4 * self.velocidad


class Monstruo:
    def __init__(self, nombre, vida, poder, jefe):
        self.nombre = nombre
        self.vida = vida
        self.poder = poder
        self.jefe = jefe

    @property
    def es_jefe(self):
        return self.jefe

    @es_jefe.setter
    def es_jefe(self, j):
        if j is True:
            self.poder = self.poder * 3

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, v):
        if int(v) > 100:
            self._vida = 100
        elif int(v) < 0:
            self._vida = 0
        else:
            self._vida = v
