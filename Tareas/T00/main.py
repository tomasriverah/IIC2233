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


def crear_tablero(n, m):

    cantidad_legos = math.ceil(m * n * pm.PROB_LEGO)
    pre_tablero = []
    tablero = []

    for i in range(0, cantidad_legos):
        pre_tablero.append("L")

    for i in range(0, m * n - cantidad_legos):
        pre_tablero.append(" ")

    random.shuffle(pre_tablero)

    fila = []
    contador = 0
    for i in pre_tablero:
        fila.append(i)
        contador += 1
        if contador == m:
            tablero.append(fila)
            fila = []
            contador = 0

    return tablero


def crear_hidden_tablero(tablero):
    contador_fila = 0
    lista_prueba = []
    indices_lego = []
    n = len(tablero)
    m = len(tablero[0])

    for fila in tablero:
        contador_casillero = 0
        for casillero in fila:
            if tablero[contador_fila][contador_casillero] == "L":
                indices_lego.append((contador_fila, contador_casillero))

            contador_casillero += 1
        contador_fila += 1

    contador_casillero = 0
    contador_fila = 0

    for fila in tablero:
        contador_casillero = 0
        for casillero in fila:
            legos_colindantes = 0

            if contador_fila - 1 >= 0 and contador_casillero - 1 >= 0:
                if tablero[contador_fila - 1][contador_casillero - 1] == "L":
                    legos_colindantes += 1

            if contador_fila - 1 >= 0:
                if tablero[contador_fila - 1][contador_casillero] == "L":
                    legos_colindantes += 1

            if contador_fila - 1 >= 0 and contador_casillero + 2 <= m:
                if tablero[contador_fila - 1][contador_casillero + 1] == "L":
                    legos_colindantes += 1

            if contador_casillero - 1 >= 0:
                if tablero[contador_fila][contador_casillero - 1] == "L":
                    legos_colindantes += 1

            if contador_casillero + 2 <= m:
                if tablero[contador_fila][contador_casillero + 1] == "L":
                    legos_colindantes += 1

            if contador_fila + 2 <= n and contador_casillero - 1 >= 0:
                if tablero[contador_fila + 1][contador_casillero - 1] == "L":
                    legos_colindantes += 1

            if contador_fila + 2 <= n:
                if tablero[contador_fila + 1][contador_casillero] == "L":
                    legos_colindantes += 1

            if contador_fila + 2 <= n and contador_casillero + 2 <= m:
                if tablero[contador_fila + 1][contador_casillero + 1] == "L":
                    legos_colindantes += 1

            lista_prueba.append(legos_colindantes)
            contador_casillero += 1

        contador_fila += 1

    fila = []
    contador = 0
    hidden_tablero = []
    for i in lista_prueba:
        fila.append(i)
        contador += 1
        if contador == m:
            hidden_tablero.append(fila)
            fila = []
            contador = 0

    for indice in indices_lego:
        hidden_tablero[indice[0]][indice[1]] = "L"

    return hidden_tablero


def jugada(tablero, hidden_tablero):

    move = input("Ingrese una jugada (Formato Ej: 0A, 1C, etc...):")
    n = int(move[0])
    m = move[1]

    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    m_num = letras.find(m)

    indices_lego = []
    indices_jugados = []

    contador_fila = 0

    for fila in tablero:
        contador_casillero = 0
        for casillero in fila:
            if tablero[contador_fila][contador_casillero] == "L":
                indices_lego.append((contador_fila, contador_casillero))
            if tablero[contador_fila][contador_casillero] in [0,1,2,3,4,5,6,7,8]:
                indices_jugados.append((contador_fila, contador_casillero))
            contador_casillero += 1
        contador_fila += 1

    if (n, m_num) in indices_lego:
        return False

    elif (n, m_num) in indices_jugados:
        return "Movimiento invalido"

    else:
        n_legos = hidden_tablero[n][m_num]
        tablero[n][m_num] = n_legos
        return tablero

def juego():

    opcion = menu_de_inicio()

    if opcion == 1:
        tamaño = input("Ingrese tamaño tablero (Ej: (3;3), (5;12), etc...)")
        n = int(tamaño[1])
        m = int(tamaño[3])
        tablero = crear_tablero(n,m)
        tablero_oculto = crear_hidden_tablero(tablero)




board = crear_tablero(3, 3)

tb.print_tablero(board)
print(board)
print(crear_hidden_tablero(board))

jugada(board, crear_hidden_tablero(board))
