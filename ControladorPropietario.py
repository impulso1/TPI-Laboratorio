from Modelo.Propietario import Propietario

class ControladorPropietario:
	def __init__(self):
		self.listaPropietarios = []
	
	#cargador de la lista
	def cargarArchivoPropietario(self):
		with open("Datos/Propietarios.txt","r") as file:
			renglones = file.readlines()
		for renglon in renglones:
			nombre, apellido, telefono, mail = renglon.strip().split(",")
			self.listaPropietarios.append(Propietario(nombre, apellido, telefono, mail))
	
	#crea nuevos propietarios
	def nuevoPropietario(self,nombre,apellido,telefono,mail):
		self.listaPropietarios.append(Propietario(nombre, apellido, telefono, mail))
	
	#mosdifica propietarios existentes
	def modificarPropietario(self, vet, opc, new):
		obj = self.buscarObjeto(vet)
		if (opc == 1):
			obj.nombre = new
		elif (opc == 2):
			obj.apellido = new
		elif (opc == 3):
			obj.telefono = new
		elif (opc == 4):
			obj.mail = new
	
	#busca un propietario de la lista
	def buscarObjeto(self,cod):
		cont = 0
		for i in self.listaPropietarios:
			cont = cont + 1
			if cont == int(cod):
				return i
	
	#agrega mascotas a un propietario
	def agregarMascota(self,propietario,mascota):
		if mascota not in propietario.mascotas:
			propietario.mascotas.append(mascota)
