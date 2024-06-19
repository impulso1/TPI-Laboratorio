from Controller.ControladorMascota import ControladorMascota
from Controller.ControladorRaza import ControladorRaza
from Controller.ControladorPropietario import ControladorPropietario
from Controller.ControladorVeterinario import ControladorVeterinario
from Controller.ControladorVacuna import ControladorVacuna
from Controller.ControladorDiagnostico import ControladorDiagnostico
from Controller.ControladorTratamiento import ControladorTratamiento
from Controller.ControladorConsulta import ControladorConsulta
from View.VistaGeneral import VistaGeneral
from View.VistaMascota import VistaMascota
from View.VistaRaza import VistaRaza
from View.VistaPropietario import VistaPropietarios
from View.VistaVeterinario import VistaVeterinarios
from View.VistaVacunas import VistaVacunas
from View.VistaDiagnostico import VistaDiagnostico
from View.VistaTratamiento import VistaTratamiento
from View.VistaConsulta import VistaConsulta


class ControladorGeneral:
    def __init__(self):
        self.controlador_mascota = ControladorMascota()
        self.controlador_raza = ControladorRaza()
        self.controlador_propietario = ControladorPropietario()
        self.controlador_veterinario = ControladorVeterinario()
        self.controlador_vacuna = ControladorVacuna()
        self.controlador_diagnostico = ControladorDiagnostico()
        self.controlador_tratamiento = ControladorTratamiento()
        self.controlador_consulta = ControladorConsulta()

    def abrir_vista_consulta(self, master):
        vista_consulta = VistaConsulta(master=master, controlador_consulta=self.controlador_consulta)
        vista_consulta.mainloop()

    def aceptar_accion(self, vista):
        if vista.selected_option.get() == "Mascotas (Activas)":
            mascotas = self.controlador_mascota.mostrar_mascotas()
            if mascotas:
                self.mostrar_vista_mascota(mascotas)
        elif vista.selected_option.get() == "Razas":
            razas = self.controlador_raza.mostrar_razas()
            if razas:
                self.mostrar_vista_raza(razas)
        elif vista.selected_option.get() == "Clientes (Propietarios)":
            propietarios = self.controlador_propietario.obtener_nombres_propietarios()
            if propietarios:
                self.mostrar_vista_propietarios(propietarios)
        elif vista.selected_option.get() == "Veterinarios":
            veterinarios = self.controlador_veterinario.mostrar_veterinarios()
            if veterinarios:
                self.mostrar_vista_veterinarios(veterinarios)
        elif vista.selected_option.get() == "Vacunas":
            vacunas = self.controlador_vacuna.mostrar_vacunas()
            if vacunas:
                self.mostrar_vista_vacunas(vacunas)
        elif vista.selected_option.get() == "Diagnosticos":
            diagnosticos = self.controlador_diagnostico.mostrar_diagnosticos()
            if diagnosticos:
                self.mostrar_vista_diagnosticos(diagnosticos)
        elif vista.selected_option.get() == "Tratamientos":
            tratamientos = self.controlador_tratamiento.mostrar_tratamientos()
            if tratamientos:
                self.mostrar_vista_tratamientos(tratamientos)

    def mostrar_mascotas(self):
        return self.controlador_mascota.mostrar_mascotas()

    def eliminar_mascota(self):
        return self.eliminar_mascota()

    def iniciar(self, root):
        self.controlador_consulta.cargar_consultas()
        self.controlador_mascota.cargar_archivo_mascotas()
        self.controlador_raza.cargar_archivo_razas()
        self.controlador_propietario.cargar_archivo_propietarios()
        self.controlador_veterinario.cargar_archivo_veterinarios()
        self.controlador_vacuna.cargar_archivo_vacunas()
        self.controlador_diagnostico.cargar_archivo_diagnosticos()
        self.controlador_tratamiento.cargar_archivo_tratamiento()
        vista_general = VistaGeneral(master=root, controlador_general=self)
        vista_general.mainloop()

    def mostrar_vista_mascota(self, mascotas):
        vista_mascota = VistaMascota(mascotas, self.controlador_mascota, self.controlador_raza,
                                     self.controlador_propietario)
        vista_mascota.mainloop()

    def mostrar_vista_raza(self, razas):
        vista_raza = VistaRaza(razas, self.controlador_raza)
        vista_raza.mainloop()

    def mostrar_vista_propietarios(self, propietarios):
        vista_propietarios = VistaPropietarios(propietarios, self.controlador_propietario)
        vista_propietarios.mainloop()

    def mostrar_vista_veterinarios(self, veterinarios):
        vista_veterinarios = VistaVeterinarios(veterinarios, self.controlador_veterinario)
        vista_veterinarios.mainloop()

    def mostrar_vista_vacunas(self, vacunas):
        vista_vacunas = VistaVacunas(vacunas, self.controlador_vacuna)
        vista_vacunas.mainloop()

    def mostrar_vista_diagnosticos(self, diagnosticos):
        vista_diagnostico = VistaDiagnostico(diagnosticos, self.controlador_diagnostico)
        vista_diagnostico.mainloop()

    def mostrar_vista_tratamientos(self, tratamiento):
        vista_tratamiento = VistaTratamiento(tratamiento, self.controlador_tratamiento)
        vista_tratamiento.mainloop()
