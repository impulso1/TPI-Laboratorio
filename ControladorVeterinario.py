from Modelo.Veterinario import Veterinario

class ControladorVeterinario:
	def __init__(self):
		self.listaVeterinarios = []
	
	#carga la lista de veterinarios
	def cargarArchivoVeterinario(self):
		with open("Datos/Veterinarios.txt","r") as file:
			renglones = file.readlines()
		for renglon in renglones:
			nombre, apellido, telefono, mail, cuil = renglon.strip().split(",")
			self.listaVeterinarios.append(Veterinario(nombre, apellido, telefono, mail, cuil))
	
	#crea un nuevo veterinario
	def nuevoVeterinario(self,nombre,apellido,telefono,mail,cuil):
		self.listaVeterinarios.append(Veterinario(nombre, apellido, telefono, mail, cuil))
	
	#modifica un veterinario existente
	def modificarVeterinario(self, vet, opc, new):
		obj = self.buscarObjeto(vet)
		if (opc == 1):
			obj.nombre = new
		elif (opc == 2):
			obj.apellido = new
		elif (opc == 3):
			obj.telefono = new
		elif (opc == 4):
			obj.mail = new
		elif (opc == 5):
			obj.cuil = new
	
	#busca un Veterianrio de la lista
	def buscarObjeto(self,cod):
		cont = 0
		for i in self.listaVeterinarios:
			cont = cont + 1
			if cont == int(cod):
				return i