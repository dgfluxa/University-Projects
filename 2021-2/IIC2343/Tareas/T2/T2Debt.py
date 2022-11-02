N = 3 # cantidad de amigues en el viaje
amigues = [0, 1, 2] # ID de cada amigue
G = 3 # cantidad de gastos realizados al final del viaje
gastos = [0.0, 3000.0, 2.0, 0.0, 1.0, 1.0, 5000.0, 1.0, 2.0, 1.0, 1000.0, -1.0] # gastos realizados al final del viaje
# Mis variables
lista = [0 for amigo in amigues]

#print("L:", lista)

n = 0 #Posición en gastos

#Agregar Gastos Netos
for i in range(G):
    paga = int(gastos[n]) # Amigo que paga
    #print("paga:", paga)
    n += 1
    cantidad = gastos[n] # Cantidad que paga
    #print("cantidad:", cantidad)
    lista[paga] -= cantidad
    n += 1
    num_part = int(gastos[n]) # Numero de amigos que participan
    #print("num_part:", num_part)
    if num_part == -1:
        num_part = N
        monto = cantidad/num_part
        for amigo in amigues:
            lista[amigo] += monto
        n += 1
    else:
        monto = cantidad/num_part
        n += 1
        for i in range(num_part):
            lista[int(gastos[n + i])] += monto
        n += num_part
    #print("monto:", monto)
print("L:", lista)

#Ajustar Cuentas
for i in range(N):
    for j in range(N):
        if lista[i] > 0:
            if lista[j] < 0:
                if lista[j] + lista[i] < 0:
                    valor = lista[i]
                else:
                    valor = lista[j] * -1
                lista[i] -= valor
                lista[j] += valor
                print(f"{i} debe pagar {valor} a {j}")
                #print("LI:", lista)
            

#print("LF:", lista)



    