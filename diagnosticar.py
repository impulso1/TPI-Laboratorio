
from TPI.model.tratamiento import Tratamiento
from TPI.model.diagnostico import Diagnostico

class DiagnosticoController:
    def __init__(self):
        self.diagnosticos = []

    def agregar_diagnostico(self, nombre, sintomas, descripcion_tratamiento, costo_tratamiento, duracion_tratamiento, indicaciones_tratamiento, observaciones):
        tratamiento = Tratamiento(descripcion_tratamiento, costo_tratamiento, duracion_tratamiento, indicaciones_tratamiento)
        nuevo_diagnostico = Diagnostico(nombre, sintomas, tratamiento, observaciones)
        self.diagnosticos.append(nuevo_diagnostico)
        return nuevo_diagnostico

    def obtener_diagnostico(self, indice):
        if 0 <= indice < len(self.diagnosticos):
            return self.diagnosticos[indice]
        else:
            raise IndexError("Índice de diagnóstico no válido")

    def actualizar_diagnostico(self, indice, nombre=None, sintomas=None, descripcion_tratamiento=None, costo_tratamiento=None, duracion_tratamiento=None, indicaciones_tratamiento=None, observaciones=None):
        diagnostico = self.obtener_diagnostico(indice)
        if nombre is not None:
            diagnostico.set_nombre(nombre)
        if sintomas is not None:
            diagnostico.set_sintomas(sintomas)
        if descripcion_tratamiento is not None or costo_tratamiento is not None or duracion_tratamiento is not None or indicaciones_tratamiento is not None:
            tratamiento = diagnostico.get_tratamiento()
            if descripcion_tratamiento is not None:
                tratamiento.descripcion = descripcion_tratamiento
            if costo_tratamiento is not None:
                tratamiento.costo = costo_tratamiento
            if duracion_tratamiento is not None:
                tratamiento.duracion = duracion_tratamiento
            if indicaciones_tratamiento is not None:
                tratamiento.indicaciones = indicaciones_tratamiento
        if observaciones is not None:
            diagnostico.set_observaciones(observaciones)
        return diagnostico

    def eliminar_diagnostico(self, indice):
        if 0 <= indice < len(self.diagnosticos):
            return self.diagnosticos.pop(indice)
        else:
            raise IndexError("Índice de diagnóstico no válido")
