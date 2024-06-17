class VistaVeterinario:
	
	def mostrarLista(self,lista):
		for i in lista:
			print(i)
	
	def getCodigo(self,lista):
		cont = 0
		for i in lista:
			cont = cont + 1
			print(f"[{cont}] - {i}")
		cod = input("seleccione Al Veterinario correspondiente.\n")
		return cod
	
	def registrarVeterinario(self):
		nombre = input("ingrese el nombre del nuevo Veterinario\n")
		apellido = input("ingrese el apellido del nuevo Veterinario\n")
		telefono = input("ingrese el telefono del nuevo Veterinario\n")
		mail = input("ingrese el mail del nuevo Veterinario\n")
		cuil = input("ingrese el cuil del nuevo Veterinario\n")
		return nombre, apellido, telefono, mail, cuil
	
	def datoAModificarVeterinario(self):
		opc = input("¿Qué desea modificar?\n[1] - nombre.\n[2] - apellido.\n[3] - telefono.\n[4] - mail.\n[5] - cuil.\n[6] - cancelar.\n")
		return opc
		
	def nuevoDato(self):
		new = input("ingrese la nueva informacion del Veterinario.\n")
		return new