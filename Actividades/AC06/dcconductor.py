import csv
from conductores import Conductor
from excepcion_patente import ErrorPatente
import os

class DCConductor:

    def __init__(self, registro_oficial, conductores):
        '''
        El constructor crea las estructuras necesarias para almacenar los datos
         proporcionados, recibe la información necesaria para el funcionamiento de la clase.
        '''
        self.registro_oficial = registro_oficial
        self.conductores = conductores
        self.seleccionados = list()


    def chequear_rut(self, conductor):
        '''
        Recibe un conductor y levanta una excepción en caso de que su rut no siga
        el formato correcto
        '''

        if '.' in conductor.rut:
            raise TypeError(f'{conductor.rut} con puntos')
        elif '-' not in conductor.rut:
            raise TypeError(f'{conductor.rut} sin guion')




    def chequear_nombre(self, conductor):
        '''
        Recibe un conductor y levanta una excepción en caso de que su nombre no
        exista en el registro oficial.
        '''

        if conductor.nombre not in self.registro_oficial:
            raise NameError(f'{conductor.nombre} no encontrado en registro ')


    def chequear_celular(self, conductor):
        '''
        Recibe un conductor y levanta una excepción en caso de que su celular
        no siga el formato correcto
        '''

        if not str.isnumeric(conductor.celular) or conductor.celular[0] != '9' or\
                len(conductor.celular) != 9:
            raise NameError(f'{conductor.celular} numero celular no válido ')


    def chequear_patente(self, conductor):
        '''
        Recibe un conductor y levanta una excepción en caso de que su patente no
        coincida con la información del registro oficial.
        '''
        if conductor.patente != self.registro_oficial[conductor.nombre]:
            raise ErrorPatente(conductor)


