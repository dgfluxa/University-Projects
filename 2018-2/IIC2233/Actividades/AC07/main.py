from collections import deque


class Terreno:

    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = set()


class Ciudad:

    def __init__(self, path):
        self.grafo = leer_archivo(path)

    def agregar_calle(self, origen, destino):
        lista_nombres_grafo = [terreno.nombre for terreno in self.grafo]
        if destino not in lista_nombres_grafo:
            self.grafo[Terreno(destino)] = set()
        for terreno in self.grafo:
            if terreno.nombre == origen:
                terreno.conexiones.add(destino)
                self.grafo[terreno].add(destino)

    def eliminar_calle(self, origen, destino):
        for terreno in self.grafo:
            if terreno.nombre == origen:
                if destino in self.grafo[terreno]:
                    terreno.conexiones.remove(destino)
                    return (origen, destino)
        return ("")

    @property
    def terrenos(self):
        conjunto = set()
        for terreno in self.grafo:
            conjunto.add(terreno.nombre)
        return conjunto

    @property
    def calles(self):
        conjunto = set()
        for terreno in self.grafo:
            for dest in self.grafo[terreno]:
                conjunto.add((terreno.nombre, dest))
        return conjunto

    def verificar_ruta(self, ruta):
        nodo_final = ruta[len(ruta)-1]
        nodo_actual = ruta.pop(0)
        if nodo_actual == nodo_final:
            return True
        for terreno in self.grafo:
            if terreno.nombre == nodo_actual:
                if ruta[0] in self.grafo[terreno]:
                    return self.verificar_ruta(ruta)
        return False

    def get_node(self, name):
        for terreno in self.grafo:
            if terreno.nombre == name:
                return terreno
        return None

    def entregar_ruta(self, origen, destino):
        if origen == destino:
            return [origen]
        origen = self.get_node(origen)
        destino = self.get_node(destino)
        if origen is None or destino is None:
            return [""]
        cola = [[origen]]
        visited = list()
        while len(cola):
            current_path = cola.pop(0)
            current = current_path[-1]
            if current not in visited:
                lista_vecinos = [self.get_node(x) for x in current.conexiones]
                for vecino in lista_vecinos:
                    cola.append(list(current_path) + [vecino])
                    if vecino == destino:
                        return [terreno.nombre for terreno in cola[-1]]
                visited.append(current)

        return [""]

    def ruta_corta(self, origen, destino):
        return self.entregar_ruta(origen, destino)


    def ruta_entre_bombas(self, origen, *destinos):
        lista = [origen]
        for dest in destinos:
            tramo = self.ruta_corta(origen, dest)
            if tramo == [""]:
                return tramo
            lista.extend(tramo[1:])
            origen = dest
        return lista

    def ruta_corta_entre_bombas(self, origen, *destinos):
        return self.ruta_entre_bombas(origen, *destinos)


def leer_archivo(path):
    dicc = {}
    with open(path, "r", encoding="UTF-8") as archivo:
        for linea in archivo:
            key, values = linea.strip().split(": ")
            terreno = Terreno(key)
            list_values = values.split(",")
            terreno.conexiones = set(value for value in list_values)
            dicc[terreno] = terreno.conexiones
    return dicc


if __name__ == '__main__':
    city1 = Ciudad("facil.txt")
    city2 = Ciudad("medio.txt")
    city3 = Ciudad("dificil.txt")
    city4 = Ciudad("kratos.txt")
    print(city1.entregar_ruta("A", "G"))
    print(city2.entregar_ruta("A", "G"))
    print(city3.entregar_ruta("A", "H"))
    print(city4.entregar_ruta("A", "F"))
    print(city3.ruta_entre_bombas("A", "G", "D", "F"))
