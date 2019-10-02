import os
from PyQt5.QtCore import QObject, pyqtSignal
import parametros_generales

class Juego(QObject):

    recibir_signal = pyqtSignal(str)
    enviar_signal = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.mapa = {}
        self.lista_mapa = None

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

        y = 0
        for fila in self.lista_mapa:
            x = 0
            for celda in fila:
                cell = Celda(celda,(x,y))
                x += 1
                self.mapa[cell.coordenadas] = cell
            y += 1

        self.actualizar_data()

    def actualizar_data(self):

        data = {'mapa' : self.mapa}

        self.enviar_signal.emit(data)

    def recibir_update(self, data):
        coordenadas = data.keys()[0]
        self.mapa[coordenadas] = Crop()
        self.mapa[coordenadas].tipo = 'cultivo'
        self.img = parametros_generales.DICCIONARIO_CULTIVOS['semilla_' + data[coordenadas]]

class Celda(QObject):
    def __init__(self, tipo, coordenadas,*args, **kwargs):
        super().__init__()
        self.tipo = tipo
        self.coordenadas = coordenadas
        self.img = None


class Crop(Celda):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.etapa = 0


class Inventario(QObject):

    inventario_signal = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.inventario = {'semilla_choclo' : Item('semilla_choclo')}
        self.enviar_inventario()

    def enviar_inventario(self):

        inventario_signal.emit(self.inventario)


class Item():
    def __init__(self, nombre):
        self.nombre = nombre





