from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect)
from PyQt5.QtGui import (QPixmap, QFont, QMovie)



"""
Debes completar la clase VentanaJuego con los elementos que
estimes necesarios.

Eres libre de agregar otras clases si lo crees conveniente.
"""

class VentanaJuego(QWidget):
    """
    Señales para enviar información (letras o palabras)
    y crear una partida, respectivamente.

    Recuerda que eviar_letra_signal debe llevar un diccionario de la forma:
        {
            'letra': <string>,
            'palabra': <string>  -> Este solo en caso de que 
                                    implementes el bonus
        }
    Es importante que SOLO UNO DE LOS ELEMENTOS lleve contenido, es decir,
    o se envía una letra o se envía una palabra, el otro DEBE 
    ir como string vacío ("").
    """
    enviar_letra_signal = pyqtSignal(dict)
    reiniciar_signal = pyqtSignal()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()
        self.datos = {}

    def recieve(self, diccionario):

        self.usadas.setText(f"Disponibles: {diccionario['usadas']}")
        self.disponibles.setText(f"Disponibles: {diccionario['disponibles']}")
        pixeles = QPixmap(diccionario["imagen"])
        self.imagen.setPixmap(pixeles)
        self.adivina.setText(diccionario['palabra'])

    def init_gui(self):



        self.setGeometry(200, 100, 400, 600)
        self.setWindowTitle('DCCRaid51')

        self.imagen = QLabel(self)

        pixeles = QPixmap("images/1.png")

        self.imagen.setPixmap(pixeles)

        self.imagen.setScaledContents(True)

        self.imagen.move(200,200)


        self.usadas = QLabel(f"Usadas:  ", self)
        self.usadas.move(100,100)

        self.adivina = QLabel("_ _ _ _ _ _ _ _ _", self)

        self.disponibles = QLabel(f"Disponibles: ", self)

        self.letra_actual = QLineEdit("", self)

        self.seleccion = QPushButton("Confirmar Letra", self)

        self.n_juego = QPushButton("Nuevo Juego", self)

        layout_arriba = QVBoxLayout()
        layout_arriba.addWidget(self.adivina)
        layout_arriba.addWidget(self.imagen)
        layout_arriba.addWidget(self.usadas)
        layout_arriba.addWidget(self.disponibles)
        layout_arriba.addWidget(self.letra_actual)
        layout_arriba.addWidget(self.seleccion)
        layout_arriba.addWidget(self.n_juego)

        self.setLayout(layout_arriba)

        self.seleccion.clicked.connect(self.confirma)
        


    def confirma(self):

        letra = self.letra_actual.text()
        self.enviar_letra_signal.emit({'letra' : letra})




