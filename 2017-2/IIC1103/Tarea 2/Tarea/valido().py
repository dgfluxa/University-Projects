
def suma(lista_mov):
    suma=int(lista_mov[0])+int(lista_mov[1])
    return suma

def distancia(lista_mov):
    d=((int(lista_mov[2])-int(lista_mov[0]))**2+(int(lista_mov[3])-int(lista_mov[1]))**2)**(1/2)
    return d

def valido(lista_mov,L):
    if suma(lista_mov)%2==0:
        if distancia(lista_mov)==1 or distancia(lista_mov)==2**(1/2):
            return True
        elif jugador=="c" and (distancia(lista_mov)==2*2**(1/2) or distancia(lista_mov)==2): #COMER
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
    elif suma(lista_mov)%2!=0:
        if distancia(lista_mov)==1:
            return True
        elif jugador=="c" and distancia(lista_mov)==2: #COMER
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

jugador = "c"

lista_mov=[2,2,0,0]
L = [["N", "G", "G", "G", "G"], ["G", "G", "G", "G", "G"], ["G", "N", "C", "N", "G"], ["N", "N", "N", "N", "N"],
         ["N", "N", "N", "N", "N"]]
print(valido(lista_mov,L))

