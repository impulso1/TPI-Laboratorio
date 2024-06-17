from Modelo.mascota import Mascota

class ControladorMascota:
    def __init__(self):
        self.listaMascotas = []

    def cargarArchivoMascotas(self, raza_controller):
        with open("Datos/Mascotas.txt", "r") as file:
            renglones = file.readlines()
        for renglon in renglones:
            nombre, especie, raza_nombre, estado, propietario = renglon.strip().split(",")
            raza = raza_controller.buscarRazaxNombre(raza_nombre)
            self.listaMascotas.append(Mascota(nombre, especie, raza, estado, propietario))

    def crearMascota(self, nombre, especie, raza, estado, propietario):
        self.listaMascotas.append(Mascota(nombre, especie, raza, estado, propietario))

    def buscarMascota(self, cod):
        cont = 0
        for i in self.listaMascotas:
            cont = cont + 1
            if cont == int(cod):
                return i

    def eliminarMascota(self, cod):
        if 0 <= cod < len(self.listaMascotas):
            self.listaMascotas[cod].eliminarMascota()
            del self.listaMascotas[cod]
            return True
        return False

    def guardarArchivoMascotas(self):
        with open("Datos/Mascotas.txt", "w") as file:
            for mascota in self.listaMascotas:
                raza_nombre = mascota.raza.nombre if mascota.raza else ''
                file.write(f"{mascota.nombre},{mascota.especie},{raza_nombre},{mascota.estado},{mascota.propietario}\n")