import time
import parametros_generales
from threading import Thread
from PyQt5.QtCore import pyqtSignal, QObject

from PyQt5.QtWidgets import QStackedWidget, QLabel
from PyQt5.QtGui import QPixmap


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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.axe = None

    def escondete(self, b):
        print(self.axe)
        if self.axe == True:
            pixeles = QPixmap(parametros_generales.DICCIONARIO_INVENTARIO[6])
            self.setPixmap(pixeles)

