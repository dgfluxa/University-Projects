import json
import os
import os.path as path
import pickle

from clases import Comida, ComidaEncoder

BOOK_PATH = 'recetas.book'


class PyKitchen:
    def __init__(self):
        self.recetas = []
        self.comidas = []
        self.despachadas = []

    def cargar_recetas(self):
        '''Esta función se encarga de cargar el archivo recetas.book'''
        with open("recetas.book", "rb") as archivo:
            self.recetas = pickle.load(archivo)

    def guardar_recetas(self):
        '''Esta función se encarga de guardar las recetas (instancias), en el
        archivo recetas.book'''
        with open("recetas.book", "wb") as archivo:
            archivo.write(pickle.dumps(self.recetas))

    def cocinar(self):
        '''Esta funcion debe:
        - filtrar recetas verificadas
        - crear comidas a partir de estas recetas
        - guardar las comidas en la carpeta horno
        '''
        for receta in self.recetas:
            if receta.verificada:
                comida = Comida.de_receta(receta)
                with open(f"{receta.nombre}.json", "wb") as archivo_comida:
                    archivo_comida.write(json.dumps(comida))

    def despachar_y_botar(self):
        ''' Esta funcion debe:
        - Cargar las comidas que están en la carpeta horno.
            Pro tip: string.endswith('.json') retorna true si un string
            termina con .json
        - Crear instancias de Comida a partir de estas.
        - Guardar en despachadas las que están preparadas
        - Imprimir las comidas que están quemadas
        - Guardar en comidas las no preparadas ni quemadas
        '''

