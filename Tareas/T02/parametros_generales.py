import os

PATH_OTROS = os.path.join('sprites', 'otros')

PATH_MAPAS = os.path.join('mapas')

PATH_IMG_MAPA = os.path.join('sprites', 'mapa')

PATH_IMG_CULTIVOS = os.path.join('sprites', 'cultivos')


DICCIONARIO_IMAGENES = {'O' : os.path.join(PATH_IMG_MAPA, 'tile006.png'),
                        'C' : os.path.join(PATH_IMG_MAPA, 'tile004.png'),
                        'R' : os.path.join(PATH_IMG_MAPA, 'tile087.png'),
                        'H' : os.path.join(PATH_IMG_MAPA, 'House.png'),
                        'T' : os.path.join(PATH_IMG_MAPA, 'Store.png')}

DICCIONARIO_CULTIVOS = {'semilla_choclo' : os.path.join(PATH_IMG_CULTIVOS, 'choclo', 'seeds.png'),
                        }