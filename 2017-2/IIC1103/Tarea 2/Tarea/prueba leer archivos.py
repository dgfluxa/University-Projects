#FUNCIONES

def tablero(L):
    f = ""
    contadormov = 1
    contadorc = 0
    x = 0
    for i in L:
        for j in L[x]:
            if contadorc != 4:
                f += j + "-"
                contadorc += 1
            else:
                f += j
                contadorc += 1
            if contadorc == 5:
                print(f)
                f = ""
                if contadormov == 5:
                    pass
                elif contadormov % 2 == 0:
                    print("|/|\|/|\|")
                    contadormov += 1
                else:
                    print("|\|/|\|/|")
                    contadormov += 1
                contadorc = 0
            else:
                pass
        x += 1

def transformar_tablero(L):
    sL = ""
    lista = []
    for i in L:
        lista.append("-".join(i))
    sL += "#".join(lista)
    return sL

def distancia(lista_mov):
    d=((int(lista_mov[2])-int(lista_mov[0]))**2+(int(lista_mov[3])-int(lista_mov[1]))**2)**(1/2)
    return d

def suma(lista_mov):
    suma=int(lista_mov[0])+int(lista_mov[1])
    return suma

def valido(lista_mov,L):
    for i in lista_mov:
        if int(i) > 4 or int(i) < 0:
            return False
    if L[int(lista_mov[2])][int(lista_mov[3])] != "N":
        return False
    if suma(lista_mov)%2==0:
        if distancia(lista_mov)==1 or distancia(lista_mov)==2**(1/2):
            return True
        elif jugador==c and (distancia(lista_mov)==2*2**(1/2) or distancia(lista_mov)==2): #COMER
            if lista_mov[0] > lista_mov[2]:
                col = int(lista_mov[0]) - 1
            elif lista_mov[0] < lista_mov[2]:
                col = int(lista_mov[2]) - 1
            elif lista_mov[0] == lista_mov[2]:
                col = int(lista_mov[0])
            if lista_mov[1] > lista_mov[3]:
                fil = int(lista_mov[1]) - 1
            elif lista_mov[1] < lista_mov[3]:
                fil = int(lista_mov[3]) - 1
            elif lista_mov[1] == lista_mov[3]:
                fil = int(lista_mov[1])
            if L[col][fil]=="G":
                L[col][fil] = "N"
                return True
            else:
                return False
        else:
            return False
    elif suma(lista_mov)%2!=0:
        if distancia(lista_mov)==1:
            return True
        elif jugador==c and distancia(lista_mov)==2: #COMER
            if lista_mov[0] > lista_mov[2]:
                col = int(lista_mov[0]) - 1
            elif lista_mov[0] < lista_mov[2]:
                col = int(lista_mov[2]) - 1
            elif lista_mov[0] == lista_mov[2]:
                col = int(lista_mov[0])
            if lista_mov[1] > lista_mov[3]:
                fil = int(lista_mov[1]) - 1
            elif lista_mov[1] < lista_mov[3]:
                fil = int(lista_mov[3]) - 1
            elif lista_mov[1] == lista_mov[3]:
                fil = int(lista_mov[1])
            if L[col][fil]=="G":
                L[col][fil]="N"
                return True
            else:
                return False
        else:
            return False

def encontrar_C(L): ######
    columna = 0
    for i in L:
        if i.count("C") != 0:
            fila = i.index("C")
            break
        else:
            columna += 1
    lista=[columna, fila]
    return lista

def comer_otra(ubicacion_C,L):
    col=int(ubicacion_C[0])
    fila=int(ubicacion_C[1])
    if suma(ubicacion_C)%2 != 0:
        l1=[col,fila,(col-2),fila]
        l2=[col,fila,(col+2),fila]
        l3=[col,fila,col,(fila-2)]
        l4=[col,fila,col,(fila+2)]
        if valido(l1,L)==True or valido(l2,L)==True or valido(l3,L)==True or valido(l4,L)==True:
            return True
        else:
            return False
    if suma(ubicacion_C)%2 == 0:
        l1 = [col, fila, (col - 2), fila]
        l2 = [col, fila, (col + 2), fila]
        l3 = [col, fila, col, (fila - 2)]
        l4 = [col, fila, col, (fila + 2)]
        l5 = [col,fila,(col-2),(fila-2)]
        l6 = [col,fila,(col-2),(fila+2)]
        l7 = [col,fila,(col+2),(fila-2)]
        l8 = [col,fila,(col+2),(fila+2)]
        if valido(l1, L) == True or valido(l2, L) == True or valido(l3, L) == True or valido(l4, L) == True or valido(l5, L) == True or valido(l6, L) == True or valido(l7, L) == True or valido(l8, L) == True:
            return True
        else:
            return False

def comio_gallina(lista,L):
    sL = str(transformar_tablero(L))
    print("sL: "+sL)
    L2=L
    if valido(lista,L2) == True:
        L2[int(lista[2])][int(lista[3])] = L2[int(lista[0])][int(lista[1])]
        L2[int(lista[0])][int(lista[1])] = "N"
        sL2 = str(transformar_tablero(L2))
        print("sL2: "+sL2)
        print(L2.count("G"),sL.count("G"))
        if sL2.count("G") < sL.count("G"):
            return True
        else:
            return False
    else:
        return False



def rodeado(ubicacion_C,L):
    fila = ubicacion_C[0]
    col = ubicacion_C[1]
    ocupado=0
    if suma(ubicacion_C)%2!=0:
        if col == 0 or col == 4:
            ocupado+=1
        if fila == 0 or col == 4:
            ocupado+=1
        if -1<(col-1)<5 and L[col-1][fila] == "G":
            ocupado += 1
        if -1<(col+1)<5 and L[col+1][fila] == "G":
            ocupado += 1
        if -1<(fila-1)<5 and L[col][fila-1] == "G":
            ocupado += 1
        if -1<(fila+1)<5 and L[col][fila+1] == "G":
            ocupado += 1
        if ocupado == 4:
            return True
        else:
            return False
    elif suma(ubicacion_C)%2==0:
        if col == 0 or col == 4:
            ocupado+=3
        if fila == 0 or col == 4:
            ocupado+=3
        if ocupado == 6:
            ocupado = 5
        if -1<(col-1)<5 and L[col-1][fila] == "G":
            ocupado += 1
        if -1<(col+1)<5 and L[col+1][fila] == "G":
            ocupado += 1
        if -1<(fila-1)<5 and L[col][fila-1] == "G":
            ocupado += 1
        if -1<(fila+1)<5 and L[col][fila+1] == "G":
            ocupado += 1
        if -1<(col-1)<5 and -1<(fila-1)<5 and L[col-1][fila-1] == "G":
            ocupado += 1
        if -1<(col-1)<5 and -1<(fila+1)<5 and L[col-1][fila+1] == "G":
            ocupado += 1
        if -1<(col+1)<5 and -1<(fila-1)<5 and L[col+1][fila-1] == "G":
            ocupado += 1
        if -1<(col+1)<5 and -1<(fila+1)<5 and L[col+1][fila+1] == "G":
            ocupado += 1
        if ocupado==8:
            return True
        else:
            return False

def ganar(L):  # COMPLETAAAAAAAR
    cantG = 0
    ocupado = 0
    for i in L:
        cantG += i.count("G")
    if cantG <= 10:
        return "C"
    else:  # COMPLETAR GANAN GALLINAS
        pass

L = [["G", "G", "G", "G", "G"],
         ["G", "G", "G", "G", "G"],
         ["G", "N", "C", "N", "G"],
         ["N", "N", "N", "N", "N"],
         ["N", "N", "N", "N", "N"]]
lista_movimientos = []
lista = []
reiniciar=""


nombre = input("Ingrese nombre de la partida (Recuerda poner .txt al final): ")
archivo = open(nombre)
nombres = archivo.readline()
ln=nombres.split(", ")
c=ln[0]
g=ln[1]
linea=archivo.readlines()
print(linea)
tablero(L)
for i in linea:
    if i[0].strip("\n")=="C":
        jugador = c
    else:
        jugador = g
    mov=i[2:9].strip("\n")
    print(jugador.strip("\n")+": "+mov)
    lista=mov.split(",")

    if jugador.strip("\n") == g:
        lista_movimientos.append("G," + mov)
        L[int(lista[2])][int(lista[3])] = L[int(lista[0])][int(lista[1])]
        L[int(lista[0])][int(lista[1])] = "N"
        tablero(L)
        jugador = c
    else:
        lista_movimientos.append("C," + mov)
        L[int(lista[2])][int(lista[3])] = L[int(lista[0])][int(lista[1])]
        L[int(lista[0])][int(lista[1])] = "N"
        tablero(L)
        jugador = g


