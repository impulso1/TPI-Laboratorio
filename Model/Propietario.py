from Model.Persona import Persona

class Propietario(Persona):
	def __init__(self, nombre, apellido, telefono, mail):
		super().__init__(nombre, apellido, telefono, mail)
		self.mascotas = []

	def __str__(self):
		return f"{self.nombre} - {self.apellido} - {self.telefono} - {self.mail}"

	def __repr__(self):
		return self.nombre

	def agregar_mascota(self, mascota):
		if mascota not in self.mascotas:
			self.mascotas.append(mascota)

	def eliminar_mascota(self, mascota):
		if mascota in self.mascotas:
			self.mascotas.remove(mascota)

	def mostrar_mascotas(self):
		for mascota in self.mascotas:
			print(mascota)