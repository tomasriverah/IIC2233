import menus
import objetos


def inicio():

    menu_sesion = menus.MenuSesion()
    menu_sesion.mostrar_menu()
    menu_sesion.recibir_input()
    juego = objetos.Juego()

    if menu_sesion.eleccion == "1":
        juego.nueva_partida()



inicio()