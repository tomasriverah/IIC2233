import socket
import json
import pickle

class Cliente:

    def __init__(self):
        '''Inicializador de cliente.

        Crea su socket, e intente conectarse a servidor.
        '''
        # --------------------
        # Completar desde aquí

        self.host = socket.gethostname()
        self.port = 9000
        self.socket_cliente =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # Aqui deberas intentar conectar al servidor.
            self.socket_cliente.connect((self.host, self.port))

            # Completar hasta aquí
            # --------------------
            print("Cliente conectado exitosamente al servidor.")
            self.interactuar_con_servidor()
        except ConnectionRefusedError:
            self.cerrar_conexion()

    def interactuar_con_servidor(self):
        '''Comienza ciclo de interacción con servidor.

        Recibe estado y envia accion.
        '''
        while True:
            mensaje, continuar = self.recibir_estado()
            if not continuar:
                break
            accion = self.procesar_comando_input()
            while accion is None:
                print('Input invalido.')
                accion = self.procesar_comando_input()
            self.enviar_accion(accion)
        self.cerrar_conexion()

    def recibir_estado(self):
        '''Recibe actualización de estado desde servidor.'''
        # ----------------------------------------------------------
        # Completar y usar un metodo para cualquier largo de mensaje

        largo_msje = int.from_bytes(self.socket_cliente.recv(4), byteorder='big')
        datos = bytearray()

        # Ahora leemos el archivo por chunks, de máximo 4096 bytes.
        while len(datos) < largo_msje:
            # El último recv será probablemente más chico que 4096
            bytes_leer = min(4096, largo_msje - len(datos))
            datos_recibidos = self.socket_cliente.recv(bytes_leer)
            datos.extend(datos_recibidos)

        # Debe haber un string para imprimirse

        mensaje = pickle.loads(datos)

        print(mensaje)
        # Debe haber un boolean para saber si continuar funcionando
        continuar = True

        # Completar hasta aquí
        # --------------------
        return mensaje, continuar

    def procesar_comando_input(self):
        '''Procesa y revisa que el input del usuario sea valido'''
        input_usuario = input('-> ')
        # ---------
        # Completar

        input_separado = input_usuario.split(' ')

        if input_usuario in ['\juego_nuevo', '\salir']:
            return input_usuario
        elif input_separado[0] == '\jugada' and input_separado[1].isnumeric():
            return input_usuario

        else:
            return None

        # Completar hasta aquí
        # --------------------

    def enviar_accion(self, accion):
        '''Envia accion asociada a comando ya procesado al servidor.'''
        # ----------------------------------------------------------
        # Completar y usar un metodo para cualquier largo de mensaje

        mensaje_codificado = accion.encode('utf-8')

        largo_msje = len(mensaje_codificado)


        self.socket_cliente.sendall(largo_msje.to_bytes(4, byteorder='big'))

        self.socket_cliente.sendall(mensaje_codificado)

        # Completar hasta aquí
        # --------------------

    def cerrar_conexion(self):
        '''Cierra socket de conexión.'''
        self.socket_cliente.close()
        print("Conexión terminada.")


if __name__ == "__main__":
    Cliente()
