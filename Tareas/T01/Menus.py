import parametros


class Menu:
    def __init__(self):
        self.opciones = []
        self.lineas = []
        self.eleccion = -1

    def mostrar_menu(self):
        for linea in self.lineas:
            print(linea)

    def recibir_input(self):
        boleano = True
        while boleano == True:
            eleccion = input("Ingrese un número válido:")
            if eleccion in self.opciones:
                boleano = False
        self.eleccion = eleccion


class MenuSesion(Menu):

    def __init__(self,):
            Menu.__init__(self)
            self.opciones = ["1", "2", "0"]
            self.lineas = ["[1] Nueva Partida", "[2] Cargar Partida","[0] Salir"]


class MenuPrincipal(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.opciones = ["1", "2", "3", "0"]
        self.lineas = ["[1] Comprar nuevos vehiculos", "[2] Nueva Carrera", "[3] Guardar Partida"
                       , "[0] Salir"]


class MenuPreparacion(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.opciones = ["1", "0"]
        self.lineas = ["[1] Seleccionar pista y vehículo", "[0] Salir"]


class MenuCarrera(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.opciones = ["1", "0"]
        self.lineas = ["[1] Entrar a pits", "[0] Seguir en pista"]


class MenuPits(Menu):
    def __init__(self, piloto):
        Menu.__init__(self)
        self.piloto= piloto
        self.mejoras = parametros.MEJORAS
        self.opciones = ["1", "2", "3", "4","0"]
        self.lineas = [f"Dinero disponible ${self.piloto.dinero}",
                       f"[1] CHASIS ${self.mejoras['CHASIS']['COSTO']}",
                       f"[2] CARROCERIA ${self.mejoras['CARROCERIA']['COSTO']}",
                       f"[3] RUEDAS ${self.mejoras['RUEDAS']['COSTO']}",
                       f"[4] MOTOR/ZAPATILLAS ${self.mejoras['MOTOR/ZAPATILLAS']['COSTO']}",
                       "[0] Volver a pista sin mejora" ]
        self.dicc = {"1":"CHASIS", "2":"CARROCERIA", "3":"RUEDAS", "4":"MOTOR/ZAPATILLAS"}


    def aplica_mejoras(self):
        parte = self.dicc[self.eleccion]
        if (self.mejoras[parte]["COSTO"]) > self.piloto.dinero:
            print("***Dinero insfuciente***")
            print("***Por no prestar atención vuelves a pista***")
        opcion = str.lower(parte)
        if parte == "MOTOR/ZAPATILLAS":
            opcion = "motor"
        else:
            self.piloto.dinero -= int(self.mejoras[parte]["COSTO"])
            multiplier = self.mejoras[parte]["EFECTO"]
            setattr(self.piloto.vehiculo, opcion, getattr(self.piloto.vehiculo, opcion)
                    * multiplier)
            return self.piloto.dinero










