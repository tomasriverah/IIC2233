class ErrorPatente(Exception):
    def __init__(self, conductor):
        self.conductor = conductor
        super().__init__(f'{self.conductor.nombre} - {self.conductor.patente}'
                         f' Patente distinta a registro oficial')


