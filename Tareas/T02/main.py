from back_end import Juego
from front_end import VentanaInicial, VentanaPrincipal
import sys
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

ventana = VentanaInicial()
ventana.show()

ventana_principal = VentanaPrincipal()


game = Juego()


ventana.partida_signal.connect(game.recibir_mapa)
ventana.partida_signal.connect(ventana_principal.cargar)
game.enviar_signal.connect(ventana_principal.mapa.recibir)



sys.exit(app.exec())