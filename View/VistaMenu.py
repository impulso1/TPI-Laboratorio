class VistaMenu:
	
	def mostrarMenu(self):
		print("\nMain Menu:\n")
		print(f"[1] - Mostrar lista de Veterinarios.\n[2] - Mostrar lista de Propietarios.\n[3] - Registrar nuevo Veterinario.\n[4] - Registrar nuevo Cliente.\n[5] - Modificar Veterinario.\n[6] - Modificar Cliente.\n[7] - Eliminar Veterinario.\n[8] - Eliminar Propietario.\n[9] - Asignar una Mascota a un Cliente.\n[10] - Mostrar cantidad de mascotas de un Cliente.\n[0] - Salir.\n")
		op = input("Seleccione una de las opciones.\n")
		return op
	
	def mensajeError(self):
		print("Ingrese una de las opciones listadas.")
		
	# este getCodigo se puede borrar cuando vistaMascota con su propio getCodigo o similar se agrege, ahora lo saco y se me rompe el codigo
	def getCodigo(self,lista):
		cont = 0
		for i in lista:
			cont = cont + 1
			print(f"[{cont}] - {i}")
		cod = input("seleccione al Propietario correspondiente.\n")
		return cod
