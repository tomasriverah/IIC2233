from cargar import cargar_archivos
from os import path


class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id = id_usuario
        self.nombre = nombre
        self.seguidos = []
        # self.seguidores = [] # almacenar a los seguidores es opcional.


class Pintogram:
    def __init__(self):
        # Recuerda que debes almacenar todos los usuarios dentro de la red
        self.usuarios = {}

    def nuevo_usuario(self, id_usuario, nombre):
        # Método que se encarga de agregar un usuario a la red
        self.usuarios[id_usuario] = Usuario(id_usuario, nombre)

    def follow(self, id_seguidor, id_seguido):
        # Método que permite a un usuario seguir a otro
        self.usuarios[id_seguidor].seguidos.append(id_seguido)

    def cargar_red(self, ruta_red):
        # Método que se encarga de generar la red social, cargando y
        # guardando cada uno de los usuarios. Quizás otras funciones de
        # Pintogram sean útiles.
        usuarios = cargar_archivos(ruta_red)
        for usuario in usuarios:
            user = Usuario(usuario[0], usuario[1])
            user.seguidos = usuario[2]
            self.usuarios[user.id] = user

    def unfollow(self, id_seguidor, id_seguido):
        # Método que pertmite a un usuario dejar de seguir a otro
        self.usuarios[id_seguidor].seguidos.remove(id_seguido)

    def mis_seguidos(self, id_usuario):
        # Método que retorna los seguidores de un usuario
        return len(self.usuarios[id_usuario].seguidos)

    def distancia_social(self, id_usuario_1, id_usuario_2):
        # Método que retorna la "distancia social" de dos usuarios
        visitados = []
        stack = [self.usuarios[id_usuario_1]]
        while len(stack) > 0:
            persona = stack.pop()
            if persona not in visitados:
                visitados.append(persona)
                for vecino in persona.seguidos:
                    if vecino not in visitados:
                        stack.append(self.usuarios[vecino])
        return len(distancia)


if __name__ == "__main__":
    pintogram = Pintogram()
    pintogram.cargar_red(path.join("archivos", "simple.txt"))
    print(pintogram.mis_seguidos("1"))
    print(pintogram.mis_seguidos("3"))
    print(pintogram.distancia_social("3", "5"))
    print(pintogram.distancia_social("2", "4"))

# Puedes agregar más consultas y utilizar los demás archivos para probar tu código
