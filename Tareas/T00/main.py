import tablero as tb
import parametros as pm
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

        if str.isdigit(opcion) == False:
            print("Ingrese numero valido")
            salir = 0

        if opcion == 1:
            return (1)
        if opcion == 1:
            return (2)
        if opcion == 1:
            return (3)
        if opcion == 0:
            quit()0




menu_de_inicio()

tablero = [[2,3,"L"], [2,4,0], [1,2,3]]
tb.print_tablero(tablero)
