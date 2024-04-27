class Razas: 
    def __init__(self,nombre_raza,tamaño,cuidado,enfermedades,especie):
        #enfermedades: Enfermedades mas comunes
        self.nombre_raza=nombre_raza
        self.tamaño=tamaño
        self.cuidado=cuidado
        self.enfermedades=enfermedades
        self.especie=especie
        
class Mascota(Razas): #Asocia dueño
    def __init__ (self,nombre_pila,peso,edad,genero,color,nombre_raza,tamaño,cuidado,enfermedades,especie):
        super().__init__(nombre_raza,tamaño,cuidado,enfermedades,especie)
        self.nombre_pila=nombre_pila
        self.peso=peso
        self.edad=edad
        self.genero=genero
        self.color=color
        
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
        
class Vacunas:
    def __init__(self,nombre_vacuna,dosis,fecha_elaboracion,fecha_vencimiento,costo,fabricante,prospecto):
        self.nombre_vacuna=nombre_vacuna
        self.dosis=dosis
        self.fecha_elaboracion=fecha_elaboracion
        self.fecha_vencimiento=fecha_vencimiento
        self.costo=costo
        self.fabricante=fabricante
        self.prospecto=prospecto
        
class Diagnostico:#Asocio Veterinario
    def __init__(self,fecha,hora,sintomas,resultado):
        self.fecha=fecha
        self.hora=hora
        self.sintomas=sintomas
        self.resultado=resultado
        
class Tratamientos: #Asocia diagnostico y vacuna. #Instrucciones del tratamiento
    def __init__(self,duracion,medicamentos,instrucciones):
        self.duracion=duracion
        self.medicamentos=medicamentos
        self.instrucciones=instrucciones

class Ficha_medica:#asocia mascota, diagnostico, tratamientos
    def __init__(self) -> None:
        pass
    
class Dueño(Persona):#asocia mascota
    def __init__(self, nombre_persona, apellido, dni, telefono, direccion):
        super().__init__(nombre_persona, apellido, dni, telefono, direccion)