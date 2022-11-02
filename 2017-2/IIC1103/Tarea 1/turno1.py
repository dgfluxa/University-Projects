def turno():
    n=0
    while True:
        numero = random.randint(1, 100)
        if app.agregar(numero) == True:
            print(numero)
            n+=1
        if n==1:
            break
    n=0
    m=0
    while True:
        if numero>80 and numero==int(app.obtener_numero(m,4,1+n)):
            app.marcar_numero(m,4,True,1+n)
        elif numero>60 and numero==int(app.obtener_numero(m,3,1+n)):
            app.marcar_numero(m,3,True,1+n)
        elif numero>40 and numero==int(app.obtener_numero(m,2,1+n)):
            app.marcar_numero(m,2,True,1+n)
        elif numero>20 and numero==int(app.obtener_numero(m,1,1+n)):
            app.marcar_numero(m,1,True,1+n)
        elif numero>0 and numero==int(app.obtener_numero(m,0,1+n)):
            app.marcar_numero(m,0,True,1+n)
        m+=1
        if m==5 and n!=1:
            n+=1
        elif m==5 and n==1:
            n=0
            m=0
            break
