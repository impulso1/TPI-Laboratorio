from Model.Vacuna import Vacuna


class ControladorVacuna:

    def __init__(self):
        self.listaVacunas = []

    def cargar_archivo_vacunas(self):
        with open("Resources/Vacunas.txt", "r") as file:
            renglones = file.readlines()
        for renglon in renglones:
            nombre, fecha_ven, dosis, costo, observaciones = renglon.strip().split(",")
            self.listaVacunas.append(Vacuna(nombre, fecha_ven, dosis, costo, observaciones))

    def nuevo_vacuna(self, nombre, fecha_ven, dosis, costo, observaciones):
        self.listaVacunas.append(Vacuna(nombre, fecha_ven, dosis, costo, observaciones))

    def modificar_vacuna(self, vac, opc, new):
        obj = self.buscar_objeto(vac)
        if opc == 1:
            obj.nombre = new
        elif opc == 2:
            obj.fecha_ven = new
        elif opc == 3:
            obj.dosis = new
        elif opc == 4:
            obj.costo = new
        elif opc == 5:
            obj.observaciones = new

    def buscar_objeto(self, cod):
        for i, vacuna in enumerate(self.listaVacunas, start=1):
            if i == int(cod):
                return vacuna

    def mostrar_vacunas(self):
        return self.listaVacunas

    def guardar_archivo_vacunas(self):
        with open("Resources/Vacunas.txt", "w") as file:
            for vacuna in self.listaVacunas:
                file.write(
                    f"{vacuna.nombre},{vacuna.fecha_ven},{vacuna.dosis},{vacuna.costo},{vacuna.observaciones}\n")

    def eliminar_vacuna(self, vacuna):
        if vacuna in self.listaVacunas:
            self.listaVacunas.remove(vacuna)
            self.guardar_archivo_vacunas()
            return True
        return False

    def buscar_vacunaxnombre(self, nombrevacuna):
        for vacuna in self.listaVacunas:
            if vacuna.nombre.lower() == nombrevacuna.lower():
                return vacuna

    def obtener_costo_vacuna(self, nombre_vacuna):
        vacuna = self.buscar_vacunaxnombre(nombre_vacuna)
        if vacuna:
            return vacuna.costo
        return None