#Comba Misael y Rosales Christian hicieron estas clases

class Persona:
    def __init__(self,nombre_persona,apellido,dni,telefono,direccion):
        self.nombre_persona=nombre_persona
        self.apellido=apellido
        self.dni=dni
        self.telefono=telefono
        self.direccion=direccion
        
class Veterinario(Persona):
    def __init__(self,matricula,nombre_persona, apellido, dni, telefono, direccion):
        super().__init__(nombre_persona, apellido, dni, telefono, direccion)
        self.matricula=matricula
        
class Duenio(Persona):#asocia mascota
    def __init__(self, nombre_persona, apellido, dni, telefono, direccion):
        super().__init__(nombre_persona, apellido, dni, telefono, direccion)