from Controller.ControladorDiagnostico import ControladorDiagnostico
from Controller.ControladorTratamiento import ControladorTratamiento
from Controller.ControladorVeterinario import ControladorVeterinario
from Controller.ControladorVacuna import ControladorVacuna
from Model.Consulta import Consulta


class ControladorConsulta:
    def __init__(self):
        self.diagnosticos = ControladorDiagnostico()
        self.tratamientos = ControladorTratamiento()
        self.veterinarios = ControladorVeterinario()
        self.vacunas = ControladorVacuna()
        self.listaConsultas = []

    def agregar_consulta(self, consulta):
        self.listaConsultas.append(consulta)

    def eliminar_consulta(self, consulta):
        if consulta in self.listaConsultas:
            self.listaConsultas.remove(consulta)

    def mostrar_consultas(self):
        return self.listaConsultas

    def cargar_consultas(self):
        self.veterinarios.cargar_archivo_veterinarios()
        self.diagnosticos.cargar_archivo_diagnosticos()
        self.tratamientos.cargar_archivo_tratamiento()
        self.vacunas.cargar_archivo_vacunas()
        with open("Resources/Consultas.txt", "r") as file:
            renglones = file.readlines()
        for renglon in renglones:
            valores = renglon.strip().split("|")
            if len(valores) == 6:
                fecha, nombreveterinario, nombrediagnostico, nombretratamiento, nombrevacunas, observaciones = valores
                veterinario = self.veterinarios.buscar_veterinarioxnombre(nombreveterinario.lower())
                diagnostico = self.diagnosticos.buscar_diagnosticoxnombre(nombrediagnostico.lower())
                tratamiento = self.tratamientos.buscar_tratamientoxnombre(nombretratamiento.lower())
                vacuna = self.vacunas.buscar_vacunaxnombre(nombrevacunas.lower())
                if veterinario and diagnostico and tratamiento:
                    self.listaConsultas.append(
                        Consulta(fecha, veterinario, diagnostico, tratamiento, vacuna, observaciones))
                else:
                    print(f"No se pudo vincular alguno de los datos.")

    def obtener_nombres_veterinarios(self):
        return [f"{vet.nombre} {vet.apellido}" for vet in self.veterinarios.mostrar_veterinarios()]

    def obtener_descripcion_tratamientos(self):
        return [f"{trat.descripcion}" for trat in self.tratamientos.mostrar_decripciondexdiagnostico()]

    def obtener_nombres_diagnosticos(self):
        return [f"{diag.nombre}" for diag in self.diagnosticos.mostrar_diagnosticos()]

    def obtener_nombres_vacunas(self):
        return [vac.nombre for vac in self.vacunas.mostrar_vacunas()]

    def guardar_consulta(self, veterinario, diagnostico, tratamiento, vacunas, observaciones):
       pass