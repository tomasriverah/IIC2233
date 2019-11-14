import pickle
import re


class Piloto:
    def __init__(self, nombre, alma, edad, *args, **kwargs):
        self.nombre = nombre
        self.alma = alma
        self.edad = edad

    def __setstate__(self, state):
        # Usar aumentar_sincronizacion
        aumentar_sincronizacion(state)

def cargar_almas(ruta):
    with open(ruta, 'rb') as file:
        lista_cargada = pickle.load(file)
        return lista_cargada

def aumentar_sincronizacion(estado):
    string = estado['alma']



if __name__ == '__main__':
    try:
        pilotos = cargar_almas('pilotos.magi')
        if pilotos:
            print("ENZOHOR200: Sincronizacion de los pilotos ESTABLE.")
            
    except Exception as error:
        print(f'Error: {error}')
        print("ENZOHOR501: CRITICO Sincronizacion de los pilotos INESTABLE")
