from Model.Persona import Persona


class Veterinario(Persona):
    def __init__(self, nombre, apellido, telefono, mail, matricula):
        super().__init__(nombre, apellido, telefono, mail)
        self.matricula = matricula

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.telefono} - {self.mail} - {self.matricula}"

    def __repr__(self):
        return f"{self.nombre} - {self.apellido} - {self.telefono} - {self.mail} - {self.matricula}"
