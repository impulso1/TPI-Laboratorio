from Ficha_Medica_modelo import *
from Vacuna_modelo import *

class ControladorFichaMedica:
    def __init__(self, ficha_medica, vista):
        self.ficha_medica = ficha_medica
        self.vista = vista

    def agregar_detalle(self):
        detalle = self.vista.obtener_detalle()
        self.ficha_medica.agregar_detalle(detalle)
        self.vista.mostrar_ficha_medica(self.ficha_medica)
    
    def eliminar_detalle(self):
        self.vista.mostrar_ficha_medica(self.ficha_medica)
        indice = self.vista.seleccionar_indice()
        self.ficha_medica.eliminar_detalle(indice)
        self.vista.mostrar_ficha_medica(self.ficha_medica)
    
    def editar_detalle(self):
        self.vista.mostrar_ficha_medica(self.ficha_medica)
        indice = self.vista.seleccionar_indice()
        nuevo_detalle = self.vista.obtener_detalle()
        self.ficha_medica.editar_detalle(indice, nuevo_detalle)
        self.vista.mostrar_ficha_medica(self.ficha_medica)
