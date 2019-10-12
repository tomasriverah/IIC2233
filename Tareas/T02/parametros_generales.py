import os
import parametros_precios

PATH_OTROS = os.path.join('sprites', 'otros')

PATH_MAPAS = os.path.join('mapas')

PATH_IMG_MAPA = os.path.join('sprites', 'mapa')

PATH_IMG_CULTIVOS = os.path.join('sprites', 'cultivos')

PATH_FONDO = os.path.join('sprites', 'otros', 'window_template.png')



DICCIONARIO_IMAGENES = {'O' : os.path.join(PATH_IMG_MAPA, 'tile006.png'),
                        'C' : os.path.join(PATH_IMG_MAPA, 'tile004.png'),
                        'R' : os.path.join(PATH_IMG_MAPA, 'tile087.png'),
                        'H' : os.path.join(PATH_IMG_MAPA, 'House.png'),
                        'T' : os.path.join(PATH_IMG_MAPA, 'Store.png')}

DICCIONARIO_CULTIVOS = {'semilla_choclo' : os.path.join(PATH_IMG_CULTIVOS, 'choclo', 'seeds.png'),
                        'semilla alcachofa' : os.path.join(PATH_IMG_CULTIVOS, 'alcachofa', 'seeds.png')
                        }

DICCIONARIO_SEMILLAS = {('choclo', 0): os.path.join(PATH_IMG_CULTIVOS, 'choclo', 'stage_1.png'),
                        ('choclo', 1): os.path.join(PATH_IMG_CULTIVOS, 'choclo', 'stage_2.png'),
                        ('choclo', 2): os.path.join(PATH_IMG_CULTIVOS, 'choclo', 'stage_3.png'),
                        ('choclo', 3): os.path.join(PATH_IMG_CULTIVOS, 'choclo', 'stage_4.png'),
                        ('choclo', 4): os.path.join(PATH_IMG_CULTIVOS, 'choclo', 'stage_5.png'),
                        ('choclo', 5): os.path.join(PATH_IMG_CULTIVOS, 'choclo', 'stage_6.png'),
                        ('choclo', 6): os.path.join(PATH_IMG_CULTIVOS, 'choclo', 'stage_7.png'),
                        ('alcachofa', 0): os.path.join(PATH_IMG_CULTIVOS, 'alcachofa', 'stage_1.png'),
                        ('alcachofa', 1): os.path.join(PATH_IMG_CULTIVOS, 'alcachofa', 'stage_2.png'),
                        ('alcachofa', 2): os.path.join(PATH_IMG_CULTIVOS, 'alcachofa', 'stage_3.png'),
                        ('alcachofa', 3): os.path.join(PATH_IMG_CULTIVOS, 'alcachofa', 'stage_4.png'),
                        ('alcachofa', 4): os.path.join(PATH_IMG_CULTIVOS, 'alcachofa', 'stage_5.png'),
                        ('alcachofa', 5): os.path.join(PATH_IMG_CULTIVOS, 'alcachofa', 'stage_6.png'),

}


DICCIONARIO_TIENDA = {'semilla_choclo' : [os.path.join(PATH_IMG_CULTIVOS, 'choclo', 'seeds.png'),
                                          parametros_precios.PRECIO_SEMILLA_CHOCLOS],
                      'semilla_alcachofa' : [os.path.join(PATH_IMG_CULTIVOS, 'alcachofa', 'seeds.png'),
                                             parametros_precios.PRECIO_SEMILLA_ALCACHOFAS],
                      'azada' : [os.path.join(PATH_OTROS, 'hoe.png'),
                                 parametros_precios.PRECIO_AZADA],
                      'hacha' :  [os.path.join(PATH_OTROS, 'axe.png'),
                                  parametros_precios.PRECIO_HACHA],
                      'alcachofa' : [os.path.join('sprites', 'recursos', 'artichoke.png'),
                                     parametros_precios.PRECIO_ALACACHOFAS],
                      'choclo' : [os.path.join('sprites', 'recursos', 'corn.png'),
                                  parametros_precios.PRECIO_CHOCLOS],
                      'leña' : [os.path.join('sprites', 'recursos', 'wood.png'),
                                parametros_precios.PRECIO_LEÑA],
                      'oro' : [os.path.join('sprites', 'recursos', 'gold.png'),
                               parametros_precios.PRECIO_ORO],
                      'ticket' : [os.path.join('sprites', 'otros', 'ticket.png'),
                               parametros_precios.PRECIO_TICKET]
}

DICCIONARIO_INVENTARIO = {0 : os.path.join(PATH_IMG_CULTIVOS, 'choclo', 'seeds.png'),
                          1 : os.path.join(PATH_IMG_CULTIVOS, 'alcachofa', 'seeds.png'),
                          2 : os.path.join('sprites', 'otros', 'hoe.png'),
                          3 : os.path.join('sprites', 'otros', 'axe.png'),
                          4 : os.path.join('sprites', 'recursos', 'corn.png'),
                          5 : os.path.join('sprites', 'recursos', 'artichoke.png'),
                          6 : os.path.join('sprites', 'recursos', 'wood.png'),
                          7 : os.path.join('sprites', 'recursos', 'gold.png'),
}
PATH_IMG_MOEDAS = os.path.join('sprites', 'otros', 'money.png')

PATH_IMG_ORO = os.path.join('sprites', 'recursos', 'gold.png')

PATH_IMG_ARBOL = os.path.join('sprites', 'otros', 'tree.png')

MONEDAS_INICIALES = 150

VEL_MOVIMIENTO = 10

ENERGIA_JUGADOR = 100

PROB_ORO = 0.5

PROB_ARBOL = 0.7

ENERGIA_DORMIR = 20

DINERO_TRAMPA = 2500