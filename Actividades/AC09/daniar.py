import os
import json
import time # Ocupe time.strftime para obtener fecha y hora


class DocengelionEncoder(json.JSONEncoder):
    def default(self, obj):

        return {'modelo': obj.modelo,
                'estado': 'reparacion',
                'registro_reparacion': time.strftime("%b %d %Y %H:%M:%S"),
                'nucleo' : obj.nucleo}



class Docengelion:
    def __init__(self, modelo, nucleo, *args, **kwargs):
        self.modelo = modelo
        self.nucleo = nucleo
        self.estado = 'funcional'
        self.registro_reparacion = None


def recibir_eva(ruta):
    lista_evas = []
    evas = json.load(open(ruta, 'r'))

    for diccionario in evas:
        eva = Docengelion(diccionario['modelo'],diccionario['nucleo'])
        eva.estado = diccionario['estado']
        eva.registro_reparacion = diccionario['registro_reparacion']
        lista_evas.append(eva)


    return lista_evas

def reparar_eva(docengelion):
    try:
        os.mkdir('Daniar')
    except:
        pass

    json_string = json.dumps(docengelion, cls=DocengelionEncoder)
    file = open(f'Daniar/Unidad-{docengelion.modelo}.json', 'w+')
    file.write(json_string)
    file.close()




if __name__ == '__main__':
    try:
        dcngelions = recibir_eva('docent.json')
        if dcngelions:
            print("DANIAR200: Ha cargado las unidades Docengelion")
        try:
            for unidad in dcngelions:
                reparar_eva(unidad)
            print("DANIAR201: Se estan reparando las unidades Docengelion")
        except Exception as error:
            print(f'Error: {error}')
            print("DANIAR501: No ha podido reparar las unidades Docengelion")
    except Exception as error:
        print(f'Error: {error}')
        print("DANIAR404: No ha podido cargar las unidades Docengelion")

