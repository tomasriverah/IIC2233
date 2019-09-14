import menus
import objetos
import funciones


def inicio():

    menu_sesion = menus.MenuSesion()
    menu_sesion.mostrar_menu()
    menu_sesion.recibir_input()
    juego = objetos.Juego()

    if menu_sesion.eleccion == "1":
        juego.nueva_partida()

    if menu_sesion.eleccion == "2":
        juego.cargar_partida()

    if menu_sesion.eleccion == "0":
        print("PEACE OUT!")
        return


    menu_principal = menus.MenuPrincipal()
    while True:

        menu_principal.mostrar_menu()
        menu_principal.recibir_input()
        if menu_principal.eleccion == "1":
            juego.comprar_vehiculo()
        if menu_principal.eleccion == "2":
            menu_pre = menus.MenuPreparacion()
            menu_pre.mostrar_menu()
            menu_pre.recibir_input()
            if menu_pre.eleccion == "1":
                juego.elegir_pista()
                juego.elegir_vehiculo()
                juego.carrera()

        if menu_principal.eleccion == "3":
            funciones.guardar(juego)

        if menu_principal.eleccion == "0":
            print("PEACE OUT!")
            break



inicio()

