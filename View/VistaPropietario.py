class VistaPropietario:
	
	def mostrarLista(self,lista):
		for i in lista:
			print(i)
	
	def getCodigo(self,lista):
		cont = 0
		for i in lista:
			cont = cont + 1
			print(f"[{cont}] - {i}")
		cod = input("seleccione al Propietario correspondiente.\n")
		return cod
	
	def registrarPropietario(self):
		nombre = input("ingrese el nombre del nuevo Propietario\n")
		apellido = input("ingrese el apellido del nuevo Propietario\n")
		telefono = input("ingrese el telefono del nuevo Propietario\n")
		mail = input("ingrese el mail del nuevo Propietario\n")
		return nombre, apellido, telefono, mail
	
	def datoAModificarPropietario(self):
		opc = input("¿Qué desea modificar?\n[1] - nombre.\n[2] - apellido.\n[3] - telefono.\n[4] - mail.\n[5] - cancelar.\n")
		return opc
	
	def nuevoDato(self):
		new = input("ingrese la nueva informacion del Propietario.\n")
		return new