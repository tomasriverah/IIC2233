# Seccion para importar liberías



class Cuadrado(object):
	def __init__(self, centro_cuadrado, lado):
		self.centro_cuadrado = centro_cuadrado
		self.lado = float(lado)

	def obtener_area(self):
		return self.lado**2

	def obtener_perimtero(self):
		return self.lado*4

class Triangulo(object):
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c


	def es_equilatero(self):
		largo1 = ((float(self.a[0])-self.b[0])**2 + (self.a[1]-self.b[1])**2)**(1/2)
		largo2 = ((self.a[0]-self.c[0])**2 + (self.a[1]-self.c[1])**2)**(1/2)
		largo3 = ((self.b[0] - self.c[0]) ** 2 + (self.b[1] - self.c[1]) ** 2) ** (1 / 2)

		if largo1 == largo2 and largo2 == largo3:
			print("Es equilatero")
		else:
			print("No es equilatero")
if __name__ == '__main__':
	c = Cuadrado((0,0),2)
	print(c.obtener_area(), c.obtener_perimtero())

	t = Triangulo((-1,2),(-1-2),(3,-2))
	t.es_equilatero()



