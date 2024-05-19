#Emgert Abdul y Rodriguez Alexis hicieron estas clases.
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
