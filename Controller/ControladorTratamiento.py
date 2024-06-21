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
                self.listaTratamientos.append(Tratamiento(diagnostico, descripcion, duracion, indicaciones))
            else:
                print(f"No se encontró el diagnostico con nombre {diagnostico}")

    def nuevo_tratamiento(self, nombrediagnostico, descripcion, duracion, indicaciones):
        diagnostico = self.diagnostico.buscar_diagnosticoxnombre(nombrediagnostico.lower())
        if diagnostico:
            tratamiento = Tratamiento(diagnostico, descripcion, duracion, indicaciones)
            self.listaTratamientos.append(tratamiento)
        else:
            pass

    def actualizar_mascota(self, cod, nombrediagnostico, descripcion, duracion, indicaciones):
        diagnostico = self.diagnostico.buscar_diagnosticoxnombre(nombrediagnostico.lower())
        if diagnostico:
            self.listaTratamientos[cod - 1] = Tratamiento(diagnostico, descripcion, duracion, indicaciones)
            self.guardar_archivo_tratamientos()

    def modificar_tratamiento(self, cod, nombrediagnostico, descripcion, duracion, indicaciones):
        tratamiento = self.buscar_objeto(cod)
        if tratamiento:
            diagnostico = self.diagnostico.buscar_diagnosticoxnombre(nombrediagnostico.lower())
            if diagnostico:
                tratamiento.diagnostico = diagnostico
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
            for tramiento in self.listaTratamientos:
                nombrediagnostico = tramiento.diagnostico.nombre if tramiento.diagnostico else ''
                file.write(
                    f"{nombrediagnostico}|{tramiento.descripcion}|{tramiento.duracion}|{tramiento.indicaciones}\n")


    def eliminar_tratamiento(self, tratamiento):
        if tratamiento in self.listaTratamientos:
            self.listaTratamientos.remove(tratamiento)
            self.guardar_archivo_tratamientos()
            return True
        return False

    def buscar_tratamientoxnombre(self, nombretratamiento):
        for tratamiento in self.listaTratamientos:
            if tratamiento.nombre.lower() == nombretratamiento.lower():
                return tratamiento

    def mostrar_decripciondexdiagnostico(self, diagnostico):
        for tratamiento in self.listaTratamientos:
            if tratamiento.diagnostico == diagnostico:
                return tratamiento.descripcion


    def obtener_lista_nombres_diagnosticos(self):
        return [diagnostico.nombre for diagnostico in self.diagnostico.listaDiagnosticos]

    def buscar_tratamiento_por_diagnostico(self, diagnostico):
        for tratamiento in self.listaTratamientos:
            if tratamiento.diagnostico.nombre == diagnostico:
                return tratamiento
        return None