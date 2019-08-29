"""
Aquí debes completar las funciones propias de Poblar el Sistema
¡OJO¡: Puedes importar lo que quieras aquí, si no lo necesitas
"""


"""
Esta estructura de datos te podría ser útil para el desarollo de la actividad, puedes usarla
si así lo deseas
"""

import os
import csv

DICT_PISOS = {
    'Chief Tamburini': 'Piso -4',
    'Jefe': 'Piso -3',
    'Mentor': 'Piso -2',
    'Nuevo': 'Piso -1',
}


def cargar_alumnos(ruta_archivo_alumnos):
    print(f'Cargando datos de {ruta_archivo_alumnos}...')

    alumnos = open(ruta_archivo_alumnos, "r",  encoding="utf-8")
    stack_alumnos = []
    for alumno in alumnos:
        nuevo = alumno.strip("\n")
        stack_alumnos.append(nuevo)

    return stack_alumnos




def cargar_ayudantes(ruta_archivo_ayudantes):
    print(f'Cargando datos de {ruta_archivo_ayudantes}...')

    ayudantes = open(ruta_archivo_ayudantes, "r", encoding="utf-8")
    stack_ayudantes = []
    for ayudante in ayudantes:
        nuevo = ayudante.strip("\n")
        stack_ayudantes.append(nuevo)

    return stack_ayudantes


print(cargar_alumnos("bases_datos/alumnos.csv"))