import funciones
import parametros
import menus
import copy
import random

class Juego():
    def __init__(self):
        self.partida = None
        self.piloto = None
        self.vehiculos = funciones.cargar_vehiculos(parametros.PATHS["VEHICULOS"])
        self.contrincantes =funciones.cargar_contrincantes(parametros.PATHS["CONTRINCANTES"])
        self.pista = None
        self.pistas = funciones.cargar_pistas(parametros.PATHS["PISTAS"])
        self.asignar_vehiculo()


    def nueva_partida(self):
        self.piloto = funciones.creacion_piloto([])
        self.piloto.vehiculo = funciones.vehiculo_incial(self.piloto)
        self.vehiculos.append(self.piloto.vehiculo)

    def cargar_partida(self):
        self.piloto = funciones.carga_piloto(parametros.PATHS["PILOTOS"])

    def comprar_vehiculo(self):
        vehiculo = funciones.comprar_vehiculo(self.piloto)
        self.vehiculos.append(vehiculo)

    def elegir_vehiculo(self):
        vehiculos_p = [vehiculo for  vehiculo in self.vehiculos if vehiculo.dueno == self.piloto.nombre ]
        eleccion = funciones.seleccion([vehiculo.nombre for vehiculo in vehiculos_p])
        for viculo in vehiculos_p:
            if viculo.nombre == eleccion:
                self.piloto.vehiculo = viculo
                self.piloto.vehiculo_og = copy.deepcopy(viculo)

    def asignar_vehiculo(self):
        for viculo in self.vehiculos:
            for contrincante in self.contrincantes:
                if viculo.dueno == contrincante.nombre:
                    contrincante.vehiculo = viculo
                    contrincante.vehiculo_og = copy.deepcopy(viculo)

    def elegir_pista(self):
        nombres_pistas = [pista.nombre for pista in self.pistas]
        eleccion = funciones.seleccion(nombre for nombre in nombres_pistas)
        seleccion_pista = None
        for pista in self.pistas:
            if pista.nombre == eleccion:
                self.pista = pista

    def carrera(self):
        race = Carrera(self.piloto, self.contrincantes, self.pista)
        race.comenzar_carrera()
        race.correr()


class Vehiculo():
    def __init__(self, nombre, dueno, categoria):
        self.nombre = nombre
        self.dueno = dueno
        self.categoria =categoria

class Bicicleta(Vehiculo):
    def __init__(self, nombre, dueno, categoria, chasis, carroceria, ruedas, motor, peso):
        Vehiculo.__init__(self, nombre, dueno, categoria)
        self.chasis = int(chasis)
        self.carroceria = int(carroceria)
        self.ruedas = int(ruedas)
        self.motor = int(motor)
        self.peso = int(peso)

class Automovil(Vehiculo):
    def __init__(self,nombre, dueno, categoria, chasis, carroceria, ruedas, motor, peso):
        Vehiculo.__init__(self, nombre, dueno, categoria)
        self.chasis = int(chasis)
        self.carroceria = int(carroceria)
        self.ruedas = int(ruedas)
        self.motor = int(motor)
        self.peso = int(peso)

class Troncomovil(Vehiculo):
    def __init__(self, nombre, dueno, categoria, chasis, carroceria, ruedas, motor, peso):
        Vehiculo.__init__(self, nombre, dueno, categoria)
        self.chasis = int(chasis)
        self.carroceria = int(carroceria)
        self.ruedas = int(ruedas)
        self.motor = int(motor)
        self.peso = int(peso)

class Motocicleta(Vehiculo):
    def __init__(self,nombre, dueno, categoria, chasis, carroceria, ruedas, motor, peso):
        Vehiculo.__init__(self, nombre, dueno, categoria)
        self.chasis = int(chasis)
        self.carroceria = int(carroceria)
        self.ruedas = int(ruedas)
        self.motor = int(motor)
        self.peso = int(peso)

class Pista():
    def __init__(self, nombre, tipo, hielo, rocas, dificultad, numerov, contrincantes, largo):
        self.nombre = nombre
        self.tipo = tipo
        self.hielo = int(hielo)
        self.rocas = int(rocas)
        self.dificultad = int(dificultad)
        self.numerov = int(numerov)
        self.contrincantes = contrincantes
        self.largo = int(largo)

class Piloto():
    def __init__(self, nombre, dinero, personalidad, contextura, equilibrio, experiencia, equipo):
        self.nombre = nombre
        self.equipo = equipo
        self.equilibrio = int(equilibrio)
        self.experiencia = int(experiencia)
        self.contextura = int(contextura)
        self.personalidad = personalidad
        self.dinero = int(dinero)
        self.vehiculo = None
        self.vehiculo_og = None

class Contrincante():
    def __init__(self, nombre, nivel, personalidad, contextura, equilibrio, experiencia, equipo):
        self.nombre = nombre
        self.nivel = nivel
        self.personalidad = personalidad
        self.contextura = int(contextura)
        self.equilibrio = int(equilibrio)
        self.experiencia = int(experiencia)
        self.equipo = equipo
        self.vehiculo = None
        self.vehiculo_og = None



class Carrera():
    def __init__(self, piloto, contrincantes, pista):
        self.piloto = piloto
        self.pista = pista
        self.contrincantes = contrincantes
        self.vuelta_actual = 0
        self.tiempos = {}

    def comenzar_carrera(self):

        contrincantes_pista = [nombre for nombre in self.pista.contrincantes.split(";")]
        contrincantes_carrera = {}
        self.tiempos[self.piloto] = [0, 0]
        for competidor in self.contrincantes:
            if competidor.nombre in contrincantes_pista:
                contrincantes_carrera[competidor.nombre] = competidor
                self.tiempos[competidor] = [0, 0]
        print("¡COMIENZA LA CARRERA!")

    def nueva_vuelta(self):
         self.vuelta_actual += 1

    def correr(self):
        prep = menus.MenuPits()
        while self.vuelta_actual < self.pista.numerov:
            self.nueva_vuelta()
            shadow_realm = []
            for competidor in self.tiempos.keys():

                time = funciones.calcula_tiempo(self.pista, competidor, self.vuelta_actual)
                l = self.tiempos[competidor]
                competidor.vehiculo.chasis += funciones.dano_recibido_x_vuelta(self.pista,
                                                                               competidor)

                p_accidente = funciones.probabilidad_accidente(self.vuelta_actual, self.pista,
                                                               competidor)
                if p_accidente > random.random():
                    shadow_realm.append(competidor)
                    print(f"*** {competidor.nombre} ha sido eliminado")
                    if competidor == self.piloto:
                        print("***HAS TENIDO UN ACCIDENTE, CARRERA TERMINADA***")
                        break

                if competidor == self.piloto and prep.eleccion == "1":
                    t_pits = funciones.tiempo_pits(competidor)
                    print(f"***Paso por pits demoró {t_pits} segundos***")
                    time += t_pits
                    prep.eleccion = "0"
                l[0] = time
                l[1] += time

            print(f"Vuelta N° {self.vuelta_actual} de {self.pista.numerov}")
            print("Pos | Nombre         | Vuelta Anterior      | Tiempo   ")

            for competidor in shadow_realm:
                del self.tiempos[competidor]

            leaderboard = []
            for competidor, tiempo in self.tiempos.items():                         ##### Tiempos y stop funcion
                leaderboard.append((competidor, tiempo))

            leaderboard = sorted(leaderboard, key=lambda x : x[1][1])
            cuenta = 1
            for competidor in leaderboard:
                print("{}.-  {:<22} {}  {:12}".format(cuenta,competidor[0].nombre, competidor[1][0], competidor[1][1]))
                cuenta += 1

            if self.vuelta_actual == self.pista.numerov:
                print("***Carrera Finalizada***")
                print(f"***Ganador {leaderboard[0][0].nombre}***")
            else:
                prep.mostrar_menu()
                prep.recibir_input()