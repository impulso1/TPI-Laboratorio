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


    def obtener_nombres_veterinarios(self):
        return [f"{vet.nombre} {vet.apellido}" for vet in self.veterinarios.mostrar_veterinarios()]

    def obtener_descripcion_tratamientos(self, tratamiento):
        tratamiento_obj = self.tratamientos.buscar_tratamientoxnombre(tratamiento)
        if tratamiento_obj:
            descripcion = (
                f"Diagnóstico: {tratamiento_obj.diagnostico.nombre}\n"
                f"Descripción: {tratamiento_obj.descripcion}\n"
                f"Duración: {tratamiento_obj.duracion}\n"
                f"Indicaciones: {tratamiento_obj.indicaciones}"
            )
            return descripcion
        return "No se encontró el tratamiento."

    def obtener_nombres_diagnosticos(self):
        return [f"{diag.nombre}" for diag in self.diagnosticos.mostrar_diagnosticos()]

    def obtener_nombres_vacunas(self):
        return [vac.nombre for vac in self.vacunas.mostrar_vacunas()]


    def obtener_tratamiento_por_diagnostico(self, diagnostico):
        tratamiento = self.tratamientos.buscar_tratamientoxnombre(diagnostico)
        if tratamiento:
            return f"Descripción: {tratamiento.descripcion}\nDuración: {tratamiento.duracion}\nIndicaciones: {tratamiento.indicaciones}"
        else:
            return "No se encontró tratamiento para el diagnóstico seleccionado."

    def obtener_nombres_mascotas(self):
        return [mascota.nombre for mascota in self.mascotas.mostrar_mascotas()]


    def guardar_consulta(self, mascota, veterinario, diagnostico, tratamiento, vacunas, observaciones, costo_total):
        fecha = datetime.now().strftime('%Y-%m-%d')
        consulta = Consulta(fecha, mascota, veterinario, diagnostico, tratamiento, vacunas, observaciones)
        nombre_archivo = f"FichaMedica{consulta.mascota}.txt"
        with open(f"Resources/Mascotas/{nombre_archivo}", "a") as file:
            file.write(f"{'#' * 10}\n")
            file.write(f"Fecha: {consulta.fecha}\n")
            file.write(f"Mascota: {consulta.mascota}\n")
            file.write(f"Veterinario: {consulta.veterinario}\n")
            file.write(f"Diagnóstico: {consulta.diagnostico}\n")
            file.write(f"Tratamiento: {consulta.tratamiento}\n")
            file.write(f"Vacunas: {', '.join(consulta.vacunas)}\n")
            file.write(f"Observaciones: {consulta.observaciones}\n")

        with open("Resources/Facturas.txt", "a") as factura_file:
            factura_file.write(f"{'#' * 10}\n")
            factura_file.write(f"Veterinario: {veterinario}\n")
            factura_file.write(f"Cliente: {self.obtener_dueno_por_mascota(mascota)}\n")
            factura_file.write(f"Paciente: {mascota}\n")
            factura_file.write(f"Costo total: ${costo_total:.2f}\n")

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
                return f"M.N. {veterinario.matricula}"
        return None

    def obtener_costo_vacuna(self, nombre_vacuna):
        vacuna = self.vacunas.buscar_vacunaxnombre(nombre_vacuna)
        if vacuna:
            return vacuna.costo
        return None

