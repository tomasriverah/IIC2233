import os
from random import random, choice
from extras import Reloj
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from parametros_generales import (VEL_MOVIMIENTO, ENERGIA_JUGADOR, MONEDAS_INICIALES, PROB_ARBOL,
                                  PROB_ORO, DICCIONARIO_TIENDA)
import parametros_plantas

class Juego(QObject):

    recibir_signal = pyqtSignal(str)
    enviar_signal = pyqtSignal(dict)
    enviar_signal_crop = pyqtSignal(object)
    signal_personaje = pyqtSignal(list)
    signal_reloj = pyqtSignal(object)
    signal_spawn = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.personaje = None
        self.mapa = {}
        self.lista_mapa = None
        self.lista_no_caminable = []
        self.time = Reloj()
        self.time.corre.start()
        self.time.its_a_new_day.connect(self.new_day)
        self.tamano_x = 0
        self.tamano_y = 0
    def recibir_mapa(self, path):

        self.cargar_mapa(path)

    def cargar_mapa(self, path):
        mapa = []
        archivo =  open(path, 'r', encoding='UTF-8')

        for linea in archivo:
            linea = linea.strip('\n')
            celdas = linea.split(' ')
            mapa.append(celdas)

        self.lista_mapa = mapa
        self.tamano_y = len(self.lista_mapa)

        y = 0
        for fila in self.lista_mapa:
            self.tamano_x = len(fila)
            x = 0
            for celda in fila:
                cell = Celda(celda,(x,y))
                x += 1
                self.mapa[cell.coordenadas] = cell
                if cell.tipo in ['R', 'T', 'S']:
                    self.lista_no_caminable.append(cell.coordenadas)
            y += 1
        self.personaje.max_y = 29 * self.tamano_y
        self.personaje.max_x = 29 * self.tamano_x
        self.actualizar_data()

    def actualizar_data(self):

        data = {'mapa' : self.mapa,
                'lista_no' : self.lista_no_caminable,
                'reloj' : self.time
                }

        self.enviar_signal.emit(data)

    def recibir_update(self, data):
        coordenadas = data[0]

        self.mapa[coordenadas] = Crop(data[1], coordenadas)
        self.mapa[coordenadas].signal_celda.connect(self.mandar_crop_update)


    def new_day(self):
        celdas_disponibles = []
        for celda in self.mapa.keys():
            if self.mapa[celda].available == True:
                celdas_disponibles.append(self.mapa[celda])

        if random() < PROB_ORO:
            cell_oro = choice(celdas_disponibles)
        else:
            cell_oro = False
        if random() < PROB_ARBOL:
            cell_arbol = choice(celdas_disponibles)
        else:
            cell_arbol = False

        self.signal_spawn.emit({'oro' : cell_oro,
                                'arbol' : cell_arbol,
        })


    def mandar_crop_update(self, crop):

        self.enviar_signal_crop.emit(crop)

class Celda(QObject):

    signal_celda = pyqtSignal(object)

    def __init__(self, tipo, coordenadas,*args, **kwargs):
        super().__init__()
        self.tipo = tipo
        self.coordenadas = coordenadas
        self.available = None
        self.init()

    def init(self):
        if self.tipo == 'O':
            self.available = True


class Crop(Celda):
    def __init__(self, tipo, coordenadas,*args, **kwargs):
        self.widget = None
        super().__init__(tipo, coordenadas)
        self.etapa = 0
        self.tiempo_e_actual = 0
        self.set_timer()
        self.available = False


    def set_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_crop)
        if self.tipo == 'choclo':
            self.timer.start(parametros_plantas.TIEMPO_CHOCLOS*500)
        elif self.tipo == 'alcachofa':
            self.timer.start(parametros_plantas.TIEMPO_ALCACHOFAS*500)


    def update_crop(self):

        if self.tipo == 'choclo' and self.etapa < 6:
            self.etapa += 1

        elif self.tipo == 'alcachofa' and self.etapa < 6:
            self.etapa += 1

        self.widget.setWidget(self.etapa)
        self.signal_celda.emit(self)

class Inventario(QObject):

    inventario_signal = pyqtSignal(dict)

    dicc_inventario = {0 : ['semilla_choclo', 0],
                       1 : ['semilla_alcachofa', 0],
                       2 : ['azada', 0],
                       4 : ['choclo', 0],
                       5 : ['alcachofa', 0],
                       3 : ['hacha', 0],
                       6 : ['leña', 0],
                       7 : ['oro', 0],
                       }


    def __init__(self, *args, **kwargs):
        super().__init__()
        self.inventario = self.dicc_inventario
        self.enviar_inventario()

    def enviar_inventario(self):

        self.inventario_signal.emit(self.inventario)



class Personaje(QObject):

    actualiza_personaje_signal = pyqtSignal(str)
    actualiza_window_signal = pyqtSignal(dict)
    signal_casa_tienda = pyqtSignal(str)

    def __init__(self, x, y):
        super().__init__()

        self.mapa = {}
        self.direction = 'R'
        self.energia = ENERGIA_JUGADOR
        self.monedas = MONEDAS_INICIALES
        self.x = 100
        self.y = 100
        self.max_x = 0
        self.max_y = 0
        self.casa = []
        self.tienda = []
        self.actualiza_personaje_signal.connect(self.move)
        self.lista_no_caminable = None
        self.axe = False


    def init_celdas(self):
        self.casa = []
        self.tienda = []
        for cell in self.mapa.keys():

            if self.mapa[cell].tipo == 'T':
                x, y = self.mapa[cell].coordenadas
                self.tienda.append((x, y))

            if self.mapa[cell].tipo == 'H':
                x, y = self.mapa[cell].coordenadas
                self.casa.append((x, y))

    def move(self, event):
        if event == 'R':
            self.direction = 'R'
            self.x += VEL_MOVIMIENTO
        elif event == 'L':
            self.direction = 'L'
            self.x -= VEL_MOVIMIENTO
        elif event == 'U':
            self.direction = 'U'
            self.y -= VEL_MOVIMIENTO
        elif event == 'D':
            self.direction = 'D'
            self.y += VEL_MOVIMIENTO

        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0

        if self.x > self.max_x:
            self.x = self.max_x

        if self.y > self.max_y:
            self.y = self.max_y
        self.actualiza_juego()
        opcion = self.check_casilla()

        if opcion != None:
            
            self.signal_casa_tienda.emit(opcion)


    def actualiza_juego(self):
        """
        Envía los datos del personaje mediante una señal a la
        interfaz para ser actualizados.
        :param position: str
        :return: None
        """
        if self.actualiza_window_signal:
            self.actualiza_window_signal.emit({
                'x': self.x,
                'y': self.y,
                'direction': self.direction,
                'position' : 'walk'
            })

    def update_monedas(self, money):

        self.monedas += money


    def check_casilla(self):

        for coordenadas in self.casa:

            if self.x in range(30*coordenadas[0], 31*coordenadas[0]) \
                    and self.y in range(30*coordenadas[1], 31*coordenadas[1]):
                return 'casa'
        for coordenadas in self.tienda:
            if self.x in range(30*coordenadas[0], 31*coordenadas[0] + 5) \
                    and self.y in range(30*coordenadas[1], 31*coordenadas[1] + 5):
                return 'tienda'







class Tienda(QObject):

    actualizar_inventario = pyqtSignal()

    dicc_item_numero = {'semilla_choclo' : 0,
                        'semilla_alcachofa' : 1,
                        'azada' : 2,
                        'choclo' : 4,
                        'alcachofa' : 5,
                        'hacha' : 3,
                        'leña' : 6,
                        'oro' : 7,
}

    def __init__(self):
        self.inventario =None
        self.personaje = None
        super().__init__()

    def compra(self, item):
        nro = self.dicc_item_numero[item]
        if self.personaje.monedas >= DICCIONARIO_TIENDA[item][1]:
            self.inventario[nro][1] += 1
            self.personaje.monedas -= DICCIONARIO_TIENDA[item][1]

        self.actualizar_inventario.emit()
        if self.inventario[3][1] > 0:
            self.personaje.axe = True

    def venta(self, item):
        nro = self.dicc_item_numero[item]

        if self.inventario[nro][1] > 0:

            self.personaje.monedas += DICCIONARIO_TIENDA[item][1]
            self.inventario[nro][1] -= 1

        self.actualizar_inventario.emit()
        if self.inventario[3][1] == 0:
            self.personaje.axe = False


