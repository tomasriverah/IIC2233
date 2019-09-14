import parametros
import objetos
import random
import math


def seleccion(lista):
    while True:
        copia_lista = []
        for i in lista:
            copia_lista.append(i)
        cuenta = 1
        for item in copia_lista:
            print(f"[{cuenta}] {item}")
            cuenta += 1
        eleccion = input("Introduzca un número:")
        if not str.isdigit(eleccion):
            print("***ELECCION INVALIDA***")
        else:
            if int(eleccion) not in range(0, cuenta ):
                print("***ELECCION INVALIDA***")
            else:
                return copia_lista[int(eleccion) - 1]

def creacion_piloto(vehiculos):

    dicc_pilotos = pilotos(parametros.PATHS["PILOTOS"])

    while True:
        nombre_usuario = input("Ingrese nombre de usuario:")
        sin_espacio = nombre_usuario.split(" ")
        if [str.isalnum(palabra) for palabra in sin_espacio] and nombre_usuario not in dicc_pilotos.keys():
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

    nombre_equipo1 = parametros.NUMEROEQUIPO[equipo]
    nombre_equipo =  str.upper(parametros.NUMEROEQUIPO[equipo])
    equilibrio = random.randint(parametros.EQUIPOS[nombre_equipo]["EQUILIBRIO"]["MIN"],
                                parametros.EQUIPOS[nombre_equipo]["EQUILIBRIO"]["MAX"])
    contextura = random.randint(parametros.EQUIPOS[nombre_equipo]["CONTEXTURA"]["MIN"],
                                parametros.EQUIPOS[nombre_equipo]["CONTEXTURA"]["MAX"])
    personalidad = parametros.EQUIPOS[nombre_equipo]["PERSONALIDAD"]
    if personalidad == "HALF":
        personalidad = random.choice(["OSADO", "PRECAVIDO"])


    piloto = objetos.Piloto(nombre_usuario, 0, personalidad, contextura, equilibrio, 0,
                            nombre_equipo1)


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
    dicc_vehiculos = {}
    for vehiculo in archivo:
        viculo = vehiculo.split(",")
        if viculo[2] == "bicicleta":
            auto = objetos.Bicicleta(viculo[0], viculo[1], viculo[2], viculo[3], viculo[4], viculo[5],
                              viculo[6], viculo[7])
            dicc_vehiculos[viculo[0]] = auto
        if viculo[2] == "automóvil":
            auto = objetos.Automovil(viculo[0], viculo[1], viculo[2], viculo[3], viculo[4], viculo[5],
                              viculo[6], viculo[7])
            dicc_vehiculos[viculo[0]] = auto
        if viculo[2] == "troncomóvil":
            auto = objetos.Troncomovil(viculo[0], viculo[1], viculo[2], viculo[3], viculo[4], viculo[5],
                              viculo[6], viculo[7])
            dicc_vehiculos[viculo[0]] = auto
        if viculo[2] == "motocicleta":
            auto = objetos.Motocicleta(viculo[0], viculo[1], viculo[2], viculo[3], viculo[4], viculo[5],
                              viculo[6], viculo[7])
            dicc_vehiculos[viculo[0]] = auto

    return dicc_vehiculos

def cargar_contrincantes(path):
    archivo = open(path, "r", encoding="UTF-8")
    lista_contrincantes = []
    for linea in archivo:
        contrincante_info = linea.split(",")
        if contrincante_info[0] != "Nombre":
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
        else:
            print("*** Nombre no encontrado ****")

def comprar_vehiculo(piloto, vehiculos):
    archivo = open(parametros.PATHS["COMPRA"], "r", encoding="UTF-8-sig")
    dicc = {}
    for linea in archivo:
        linea_s_salto = linea.strip("\n")
        vehiculo = linea_s_salto.split(",")
        dicc[vehiculo[0]] = vehiculo

    del dicc["Nombre"]
    while True:
        print(f"Dinero disponible ${piloto.dinero}")
        lista = [dicc[llave][0] + "; $:" + dicc[llave][1] for llave in dicc.keys()]
        lista.append("Salir" )
        eleccion = seleccion(lista)
        if eleccion == "Salir":
            return
        viculo = dicc[eleccion.split(";")[0]]
        if piloto.dinero < int(dicc[viculo[0]][1]):
            print("***No tienes dinero suficiente***")
        else:
            break

    nombre = input("Introduce el nombre de tu vehículo:")

    if viculo[2] == "bicicleta":
        auto = objetos.Bicicleta(nombre, piloto.nombre,
                                 viculo[2], viculo[3], viculo[4], viculo[5],
                                 viculo[6], viculo[7])
    if viculo[2] == "automóvil":
        auto = objetos.Automovil(nombre, piloto.nombre,
                                 viculo[2], viculo[3], viculo[4], viculo[5],
                                 viculo[6], viculo[7])
    if viculo[2] == "troncomóvil":
        auto = objetos.Troncomovil(nombre, piloto.nombre,
                                 viculo[2], viculo[3], viculo[4], viculo[5],
                                 viculo[6], viculo[7])

    if viculo[2] == "motocicleta":
        auto = objetos.Motocicleta(nombre, piloto.nombre,
                                 viculo[2], viculo[3], viculo[4], viculo[5],
                                 viculo[6], viculo[7])

    vehiculos[auto.nombre] = auto
    piloto.dinero -= int(dicc[viculo[0]][1])

def cargar_pistas(path):
    archivo = open(path, "r", encoding="UTF-8")
    lista_pistas = []
    for linea in archivo:
        pre_pista = linea.split(",")
        if pre_pista[0] != "Nombre":
            pista = objetos.Pista(pre_pista[0], pre_pista[1], pre_pista[2], pre_pista[3], pre_pista[4],
                                  pre_pista[5], pre_pista[6], pre_pista[7])
            lista_pistas.append(pista)

    return lista_pistas

def dano_recibido_x_vuelta(pista, piloto):
    if pista.tipo in ["pista rocosa", "pista suprema"]:
        return max(0, pista.rocas - piloto.vehiculo.carroceria)
    return 0

def tiempo_pits(piloto):
    tiempo = parametros.TIEMPO_MINIMO_PITS + (piloto.vehiculo_og.chasis - piloto.vehiculo.chasis)\
             * parametros.VELOCIDAD_PITS
    return tiempo

def dinero_x_vuelta(pista , n_vuelta):
    return pista.dificultad*n_vuelta

def dificultad_control(piloto):
    if piloto.vehiculo.categoria in ["bicicleta", "motocircleta"]:
        if piloto.personalidad == "precavido":
            return min(0, piloto.equilibrio * parametros.EQUILIBRIO_PRECAVIDO -
                    math.floor(parametros.PESO_MEDIO/piloto.vehiculo.peso))
        if piloto.personalidad == "osado":
            if piloto.personalidad == "precavido":
                return min(0, piloto.equilibrio -
                        math.floor(parametros.PESO_MEDIO / piloto.vehiculo.peso))


    return 0

def probabilidad_accidente(vuelta, pista, piloto):

    efecto_chasis = math.floor(((piloto.vehiculo_og.chasis -
                                piloto.vehiculo.chasis))/piloto.vehiculo_og.chasis)
    p_accidente = min(1, max(0, (velocidad_real(vuelta, pista, piloto) -
                             velocidad_recomendada(piloto.vehiculo, piloto.experiencia, pista))
                             / velocidad_recomendada(piloto.vehiculo, piloto.experiencia, pista))
                      + efecto_chasis)

    return p_accidente

def velocidad_recomendada(vehiculo, exp, pista):
    if pista.tipo == "pista hielo":
        v_recomendada = vehiculo.motor + (vehiculo.ruedas - pista.hielo) \
                        * parametros.POND_EFECT_HIELO + (exp - pista.dificultad)\
                        * parametros.POND_EFECT_DIFICULTAD
    elif pista.tipo == "pista hielo":
        v_recomendada = vehiculo.motor + (vehiculo.carroceria - pista.rocas) \
                        * parametros.POND_EFECT_ROCAS + (exp - pista.dificultad)\
                        * parametros.POND_EFECT_DIFICULTAD

    else:
        v_recomendada = vehiculo.motor + (vehiculo.ruedas - pista.hielo) \
                        * parametros.POND_EFECT_HIELO + (vehiculo.carroceria - pista.rocas) \
                        * parametros.POND_EFECT_ROCAS + (exp - pista.dificultad)\
                        * parametros.POND_EFECT_DIFICULTAD
    return v_recomendada


def velocidad_intencional(personalidad, v_recomendada):
    v_intencional = getattr(parametros, "EFECTO_" + str.upper(personalidad)) * v_recomendada
    return v_intencional


def hipotermia(vuelta, pista, piloto):
    if pista.tipo == "pista hielo" or pista.tipo == "pista suprema":
        hipo = min(0, vuelta * (piloto.contextura - pista.hielo))
        return hipo
    else:
        return 0


def velocidad_real(vuelta, pista, piloto):
    v_real = max(parametros.VELOCIDAD_MINIMA,
                 velocidad_intencional(piloto.personalidad,
                 velocidad_recomendada(piloto.vehiculo, piloto.experiencia,
                 pista)) +  dificultad_control(piloto) + hipotermia(vuelta, pista, piloto))
    return v_real

def calcula_tiempo(pista, competidor, vuelta):
    tiempo = pista.largo / velocidad_real(vuelta, pista, competidor)
    return tiempo

def ventaja(tiempo1, tiempon):
    return tiempon - tiempo1

def experiencia_recibida(piloto, ventaja, pista):
    if piloto.personalidad == "osado":
        return round((ventaja + pista.dificultad)* parametros.BONIFICACION_OSADO)
    else:
        return round((ventaja + pista.dificultad)* parametros.BONIFICACION_PRECAVIDO)

def dinero_ganador(pista):
    return pista.numerov * (pista.dificultad + pista.rocas + pista.hielo)

def guardar(partida):
    print(f"***Guardando partida de {partida.piloto.nombre}***")
    archivo_pilotos = open(parametros.PATHS["PILOTOS"], "r+", encoding="UTF-8")
    archivo_vehiculos = open(parametros.PATHS["VEHICULOS"], "r+", encoding="UTF-8")
    lineas = []
    lineas_a =[]
    lista_nombres = []
    coma = ","
    for linea in archivo_pilotos:
        lineas.append(linea.split(","))
    for line in lineas:
        lista_nombres.append(line[0])

        if line[0] == partida.piloto.nombre:
            line = [partida.piloto.nombre, str(partida.piloto.dinero), partida.piloto.personalidad,
                    str(partida.piloto.contextura), str(partida.piloto.equilibrio),
                    str(partida.piloto.experiencia), partida.piloto.equipo + "\n"]
        lineas_a.append(coma.join(line))


    if partida.piloto.nombre not in lista_nombres:
        pilot = [partida.piloto.nombre, str(partida.piloto.dinero),
                 str.lower(partida.piloto.personalidad),
                 str(partida.piloto.contextura), str(partida.piloto.equilibrio),
                 str(partida.piloto.experiencia), partida.piloto.equipo]
        lineas_a.append(coma.join(pilot))

    archivo_pilotos.close()
    archivo_pilotos = open(parametros.PATHS["PILOTOS"], "w", encoding="UTF-8")

    for linea in lineas_a:
        archivo_pilotos.writelines(linea)
    archivo_pilotos.close()


    archivo_vehiculos= open(parametros.PATHS["VEHICULOS"], "w", encoding="UTF-8")
    archivo_vehiculos.writelines("Nombre,Dueño,Categoría,Chasis,Carrocería,Ruedas,Motor o "
                                 "Zapatillas,Peso\n")
    for vehiculo in partida.vehiculos.values():
        archivo_vehiculos.writelines(vehiculo.nombre + "," + vehiculo.dueno + "," +
                                     vehiculo.categoria + "," + str(vehiculo.chasis)  + "," +
                                     str(vehiculo.carroceria) + "," +  str(vehiculo.ruedas)  +
                                     "," + str(vehiculo.motor)  + "," + str(vehiculo.peso) +"\n" )
    archivo_pilotos.close()