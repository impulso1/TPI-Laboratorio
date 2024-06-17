from Vista.VistaMenu import VistaMenu
from Vista.VistaVeterinario import VistaVeterinario
from Vista.VistaPropietario import VistaPropietario
from Controlador.ControladorVeterinario import ControladorVeterinario
from Controlador.ControladorPropietario import ControladorPropietario
from Controlador.ControladorMascota import ControladorMascota

class ControladorGeneral:
	def __init__(self):
		self.vista = VistaMenu()
		self.vistaVeterinario = VistaVeterinario()
		self.vistaPropietario = VistaPropietario()
		self.controladorVeterinario = ControladorVeterinario()
		self.controladorPropietario = ControladorPropietario()
		self.controladorMascota = ControladorMascota()
		
	def mostrarMenu(self):
		while True:
			op = self.vista.mostrarMenu()
			if (op == "1"):
				self.vistaVeterinario.mostrarLista(self.controladorVeterinario.listaVeterinarios)
			elif (op == "2"):
				self.vistaPropietario.mostrarLista(self.controladorPropietario.listaPropietarios)
			elif (op == "3"):
				nom, ape, tel, mail, cuil = self.vistaVeterinario.registrarVeterinario()
				self.controladorVeterinario.nuevoVeterinario(nom, ape, tel, mail, cuil)
			elif (op == "4"):
				nom, ape, tel, mail = self.vistaPropietario.registrarPropietario()
				self.controladorPropietario.nuevoPropietario(nom, ape, tel, mail)
			elif (op == "5"):
				while True:
					try:
						vet = int(self.vistaVeterinario.getCodigo(self.controladorVeterinario.listaVeterinarios))
					except ValueError:
						self.vista.mensajeError()
					else: 
						if (0 < vet < (len(self.controladorVeterinario.listaVeterinarios)+1)):
							break
				while True:
					try:
						opc = int(self.vistaVeterinario.datoAModificarVeterinario())
					except ValueError:
						self.vista.mensajeError()
					else:
						if (0 < opc < 7):
							break
				if (0 < opc < 6):
					new = self.vistaVeterinario.nuevoDato()
					self.controladorVeterinario.modificarVeterinario(vet, opc, new)
			elif (op == "6"):
				while True:
					try:
						vet = int(self.vistaPropietario.getCodigo(self.controladorPropietario.listaPropietarios))
					except ValueError:
						self.vista.mensajeError()
					else: 
						if (0 < vet < (len(self.controladorPropietario.listaPropietarios)+1)):
							break
				while True:
					try:
						opc = int(self.vistaPropietario.datoAModificarPropietario())
					except ValueError:
						self.vista.mensajeError()
					else:
						if (0 < opc < 6):
							break
				if (0 < opc < 5):
					new = self.vistaPropietario.nuevoDato()
					self.controladorPropietario.modificarPropietario(vet, opc, new)
			elif (op == "7"):
				while True:
					try:
						vet = int(self.vistaVeterinario.getCodigo(self.controladorVeterinario.listaVeterinarios))
					except ValueError:
						self.vista.mensajeError()
					else: 
						if (0 < vet < (len(self.controladorVeterinario.listaVeterinarios)+1)):
							break
				obVet = self.controladorVeterinario.buscarObjeto(vet)
				self.controladorVeterinario.listaVeterinarios.remove(obVet)
			elif (op == "8"):
				while True:
					try:
						prop = int(self.vistaPropietario.getCodigo(self.controladorPropietario.listaPropietarios))
					except ValueError:
						self.vista.mensajeError()
					else: 
						if (0 < prop < (len(self.controladorPropietario.listaPropietarios)+1)):
							break
				obProp = self.controladorPropietario.buscarObjeto(prop)
				self.controladorPropietario.listaPropietarios.remove(obProp)
			elif (op == "9"):
				while True:
					try:
						masc = int(self.vista.getCodigo(self.controladorMascota.listaMascotas))
					except ValueError:
						self.vista.mensajeError()
					else: 
						if (0 < masc < (len(self.controladorMascota.listaMascotas)+1)):
							break
				obMasc = self.controladorMascota.buscarObjeto(masc)
				while True:
					try:
						prop = int(self.vistaPropietario.getCodigo(self.controladorPropietario.listaPropietarios))
					except ValueError:
						self.vista.mensajeError()
					else: 
						if (0 < prop < (len(self.controladorPropietario.listaPropietarios)+1)):
							break
				obProp = self.controladorPropietario.buscarObjeto(prop)
				self.controladorPropietario.agregarMascota(obProp,obMasc)
			elif (op == "10"):
				while True:
					try:
						prop = int(self.vistaPropietario.getCodigo(self.controladorPropietario.listaPropietarios))
					except ValueError:
						self.vista.mensajeError()
					else: 
						if (0 < prop < (len(self.controladorPropietario.listaPropietarios)+1)):
							break
				obProp = self.controladorPropietario.buscarObjeto(prop)
				self.vistaPropietario.mostrarLista(obProp.mascotas)
			elif (op == "0"):
				break
			else:
				self.vista.mensajeError()
	
	def iniciar(self):
		self.controladorVeterinario.cargarArchivoVeterinario()
		self.controladorPropietario.cargarArchivoPropietario()
		self.controladorMascota.cargarArchivoMascotas()
	