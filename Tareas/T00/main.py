import tablero as tb
import parametros as pm
import math
import random
import string



def menu_de_inicio():

    salir = 0

    while salir == 0:

        salir = 1

        print("Menú de Inicio:")
        print("[1] Nueva Partida")
        print("[2] Cargar Ranking de puntajes")
        print("[3] Ver mejores puntajes")
        print("[0] Salir")

        opcion = input()

        if opcion not in ["0", "1", "2", "3"]:
            print("Ingrese numero valido")
            salir = 0

        elif opcion == 1:
            return (1)
        elif opcion == 1:
            return (2)
        elif opcion == 1:
            return (3)
        elif opcion == 0:
            quit()

def crear_tablero(m, n):

    cantidad_legos = math.ceil(m * n * pm.PROB_LEGO)
    pre_tablero = []
    tablero = []

    for i in range(0, cantidad_legos):
        pre_tablero.append("L")

    for i in range(0, m*n - cantidad_legos):
        pre_tablero.append(" ")

    random.shuffle(pre_tablero)

    fila = []
    contador = 0
    for i in pre_tablero:
        fila.append(i)
        contador += 1
        if contador == n:
            tablero.append(fila)
            fila = []
            contador = 0

    return tablero

tb.print_tablero(crear_tablero(3,5))
