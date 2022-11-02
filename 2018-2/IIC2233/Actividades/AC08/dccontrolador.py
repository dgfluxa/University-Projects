from collections import Counter, namedtuple

###############################################################################
"""
Excepciones Personalizadas
Acá crea tus excepciones personalizadas
"""


class RepeatedError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


class InconsistencyError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


###############################################################################


class Producto:
    def __init__(self, nombre, precio_base, descuento=0):
        self.nombre = nombre
        self.precio_base = precio_base
        self._descuento = descuento

    @property
    def precio(self):
        return self.precio_base * (1 - self.descuento)

    @precio.setter
    def precio(self, value):
        if value < 0:
            raise ValueError("precio base menor que 0")
        else:
            self.precio = value

    @property
    def descuento(self):
        if self._descuento >= 0 and self._descuento <= 0.5:
            return self._descuento
        raise ValueError("descuento no est´a entre 0 % y 50 %")


    def __str__(self):
        porcentaje_descuento = self.descuento * 100
        return f'{self.nombre}: '\
                f'${self.precio_base} ({porcentaje_descuento}% dscto.)'

    def __repr__(self):
        return f'<Producto {self}>'


class Supermercado:
    CARCTERES_INVALIDOS = '-&%#@*()'

    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = {}
        self.car_inv = '-&%#@*()'


    @property
    def productos(self):
        return self.catalogo.values()

    def agregar_producto(self, codigo, producto):
        for caracter in self.car_inv:
            if caracter in codigo:
                raise ValueError(f"código posee caracteres inválido: "
                                 f"{self.car_inv}")
        if producto in self.productos:
            raise RepeatedError(f"{codigo} ya está siendo utilizado")
        self.catalogo[codigo] = producto

    def __getitem__(self, key):
        return self.catalogo[key]

    def __contains__(self, producto):
        return producto in self.catalogo

    def __iter__(self):
        yield from self.catalogo.values()


class PedidoOnline:
    def __init__(self, supermercado, orden=None):
        self.supermercado = supermercado

        # orden puede ser un arreglo de elementos:
        # ['a', 'a', 'b', 'c', 'a', 'b'] => {'a': 3, 'b': 2, 'c': 1}
        # o un dict con los conteos
        # {'a': 3, 'b': 2, 'c': 1} => {'a': 3, 'b': 2, 'c': 1}
        self.orden = Counter(orden)

    def añadir_producto(self, producto, cantidad=1):
        if cantidad < 0:
            raise ValueError("cantidad menor que 0")
        elif producto not in self.supermercado.productos:
            raise KeyError("el producto no existe en el supermercado")
        else:
            self.orden[producto] += cantidad

    @property
    def productos(self):
        return self.orden.keys()

    @property
    def total(self):
        return sum(producto.precio * cantidad for producto, cantidad in self)

    def comprar(self, dinero):
        if dinero < self.total:
            print('Falta dinero, la compra no fue exitosa.')
            return

        print(f'Compra exitosa! (El Dr. H^4 aplaude silenciosamente).')
        self.orden.clear()
        return dinero - self.total  # vuelto

    def __add__(self, other):
        if self.supermercado != other.supermercado:
            raise InconsistencyError("carros de compra de distintos "
                                     "supermercados")
        else:
            nueva_orden = self.orden + other.orden

            return PedidoOnline(self.supermercado, nueva_orden)

    def __iter__(self):
        yield from self.orden.items()

    def __contains__(self, producto):
        return producto in self.orden
