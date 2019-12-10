from bugterpie import Bugterpie
import json


indices_generaciones = {
    1: (1, 151),
    2: (152, 251),
    3: (252, 386),
    4: (387, 493),
    5: (494, 649)
}


class Programon:
    def __init__(self, id, nombre, tipo, generacion):
        self.id = int(id)
        self.nombre = nombre
        self.tipo = tipo
        self.generacion = int(generacion)

    def __repr__(self):
        return f'PROGRáMON N°{self.id:0>3}: {self.nombre}'


class Pydgey:
    def __init__(self, path_data):
        self.data = None
        self.cargar_data(path_data)

    def cargar_data(self, path_data):
        with open(path_data, 'r', encoding='utf-8') as file:
            self.data = json.load(file, object_hook=lambda x: Programon(**x))

    @staticmethod
    def aire_afilatipo(programon):
        '''
        Acá debes completar el método aire_afilatipo
        '''
        if len(programon.tipo) > 2:
            raise TypeError('Programón con más de dos tipos')
        if len(programon.tipo) > 1:
            if programon.tipo[0] == programon.tipo[1]:
                raise TypeError('Programón con tipo repetido')


    @staticmethod
    def pico_taladraid(programon):
        '''
        Acá debes completar el método pico_taladraid
        '''

        ##### Consideré el rango inclusive el ultimo numero del rango del diccionario

        if programon.id not in range(indices_generaciones[programon.generacion][0],
                                     indices_generaciones[programon.generacion][1] + 1):
            raise IndexError('Id no pertenece a generación')

    @staticmethod
    def remolinombre(programon):
        '''
        Acá debes completar el método remolinombre
        '''
        if 'Bug' in programon.nombre or 'bug' in programon.nombre:
            raise Bugterpie

    def encontrar_errores(self):
        for programon in self.data:
            print(f'>> Se procesa {programon}')
            try:
                self.aire_afilatipo(programon)

            except TypeError as err:
                '''
                Acá debes manejar la excepción del aire_afilatipo
                '''
                print(err)
                programon.tipo = programon.tipo[0:2]
                programon.tipo = set(programon.tipo)
                programon.tipo = list(programon.tipo)

            try:
                self.pico_taladraid(programon)

            except IndexError as err:
                '''
                Acá debes manejar la excepción del pico_taladraid
                '''
                print(err)
                count = 0
                for i in indices_generaciones:
                    count += 1
                    if programon.id in range(i):
                        programon.generacion = count

            try:
                self.remolinombre(programon)

            except Bugterpie as err:
                '''
                Acá debes manejar la excepción del remolinombre
                '''
                print(err)
                programon.nombre = programon.nombre.lower().replace('bug', 'progra')

