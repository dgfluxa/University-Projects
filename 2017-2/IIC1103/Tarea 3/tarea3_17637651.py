#Clases

class Simulacion:
    def __init__(self,consumibles,equipos,pruebas,personaje,tiempo):
        self.listaC = consumibles
        self.listaE = equipos
        self.listaP = pruebas
        self.personaje = personaje
        self.tiempoi = tiempo

    def equipamiento(self):
        personajei = str(self.personaje)
        contador = 0
        print("-*-" * 50)

        print(
            "Aquí está el listado de todos los equipamientos que hay, elige un número para equiparlo. En caso de que ya no quieras equiparte más ingresa -1.")
        print("Solo puedes elegir 3 equipamientos, por lo que debes elegir sabiamente")
        print("")


        while True:

            if len(self.listaE) == 0:
                print("")
                print("No quedan equipamientos disponibles")
                return personajei

            elif contador == 3:
                print("")
                print("Llegaste al máximo de equipamientos")
                return personajei

            for i in self.listaE:
                print(str(self.listaE.index(i) + 1) + ".-", i)

            print("")
            numero = int(input())

            if numero == int(-1):
                return personajei

            elif 1 <= numero <= len(self.listaE):
                equipo = self.listaE[numero - 1]

                if equipo.aa == "vida":
                    self.personaje.vida = int(round(self.personaje.vida * equipo.bon))

                elif equipo.aa == "destreza":
                    self.personaje.des = int(round(self.personaje.des * equipo.bon))

                elif equipo.aa == "resistencia":
                    self.personaje.res = int(round(self.personaje.res * equipo.bon))

                elif equipo.aa == "inteligencia":
                    self.personaje.inte = int(round(self.personaje.inte * int(equipo.bon)))

                elif equipo.aa == "suerte":
                    self.personaje.suerte = int(round(self.personaje.suerte * equipo.bon))

                self.listaE.pop(numero - 1)
                contador += 1

            else:
                print("Ese no es un número válido, por favor ingresa otro")


    def consumibles(self):

        print("-*-" * 50)
        print("Aquí están los consumibles, selecciona el número del objeto que deseas.")
        print("Para comenzar la evaluación ingresa -1.")
        vidaA = 0
        desA = 0
        resA = 0
        inteA = 0
        suerteA = 0

        while True:

            if len(self.listaC) == 0:
                print("")
                print("No quedan consumibles disponibles")
                lista = [vidaA, desA, resA, inteA, suerteA]
                return lista

            else:
                print("Stats actuales:", personaje)
                print("Tiempo disponible:", self.personaje.tiempo)

            for i in self.listaC:
                print(str(self.listaC.index(i) + 1) + ".-", i)
            print("")
            numero = int(input())

            if numero == int(-1):
                lista = [vidaA, desA, resA, inteA, suerteA]
                return lista

            elif 1 <= numero <= len(self.listaC):
                cons = self.listaC[numero - 1]

                if cons.sa == "vida":
                    vidaA += cons.ca
                    self.personaje.vida += cons.ca
                    self.personaje.tiempo -= cons.ct

                elif cons.sa == "destreza":
                    desA += cons.ca
                    self.personaje.des += cons.ca
                    self.personaje.tiempo -= cons.ct

                elif cons.sa == "resistencia":
                    resA += cons.ca
                    self.personaje.res += cons.ca
                    self.personaje.tiempo -= cons.ct

                elif cons.sa == "inteligencia":
                    inteA += cons.ca
                    self.personaje.inte += cons.ca
                    self.personaje.tiempo -= cons.ct

                elif cons.sa == "suerte":
                    suerteA += cons.ca
                    self.personaje.suerte += cons.ca
                    self.personaje.tiempo -= cons.ct

                cons.stock -= 1
                if cons.stock == 0:
                    self.listaC.pop(numero - 1)

            else:
                print("Ese no es un número válido, por favor ingresa otro")

    def pruebas(self):

        print("")
        print("-*-" * 50)
        print("¡Llegó la hora de la evaluación!")

        for prueba in self.listaP:
            print("Prepárate "+str(self.personaje.n)+" para enfrentar a la " + str(prueba.n) + " (música dramática)")
            print("Esta prueba posee", prueba, "¿Podrás superarla?")

            lista = self.consumibles()
            vidaA = lista[0]
            desA = lista[1]
            resA = lista[2]
            inteA = lista[3]
            suerteA = lista[4]


            vidaperdida1 = ((self.personaje.des - prueba.des) + (self.personaje.res - prueba.res) + (
            self.personaje.inte - prueba.inte) + (
                                self.personaje.suerte - prueba.suerte))

            if prueba.deb == "destreza":
                vidaperdida2 = (prueba.vida // self.personaje.des)

            elif prueba.deb == "resistencia":
                vidaperdida2 = (prueba.vida // self.personaje.res)

            elif prueba.deb == "inteligencia":
                vidaperdida2 = (prueba.vida // self.personaje.inte)

            else:
                vidaperdida2 = (prueba.vida // self.personaje.suerte)

            vidaperdida = (vidaperdida1 * vidaperdida2)
            if vidaperdida >= 0:
                pass
            else:
                self.personaje.vida += vidaperdida

            self.personaje.vida -= vidaA
            self.personaje.des -= desA
            self.personaje.res -= resA
            self.personaje.inte -= inteA
            self.personaje.suerte -= suerteA

            if self.personaje.vida <= 0:
                print("")
                print("-*-" * 50)
                print("¡Oh no, te has quedado sin vida!.")
                print("La "+str(prueba.n)+" te ha derrotado, vuelve a intentarlo con una nueva estrategia.")
                return False

            else:
                print("")
                print("-*-" * 50)
                print("¡Felicitaciones "+str(self.personaje.n)+"!, derrotaste a la"+str(prueba.n))
                print("Estos son tus stats tras la prueba: "+str(self.personaje))
                print("-*-" * 50)
                print("")
                print("Un tiempo después...")
                print("")
                print("-*-" * 50)

        return True





    def run(self):

        personajei = self.equipamiento()

        gana = self.pruebas()

        if gana == True:
            print("-*-" * 50)
            print("-*-" * 50)
            print("-*-" * 50)
            print("")
            print("¡Muchas Felicitaciones "+str(self.personaje.n)+"!, has logrado pasar todas tus pruebas")
            print("Estos fueron tus stats finales: "+str(self.personaje))
            print("")
            print("-*-" * 50)
            print("-*-" * 50)
            print("-*-" * 50)
            print("")
            while True:
                print("¿Deseas guardar tus stats finales?(Ingresa (1) para guardar y (2) para terminar sin guardar)")
                guardar = int(input())
                if guardar == 1:
                    listapi = personajei.split(" ")

                    print("Por favor ingresa el nombre de la partida")
                    nombre = str(input())
                    archivo = open(nombre+".txt", "w", encoding="utf-8")
                    archivo.write(str(self.personaje.n)+"\n")
                    archivo.write(str(listapi[1])+","+str(listapi[3])+","+str(listapi[5])+","+str(listapi[7])+","+str(listapi[9])+","+str(self.tiempoi) + "\n")
                    archivo.write(
                        str(self.personaje.vida) +","+ str(self.personaje.des) +","+ str(self.personaje.res) +","+ str(self.personaje.inte) +","+ str(
                            self.personaje.suerte) +","+ str(self.personaje.tiempo) + "\n")
                    archivo.write(str(int(listapi[1]) - self.personaje.vida)+"\n")
                    nP = []
                    for prueba in self.listaP:
                        nP.append(prueba.n)
                    archivo.write(str(",".join(nP))+"\n")
                    archivo.write(str(int(self.tiempoi) - int(self.personaje.tiempo))+"\n")
                    archivo.close()
                    print("Tu archivo se ha guardado con éxito")
                    print("¡Adiós, " + str(self.personaje.n) + "!")



                    return


                elif guardar == 2:
                    print("Hasta luego")
                    return
                else:
                    print("Carácter inválido, por favor ingresa 1 o 2")



class Personaje:
    def __init__(self,nombre, vida, des, res, inte, suerte, tiempo):
        self.n = nombre
        self.vida = int(vida)
        self.des = int(des)
        self.res = int(res)
        self.inte = int(inte)
        self.suerte = int(suerte)
        self.tiempo = int(tiempo)

    def __str__(self):
        return("Vida: "+str(self.vida)+" Destreza: "+str(self.des)+" Resistencia: "+str(self.res)+" Inteligencia: "+str(self.inte)+" Suerte: "+str(self.suerte))


class Prueba:
    def __init__(self, nombre, vida, des, res, inte, suerte, debilidad):
        self.n = nombre
        self.vida = int(vida)
        self.des = int(des)
        self.res = int(res)
        self.inte = int(inte)
        self.suerte = int(suerte)
        self.deb = debilidad

    def __str__(self):
        return("Vida: "+str(self.vida)+" Destreza: "+str(self.des)+" Resistencia: "+str(self.res)+" Inteligencia: "+str(self.inte)+" Suerte: "+str(self.suerte)+" y es débil contra la "+str(self.deb))

class Consumible:
    def __init__(self, nombre, stock, stataumentado, cantidadaumentada, costotiempo):
        self.n = nombre
        self.stock = int(stock)
        self.sa = stataumentado
        self.ca = int(cantidadaumentada)
        self.ct = int(costotiempo)

    def __str__(self):
        return("("+str(self.stock)+") "+str(self.n)+": "+str(self.ct)+" de tiempo, "+str(self.ca)+" de "+str(self.sa))

    def __return__(self):
        return ("(" + str(self.stock) + ")",str(self.n) + ": " + str(self.ct) + " de tiempo, " + str(self.ca) + " de " + str(self.sa))

class Equipamiento:
    def __init__(self, nombre, atributoaumentado, bonificador):
        self.n = nombre
        self.aa = atributoaumentado
        self.bon = float(bonificador)

    def __str__(self):
        return (self.n+": Bonificador "+str(self.bon)+" a "+str(self.aa))

#Funciones


#Programa

archivo = open("base.txt", "r", encoding="utf-8")#preguntar

linea1 = archivo.readline()
linea1 = linea1.strip("\n")
listal1 = linea1.split(",")
vidab = int(listal1[0])
tiempo = int(listal1[1])
pds = int(listal1[2])

linea2 = archivo.readline()
linea2 = linea2.strip("\n")
listal2 = linea2.split(",")
numC = int(listal2[0])
numE = int(listal2[1])

listaC = []
listaE = []
listaP = []

for i in range(numC):
    linea = archivo.readline()
    linea = linea.strip("\n")
    listalinea = linea.split(",")
    listaC.append(Consumible(listalinea[0], listalinea[1], listalinea[2], listalinea[3], listalinea[4]))

for j in range(numE):
    linea = archivo.readline()
    linea = linea.strip("\n")
    listalinea = linea.split(",")
    listaE.append(Equipamiento(listalinea[0], listalinea[1], listalinea[2]))

for k in range(3):
    lineap = archivo.readline()
    lineap = lineap.strip("\n")
    listap = lineap.split(",")
    prueba = Prueba(listap[0], listap[1], listap[2], listap[3], listap[4], listap[5], listap[6])
    listaP.append(prueba)

archivo.close()


print("Bienvenido a la simulación de pruebas")
print("Por favor escribe el nombre de tu personaje:")

nombre = input()

print("-*-"*50)

print("Muy bien", nombre+", te informo que posees:")
print(vidab,"puntos de Vida base")
print(tiempo, "puntos de Tiempo")
print(pds, "puntos para gastar en stats iniciales")

print("-*-"*50)

while True:
    pds2 = pds
    print("¿Como quieres repartir tus", pds, "puntos?")
    print("Vida:")
    puntos = int(input())
    if puntos <= pds2:
        vida = vidab + puntos
        pds2 -= puntos

        print("Destreza:")
        puntos = int(input())
        if puntos <= pds2:
            des = puntos
            pds2 -= puntos

            print("Resistencia:")
            puntos = int(input())
            if puntos <= pds2:
                res = puntos
                pds2 -= puntos

                print("Inteligencia:")
                puntos = int(input())
                if puntos <= pds2:
                    inte = puntos
                    pds2 -= puntos

                    print("Suerte:")
                    puntos = int(input())
                    if puntos <= pds2:
                        suerte = puntos
                        pds2 -= puntos
                        break

    print("-*-" * 50)
    print("Lo siento, esa cantidad excede lo que tienes disponible.")
    print("Empezaremos de nuevo por si te equivocaste al repartir.")
    print("-*-" * 50)


if pds2 > 0:
    print("¡Te sobran puntos! Dadas tus malas matemáticas, te las asignaremos a Suerte (puede que la necesites).")
    suerte += pds2
    pds2 = 0

personaje = Personaje(nombre, vida, des, res, inte, suerte, tiempo)

print("-*-"*50)
print("Tus stats iniciales son:")
print(personaje)

simulacion = Simulacion(listaC, listaE, listaP, personaje,tiempo)

simulacion.run()


