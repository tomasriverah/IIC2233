import sys
import os
import parametros_generales
import extras
import time
from threading import Thread
from back_end import Personaje, Inventario, Tienda
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QLineEdit, QHBoxLayout, QVBoxLayout, QSpinBox, QFrame, QMainWindow,
                             QGridLayout, QDockWidget, QStackedWidget, QProgressBar)
from PyQt5.QtGui import QFont, QColor, QDrag, QPixmap, QPainter
from random import randint
from PyQt5.QtCore import pyqtSignal, QMimeData, Qt



class VentanaInicial(QWidget):
    partida_signal = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle('DCCAMPO')
        self.setGeometry(300, 300, 700, 400 )

        self.boton = QPushButton('Jugar',self)
        self.boton.setGeometry(50, 50, 50, 50)
        self.boton.clicked.connect(self.check_map)

        self.imagen = QLabel(self)
        self.imagen.setGeometry(50, 50, 656, 188)
        ruta_imagen = os.path.join(parametros_generales.PATH_OTROS, 'logo.png')
        pixeles = QPixmap(ruta_imagen)
        self.imagen.setPixmap(pixeles)
        self.imagen.setScaledContents(True)

        self.texto = QLabel('Introduzca nombre de mapa:', self)

        self.mapa = QLineEdit('', self)
        self.mapa.setGeometry(0, 0 ,100 , 30)

        vbox = QVBoxLayout()
        vbox.addWidget(self.imagen)
        vbox.addWidget(self.texto)
        vbox.addWidget(self.mapa)
        vbox.addWidget(self.boton)
        self.setLayout(vbox)

    def check_map(self):

        path_mapa = os.path.join(parametros_generales.PATH_MAPAS, self.mapa.text())
        if os.path.exists(path_mapa):
            self.partida_signal.emit(path_mapa)
        else:

            self.error = VentanaError()
            self.error.show()


class VentanaError(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle('Error')
        self.setGeometry(800, 450, 400, 200 )

        self.mensaje = QLabel('Mapa no encontrado', self)

        self.ok = QPushButton('Ok', self)
        self.ok.clicked.connect(self.cerrar)

        vbox = QVBoxLayout()
        vbox.addWidget(self.mensaje)
        vbox.addWidget(self.ok)
        self.setLayout(vbox)

    def cerrar(self):

        self.close()

class VentanaPrincipal(QWidget):

    signal_v_principal = pyqtSignal()

    def __init__(self, juego, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.juego = juego
        self.reloj = juego.time
        self.init_gui()
        self.init_signals()
        self.datos = {'mapa' : None}

    def init_gui(self):
        self.setWindowTitle('DCCAMPO')

        self.v_juego = VentanaJuego()
        self.inventario = VentanaInventario()
        self.personaje_back = self.v_juego.personaje_back
        self.juego.personaje = self.personaje_back
        self.tienda_back = Tienda()
        self.tienda_back.personaje = self.personaje_back
        self.tienda_back.inventario = self.inventario.inventario.inventario
        self.status_bar = StatusBar(self.reloj, self.personaje_back)
        self.tienda = VentanaTienda()
        self.tienda.tienda_back = self.tienda_back



        vbox = QVBoxLayout()
        vbox.addWidget(self.status_bar)
        vbox.addWidget(self.inventario)
        vbox.addWidget(self.v_juego)


        self.setLayout(vbox)

    def init_signals(self):
        self.update_character_signal = self.personaje_back.actualiza_personaje_signal

        self.personaje_back.actualiza_window_signal.connect(self.v_juego.update_window)

        self.personaje_back.signal_casa_tienda.connect(self.pos_jugador)

        self.juego.signal_spawn.connect(self.v_juego.spawn)

        self.tienda.signal_compra.connect(self.tienda_back.compra)

        self.tienda.signal_venta.connect(self.tienda_back.venta)


        self.tienda_back.actualizar_inventario.connect(self.inventario.inventario.enviar_inventario)

    def cargar(self, data):
        self.show()

    def pos_jugador(self, data):
        if data == 'tienda':
            self.tienda.show()

        elif data == 'casa':
            self.reloj.horas = 0
            self.reloj.minutos = 0
            self.reloj.dia +=1
            self.reloj.its_a_new_day.emit()

    key_event_dict = {
        Qt.Key_D: 'R',
        Qt.Key_A: 'L',
        Qt.Key_W: 'U',
        Qt.Key_S: 'D'
    }

    def keyPressEvent(self, event):

        if event.key() in self.key_event_dict:
            action = self.key_event_dict[event.key()]
            self.update_character_signal.emit(action)

class StatusBar(QWidget):
    def __init__(self, reloj, personaje, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reloj = reloj
        self.personaje = personaje
        self.init_gui()


    def init_gui(self):
        self.setGeometry(0, 0, 200, 200)
        
        hbox = QHBoxLayout()
        hbox1 = QHBoxLayout()

        self.dia =  QLabel(f'Dia n°: {self.reloj.dia}')
        hbox.addWidget(self.dia)

        self.watch = QLabel(f'{self.reloj.hora}:{self.reloj.minutos}')
        hbox.addWidget(self.watch)

        self.monedas = QLabel(f'{self.personaje.monedas}')
        img = QLabel()
        img.setFixedSize(50, 50)
        pixeles = QPixmap(parametros_generales.PATH_IMG_MOEDAS)
        img.setPixmap(pixeles)
        img.setScaledContents(True)
        hbox1.addWidget(img)
        hbox1.addWidget(self.monedas)

        vbox = QVBoxLayout()
        self.energia = QLabel('Energía')
        vbox.addWidget(self.energia)

        self.progress = QProgressBar(self)
        self.progress.setFixedSize(200, 30)
        self.progress.setMaximum(parametros_generales.ENERGIA_JUGADOR)
        self.progress.setValue(parametros_generales.ENERGIA_JUGADOR)
        vbox.addWidget(self.progress)
        hbox.addLayout(vbox)
        hbox.addLayout(hbox1)
        self.setLayout(hbox)

        self.reloj.update_clock.connect(self.update_watch)


    def update_watch(self):

        self.watch.setText(f'Reloj: {self.reloj.hora}:{self.reloj.minutos}')
        self.monedas.setText(f'{self.personaje.monedas}')
        self.progress.setValue(self.personaje.energia)
        self.dia.setText(f'Dia n°: {self.reloj.dia}')


class VentanaJuego(QWidget):

    sprites_paths = {
        ('stand', 'D'): os.path.join('sprites', 'personaje', 'down_1.png'),
        ('walk', 'D', 1): os.path.join('sprites', 'personaje', 'down_2.png'),
        ('walk', 'D', 2): os.path.join('sprites', 'personaje', 'down_3.png'),
        ('walk', 'D', 3): os.path.join('sprites', 'personaje', 'down_4.png'),
        ('stand', 'L'): os.path.join('sprites', 'personaje', 'left_1.png'),
        ('walk', 'L', 1): os.path.join('sprites', 'personaje', 'left_2.png'),
        ('walk', 'L', 2): os.path.join('sprites', 'personaje', 'left_3.png'),
        ('walk', 'L', 3): os.path.join('sprites', 'personaje', 'left_4.png'),
        ('stand', 'R'): os.path.join('sprites', 'personaje', 'right_1.png'),
        ('walk', 'R', 1): os.path.join('sprites', 'personaje', 'right_2.png'),
        ('walk', 'R', 2): os.path.join('sprites', 'personaje', 'right_3.png'),
        ('walk', 'R', 3): os.path.join('sprites', 'personaje', 'right_4.png'),
        ('stand', 'U'): os.path.join('sprites', 'personaje', 'up_1.png'),
        ('walk', 'U', 1): os.path.join('sprites', 'personaje', 'up_2.png'),
        ('walk', 'U', 2): os.path.join('sprites', 'personaje', 'up_3.png'),
        ('walk', 'U', 3): os.path.join('sprites', 'personaje', 'up_4.png')
    }


    signal_v_juego = pyqtSignal(list)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frame = 1
        self.personaje_back = Personaje(10, 10)
        self.n_walk_coord = []


    def init_gui(self):

        is_casa = False
        is_tienda = False

        self.personaje_back.mapa = self.mapa
        self.personaje_back.init_celdas()

        grid = QGridLayout(self)
        grid.setSpacing(0)
        grid.setContentsMargins(0, 0, 0, 0)

        grid1 = QGridLayout(self)
        grid1.setSpacing(0)

        house = QVBoxLayout(self)

        store = QVBoxLayout(self)




        for coordenadas in self.mapa.keys():

            x = coordenadas[0]
            y = coordenadas[1]
            celda = self.mapa[coordenadas]
            self.cell = DropLabel(self)
            self.cell.setFixedSize(30, 30)
            if celda.tipo == 'C':

                pixeles = QPixmap(parametros_generales.DICCIONARIO_IMAGENES['C'])

            else:
                self.cell = QLabel(self)
                self.cell.setFixedSize(30, 30)
                pixeles = QPixmap(parametros_generales.DICCIONARIO_IMAGENES['O'])


            self.cell.setPixmap(pixeles)
            self.cell.setScaledContents(True)

            grid.addWidget(self.cell, y, x)

        for coordenadas in self.mapa.keys():

            x = coordenadas[0]
            y = coordenadas[1]
            celda = self.mapa[coordenadas]
            self.cell = QLabel(self)
            self.cell.setFixedSize(30, 30)
            if celda.tipo == 'C':
                self.cell = DropLabel(self)
                self.cell.send_crops.connect(self.planta_cultivo)
                self.cell.coordenadas = (x, y)
                self.cell.setFixedSize(30, 30)
            if celda.tipo == 'R':
                self.n_walk_coord.append((x, y))
                pixeles = QPixmap(parametros_generales.DICCIONARIO_IMAGENES['R'])
                self.cell.setPixmap(pixeles)
                self.cell.setScaledContents(True)
            grid1.addWidget(self.cell, y, x)

        for coordenadas in self.mapa.keys():
            x = coordenadas[0]
            y = coordenadas[1]
            celda = self.mapa[coordenadas]


            if celda.tipo == 'H' and not is_casa :
                self.n_walk_coord.append((x, y))
                self.cell = QLabel(self)
                self.cell.setFixedSize(60,60)
                is_casa = True
                x_casa = coordenadas[0]
                y_casa = coordenadas[1]
                pixeles = QPixmap(parametros_generales.DICCIONARIO_IMAGENES['H'])
                self.cell.setPixmap(pixeles)
                self.cell.setScaledContents(True)
                house.addWidget(self.cell)

            if celda.tipo == 'T' and not is_tienda :

                self.cell = QLabel(self)
                self.cell.setFixedSize(60,60)
                is_tienda = True
                x_tienda = coordenadas[0]
                y_tienda = coordenadas[1]
                pixeles = QPixmap(parametros_generales.DICCIONARIO_IMAGENES['T'])
                self.cell.setPixmap(pixeles)
                self.cell.setScaledContents(True)
                store.addWidget(self.cell)


        grid.addLayout(grid1,0 ,0 ,0 ,0)
        grid.addLayout(store,y_tienda, x_tienda, 0, 0)
        grid.addLayout(house, y_casa, x_casa, 0, 0)


        self.grid = grid
        self.setLayout(grid)

        self.front_character = QLabel(self)
        self.front_character.setFixedSize(20, 30)
        current_sprite = QPixmap(self.sprites_paths[('walk', 'D', 1)])
        self.front_character.setPixmap(current_sprite)
        self.front_character.setScaledContents(True)



    def planta_cultivo(self, data):
        coordenadas = data[0]

        x = coordenadas[0]
        y = coordenadas[1]

        cell = extras.genera_cultivo_widget(data[1])
        hbox = QHBoxLayout()
        hbox.addWidget(cell)
        self.grid.addLayout(hbox, y, x, 0, 0)
        self.signal_v_juego.emit(data)

    def crece_cultivo(self, cultivo):
        x,y = cultivo.coordenadas
        self.cell = QStackedWidget(self)
        cultivo.signal_celda.connect(self.cell.setCurrentWidget())
        self.cell.setFixedSize(30, 30)
        for i in range(0, 7):
            label = QLabel()
            pixeles = QPixmap(parametros_generales.DICCIONARIO_SEMILLAS[cultivo.tipo, cultivo.etapa])
            label.setPixmap(pixeles)
            label.setScaledContents(True)
            self.cell.addWidget(label)

        self.grid.addWidget(self.cell, y, x, 0, 0)

    def spawn(self, dicc):
        if dicc['oro']:
            x,y = dicc['oro'].coordenadas
            self.celda = QLabel(self)
            self.celda.setFixedSize(30, 30)
            sprite = QPixmap(parametros_generales.PATH_IMG_ORO)
            self.celda.setPixmap(sprite)
            self.celda.setScaledContents(True)
            self.grid.addWidget(self.celda, y, x, 0, 0)

        if dicc['arbol']:
            x, y = dicc['arbol'].coordenadas
            self.celda = extras.QLabelBacan(self)
            self.celda.axe = self.personaje_back.axe
            self.celda.setFixedSize(30, 30)
            sprite = QPixmap(parametros_generales.PATH_IMG_ARBOL)
            self.celda.setPixmap(sprite)
            self.celda.setScaledContents(True)
            self.celda.mouseDoubleClickEvent = self.celda.escondete
            self.grid.addWidget(self.celda, y, x, 0, 0)




    @property
    def frame(self):
        return self._frame

    @frame.setter
    def frame(self, value):
        """
        Actualiza el estado de animación de la imagen del personaje.
        Solo tiene 3 estados.
        :param value: int
        :return: None
        """
        self._frame = value if value < 4 else 1




    def recibir(self, data):

        self.mapa = data['mapa']
        self.personaje_back.lista_no_caminable = data['lista_no']
        self.init_gui()

    def update_window(self, event):
        """
        Función que recibe un diccionario con la información del
        personaje y las actualiza en el front-end.
        :param event: dict
        :return: None
        """
        direction = event['direction']
        position = event['position']
        if position == 'walk':
            self.frame += 1
            self.current_sprite = QPixmap(self.sprites_paths[(position, direction, self.frame)])
        else:
            self.current_sprite = QPixmap(self.sprites_paths[(position, direction)])
        self.front_character.setPixmap(self.current_sprite)
        self.front_character.move(event['x'], event['y'])


class VentanaInventario(QWidget):


    dicc = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()
        self.inventario = Inventario()
        self.inventario.inventario_signal.connect(self.update_inventario)
        self.inventario.enviar_inventario()



    def init_gui(self):
        self.setGeometry(0,0, 200,200)

        self.titulo = QLabel('Inventario')
        vbox = QVBoxLayout()
        vbox.addWidget(self.titulo)
        hbox = QHBoxLayout()
        for i in range(0,8):
            if i in [0, 1]:
                self.imagen = DraggableLabel(self)
                if i == 0:
                    self.imagen.tipo = 'choclo'
                else:
                    self.imagen.tipo = 'alcachofa'
            else:
                self.imagen = QLabel(self)
            self.imagen.setFixedSize(30, 30)
            ruta_imagen = parametros_generales.DICCIONARIO_INVENTARIO[i]
            pixeles = QPixmap(ruta_imagen)
            self.imagen.setPixmap(pixeles)
            self.imagen.setScaledContents(True)
            hbox.addWidget(self.imagen)
            self.dicc[i] = self.imagen
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def update_inventario(self, data):

        for i in range(0, 8):
            if data[i][1] > 0:
                self.dicc[i].show()
            else:
                self.dicc[i].hide()



class VentanaTienda(QWidget):

    signal_venta = pyqtSignal(str)
    signal_compra = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dicc_items = parametros_generales.DICCIONARIO_TIENDA
        self.items_tienda = self.dicc_items.keys()
        self.init_gui()


    def init_gui(self):
        self.setWindowTitle('Tienda')
        self.setFixedSize(300, 700)

        vbox = QVBoxLayout(self)

        for item in self.items_tienda:

            layout_h = QHBoxLayout(self)
            layout_botones = QVBoxLayout(self)
            boton_c = QPushButton('Comprar')
            boton_v = QPushButton('Vender')
            boton_c.setObjectName(item)
            boton_v.setObjectName(item)
            layout_botones.addWidget(boton_c)
            layout_botones.addWidget(boton_v)



            boton_v.clicked.connect(self.venta)
            boton_c.clicked.connect(self.compra)

            precio = QLabel(f'${self.dicc_items[item][1]}')

            imagen = QLabel(self)
            imagen.setFixedSize(50, 50)
            current_sprite = QPixmap(self.dicc_items[item][0])
            imagen.setPixmap(current_sprite)
            imagen.setScaledContents(True)

            layout_h.addWidget(imagen)
            layout_h.addWidget(precio)
            layout_h.addLayout(layout_botones)

            vbox.addLayout(layout_h)
        self.setLayout(vbox)




    def venta(self):
        sender = self.sender()
        self.signal_venta.emit(sender.objectName())

    def compra(self, item):
        sender = self.sender()
        self.signal_compra.emit(sender.objectName())

'''
class DraggableLabel y Drop Label  sacada de internet, link:
https://stackoverflow.com/questions/50232639/drag-and-drop-qlabels-with-pyqt5

'''

class DraggableLabel(QLabel):
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < \
                QApplication.startDragDistance():
            return
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.text())
        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.CopyAction | Qt.MoveAction)

class DropLabel(QLabel):

    send_crops = pyqtSignal(list)

    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.setAcceptDrops(True)
        self.coordenadas = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        pos = event.pos()
        semilla = event.source().tipo
        text = event.mimeData().text()
        self.setText(text)
        event.acceptProposedAction()

        self.send_crops.emit([self.coordenadas, semilla])



if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaInicial()

    ventana.show()
    sys.exit(app.exec_())