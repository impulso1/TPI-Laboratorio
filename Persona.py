# esta clase no tiene ni controlador ni vista, es solo una clase padre para que hereden Propietario y Veterinario.

class Persona:
	def __init__(self,nombre, apellido, telefono, mail):
		self.nombre = nombre
		self.apellido = apellido
		self.telefono = telefono
		self.mail = mail
	
	def __str__(self):
		return self.nombre
		
	def __repr__(self):
		return self.nombre
	