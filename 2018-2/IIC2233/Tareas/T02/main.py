from clase_simulacion import Simulacion
import gui
import os
from parameters import delay

print(f"{'-' * 20} Bienvenido a DCCasino {'-'*20}\n")

while True:
    while True:
        print("¿Deseas simular dias (1), horas (2) o minutos (3)?")
        accion = input()
        if accion in ("1", "2", "3"):
            break
        else:
            print("Debes ingesar (1), (2) o (3)\n")
    if accion == "1":
        print("\n¿Cuantos días quieres que dure la simulacion?")
        dias = input()
        if dias.isnumeric():
            tiempo = int(dias) * 1440
            break
        print("Debes ingresar un numero entero\n")
    elif accion == "2":
        print("\n¿Cuantas horas quieres que dure la simulacion?")
        horas = input()
        if horas.isnumeric():
            tiempo = int(horas) * 60
            break
        print("Debes ingresar un numero entero\n")
    else:
        print("\n¿Cuantos minutos quieres que dure la simulacion?")
        minutos = input()
        if minutos.isnumeric():
            tiempo = int(minutos)
            break
        print("Debes ingresar un numero entero\n")

'''
Para poblar con el doble de inst y juegos 
reemplzar sim.poblar() por sim.poblar2()
'''

_PATH = os.path.dirname(os.path.abspath(__file__))
gui.init()
sim = Simulacion(tiempo=tiempo, gui=gui)
sim.gui.set_size(773, 485)
#sim.poblar()
sim.poblar2()
sim.gui.run(sim.tick, delay)
