from back_end import Juego
from front_end import VentanaInicial, VentanaPrincipal
import sys
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

ventana = VentanaInicial()
ventana.show()

game = Juego()

ventana_principal = VentanaPrincipal(game)




ventana.partida_signal.connect(game.recibir_mapa)
ventana.partida_signal.connect(ventana_principal.cargar)

ventana_principal.v_juego.signal_v_juego.connect(game.recibir_update)


game.enviar_signal.connect(ventana_principal.v_juego.recibir)
game.enviar_signal_crop.connect(ventana_principal.v_juego.crece_cultivo)



sys.exit(app.exec())