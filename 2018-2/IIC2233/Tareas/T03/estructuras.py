
class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.siguiente = None

    def __repr__(self):
        return self.valor.__repr__()

    def __str__(self):
        return self.valor.__str__()


# Rescatado en parte de contenidos semana 06
class Lista:

    def __init__(self, *args):
        self.cabeza = None
        self.cola = None
        for arg in args:
            self.append(arg)

    def append(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
            self.cola = self.cabeza
        else:
            self.cola.siguiente = nuevo
            self.cola = self.cola.siguiente

    def extend(self, lista):
        for i in lista:
            self.append(i.valor)

    def remove(self, posicion):
        if posicion > 0 and posicion < len(self) - 1:
            self[posicion - 1].siguiente = self[posicion].siguiente
        elif posicion == 0:
            self.cabeza = self[posicion + 1]
        else:
            self.cola = self[posicion - 1]
            self.cola.siguiente = None

    def index(self, objeto):
        contador = 0
        for nodo in self:
            if nodo.valor == objeto:
                return contador
            contador += 1
        return False

    def __iter__(self):
        return Iterador(self.cabeza)

    def __getitem__(self, item):
        contador = 0
        for i in self:
            if contador == item:
                return i
            else:
                contador += 1

    def __len__(self):
        contador = 0
        for i in self:
            contador += 1
        return contador

    def __repr__(self):
        """Forma una representación de la lista"""
        string = "("
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual != self.cola:
                string = f"{string}{nodo_actual} → "
                nodo_actual = nodo_actual.siguiente
            else:
                string = f"{string}{nodo_actual}"
                nodo_actual = nodo_actual.siguiente
        string += ")"
        return string

    def __contains__(self, item):
        for i in self:
            if i.valor == item:
                return True
        return False

    def __setitem__(self, key, value):
        self[key].valor = value


# Rescatado de contenidos semana 2
class Iterador:

    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterable is None:
            raise StopIteration("Llegamos al final")
        else:
            valor = self.iterable
            self.iterable = self.iterable.siguiente
            return valor
