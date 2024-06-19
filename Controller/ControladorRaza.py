from Model.Raza import Raza


class ControladorRaza:
    def __init__(self):
        self.listaRazas = []

    def cargar_archivo_razas(self):
        with open("Resources/Razas.txt", "r") as file:
            renglones = file.readlines()
        for renglon in renglones:
            nombre, caracteristicas = renglon.strip().split(",")
            self.listaRazas.append(Raza(nombre, caracteristicas))

    def crear_raza(self, nombre, caracteristicas):
        self.listaRazas.append(Raza(nombre, caracteristicas))

    def buscar_raza(self, cod):
        for i, raza in enumerate(self.listaRazas, start=1):
            if i == int(cod):
                return raza

    def buscar_razaxnombre(self, nombreraza):
        for raza in self.listaRazas:
            if raza.nombre.lower() == nombreraza.lower():
                return raza


    def eliminar_raza(self, cod):
        if 0 <= cod < len(self.listaRazas):
            del self.listaRazas[cod]
            return True
        return False

    def guardar_archivo_razas(self):
        with open("Resources/Razas.txt", "w") as file:
            for raza in self.listaRazas:
                file.write(f"{raza.nombre},{raza.caracteristicas}\n")

    def mostrar_razas(self):
        return self.listaRazas
