from Modelo.Persona import Persona

class Propietario(Persona):
	def __init__(self,nombre, apellido, telefono, mail):
		super().__init__(nombre, apellido, telefono, mail)
		self.mascotas = []
	
	def __str__(self):
		return self.nombre+" "+self.apellido
		
	def __repr__(self):
		return self.nombre
	# Hereda de persona y Puede tener 0...* mascotas