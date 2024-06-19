from Model.Diagnostico import Diagnostico


class ControladorDiagnostico:

    def __init__(self):
        self.listaDiagnosticos = []

    def cargar_archivo_diagnosticos(self):
        with open("Resources/Diagnosticos.txt", "r") as file:
            renglones = file.readlines()
        for renglon in renglones:
            nombre, sintomas, tratamiento, observaciones = renglon.strip().split(",")
            self.listaDiagnosticos.append(Diagnostico(nombre, sintomas, tratamiento, observaciones))

    def nuevo_diagnostico(self, nombre, sintomas, tratamiento, observaciones):
        self.listaDiagnosticos.append(Diagnostico(nombre, sintomas, tratamiento, observaciones))

    def modificar_diagnostico(self, diag, opc, new):
        obj = self.buscar_objeto(diag)
        if opc == 1:
            obj.nombre = new
        elif opc == 2:
            obj.sintomas = new
        elif opc == 3:
            obj.tratamiento = new
        elif opc == 4:
            obj.observaciones = new

    def buscar_objeto(self, cod):
        for i, diagnostico in enumerate(self.listaDiagnosticos, start=1):
            if i == int(cod):
                return diagnostico

    def mostrar_diagnosticos(self):
        return self.listaDiagnosticos

    def guardar_archivo_diagnosticos(self):
        with open("Resources/Diagnosticos.txt", "w") as file:
            for diagnostico in self.listaDiagnosticos:
                file.write(
                    f"{diagnostico.nombre},{diagnostico.sintomas},{diagnostico.tratamiento},{diagnostico.observaciones}\n")

    def eliminar_diagnostico(self, diagnostico):
        if diagnostico in self.listaDiagnosticos:
            self.listaDiagnosticos.remove(diagnostico)
            self.guardar_archivo_diagnosticos()
            return True
        return False

    def buscar_diagnosticoxnombre(self, nombrediagnostico):
        for diagnostico in self.listaDiagnosticos:
            if diagnostico.nombre.lower() == nombrediagnostico.lower():
                return diagnostico