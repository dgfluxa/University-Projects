# Aqui abajo debes escribir el código de tus clases
from abc import ABC


class Ser(ABC):
    def __init__(self, nombre, fuerza, resistencia, vida, ki, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nombre = nombre
        self.fuerza = fuerza
        self.res = resistencia
        self.vida = vida
        self.ki = ki

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, v):
        if int(v) < 0:
            self._vida = 0
        else:
            self._vida = v


class Humano(Ser):
    def __init__(self, inteligencia=100, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.int = inteligencia

    def atacar(self, enemigo):
        vida_perdida = self.ki*((1 + self.fuerza - enemigo.res)/2)
        enemigo.vida = enemigo.vida - vida_perdida
        print(f"{self.nombre} le quita {vida_perdida} de vida a"
              f" {enemigo.nombre}")

    def meditar(self):
        self.ki += (self.int/100)
        print(f"Yo {self.nombre} estoy meditando!")


class Extraterrestre(Ser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def atacar(self, enemigo):
        vida_perdida = self.ki*(1 + self.fuerza - enemigo.res)
        enemigo.vida -= vida_perdida
        self.fuerza += 0.3 * self.fuerza
        print(f"{self.nombre} le quita {vida_perdida} de vida a"
              f" {enemigo.nombre}")


class Supersaiyayin(Extraterrestre, Humano):
    def __init__(self, cola=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cola = cola

    def perder_cola(self):
        # Se agregaron prints para aclarar lo ocurrido
        if self.cola:
            self.res -= 0.6 * self.res
            print(f"{self.nombre} ha perdido su cola")
            self.cola = False
        else:
            print(f"{self.nombre} no tenía cola")


class Hakashi(Extraterrestre):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def robar_ki(self, *adversarios):
        # Se agregaron prints para aclarar lo ocurrido
        ki_robado = 0
        for adversario in adversarios:
            ki_robado += 0.5 * adversario.ki
            adversario.ki = 0.5 * adversario.ki
        self.ki += ki_robado
        print(f"{self.nombre} ha robado {ki_robado} de ki, su ki actual es de "
              f"{self.ki}")


if __name__ == '__main__':
    """
    A continuación debes instanciar cada uno de los objetos pedidos,
    para que puedas simular la batalla.
    """
    humano = Humano(inteligencia=150, nombre="Pepe", fuerza=51, resistencia=30,
                    vida=200, ki=50)
    saiyayin1 = Supersaiyayin(nombre="Cooler Pepe", fuerza=60, resistencia=30,
                              vida=200, ki=50)
    saiyayin2 = Supersaiyayin(nombre="Ermenegildo", fuerza=100, resistencia=50,
                              vida=1000, ki=200)
    hakashi1 = Hakashi(nombre="Rapero Maldito", fuerza=60, resistencia=50,
                       vida=300, ki=10)
    hakashi2 = Hakashi(nombre="Care Malo", fuerza=100, resistencia=100,
                       vida=600, ki=50)