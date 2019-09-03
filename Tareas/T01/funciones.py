import parametros
import objetos
import random




def creacion_piloto(pilotos, vehiculos):


    while True:
        nombre_usuario = input("Ingrese nombre de usuario:")
        sin_espacio = nombre_usuario.strip(" ")
        if str.isalnum(sin_espacio) and nombre_usuario not in pilotos:
            break
        else:
            print("*****Nombre invalido*****")

    while True:
        equipo = input("Seleccione su equipo:\n [1] Tareos\n [2] Docencios\n [3] Hibridos"
                       "\nIngrese:")
        if equipo in ["1", "2", "3"]:
            break
        else:
            print("*****Opción Invalida*****")

    nombre_equipo =  parametros.NUMEROEQUIPO[equipo]
    equilibrio = random.randint(parametros.EQUIPOS[nombre_equipo]["EQUILIBRIO"]["MIN"],
                                parametros.EQUIPOS[nombre_equipo]["EQUILIBRIO"]["MAX"])
    contextura = random.randint(parametros.EQUIPOS[nombre_equipo]["CONTEXTURA"]["MIN"],
                                parametros.EQUIPOS[nombre_equipo]["CONTEXTURA"]["MAX"])
    personalidad = parametros.EQUIPOS[nombre_equipo]["PERSONALIDAD"]
    if personalidad == "HALF":
        personalidad = random.choice(["OSADO", "PRECAVIDO"])


    piloto = objetos.Piloto(nombre_usuario,nombre_equipo, equilibrio, 0, contextura, personalidad)


    return piloto