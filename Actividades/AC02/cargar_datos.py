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
        alumno2 = nuevo.split(";")
        comidas = alumno2[1].split(",")
        stack_alumnos.append([alumno2[0], set(comidas)])

    return stack_alumnos




def cargar_ayudantes(ruta_archivo_ayudantes):
    print(f'Cargando datos de {ruta_archivo_ayudantes}...')

    ayudantes = open(ruta_archivo_ayudantes, "r", encoding="utf-8")
    stack_ayudantes = []
    for ayudante in ayudantes:
        sin_salto = ayudante.strip("\n")
        ayudante2 = sin_salto.split(";")
        comidas = ayudante2[2].split(",")
        ayudante_final = [{ayudante2[0], ayudante2[1]}, set(comidas), []]
        stack_ayudantes.append(ayudante_final)

    return stack_ayudantes

alumnos = cargar_alumnos("bases_datos/alumnos.csv")
ayudantes = cargar_ayudantes("bases_datos/ayudantes.csv")

print(alumnos[0])
print(ayudantes[0])