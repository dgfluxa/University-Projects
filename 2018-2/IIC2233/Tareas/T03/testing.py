import unittest
import os
from clase_grafo import RedElectrica
from consultas import energia_comuna


# Rescatado en parte de ayudantia 8
class TestRed(unittest.TestCase):

    def setUp(self):
        self.red = RedElectrica("small")

    def tearDown(self):
        # No se crean archivos ni otros por lo que no hay necesidad de usarlo
        nombre_archivo_creado = 'archivo.txt'
        if os.path.isfile(nombre_archivo_creado):
            os.remove(nombre_archivo_creado)

    def test_energia_comuna(self):
        comuna = "TOCOPILLA"
        energia = 0
        porcentaje = 0
        # Se puede cambiar para otros valores si se conoce el resultado
        self.assertEqual(energia_comuna(self.red, comuna)[0].valor, energia)
        self.assertEqual(energia_comuna(self.red, comuna)[1].valor, porcentaje)







