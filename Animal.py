#Giordano Ivan hizo esta clase
class Raza: 
    def __init__(self,nombre_raza,tamaño,cuidado,enfermedades,especie):
        #enfermedades: Enfermedades mas comunes
        self.nombre_raza=nombre_raza
        self.tamaño=tamaño
        self.cuidado=cuidado
        self.enfermedades=enfermedades
        self.especie=especie
        
class Mascota: #Asocia dueño
    def __init__ (self,nombre_pila,peso,edad,genero,color,raza):
        self.nombre_pila=nombre_pila
        self.peso=peso
        self.edad=edad
        self.genero=genero
        self.color=color
        self.raza=raza