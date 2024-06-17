from Modelo.Persona import Persona

class Veterinario(Persona):
	def __init__(self,nombre, apellido, telefono, mail, cuil):
		super().__init__(nombre, apellido, telefono, mail)
		self.cuil = cuil
	
	def __str__(self):
		return self.nombre+" "+self.apellido
		
	def __repr__(self):
		return self.nombre
	
	# hereda de persona