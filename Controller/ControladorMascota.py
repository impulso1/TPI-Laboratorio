from Model.Mascota import Mascota
from Controller.ControladorRaza import ControladorRaza
from Controller.ControladorPropietario import ControladorPropietario


class ControladorMascota:
    def __init__(self):
        self.razas = ControladorRaza()
        self.propietario = ControladorPropietario()
        self.listaMascotas = []

    def cargar_archivo_mascotas(self):
        self.razas.cargar_archivo_razas()
        with open("Resources/Mascotas.txt", "r") as file:
            renglones = file.readlines()
        for renglon in renglones:
            valores = renglon.strip().split(",")
            if len(valores) == 5:
                nombre, especie, nombre_raza, estado, propietario = valores
                raza = self.razas.buscar_razaxnombre(nombre_raza.lower())
                if raza:
                    self.listaMascotas.append(Mascota(nombre, especie, raza, estado, propietario))
                else:
                    print(f"No se encontró la raza con nombre {nombre_raza}")

    def crear_mascota(self, nombre, especie, nombre_raza, estado, propietario):
        raza = self.razas.buscar_razaxnombre(nombre_raza.lower())
        if raza:
            mascota = Mascota(nombre, especie, raza, estado, propietario)
            self.listaMascotas.append(mascota)
            self.propietario.agregar_mascota(mascota)
        else:
            pass

    def modificar_mascota(self, nombre, especie, raza, estado, propietario):
        self.listaMascotas.append(Mascota(nombre, especie, raza, estado, propietario))

    def actualizar_mascota(self, cod, nombre, especie, nombre_raza, estado, propietario):
        raza = self.razas.buscar_razaxnombre(nombre_raza.lower())
        if raza:
            self.listaMascotas[cod - 1] = Mascota(nombre, especie, raza, estado, propietario)
            self.guardar_archivo_mascotas()

    def buscar_mascota(self, cod):
        for i, mascota in enumerate(self.listaMascotas, start=1):
            if i == int(cod):
                return mascota

    def eliminar_mascota(self, mascota):
        if mascota in self.listaMascotas:
            self.listaMascotas.remove(mascota)
            self.guardar_archivo_mascotas()
            return True
        return False

    def guardar_archivo_mascotas(self):
        with open("Resources/Mascotas.txt", "w") as file:
            for mascota in self.listaMascotas:
                raza_nombre = mascota.raza.nombre if mascota.raza else ''
                file.write(
                    f"{mascota.nombre},{mascota.especie},{raza_nombre},{mascota.estado},{mascota.propietario}\n")

    def mostrar_mascotas(self):
        return self.listaMascotas

    def obtener_mascotas_y_propietarios(self):
        return [(f"{mascota.nombre} (Dueño: {mascota.propietario})", mascota.nombre) for mascota in self.listaMascotas]
