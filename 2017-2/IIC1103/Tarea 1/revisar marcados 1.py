def revisar_ganador():
    while True:
        f=0
        c=0
        j=1
        p1=0
        p2=0
        if app.esta marcado(f,c,j)==True:
            f+=1
            if j==1:
                p1+=1
            elif j==2:
                p2+=1
            if f==5:
                f=0
                c+=1
                if c==5:
                    j+=1
                    if j==3:
                        break
    if p1==25 and p2==25:
        print("Empate")
    elif p1==25:
        print("Jugador 1 gana")
    elif p2==25:
        print("Jugador 2 gana")
    else:
        break
            

    
