

class Menu:
    def __init__(self):
        self.opciones = []
        self.lineas = []

    def mostrar_menu(self):
        for linea in self.lineas:
            print(linea)


    def recibir_input(self):
        boleano = True
        while boleano == True:
            eleccion = input("Ingrese un número válido:")
            if eleccion in self.opciones:
                boleano = False
        return eleccion



class MenuSesion(Menu):

    def __init__(self,):
            Menu.__init__(self)
            self.opciones = ["1", "2", "0"]
            self.lineas = ["[1] Nueva Partida", "[2] Cargar Partida, [0] Salir"]
        
    def nueva_partida(self):
        pass

    def cargar_partida(self):
        pass


class MenuPrincipal(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.opciones = ["1", "2", "3", "0"]
        self.lineas = ["[1] Comprar nuevos vehiculos", "[2] Nueva Carrera", "[3] Guardar Partida"
                       , "[0] Salir"]

class MenuCompra(Menu):
    pass

class MenuPreparacion(Menu):
    pass

class MenuCarrera(Menu):
    pass

class MenuPits(Menu):
    pass






hola = MenuSesion()
holi = MenuPrincipal()
holi.mostrar_menu()
holi.recibir_input()



