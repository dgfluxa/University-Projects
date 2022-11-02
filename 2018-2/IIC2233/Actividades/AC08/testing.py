import unittest
from dccontrolador import Producto, Supermercado, PedidoOnline

###############################################################################
"""
Tests
Acá escribe los test pedidos.
"""

class Test(unittest.TestCase):

    def setUp(self):
        self.producto1 = Producto("Prueba", 100)
        self.producto2 = Producto("Prueb@", 100)

    def test_str_bueno(self):
        tupla_prohibidos = ("-", "&", "%", "#", "@", "*", "(", ")")
        for c in self.str_bueno:
            self.assertNotIn(c, tupla_prohibidos)

    def test_str_malo(self):
        tupla_prohibidos = ("-", "&", "%", "#", "@", "*", "(", ")")
        for c in self.str_malo:
            self.assertNotIn(c, tupla_prohibidos)

    def test_





###############################################################################

if __name__ == '__main__':
    unittest.main()
