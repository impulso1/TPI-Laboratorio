from Model.Diagnostico import Diagnostico


class ControladorDiagnostico:
    def __init__(self):
        self.listaDiagnosticos = []

    def cargar_archivo_diagnosticos(self):
        with open("Resources/Diagnosticos.txt", "r") as file:
            renglones = file.readlines()
        for renglon in renglones:
            nombre, sintomas, observaciones = renglon.strip().split("|")
            self.listaDiagnosticos.append(Diagnostico(nombre, sintomas, [], observaciones))

    def nuevo_diagnostico(self, nombre, sintomas, observaciones):
        self.listaDiagnosticos.append(Diagnostico(nombre, sintomas, [], observaciones))
        self.guardar_archivo_diagnosticos()

    def modificar_diagnostico(self, diag, opc, new):
        obj = self.buscar_objeto(diag)
        if opc == 1:
            obj.nombre = new
        elif opc == 2:
            obj.sintomas = new
        elif opc == 3:
            obj.tratamientos = new  # Actualizar el atributo tratamientos
        elif opc == 4:
            obj.observaciones = new


    def mostrar_diagnosticos(self):
        return self.listaDiagnosticos

    def guardar_archivo_diagnosticos(self):
        with open("Resources/Diagnosticos.txt", "w") as file:
            for diagnostico in self.listaDiagnosticos:
                file.write(f"{diagnostico.nombre}|{diagnostico.sintomas}|{diagnostico.observaciones}\n")

    def eliminar_diagnostico(self, diagnostico):
        if diagnostico in self.listaDiagnosticos:
            self.listaDiagnosticos.remove(diagnostico)
            self.guardar_archivo_diagnosticos()
            return True
        return False


    def buscar_objeto(self, cod):
        for i, diagnostico in enumerate(self.listaDiagnosticos, start=1):
            if i == int(cod):
                return diagnostico

    def buscar_diagnosticoxnombre(self, nombre):
        for diagnostico in self.listaDiagnosticos:
            if diagnostico.nombre.lower() == nombre.lower():
                return diagnostico
        return None

    def obtener_tratamientos_por_diagnostico(self, nombre_diagnostico):
        diagnostico = self.buscar_diagnosticoxnombre(nombre_diagnostico)
        if diagnostico:
            return [tratamiento.descripcion for tratamiento in diagnostico.tratamientos]
        return []

    def buscar_tratamiento_por_diagnostico(self, diagnostico):
        from Controller.ControladorTratamiento import ControladorTratamiento
        tratamientos = ControladorTratamiento()
        tratamientos.cargar_archivo_tratamiento()
        tratamientos_relacionados = []
        for tratamiento in tratamientos.listaTratamientos:
            if tratamiento.diagnostico.nombre.lower() == diagnostico.lower():
                tratamientos_relacionados.append(tratamiento.descripcion)
        return tratamientos_relacionados

    def obtener_descripcion_tratamientos(self, tratamiento):
        from Controller.ControladorTratamiento import ControladorTratamiento
        tratamientos = ControladorTratamiento()
        tratamientos.cargar_archivo_tratamiento()
        tratamiento_obj = tratamientos.buscar_tratamientoxnombre(tratamiento)
        if tratamiento_obj:
            descripcion = (
                f"Diagnóstico: {tratamiento_obj.diagnostico.nombre}\n"
                f"Descripción: {tratamiento_obj.descripcion}\n"
                f"Duración: {tratamiento_obj.duracion}\n"
                f"Indicaciones: {tratamiento_obj.indicaciones}"
            )
            return descripcion
        return "No se encontró el tratamiento."