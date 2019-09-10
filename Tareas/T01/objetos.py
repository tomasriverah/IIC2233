import funciones
import parametros


class Juego():
    def __init__(self):
        self.partida = None
        self.piloto = None
        self.vehiculos = funciones.cargar_vehiculos(parametros.PATHS["VEHICULOS"])
        self.vehiculo_actual = None
        self.contrincantes =funciones.cargar_contrincantes(parametros.PATHS["CONTRINCANTES"])
        self.pistas = funciones.cargar_pistas(parametros.PATHS["PISTAS"])


    def nueva_partida(self):
        self.piloto = funciones.creacion_piloto([])
        self.vehiculo = funciones.vehiculo_incial(piloto)

    def cargar_partida(self):
        self.piloto = funciones.carga_piloto(parametros.PATHS["PILOTOS"])

    def comprar_vehiculo(self):
        vehiculo = funciones.comprar_vehiculo(self.piloto)
        self.vehiculos.append(vehiculo)

    def elegir_vehiculo(self):
        vehiculos_p = [vehiculo for  vehiculo in vehiculos if vehiculo.dueno == self.piloto ]
        eleccion = funciones.seleccion([vehiculo.nombre for vehiculo in vehiculos_p])

    def elegir_pista(self):
        nombres_pistas = [pista.nombre for pista in self.pistas]
        eleccion = funciones.seleccion(nombre for nombre in nombres_pistas)

class Vehiculo():
    def __init__(self, nombre, dueno, categoria):
        self.nombre = nombre
        self. dueno = dueno
        self.categoria =categoria

class Bicicleta(Vehiculo):
    def __init__(self, nombre, dueno, categoria, chasis, carroceria, ruedas, zapatillas, peso):
        Vehiculo.__init__(self, nombre, dueno, categoria)
        self.chasis = chasis
        self.carroceria = carroceria
        self.ruedas = ruedas
        self.zapatillas = zapatillas
        self.peso = peso

class Automovil(Vehiculo):
    def __init__(self,nombre, dueno, categoria, chasis, carroceria, ruedas, motor, peso):
        Vehiculo.__init__(self, nombre, dueno, categoria)
        self.chasis = chasis
        self.carroceria = carroceria
        self.ruedas = ruedas
        self.motor = motor
        self.peso = peso

class Troncomovil(Vehiculo):
    def __init__(self, nombre, dueno, categoria, chasis, carroceria, ruedas, zapatillas, peso):
        Vehiculo.__init__(self, nombre, dueno, categoria)
        self.chasis = chasis
        self.carroceria = carroceria
        self.ruedas = ruedas
        self.zapatillas = zapatillas
        self.peso = peso

class Motocicleta(Vehiculo):
    def __init__(self,nombre, dueno, categoria, chasis, carroceria, ruedas, motor, peso):
        Vehiculo.__init__(self, nombre, dueno, categoria)
        self.chasis = chasis
        self.carroceria = carroceria
        self.ruedas = ruedas
        self.motor = motor
        self.peso = peso

class Pista():
    def __init__(self, nombre, tipo, hielo, rocas, dificultad, numerov, contrincantes, largo):
        self.nombre = nombre
        self.tipo = tipo
        self.hielo = hielo
        self.rocas = rocas
        self.dificultad = dificultad
        self.numerov = numerov
        self.contrincantes = contrincantes
        self.largo = largo

class Piloto():
    def __init__(self, nombre, dinero, personalidad, contextura, equilibrio, experiencia, equipo):
        self.nombre = nombre
        self.equipo = equipo
        self.equilibrio = equilibrio
        self.experiencia = experiencia
        self.contextura = contextura
        self.personalidad = personalidad
        self.dinero = dinero


class Contrincante():
    def __init__(self, nombre, nivel, personalidad, contextura, equilibrio, experiencia, equipo):
        self.nombre = nombre
        self.nivel = nivel
        self.personalidad = personalidad
        self.contextura = contextura
        self.equilibrio = equilibrio
        self.experiencia = experiencia
        self.equipo = equipo

class Carrera():
    def __init__(self, piloto):
        self.piloto = piloto
        self.pista = None

