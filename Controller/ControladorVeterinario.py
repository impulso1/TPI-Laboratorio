from Model.Veterinario import Veterinario


class ControladorVeterinario:

    def __init__(self):
        self.listaVeterinarios = []

    def cargar_archivo_veterinarios(self):
        with open("Resources/Veterinarios.txt", "r") as file:
            renglones = file.readlines()
        for renglon in renglones:
            nombre, apellido, telefono, mail, matricula = renglon.strip().split(",")
            self.listaVeterinarios.append(Veterinario(nombre, apellido, telefono, mail, matricula))

    def nuevo_veterinario(self, nombre, apellido, telefono, mail, matricula):
        self.listaVeterinarios.append(Veterinario(nombre, apellido, telefono, mail, matricula))

    def modificar_veterinario(self, vet, opc, new):
        obj = self.buscar_objeto(vet)
        if opc == 1:
            obj.nombre = new
        elif opc == 2:
            obj.apellido = new
        elif opc == 3:
            obj.telefono = new
        elif opc == 4:
            obj.mail = new
        elif opc == 5:
            obj.cuil = new

    def buscar_objeto(self, cod):
        for i, veterinario in enumerate(self.listaVeterinarios, start=1):
            if i == int(cod):
                return veterinario

    def mostrar_veterinarios(self):
        return self.listaVeterinarios

    def guardar_archivo_veterinarios(self):
        with open("Resources/Veterinarios.txt", "w") as file:
            for veterinario in self.listaVeterinarios:
                file.write(
                    f"{veterinario.nombre},{veterinario.apellido},{veterinario.telefono},{veterinario.mail},{veterinario.matricula}\n")

    def buscar_veterinarioxnombre(self, nombreveterinario):
        for veterinario in self.listaVeterinarios:
            if veterinario.nombre.lower() == nombreveterinario.lower():
                return veterinario