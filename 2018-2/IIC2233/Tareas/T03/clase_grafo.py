from funciones import aplicar_conexiones, crear_lista_sist, poblar_conexiones, \
    poblar_nodos
from clases import Central, Casa, Conexion, Elevadora, Transmision, \
    Distribucion
from estructuras import Lista
from excepciones import ElectricalOverload, ForbiddenAction, InvalidQuery
from copy import deepcopy


class RedElectrica:

    def __init__(self, tamaño):
        self.conexiones = poblar_conexiones(tamaño)
        self.nodos = aplicar_conexiones(poblar_nodos(tamaño), self.conexiones)

    @property
    def nodos_activos(self):
        lista1 = deepcopy(self.nodos)
        return crear_lista_sist(lista1)

    @property
    def demanda_total(self):
        '''Se calcula la demanda de las elevadoras y luego lo que se pierde
        en las conexiones con sus padres con el fin de optimizar, pues
        calcular la demanda de cada central se demoraba mucho.'''
        demanda = 0
        for nodo in self.nodos_activos:
            if type(nodo.valor) is Elevadora:
                demanda_nodo = self.calcular_demanda(nodo.valor)
                for padre in nodo.valor.padres:
                    for n in self.nodos_activos:
                        if padre.valor.id == n.valor.id:
                            for hijo in n.valor.hijos:
                                if hijo.valor[0].valor.id == nodo.valor.id:
                                    demanda += (demanda_nodo / len(
                                        nodo.valor.padres)) / (1 - (
                                            0.0172 *
                                            float(hijo.valor[1].valor.valor))
                                                               / 253)
        return demanda

    @property
    def oferta_total(self):
        oferta = 0
        for nodo in self.nodos_activos:
            if isinstance(nodo.valor, Central):
                oferta += float(nodo.valor.potencia)
        return oferta

    @staticmethod
    def ordenar_nodos(lista):
        lista_nueva = Lista()
        for nodo in lista:
            if isinstance(nodo.valor, Central):
                lista_nueva.append(nodo.valor)
        for nodo in lista:
            if isinstance(nodo.valor, Elevadora):
                lista_nueva.append(nodo.valor)
        for nodo in lista:
            if isinstance(nodo.valor, Transmision):
                lista_nueva.append(nodo.valor)
        for nodo in lista:
            if isinstance(nodo.valor, Distribucion):
                lista_nueva.append(nodo.valor)
        for nodo in lista:
            if isinstance(nodo.valor, Casa):
                lista_nueva.append(nodo.valor)
        return lista_nueva

    def encontrar_nodo(self, clase, id_):
        copia = self.nodos
        for nodo in copia:
            if isinstance(nodo.valor, clase) and str(id_) == str(nodo.valor.id):
                return nodo.valor
        return False

    def encontrar_nodo_activo(self, clase, id_):
        for nodo in self.nodos_activos:
            if isinstance(nodo.valor, clase) and id_ == nodo.valor.id:
                return nodo.valor
        return False

    def encontrar_conexion(self, indice, id1, id2):
        for conexion in self.conexiones[indice]:
            if conexion.valor.id1 == id1 and conexion.valor.id2 == id2:
                return conexion.valor
        return False

    def nodos_agregar(self, lista, nodo):
        lista.append(nodo)
        lista_nueva = self.ordenar_nodos(lista)
        return lista_nueva

    def agregar_nodo(self, clase):
        # se asumirá que se ingresará una comuna y provincia existente
        lista_sist = Lista("SIC", "SING", "MAGALLANES", "AYSEN")
        lista_tipo = Lista("Solar", "Termoelectrica", "Biomasa")
        if clase is Central:
            print("Por favor ingresa: (Sin tildes)")
            id_ = input("ID: ")
            nombre = input("Nombre: ")
            sist = str(input("Sistema: ")).upper()
            prov = str(input("Provincia: ")).upper()
            comuna = str(input("Comuna: ")).upper()
            tipo = str(input("Tipo: ")).lower().capitalize()
            potencia = input("Potencia (MW): ")

            lista = Lista(id_, nombre, sist, prov, comuna, tipo, potencia)

            print("\nEspere mientras procesamos la información\n")

            if id_.isnumeric() is False:
                raise InvalidQuery("El id debe ser un entero")
            elif self.encontrar_nodo(clase, id_) is not False:
                raise InvalidQuery(
                    f"Ya existe una clase {clase} con el id {id_}")
            elif sist not in lista_sist:
                raise InvalidQuery(f"No existe el sistema '{sist}'")
            elif tipo not in lista_tipo:
                raise InvalidQuery(f"El tipo '{tipo}' no es válido")
            elif potencia.isnumeric() is False or 20 > int(potencia) or int(
                    potencia) > 200:
                raise InvalidQuery("La potencia debe ser un entero "
                                   "entre 20 y 200")

            else:
                nodo = clase(*lista)
                self.nodos = self.nodos_agregar(self.nodos, nodo)
                print("¡Listo! Se ha agregado el nodo correctamente\n")

        elif clase is Casa:
            print("Por favor ingresa: (Sin tildes)")
            id_ = input("ID: ")
            sist = str(input("Sistema: ")).upper()
            prov = str(input("Provincia: ")).upper()
            comuna = str(input("Comuna: ")).upper()
            consumo = input("Consumo (kW): ")

            lista = Lista(id_, sist, prov, comuna, consumo)

            print("\nEspere mientras procesamos la información\n")

            if self.encontrar_nodo(clase, id_):
                raise InvalidQuery(
                    f"Ya existe una clase {clase} con el id {id_}")
            elif sist not in lista_sist:
                raise InvalidQuery(f"No existe el sistema '{sist}'")
            elif consumo.isnumeric() is False:
                raise InvalidQuery(f"El consumo debe ser un dato numerico")
            else:
                nodo = clase(*lista)
                self.nodos = self.nodos_agregar(self.nodos, nodo)
                print("¡Listo! Se ha agregado el nodo correctamente\n")
        else:
            print("Por favor ingresa: (Sin tildes)")
            id_ = input("ID: ")
            nombre = input("Nombre: ")
            sist = str(input("Sistema: ")).upper()
            prov = str(input("Provincia: ")).upper()
            comuna = str(input("Comuna: ")).upper()
            consumo = input("Consumo (MW): ")

            lista = Lista(id_, nombre, sist, prov, comuna, consumo)

            print("\nEspere mientras procesamos la información\n")

            if self.encontrar_nodo(clase, id_):
                raise InvalidQuery(
                    f"Ya existe una clase {clase} con el id {id_}")
            elif sist not in lista_sist:
                raise InvalidQuery(f"No existe el sistema '{sist}'")
            elif consumo.isnumeric() is False:
                raise InvalidQuery(f"La potencia debe ser un dato numerico")
            else:
                nodo = clase(*lista)
                self.nodos = self.nodos_agregar(self.nodos, nodo)
                print("¡Listo! Se ha agregado el nodo correctamente\n")

    def remover_nodo(self, clase, id_):
        print("\nEspere mientras procesamos la información\n")
        if id_.isnumeric() is False:
            raise InvalidQuery("El id debe ser un entero")
        elif self.encontrar_nodo(clase, id_) is False:
            raise InvalidQuery(f"No existe un nodo de clase '{clase}'"
                               f" y de id {id_}")
        else:
            nodo = self.encontrar_nodo(clase, id_)
            nodos_copia = deepcopy(self.nodos)
            nodos_copia = nodos_copia.remove(nodos_copia.index(nodo))
            self.calcular_consumo_real(nodos_copia)
            # Levantara ElectricOverload sin cambiar sistema real
            self.nodos.remove(self.nodos.index(nodo))
            for sub_lista in self.conexiones:
                for nodo in sub_lista.valor:
                    if nodo.valor.id1 == id_ or nodo.valor.id2 == id_:
                        sub_lista.valor.remove(sub_lista.index(nodo.valor))
            print("¡Listo! Se eliminó el nodo correctamente\n")

    def agregar_conexion(self, clase1, clase2, id1, id2, dist):
        print("\nEspere mientras procesamos la información\n")
        if clase1 is Central and clase2 is Elevadora:
            indice = 0
        elif clase1 is Elevadora and clase2 is Transmision:
            indice = 1
        elif clase1 is Transmision and clase2 is Distribucion:
            indice = 2
        elif clase1 is Distribucion and clase2 is Casa:
            indice = 3
        else:
            indice = 4

        if id1.isnumeric() is False or id2.isnumeric() is False or \
                dist.isnumeric() is False:
            raise InvalidQuery("El id de los nodos y la distancia deben"
                               " ser numeros")

        elif self.encontrar_nodo(clase1, id1) is False:
            raise InvalidQuery(f"No existe un nodo de clase '{clase1}'"
                               f" e id {id1}")
        elif self.encontrar_nodo(clase2, id2) is False:
            raise InvalidQuery(f"No existe un nodo de clase '{clase2}'"
                               f" e id {id2}")
        elif indice == 3 or indice == 4:
            nodo1 = self.encontrar_nodo(clase1, id1)
            nodo2 = self.encontrar_nodo(clase2, id2)
            if nodo1.comuna != nodo2.comuna:
                mensaje = "entre una casa y otro nodo de una comuna distinta"
                raise ForbiddenAction("agregar_conexion", mensaje)
        else:
            lista = Lista(id1, id2, dist)
            con_copia = deepcopy(self.conexiones)
            con_copia[indice].valor.append(Conexion(*lista))
            nod_copia = deepcopy(self.nodos)
            nodos_copia = aplicar_conexiones(nod_copia, con_copia)
            self.calcular_consumo_real(nodos_copia)
            # Levantara ElectricOverload sin cambiar sistema real
            self.conexiones[indice].valor.append(Conexion(*lista))
            self.nodos = aplicar_conexiones(self.nodos, self.conexiones)
            print("¡Listo! Se agregó la conexión correctamente\n")

    def remover_conexion(self, clase1, clase2, id1, id2):
        print("\nEspere mientras procesamos la información\n")
        if clase1 is Central and clase2 is Elevadora:
            indice = 0
        elif clase1 is Elevadora and clase2 is Transmision:
            indice = 1
        elif clase1 is Transmision and clase2 is Distribucion:
            indice = 2
        elif clase1 is Distribucion and clase2 is Casa:
            indice = 3
        else:
            indice = 4

        if not id1.isnumeric() or not id2.isnumeric():
            raise InvalidQuery("El id de los nodos deben ser numeros enteros")
        elif self.encontrar_conexion(indice, id1, id2) is False:
            raise InvalidQuery("La conexión especificada no existe")
        else:
            conexion = self.encontrar_conexion(indice, id1, id2)
            con_copia = deepcopy(self.conexiones)
            con_copia[indice].valor.remove(
                self.conexiones[indice].valor.index(conexion))
            nod_copia = deepcopy(self.nodos)
            nodos_copia = aplicar_conexiones(nod_copia, con_copia)
            self.calcular_consumo_real(nodos_copia)
            # Levantara ElectricOverload sin cambiar sistema real
            self.conexiones[indice].valor.remove(
                self.conexiones[indice].valor.index(conexion))
            self.nodos = aplicar_conexiones(self.nodos, self.conexiones)
            print("¡Listo! Se eliminó la conexión correctamente\n")

    @staticmethod
    def definir_s(nodo):
        if isinstance(nodo, Central):
            return 253
        elif isinstance(nodo, Elevadora):
            return 202.7
        elif isinstance(nodo, Transmision):
            return 152
        else:
            return 85

    def calcular_demanda(self, nodo):
        s = self.definir_s(nodo)
        demanda = float(nodo.consumo)
        if len(nodo.hijos) == 0:
            return demanda
        else:
            for n in nodo.hijos:
                if self.encontrar_nodo_activo(type(n.valor[0].valor),
                                              n.valor[0].valor.id) is not False:
                    demanda += float(
                        (self.calcular_demanda(n.valor[0].valor) / len(
                            self.encontrar_nodo_activo(type(
                                n.valor[0].valor), n.valor[0].valor.id).padres)
                         ) / (1 - (0.0172 * float(n.valor[1].valor.valor)) / s))

            return demanda

    def calcular_consumo_real(self, lista):
        for nodo in lista:
            if not isinstance(nodo.valor, Central):
                nodo.valor.potencia = 0
        for nodo in lista:
            lista_demandas = Lista()
            s = self.definir_s(nodo.valor)
            if len(nodo.valor.hijos) > 0:
                for hijo in nodo.valor.hijos:
                    nodo_hijo = self.encontrar_nodo_activo(type(
                        hijo.valor[0].valor), hijo.valor[0].valor.id)
                    lista_demandas.append(nodo_hijo.consumo)
                total_demandas = 0
                for i in lista_demandas:
                    total_demandas += float(i.valor)
                for hijo in nodo.valor.hijos:
                    contador = 0
                    nodo_hijo = self.encontrar_nodo_activo(type(
                        hijo.valor[0].valor), hijo.valor[0].valor.id)
                    i = self.nodos.index(nodo_hijo)
                    pot_enviada = (float(nodo.valor.potencia) - float(
                        nodo.valor.consumo)) * (
                            float(lista_demandas[
                                      contador].valor) / total_demandas)
                    if pot_enviada < 0:
                        pot_enviada = 0
                    pot_recibida = pot_enviada / (1 - (0.0172 * float(
                        hijo.valor[1].valor.valor) / s))
                    if pot_recibida < 0:
                        pot_recibida = 0
                    nodo_hijo.potencia += pot_recibida
                    if isinstance(nodo_hijo, Casa) and \
                            nodo_hijo.potencia > 30000:
                        raise ElectricalOverload(nodo_hijo.potencia - 30000,
                                                 nodo_hijo.id)
                    else:
                        self.nodos[i] = nodo_hijo
                        contador += 1

    def calcular_consumo(self, nodo):
        if self.demanda_total >= self.oferta_total:
            return float(nodo.consumo)
        else:
            return float(nodo.consumo_real)

    def print_estadisticas(self):
        print(f'''
ESTADÍSTICAS DE RED:
    Numero Nodos: {len(self.nodos)}
    Numero Nodos Activos: {len(self.nodos_activos)}
    Demanda Total: {self.demanda_total}
    Oferta Total: {self.oferta_total}
    ''')
