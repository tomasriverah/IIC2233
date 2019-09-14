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
        self.vehiculos[self.piloto.vehiculo.nombre] = (self.piloto.vehiculo)

    def cargar_partida(self):
        self.piloto = funciones.carga_piloto(parametros.PATHS["PILOTOS"])


    def comprar_vehiculo(self):
        funciones.comprar_vehiculo(self.piloto, self.vehiculos)


    def elegir_vehiculo(self):
        vehiculos_p = []
        for vehiculo in self.vehiculos.keys():
            if self.vehiculos[vehiculo].dueno == self.piloto.nombre:
                vehiculos_p.append(self.vehiculos[vehiculo])
        eleccion = funciones.seleccion([vehiculo.nombre for vehiculo in vehiculos_p])
        for viculo in vehiculos_p:
            if viculo.nombre == eleccion:
                self.piloto.vehiculo = viculo
                self.piloto.vehiculo_og = copy.deepcopy(viculo)

    def asignar_vehiculo(self):
        for viculo in self.vehiculos.keys():
            for contrincante in self.contrincantes:
                if self.vehiculos[viculo].dueno == contrincante.nombre:
                    contrincante.vehiculo = self.vehiculos[viculo]
                    contrincante.vehiculo_og = copy.deepcopy(contrincante.vehiculo)

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
        vehiculo_new = race.retorna_vehiculo()
        self.vehiculos[vehiculo_new.nombre] = vehiculo_new


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
        self.cero()

    def cero(self):
        if self.tipo == "pista rocosa":
            self.hielo = 0
        elif self.tipo == "pista hielo":
            self.rocas = 0


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
        prep = menus.MenuCarrera()

        leaderboard = []
        while self.vuelta_actual < self.pista.numerov:
            out = False
            rompe_loop = 0
            self.nueva_vuelta()
            shadow_realm = []
            leaderboard = []
            for competidor in self.tiempos.keys():

                time = funciones.calcula_tiempo(self.pista, competidor, self.vuelta_actual)
                l = self.tiempos[competidor]
                competidor.vehiculo.chasis -= funciones.dano_recibido_x_vuelta(self.pista,
                                                                               competidor)

                p_accidente = funciones.probabilidad_accidente(self.vuelta_actual, self.pista,
                                                               competidor)

                if p_accidente > random.random() or competidor.vehiculo.chasis <= 0:
                    shadow_realm.append(competidor)
                    print(f"*** {competidor.nombre} ha sido eliminado")
                    if competidor == self.piloto:
                        print("***HAS TENIDO UN ACCIDENTE, CARRERA TERMINADA***")
                        rompe_loop = 1
                        out = True


                if competidor == self.piloto and prep.eleccion == "1" and not out:
                    t_pits = funciones.tiempo_pits(self.piloto)
                    pits = menus.MenuPits(self.piloto)
                    pits.mostrar_menu()
                    pits.recibir_input()
                    competidor.vehiculo = copy.deepcopy(competidor.vehiculo_og)
                    if pits.eleccion != "0":
                        self.piloto.dinero = pits.aplica_mejoras()
                        competidor.vehiculo_og = copy.deepcopy(competidor.vehiculo)
                    print(f"***Paso por pits demoró {t_pits} segundos***")
                    time += t_pits
                    prep.eleccion = "0"
                l[0] = time
                l[1] += time

            if rompe_loop == 1:
                break
            print(f"Vuelta N° {self.vuelta_actual} de {self.pista.numerov}")
            print("Pos | Nombre         | Vuelta Anterior      | Tiempo   ")

            for competidor in shadow_realm:
                del self.tiempos[competidor]


            for competidor, tiempo in self.tiempos.items():
                leaderboard.append((competidor, tiempo))

            leaderboard = sorted(leaderboard, key=lambda x : x[1][1])
            cuenta = 1
            for competidor in leaderboard:
                print("{}.-  {:<22} {}  {:12}".format(cuenta,competidor[0].nombre,
                                                      competidor[1][0], competidor[1][1]))
                cuenta += 1

            self.piloto.dinero += funciones.dinero_x_vuelta(self.pista, self.vuelta_actual)

            if self.vuelta_actual == self.pista.numerov:
                print("***Carrera Finalizada***")
                print(f"***Ganador {leaderboard[0][0].nombre}***")
            else:
                prep.mostrar_menu()
                prep.recibir_input()

        if leaderboard != []:
            if leaderboard[0][0] == self.piloto:
                ventaja = funciones.ventaja(leaderboard[0][1][1], leaderboard[len(leaderboard) - 1][1][1])
                dinero = funciones.dinero_ganador(self.pista)
                xp = funciones.experiencia_recibida(self.piloto, ventaja, self.pista)
                print(f"Has ganado ${dinero} y exp {xp}")
                self.piloto.dinero += dinero
                self.piloto.experiencia += xp

        for competidor in self.contrincantes:
            competidor.vehiculo = copy.deepcopy(competidor.vehiculo_og)

        self.piloto.vehiculo = copy.deepcopy(self.piloto.vehiculo_og)

    def retorna_vehiculo(self):
        return self.piloto.vehiculo