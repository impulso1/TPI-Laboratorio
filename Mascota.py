# esto no es la verdadera clase mascota, es un borrador para probar la funcion de agregar mascota a Propietario.

class Mascota:
	def __init__(self,raza,nombre):
		self.raza = raza
		self.nombre = nombre
	
	def __str__(self):
		return self.nombre+" "+self.raza
		
	def __repr__(self):
		return self.nombre
	