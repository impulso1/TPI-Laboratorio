from Modelo.Mascota import Mascota

class ControladorMascota:
	def __init__(self):
		self.listaMascotas = []
	
	def cargarArchivoMascotas(self):
		with open("Datos/Mascotas.txt","r") as file:
			renglones = file.readlines()
		for renglon in renglones:
			raza, nombre = renglon.strip().split(",")
			self.listaMascotas.append(Mascota(raza, nombre))
	
	def buscarObjeto(self,cod):
		cont = 0
		for i in self.listaMascotas:
			cont = cont + 1
			if cont == int(cod):
				return i
	
	# este es un borrador del controlador mascota, para poder provar la relacion Propietario mascota, borrar cuando se adjunte el verdader ControladorMascota.