from Model.Tratamiento import Tratamiento
from Controller.ControladorDiagnostico import ControladorDiagnostico

class ControladorTratamiento:
    def __init__(self):
        self.diagnostico = ControladorDiagnostico()
        self.listaTratamientos = []

    def cargar_archivo_tratamiento(self):
        self.diagnostico.cargar_archivo_diagnosticos()
        with open("Resources/Tratamientos.txt", "r") as file:
            renglones = file.readlines()
        for renglon in renglones:
            nombrediagnostico, descripcion, duracion, indicaciones = renglon.strip().split("|")
            diagnostico = self.diagnostico.buscar_diagnosticoxnombre(nombrediagnostico.lower())
            if diagnostico:
                tratamiento = Tratamiento(diagnostico, descripcion, duracion, indicaciones)
                self.listaTratamientos.append(tratamiento)
                diagnostico.tratamientos.append(tratamiento)  # Actualizar el atributo tratamientos
            else:
                print(f"No se encontró el diagnóstico con nombre {nombrediagnostico}")

    def nuevo_tratamiento(self, nombrediagnostico, descripcion, duracion, indicaciones):
        diagnostico = self.diagnostico.buscar_diagnosticoxnombre(nombrediagnostico.lower())
        if diagnostico:
            tratamiento = Tratamiento(diagnostico, descripcion, duracion, indicaciones)
            self.listaTratamientos.append(tratamiento)
            diagnostico.tratamientos.append(tratamiento)

    def modificar_tratamiento(self, cod, descripcion, duracion, indicaciones):
        tratamiento = self.buscar_objeto(cod)
        if tratamiento:
            tratamiento.descripcion = descripcion
            tratamiento.duracion = duracion
            tratamiento.indicaciones = indicaciones

    def buscar_objeto(self, cod):
        for i, tratamiento in enumerate(self.listaTratamientos, start=1):
            if i == int(cod):
                return tratamiento

    def mostrar_tratamientos(self):
        return self.listaTratamientos

    def guardar_archivo_tratamientos(self):
        with open("Resources/Tratamientos.txt", "w") as file:
            for tratamiento in self.listaTratamientos:
                nombrediagnostico = tratamiento.diagnostico.nombre if tratamiento.diagnostico else ''
                file.write(f"{nombrediagnostico}|{tratamiento.descripcion}|{tratamiento.duracion}|{tratamiento.indicaciones}\n")

    def eliminar_tratamiento(self, tratamiento):
        if tratamiento in self.listaTratamientos:
            self.listaTratamientos.remove(tratamiento)
            tratamiento.diagnostico.tratamientos.remove(tratamiento)  # Asegurarse de que este atributo exista en Diagnostico
            self.guardar_archivo_tratamientos()
            return True
        return False

    def buscar_tratamientoxnombre(self, nombretratamiento):
        for tratamiento in self.listaTratamientos:
            if tratamiento.descripcion.lower() == nombretratamiento.lower():
                return tratamiento

    def mostrar_descripcion_por_diagnostico(self, diagnostico):
        return [tratamiento.descripcion for tratamiento in self.listaTratamientos if tratamiento.diagnostico == diagnostico]

    def obtener_lista_nombres_diagnosticos(self):
        return [diagnostico.nombre for diagnostico in self.diagnostico.listaDiagnosticos]

    def buscar_tratamiento_por_diagnostico(self, diagnostico):
        tratamientos_relacionados = []
        for tratamiento in self.listaTratamientos:
            if tratamiento.diagnostico.nombre.lower() == diagnostico.lower():
                tratamientos_relacionados.append(tratamiento.descripcion)
        return tratamientos_relacionados

    def buscar_descripcion(self, tratamiento_nombre):
        for tratamiento in self.listaTratamientos:
            if tratamiento.diagnostico == tratamiento_nombre:
                return (f"Descripción: {tratamiento.descripcion}\n"
                        f"Duracion: {tratamiento.duracion}\n"
                        f"Indicaciones: {tratamiento.indicaciones}")
        return "Descripción no encontrada."
