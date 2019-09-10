import parametros
import objetos
import random


def seleccion(lista):
    copia_lista = []
    for i in lista:
        copia_lista.append(i)
    cuenta = 1
    for item in copia_lista:
        print(f"[{cuenta}] {item}")
        cuenta += 1
    eleccion = input("Introduzca un número:")

    return copia_lista[int(eleccion) - 1]

def creacion_piloto(vehiculos):

    dicc_pilotos = pilotos(parametros.PATHS["PILOTOS"])

    while True:
        nombre_usuario = input("Ingrese nombre de usuario:")
        sin_espacio = nombre_usuario.strip(" ")
        if str.isalnum(sin_espacio) and nombre_usuario not in dicc_pilotos.keys():
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


    piloto = objetos.Piloto(nombre_usuario, 0, personalidad, contextura, equilibrio, 0, equipo)


    return piloto

def vehiculo_incial(piloto):
    print("Seleccione vehículo inicial:")
    eleccion = seleccion(["bicicleta", "automóvil", "troncomóvil", "motocicleta"])
    ELECCION = eleccion.upper()
    nombre = input("Escriba el nombre de su vehiculo:")
    if eleccion == "bicicleta":
        viculo = objetos.Bicicleta(nombre, piloto.nombre, eleccion,
                                   asignador_stat(ELECCION, "CHASIS"),
                                   asignador_stat(ELECCION, "CARROCERIA"),
                                   asignador_stat(ELECCION, "RUEDAS"),
                                   asignador_stat(ELECCION, "ZAPATILLAS"),
                                   asignador_stat(ELECCION, "PESO"))

    elif eleccion == "automóvil":
        viculo = objetos.Automovil(nombre, piloto.nombre, eleccion,
                                   asignador_stat(ELECCION, "CHASIS"),
                                   asignador_stat(ELECCION, "CARROCERIA"),
                                   asignador_stat(ELECCION, "RUEDAS"),
                                   asignador_stat(ELECCION, "MOTOR"),
                                   asignador_stat(ELECCION, "PESO"))

    elif eleccion == "troncomóvil":
        viculo = objetos.Troncomovil(nombre, piloto.nombre, eleccion,
                                   asignador_stat(ELECCION, "CHASIS"),
                                   asignador_stat(ELECCION, "CARROCERIA"),
                                   asignador_stat(ELECCION, "RUEDAS"),
                                   asignador_stat(ELECCION, "ZAPATILLAS"),
                                   asignador_stat(ELECCION, "PESO"))
    elif eleccion == "motocicleta":
        viculo = objetos.Motocicleta(nombre, piloto.nombre, eleccion,
                                   asignador_stat(ELECCION, "CHASIS"),
                                   asignador_stat(ELECCION, "CARROCERIA"),
                                   asignador_stat(ELECCION, "RUEDAS"),
                                   asignador_stat(ELECCION, "MOTOR"),
                                   asignador_stat(ELECCION, "PESO"))

    return viculo

def asignador_stat(vehiculo, stat):
    info = getattr(parametros, vehiculo)
    minimo = info[stat]["MIN"]
    maximo = info[stat]["MAX"]
    numero = random.randint(minimo, maximo)
    return numero

def cargar_vehiculos(path):
    archivo = open(path, "r", encoding="UTF-8" )
    lista_vehiculos = []
    for vehiculo in archivo:
        viculo = vehiculo.split(",")
        if viculo[2] == "bicicleta":
            auto = objetos.Bicicleta(viculo[0], viculo[1], viculo[2], viculo[3], viculo[4], viculo[5],
                              viculo[6], viculo[7])
            lista_vehiculos.append(auto)
        if viculo[2] == "automóvil":
            auto = objetos.Automovil(viculo[0], viculo[1], viculo[2], viculo[3], viculo[4], viculo[5],
                              viculo[6], viculo[7])
            lista_vehiculos.append(auto)
        if viculo[2] == "troncomóvil":
            auto = objetos.Troncomovil(viculo[0], viculo[1], viculo[2], viculo[3], viculo[4], viculo[5],
                              viculo[6], viculo[7])
            lista_vehiculos.append(auto)
        if viculo[2] == "motocicleta":
            auto = objetos.Motocicleta(viculo[0], viculo[1], viculo[2], viculo[3], viculo[4], viculo[5],
                              viculo[6], viculo[7])
            lista_vehiculos.append(auto)

    return lista_vehiculos

def cargar_contrincantes(path):
    archivo = open(path, "r", encoding="UTF-8")
    lista_contrincantes = []
    for linea in archivo:
        contrincante_info = linea.split(",")
        contrincante = objetos.Contrincante(contrincante_info[0], contrincante_info[1],
                                            contrincante_info[2], contrincante_info[3],
                                            contrincante_info[4], contrincante_info[5],
                                            contrincante_info[6])
        lista_contrincantes.append(contrincante)

    return lista_contrincantes

def pilotos(path):
    archivo = open(path, "r", encoding="UTF-8")
    dicc_pilotos = {}
    for linea in archivo:
        piloto = linea.split(",")
        diccpiloto = {"nombre": piloto[0], "dinero": piloto[1], "personalidad": piloto[2],
                      "contextura": piloto[3], "equilibrio": piloto[4], "exp": piloto[5],
                      "equipo": piloto[6]}
        dicc_pilotos[piloto[0]] = diccpiloto

    return dicc_pilotos

def carga_piloto(path):

    dicc_pilotos = pilotos(path)

    while True:
        nombre = input("Introduzca nombre de piloto:")
        if nombre in dicc_pilotos.keys():
            pre_piloto = dicc_pilotos[nombre]
            new_piloto = objetos.Piloto(pre_piloto["nombre"], pre_piloto["dinero"],
                                        pre_piloto["personalidad"], pre_piloto["contextura"],
                                        pre_piloto["equilibrio"], pre_piloto["exp"],
                                        pre_piloto["equipo"])
            return new_piloto
            break
        else:
            print("*** Nombre no encontrado ****")

def comprar_vehiculo(piloto):                                                       ##por completar
    archivo = open(parametros.PATHS["COMPRA"], "r", encoding="UTF-8-sig")
    dicc = {}
    for linea in archivo:
        linea_s_salto = linea.strip("\n")
        vehiculo = linea_s_salto.split(",")
        dicc[vehiculo[0]] = vehiculo

    del dicc["Nombre"]
    lista = [dicc[llave][0] + " $:" + dicc[llave][1] for llave in dicc.keys()]


    eleccion = seleccion(lista)

def cargar_pistas(path):
    archivo = open(path, "r", encoding="UTF-8")
    lista_pistas = []
    for linea in archivo:
        pre_pista = linea.split(",")
        pista = objetos.Pista(pre_pista[0], pre_pista[1], pre_pista[2], pre_pista[3], pre_pista[4],
                              pre_pista[5], pre_pista[6], pre_pista[7])
        lista_pistas.append(pista)
    lista_pistas.pop(0)
    return lista_pistas