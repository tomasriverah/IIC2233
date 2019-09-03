import funciones


class Juego():
    def __init__(self):
        self.partida = 0




    def nueva_partida(self):
        nuevo_piloto = funciones.creacion_piloto([],[])



class Vehiculo():
    def __init__(self):
        pass

class Pista():
    def __init__(self):
        pass

class Piloto():
    def __init__(self, nombre, equipo, equilibrio, experiencia, contextura, personalidad):
        self.nombre = nombre
        self.equipo = equipo
        self.equilibrio = equilibrio
        self.experiencia = experiencia
        self.contextura = contextura
        self.personalidad = personalidad

class Contrincante():
    def __init__(self):
        pass