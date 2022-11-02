#carton 1
n=0
while True:
    numero=random.randint(1,20)
    if app.agregar(numero) == True:
        app.colocar_numero(n,0,numero,1)
        n+=1
    if n==5:
        n=0
        break
while True:
    numero=random.randint(21,40)
    if app.agregar(numero) == True:
        app.colocar_numero(n,1,numero,1)
        n+=1
    if n==5:
        n=0
        break
while True:
    numero=random.randint(41,60)
    if app.agregar(numero) == True:
        app.colocar_numero(n,2,numero,1)
        n+=1
    if n==5:
        n=0
        break
while True:
    numero=random.randint(61,80)
    if app.agregar(numero) == True:
        app.colocar_numero(n,3,numero,1)
        n+=1
    if n==5:
        n=0
        break
while True:
    numero=random.randint(81,100)
    if app.agregar(numero) == True:
        app.colocar_numero(n,4,numero,1)
        n+=1
    if n==5:
        n=0
        break

#carton 2
n=0
while True:
    numero=random.randint(1,20)
    if app.agregar(numero) == True:
        app.colocar_numero(n,0,numero,2)
        n+=1
    if n==5:
        n=0
        break
while True:
    numero=random.randint(21,40)
    if app.agregar(numero) == True:
        app.colocar_numero(n,1,numero,2)
        n+=1
    if n==5:
        n=0
        break
while True:
    numero=random.randint(41,60)
    if app.agregar(numero) == True:
        app.colocar_numero(n,2,numero,2)
        n+=1
    if n==5:
        n=0
        break
while True:
    numero=random.randint(61,80)
    if app.agregar(numero) == True:
        app.colocar_numero(n,3,numero,2)
        n+=1
    if n==5:
        n=0
        break
while True:
    numero=random.randint(81,100)
    if app.agregar(numero) == True:
        app.colocar_numero(n,4,numero,2)
        n+=1
    if n==5:
        n=0
        break
