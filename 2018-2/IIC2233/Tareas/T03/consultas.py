from estructuras import Lista
from excepciones import InvalidQuery
from clases import Casa, Transmision, Distribucion, Elevadora


def energia_comuna(red, comuna):
    red.calcular_consumo_real(red.nodos)
    energia = 0
    total = 0
    error = True
    for nodo in red.nodos:
        if nodo.valor.comuna == comuna:
            error = False
    if error:
        raise InvalidQuery(f"La comuna {comuna} no existe en la red")
    for nodo in red.nodos:
        total += float(nodo.valor.consumo_real)
        if nodo.valor.comuna == comuna:
            energia += float(nodo.valor.consumo_real)
    if total == 0:
        porc = 0
    else:
        porc = energia/total * 100
    return Lista(energia, porc)


def mayor_consumo(red, sigla):
    red.calcular_consumo_real(red.nodos)
    lista_sist = Lista("SIC", "SING", "MAGALLANES", "AYSEN")
    mayor = 0
    nodo_mayor = None
    if sigla not in lista_sist:
        raise InvalidQuery(f"La sigla {sigla} no existe")
    for nodo in red.nodos:
        if isinstance(nodo.valor, Casa) and nodo.valor.sist == sigla:
            if nodo_mayor is None:
                nodo_mayor = nodo.valor
            if float(nodo.valor.consumo_real) > mayor:
                mayor = float(nodo.valor.consumo_real)
                nodo_mayor = nodo.valor
    if nodo_mayor is None:
        raise InvalidQuery(f"No existen casas en el sistema {sigla}")
    return nodo_mayor


def menor_consumo(red, sigla):
    red.calcular_consumo_real(red.nodos)
    lista_sist = Lista("SIC", "SING", "MAGALLANES", "AYSEN")
    menor = None
    nodo_menor = None
    if sigla not in lista_sist:
        raise InvalidQuery(f"La sigla {sigla} no existe")
    for nodo in red.nodos:
        if isinstance(nodo.valor, Casa) and nodo.valor.sist == sigla:
            if nodo_menor is None:
                nodo_menor = nodo.valor
                menor = float(nodo.valor.consumo_real)
            if float(nodo.valor.consumo_real) > menor:
                menor = float(nodo.valor.consumo_real)
                nodo_menor = nodo.valor
    if nodo_menor is None:
        raise InvalidQuery(f"No existen casas en el sistema {sigla}")
    return nodo_menor


def encontrar_cam_elev(red, id1, clase, camino):
    nodo = red.encontrar_nodo(clase, id1)
    for padre in nodo.padres:
        camino.append(padre.valor)
        if isinstance(padre.valor, Elevadora):
            return camino
        else:
            return encontrar_cam_elev(
                red, padre.valor.id, type(padre.valor), camino)




def potencia_perdida(red, id_):
    nodo = red.encontrar_nodo(Casa, id_)
    if nodo is False:
        raise InvalidQuery(f"No existe la casa de id {id_}")
    c = Lista()
    camino = encontrar_cam_elev(red, id_, Casa, c)
    perdida = float(camino[len(camino) - 1].valor.consumo_real
                    ) - float(nodo.consumo_real)
    return perdida





def consumo_subestacion(red, id_, num):
    lista_num = Lista("1", "2")
    if id_.isnumeric() is False:
        raise InvalidQuery("El id debe ser un número entero")
    if num.isnumeric() is False or num not in lista_num:
        raise InvalidQuery(f"El numero {num} no es válido")
    if num == "1":
        clase = Transmision
    else:
        clase = Distribucion
    nodo = red.encontrar_nodo(clase, id_)
    if nodo is False:
        raise InvalidQuery(f"No existe una subestacion de clase {clase}"
                           f" e id {id_}")
    red.calcular_consumo_real(red.nodos)
    nodo = red.encontrar_nodo(clase, id_)
    consumo = nodo.potencia
    return consumo


