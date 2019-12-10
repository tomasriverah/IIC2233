import json
from textwrap import indent


class NodoProgramon:

    def __init__(self, numero, nombre):
        self.numero = numero
        self.nombre = nombre
        self.hije_izquierdo = None
        self.hije_derecho = None

    def tiene_hije_izquierdo(self):
        return True if self.hije_izquierdo else False

    def tiene_hije_derecho(self):
        return True if self.hije_derecho else False

    def __repr__(self):
        texto = f'{self.numero}. {self.nombre} \n'
        repr_hijos = []
        izq = 'Izq: '
        izq += repr(self.hije_izquierdo) if self.tiene_hije_izquierdo() else '-'
        der = 'Der: '
        der += repr(self.hije_derecho) if self.tiene_hije_derecho() else '-'
        repr_hijos.append(izq)
        repr_hijos.append(der)
        texto_hijos = [indent(texto_hijo, '   ') for texto_hijo in repr_hijos]
        return texto + '\n'.join(texto_hijos)


class ProgramonTree:
    '''Estructura que almacena NodoProgramones.'''

    def __init__(self):
        self.raiz = None

    def cargar_nodos(self, ruta):
        with open(ruta) as archivo:
            datos = json.load(archivo)
        for programon in datos:
            nodo_programon = NodoProgramon(**programon)
            self.insertar_programon(nodo_programon)
            # Cada vez que agrega un nodo se imprime para ver como está.
            print(self)
            print()

    def insertar_programon(self, programon):
        if self.raiz == None:
            self.raiz = programon
        else:
            # Completar
            if self.raiz.numero < programon.numero:
                if self.raiz.tiene_hije_derecho():
                    self.raiz = self.raiz.hije_derecho
                    self.insertar_programon(programon)
                else:
                    self.raiz.hije_derecho = programon

            elif self.raiz.numero > programon.numero:
                if self.raiz.tiene_hije_izquierdo():
                    self.raiz = self.raiz.hije_izquierdo
                    self.insertar_programon(programon)
                else:
                    self.raiz.hije_izquierdo = programon

    def numero_programon(self, nombre):
        por_visitar = []
        por_visitar.append(self.raiz)

        # Completar
        for nodo in por_visitar:
            if nombre == nodo.nombre:
                numero = nodo.numero

                return numero
            else:
                por_visitar.remove(nodo)
                if nodo.hije_izquierdo:
                    por_visitar.append(nodo.hije_izquierdo)
                if nodo.hije_derecho:
                    por_visitar.append(nodo.hije_derecho)

    def ruta_programon(self, nombre):
        numero = self.numero_programon(nombre)
        nodo_previo = None
        nodo_actual = self.raiz
        ruta = [nodo_actual.numero]
        nodo_encontrado = False
        nodo_out = []
        while not nodo_encontrado:
            ruta.append(nodo_actual)
            if nodo_actual.numero == numero:
                nodo_encontrado = True

            elif nodo_actual in nodo_out:
                nodo_actual = nodo_previo

            else:
                if nodo_actual.tiene_hije_izquierdo:
                    ruta.append(nodo_actual)
                    nodo_previo = nodo_actual
                    nodo_actual = nodo.hije_izquierdo

                elif nodo_actual.tiene_hije_derecho:
                    nodo_previo = nodo_actual
                    nodo_out.append(nodo_actual)
                    nodo_actual = nodo.hije_derecho

                else:
                    nodo_actual = nodo_previo

        return ruta

    def __repr__(self):
        return repr(self.raiz)


if __name__ == '__main__':
    programontree = ProgramonTree()
    programontree.cargar_nodos('programones.json')
    print(programontree)

    print(programontree.numero_programon('Pidgeot'))
    print(programontree.ruta_programon('Pidgeot'))

    print(programontree.numero_programon('Bulbasaur'))
    print(programontree.ruta_programon('Bulbasaur'))

    print(programontree.numero_programon('Ekanz'))
    print(programontree.ruta_programon('Ekanz'))