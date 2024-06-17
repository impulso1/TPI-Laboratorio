from Modelo.raza import Raza
class Mascota:
    def __init__(self, nombre, especie, raza, estado, propietario):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.estado = estado
        self.propietario = propietario

    def __str__(self):
     return (
        f"nombre: {self.nombre}, especie: {self.especie}, raza: {self.raza}, estado: {self.estado}, propietario: {self.propietario}")

    def __repr__(self):
        return f"Mascota(nombre: {self.nombre}, especie: {self.especie}, raza: {self.raza}, estado: {self.estado}, propietario: {self.propietario})"

    def eliminarMascota(self):
        self.nombre = None
        self.especie = None
        self.raza = None
        self.estado = None
        self.propietario = None