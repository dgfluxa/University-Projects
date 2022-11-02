    #carton1
    while True:
        if m!=5:
            while True:
                n1 = random.randint(1 + (m * 20), 20 + (m * 20))
                n2 = random.randint(1 + (m * 20), 20 + (m * 20))
                n3 = random.randint(1 + (m * 20), 20 + (m * 20))
                n4 = random.randint(1 + (m * 20), 20 + (m * 20))
                n5 = random.randint(1 + (m * 20), 20 + (m * 20))
                app.colocar_numero(0, m, n1, 1)
                if n2 != n1 and n == 0:
                    app.colocar_numero(1, m, n2, 1)
                    n += 1
                if n3 != n1 and n3 != n2 and n == 1:
                    app.colocar_numero(2, m, n3, 1)
                    n += 1
                if n4 != n1 and n4 != n2 and n4 != n3 and n == 2:
                    app.colocar_numero(3, m, n4, 1)
                    n += 1
                if n5 != n1 and n5 != n2 and n5 != n3 and n5 != n4 and n == 3:
                    app.colocar_numero(4, m, n5, 1)
                    n += 1
                if n == 4:
                    n = 0
                    break
            m += 1
        else:
            m = 0
            break
    #carton 2
    while True:
        if m != 5:
            while True:
                n1 = random.randint(1 + (m * 20), 20 + (m * 20))
                n2 = random.randint(1 + (m * 20), 20 + (m * 20))
                n3 = random.randint(1 + (m * 20), 20 + (m * 20))
                n4 = random.randint(1 + (m * 20), 20 + (m * 20))
                n5 = random.randint(1 + (m * 20), 20 + (m * 20))
                app.colocar_numero(0, m, n1, 2)
                if n2 != n1 and n == 0:
                    app.colocar_numero(1, m, n2, 2)
                    n += 1
                if n3 != n1 and n3 != n2 and n == 1:
                    app.colocar_numero(2, m, n3, 2)
                    n += 1
                if n4 != n1 and n4 != n2 and n4 != n3 and n == 2:
                    app.colocar_numero(3, m, n4, 2)
                    n += 1
                if n5 != n1 and n5 != n2 and n5 != n3 and n5 != n4 and n == 3:
                    app.colocar_numero(4, m, n5, 2)
                    n += 1
                if n == 4:
                    n = 0
                    break
            m += 1
        else:
            m = 0
            break
