from Modelo.raza import Raza

class ControladorRaza:
    def __init__(self):
        self.razas = []

    def cargarArchivoRazas(self):
        with open("Datos/Razas.txt", "r") as file:
            renglones = file.readlines()
        for renglon in renglones:
            valores = renglon.strip().split(",")
            if len(valores) != 2:
                print(f"Error: línea mal formateada en el archivo Razas.txt: {renglon.strip()}")
                continue  # Saltar esta línea y pasar a la siguiente

            nombre, caracteristicas = valores
            self.razas.append(Raza(nombre, caracteristicas))

    def crearRaza(self, nombre, caracteristicas):
        self.razas.append(Raza(nombre, caracteristicas))

    def buscarRaza(self, cod):
        cont = 0
        for i in self.razas:
            cont = cont + 1
            if cont == int(cod):
                return i

    def buscarRazaxNombre(self, nombre):
        for raza in self.razas:
            if raza.nombre == nombre:
                return raza
        return None

    def eliminarRaza(self, cod):
        if 0 <= cod < len(self.razas):
            del self.razas[cod]
            return True
        return False

    def guardarArchivoRazas(self):
        with open("Datos/Razas.txt", "w") as file:
            for raza in self.razas:
                file.write(f"{raza.nombre},{raza.caracteristicas}\n")