"""
Aquí debes completar las funciones de las consultas
"""


def resumen_actual(ayudantes, alumnos):
    # Com
    nivel_1 = 0
    nivel_2 = 0
    nivel_3 = 0
    nivel_4 = 0
    print(f"Alumnos restantes: {len(alumnos)}")
    print(f"Ayudantes restantes: {len(ayudantes)}")

    for ayudante in ayudantes:
        if "Nuevo" in ayudante[0]:
            nivel_1 += 1
        if "Mentor" in ayudante[0]:
            nivel_2 += 1
        if "Jefe" in ayudante[0]:
            nivel_3 += 1
        if "Chief Tamburini" in ayudante[0]:
            nivel_4 += 1

    print(f"Alumnos restantes: {len(alumnos)}")
    print(f"Ayudantes restantes: {len(ayudantes)}")
    print(f"Nivel -1: {nivel_1}")
    print(f"Nivel -2: {nivel_2}")
    print(f"Nivel -3: {nivel_3}")
    print(f"Nivel -4: {nivel_4}")

def stock_comida(alumnos):
    # Completar

    pass
