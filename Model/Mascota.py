class Mascota:
    def __init__(self, nombre, especie, raza, estado, propietario):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.estado = estado
        self.propietario = propietario

    def __str__(self):
        return (f"{self.nombre} - {self.especie} - {self.raza} - {self.estado} - "
                f"{self.propietario}")

    def __repr__(self):
        return (f"{self.nombre} - {self.especie} - {self.raza} - {self.estado} - "
                f"{self.propietario}")

    def eliminar_mascota(self):
        self.nombre = None
        self.especie = None
        self.raza = None
        self.estado = None
        self.propietario = None
