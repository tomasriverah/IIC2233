import time
import parametros_generales
from threading import Thread
from PyQt5.QtCore import pyqtSignal, QObject

import math
from PyQt5.QtWidgets import QStackedWidget, QLabel, QApplication
from PyQt5.QtGui import QPixmap, QDrag, QPainter
from PyQt5.QtCore import pyqtSignal, QMimeData, Qt

class Reloj(QObject):


    update_clock = pyqtSignal()
    its_a_new_day = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hora = 0
        self.minutos = 0
        self.dia = 0
        self.corre = Thread(target=self.corre_reloj, daemon=True)



    def corre_reloj(self):
        while True:
            time.sleep(0.5)
            self.minutos +=1
            if self.minutos == 60:
                self.minutos = 0
                self.hora += 1
                if self.hora == 24:
                    self.hora = 0
                    self.dia += 1
                    self.its_a_new_day.emit()
            self.update_clock.emit()




def genera_cultivo_widget(tipo):

    widget = QStackedWidget()
    widget.setFixedSize(30, 30)

    if tipo == 'choclo':
        for n in range(0, 7):
            label = QLabel()
            label.setFixedSize(30, 30)
            pixeles = QPixmap(parametros_generales.DICCIONARIO_SEMILLAS[('choclo', n)])
            label.setPixmap(pixeles)
            label.setScaledContents(True)
            widget.addWidget(label)

    else:
        for n in range(0, 6):
            label = QLabel()
            label.setFixedSize(30, 30)
            pixeles = QPixmap(parametros_generales.DICCIONARIO_SEMILLAS[('alcachofa', n)])
            label.setPixmap(pixeles)
            label.setScaledContents(True)
            widget.addWidget(label)

    return widget


class QLabelBacan(QLabel):

    add_inventario_signal = pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tipo = None
        self.axe = None
        self.x = None
        self.y = None
        self.recolectable = True
    def escondete(self, b):

        if self.axe == True:
            pixeles = QPixmap(parametros_generales.DICCIONARIO_INVENTARIO[6])
            self.setPixmap(pixeles)
            self.recolectable = True

    def areate(self, b):
        pixeles =  QPixmap(parametros_generales.DICCIONARIO_IMAGENES['C'])
        self.setPixmap(pixeles)

    def recoleccion(self, pos_personaje):
        if self.x*30 == roundup(pos_personaje[0]) and self.y*30 == roundup(pos_personaje[1])\
                and self.recolectable == True:
            self.hide()
            self.add_inventario_signal.emit(self.tipo)

    def artichoke(self):
        pixeles = QPixmap(parametros_generales.DICCIONARIO_TIENDA['alcachofa'][0])
        self.setPixmap(pixeles)
        self.setFixedSize(30, 30)
        self.setScaledContents(True)


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

class DropLabelBacan(DropLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(False)

    def areate(self, b):

        self.setAcceptDrops(True)
        pixeles = QPixmap(parametros_generales.DICCIONARIO_IMAGENES['C'])
        self.setPixmap(pixeles)

'https://stackoverflow.com/questions/34001496/how-do-i-round-up-a-number-to-the-nearest-10-in-python-3-4-0'

def roundup(x, n=10):
    res = math.ceil(x/n)*n
    if (x%n < n/2)and (x%n>0):
        res-=n
    return res