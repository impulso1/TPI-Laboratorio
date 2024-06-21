from Controller.ControladorDiagnostico import ControladorDiagnostico
from Controller.ControladorTratamiento import ControladorTratamiento
from Controller.ControladorVeterinario import ControladorVeterinario
from Controller.ControladorVacuna import ControladorVacuna
from Controller.ControladorMascota import ControladorMascota
from Model.Consulta import Consulta
from datetime import datetime


class ControladorConsulta:
    def __init__(self):
        self.diagnosticos = ControladorDiagnostico()
        self.tratamientos = ControladorTratamiento()
        self.veterinarios = ControladorVeterinario()
        self.vacunas = ControladorVacuna()
        self.mascotas = ControladorMascota()
        self.listaConsultas = []

    def eliminar_consulta(self, consulta):
        if consulta in self.listaConsultas:
            self.listaConsultas.remove(consulta)

    def mostrar_consultas(self):
        return self.listaConsultas

    def cargar_consultas(self):
        self.mascotas.cargar_archivo_mascotas()
        self.veterinarios.cargar_archivo_veterinarios()
        self.diagnosticos.cargar_archivo_diagnosticos()
        self.tratamientos.cargar_archivo_tratamiento()
        self.vacunas.cargar_archivo_vacunas()
        with open("Resources/Consultas.txt", "r") as file:
            renglones = file.readlines()
        for renglon in renglones:
            valores = renglon.strip().split("^")
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
        return [f"{trat.descripcion}" for trat in self.tratamientos.mostrar_tratamientos()]

    def obtener_nombres_diagnosticos(self):
        return [f"{diag.nombre}" for diag in self.diagnosticos.mostrar_diagnosticos()]

    def obtener_nombres_vacunas(self):
        return [vac.nombre for vac in self.vacunas.mostrar_vacunas()]

    def guardar_archivo_consultas(self):
        with open("Resources/Consultas.txt", "w") as file:
            for consulta in self.listaConsultas:
                file.write(f"{consulta.fecha}^{consulta.veterinario}^{consulta.diagnostico}^{consulta.tratamiento}^{','.join(consulta.vacunas)}^{consulta.observaciones}\n")

    def obtener_tratamiento_por_diagnostico(self, diagnostico):
        tratamiento = self.tratamientos.buscar_tratamiento_por_diagnostico(diagnostico)
        if tratamiento:
            return f"Descripción: {tratamiento.descripcion}\nDuración: {tratamiento.duracion}\nIndicaciones: {tratamiento.indicaciones}"
        else:
            return "No se encontró tratamiento para el diagnóstico seleccionado."

    def obtener_nombres_mascotas(self):
        return [mascota.nombre for mascota in self.mascotas.mostrar_mascotas()]

    def guardar_consulta(self, mascota, veterinario, diagnostico, tratamiento, vacunas, observaciones):
        fecha = datetime.now().strftime('%Y-%m-%d')
        consulta = Consulta(fecha, mascota, veterinario, diagnostico, tratamiento, vacunas, observaciones)
        self.agregar_consulta(consulta)
        self.guardar_archivo_consultas()

    def agregar_consulta(self, consulta):
        if isinstance(consulta, Consulta):
            self.listaConsultas.append(consulta)
        else:
            raise TypeError("Se esperaba una instancia de Consulta.")

    def obtener_dueno_por_mascota(self, nombre_mascota):
        for mascota in self.mascotas.mostrar_mascotas():
            if mascota.nombre == nombre_mascota:
                return mascota.propietario
        return None

    def obtener_matricula_por_veterinario(self, nombre_veterinario):
        for veterinario in self.veterinarios.mostrar_veterinarios():
            if f"{veterinario.nombre} {veterinario.apellido}" == nombre_veterinario:
                return veterinario.matricula
        return None

    def obtener_costo_vacuna(self, nombre_vacuna):
        vacuna = self.vacunas.buscar_vacunaxnombre(nombre_vacuna)
        if vacuna:
            return vacuna.costo
        return None