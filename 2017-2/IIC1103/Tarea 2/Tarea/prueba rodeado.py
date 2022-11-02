def suma(lista_mov):
    suma=int(lista_mov[0])+int(lista_mov[1])
    return suma

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


L = [["G", "G", "C", "G", "N"], ["G", "N", "G", "G", "G"], ["G", "N", "G", "N", "N"], ["N", "N", "N", "G", "N"],
         ["N", "N", "N", "N", "N"]]

ubicacion_C=[0,0]

print(rodeado(ubicacion_C,L))

