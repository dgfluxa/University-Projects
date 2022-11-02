def tablero(L):
    f=""
    contadormov=1
    contadorc=0
    x=0
    for i in L:
        for j in L[x]:
            if contadorc!=4:
                f+=j+"-"
                contadorc+=1
            else:
                f+=j
                contadorc+=1
            if contadorc==5:
                print(f)
                f=""
                if contadormov==5:
                    pass
                elif contadormov%2==0:
                    print("|/|\|/|\|")
                    contadormov+=1
                else:
                    print("|\|/|\|/|")
                    contadormov+=1
                contadorc=0
            else:
                pass
        x+=1

L=[["G","G","G","G","G"],["G","G","G","G","G"],["G","N","C","N","G"],["N","N","N","N","N"],["N","N","N","N","N"]]  
tablero(L)
