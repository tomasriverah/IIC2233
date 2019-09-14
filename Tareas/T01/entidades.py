import parametros
import objetos


def we_import_vehicles():
    lista_vehiculos = []
    archivo = open(parametros.PATHS["VEHICULOS"], "r+", encoding="UTF-8")
    for linea in archivo:
        vehiculo = linea.split(",")
        if vehiculo[2] == "bicicleta":
            viculo = objetos.Bicicleta(vehiculo[0], vehiculo[1], vehiculo[2], vehiculo[3],
                                       vehiculo[4], vehiculo[5], vehiculo[6], vehiculo[7])
            lista_vehiculos.append(viculo)
        elif vehiculo[2] == "automóvil":
            viculo = objetos.Automovil(vehiculo[0], vehiculo[1], vehiculo[2], vehiculo[3],
                                       vehiculo[4], vehiculo[5], vehiculo[6], vehiculo[7])
            lista_vehiculos.append(viculo)
        elif vehiculo[2] == "troncomóvil":
            viculo = objetos.Troncomovil(vehiculo[0], vehiculo[1], vehiculo[2], vehiculo[3],
                                       vehiculo[4], vehiculo[5], vehiculo[6], vehiculo[7])
            lista_vehiculos.append(viculo)
        elif vehiculo[2] == "motocicleta":
            viculo = objetos.Motocicleta(vehiculo[0], vehiculo[1], vehiculo[2], vehiculo[3],
                                       vehiculo[4], vehiculo[5], vehiculo[6], vehiculo[7])
            lista_vehiculos.append(viculo)
    return lista_vehiculos


def we_import_pilotos(path):
    archivo = open(path, "r", encoding="UTF-8")

vehiculos = we_import_vehicles()
