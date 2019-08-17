import tablero as tb
import parametros as pm
import math
import random
import os
import ast
import copy


def menu_de_inicio():
    salir = 0

    while salir == 0:

        salir = 1

        print("Menú de Inicio:")
        print("[1] Nueva Partida")
        print("[2] Cargar Partida")
        print("[3] Ver mejores puntajes")
        print("[0] Salir")

        opcion = input()

        if opcion not in ["0", "1", "2", "3"]:
            print("Ingrese numero valido")
            salir = 0

        elif opcion == "1":
            return 1
        elif opcion == "2":
            return 2
        elif opcion == "3":
            return 3
        elif opcion == "0":
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


def menu_de_juego():
    a = 0
    while a == 0:
        accion = input("[1] Descubrir casillero:\n[2] Guardar \n[3] Guardar y volver al menu de in"
                       "icio:\n[4] Volver al menu de inicio:\n")
        if accion not in ["1", "2", "3", "4"]:
            print("Intenete nuevamente:")
        else:
            a = 1

    return int(accion)

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


def guardar_partida(tablero, hidden_tablero, nombre_usuario):

    if os.path.isdir("partidas") == False:
        os.mkdir("partidas")

    archivo = open("partidas/" + nombre_usuario + ".txt", "w+")
    archivo.writelines(str(tablero)+ ";" + str(hidden_tablero))
    archivo.close()

def guardar_puntaje(nombre_usuario, puntaje):

    archivo = open("puntaje.txt", "a+")
    archivo.writelines(nombre_usuario + ":" + str(puntaje) + "\n")
    archivo.close()

def takesecond(elem):           ### Codigo de Internet referencia en Readme
    return int(elem[1])         ###


def chequear_ranking():

    lista_puntajes = []
    archivo = open("puntaje.txt", "r+")

    lineas = archivo.readlines()

    for i in lineas:
        i = i.rstrip("\n")
        beta = i.split(":")
        lista_puntajes.append(beta)

    lista_puntajes.sort(reverse = True, key = takesecond)
    print("Ranking:")

    if len(lista_puntajes) > 10:
        for i in range (0,10):
            print(str(i + 1) + ".- " + lista_puntajes[i][0] + ": " + lista_puntajes[i][1])

    else:
        for i in range (0, len(lista_puntajes)):
            print(str(i + 1) + ".- " + lista_puntajes[i][0] + ": " + lista_puntajes[i][1])



indices_jugados = []
indices_lego = []

def jugada(tablero, hidden_tablero, puntaje):

    tb.print_tablero(tablero)
    accion = menu_de_juego()

    if accion == 2:
        return 2
    elif accion == 3:
        return 3
    elif accion == 4:
        return 4

    elif accion == 1:
        move = input("Ingrese una jugada (Formato Ej: 0A, 1C, etc...):")
        n = int(move[0])
        m = move[1]

        letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        m_num = letras.find(m)

        contador_fila = 0
        for fila in hidden_tablero:
            contador_casillero = 0
            for casillero in fila:
                if hidden_tablero[contador_fila][contador_casillero] == "L":
                    indices_lego.append((contador_fila, contador_casillero))
                contador_casillero += 1
            contador_fila += 1

        if (n, m_num) in indices_lego:

            for indice in indices_lego:
                tablero[indice[0]][indice[1]] = "L"

            tb.print_tablero(tablero)
            print("****  Pierdes  :( ****")

            return False, tablero
        elif tablero[n][m_num] in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            return print("**********************\n Movimiento invalido \n**********************")
        else:
            n_legos = hidden_tablero[n][m_num]
            tablero[n][m_num] = n_legos
            if check_ganador(tablero, hidden_tablero) == True:
                tb.print_tablero(tablero)
                print("¡¡¡GANASTE!!!")
                print("Puntaje: " + str(puntaje))
                return False, tablero
            return tablero


def check_ganador(tablero, tablero_escondido):
    contador_fila = 0
    copia = copy.deepcopy(tablero_escondido)

    for fila in copia:
        contador_casillero = 0
        for  casillero in fila:
            if copia[contador_fila][contador_casillero] == "L":
                copia[contador_fila][contador_casillero] = " "
            contador_casillero += 1
        contador_fila += 1

    if tablero == copia:
        return True
    else:
        return False

def cargar_tablero(nombre_usuario):

    partidas = os.listdir("partidas/")
    nombre_archivo = nombre_usuario + ".txt"
    if nombre_archivo in partidas:
        partida = open("partidas/" + nombre_archivo, "r+")
        tableros = partida.readline()

        tableros = tableros.split(";")

        tablero = tableros[0]
        tablero = tablero[:-1]
        tablero = tablero[1:]

        hidden_tablero = tableros[1]
        hidden_tablero = hidden_tablero[:-1]
        hidden_tablero = hidden_tablero[1:]

        tablero = ast.literal_eval(tablero)
        hidden_tablero = ast.literal_eval(hidden_tablero)

        return [list(tablero), list(hidden_tablero)]

    else:
        return False

def juego():

    stop = 0
    while stop == 0:

        puntaje = 0
        respuesta = menu_de_inicio()

        if respuesta == 1:
            nombre_usuario = input("Ingrese nombre de usuario: ")
            tamano = input("Ingrese tamaño tablero (Ej: 3;3, 5;12, etc...)")
            x = tamano.split(";")
            n = int(x[0])
            m = int(x[1])
            tablero = crear_tablero(n, m)
            tablero_oculto = crear_hidden_tablero(tablero)
            tablero_de_juego = []

            for i in range(0, n):
                fila = []
                for j in range(0, m):
                    fila.append(" ")
                tablero_de_juego.append(fila)
            a = 0
            while a == 0:
                b = jugada(tablero_de_juego, tablero_oculto, puntaje)

                L = 0
                descubierto = 0
                for fila in tablero_de_juego:
                    for casilla in fila:
                        if casilla in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                            descubierto += 1
                for fila in tablero_oculto:
                    for casilla in fila:
                        if casilla == "L":
                            L =+ 1

                puntaje = descubierto * L * pm.POND_PUNT

                if b == 2:
                    guardar_partida(tablero_de_juego, tablero_oculto, nombre_usuario)
                    guardar_puntaje(nombre_usuario, puntaje)

                elif b == 3:
                    guardar_partida(tablero_de_juego, tablero_oculto, nombre_usuario)
                    guardar_puntaje(nombre_usuario, puntaje)
                    a = 1

                elif b == 4:
                    a = 1

                elif type(b) == tuple:
                    a = 1
                    respuesta = input("Te gustaría guardar la partida y el puntaje?(Y/N)")

                    if respuesta in ["y", "Y"]:
                        guardar_partida(tablero_de_juego, tablero_oculto, nombre_usuario)
                        guardar_puntaje(nombre_usuario, puntaje)



        if respuesta == 2:

            nombre = input("Inserte nombre de usario de partida (sin .txt): ")
            tableros = cargar_tablero(nombre)
            if tableros == False:
                print("Archivo Inexistente")
                pass
            else:
                tablero_de_juego = tableros[0]
                tablero_oculto = tableros[1]

                print(tablero_de_juego)
                print(tablero_oculto)
                a = 0
                while a == 0:
                    b = jugada(tablero_de_juego, tablero_oculto, puntaje)

                    L = 0
                    descubierto = 0
                    for fila in tablero_de_juego:
                        for casilla in fila:
                            if casilla in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                                descubierto += 1
                    for fila in tablero_oculto:
                        for casilla in fila:
                            if casilla == "L":
                                L = + 1

                    puntaje = descubierto * L * pm.POND_PUNT

                    if b == 2:
                        guardar_partida(tablero_de_juego, tablero_oculto, nombre)
                        guardar_puntaje(nombre, puntaje)
                        a = 1
                    elif b == 3:
                        a = 1

                    elif type(b) == tuple:
                        a = 1
                        respuesta = input("Te gustaría guardar la partida y el puntaje?(Y/N)")

                        if respuesta in ["y", "Y"]:
                            guardar_partida(tablero_de_juego, tablero_oculto, nombre_usuario)
                            guardar_puntaje(nombre_usuario, puntaje)


        if respuesta == 3:
            chequear_ranking()

        if respuesta == 0:
            stop = 1


juego()
