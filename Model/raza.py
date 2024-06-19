class Raza:
    def __init__(self, nombre, caracteristicas):
        self.nombre = nombre
        self.caracteristicas = caracteristicas

    def __str__(self):
        return f"{self.nombre} - {self.caracteristicas}"

    def __repr__(self):
        return f"{self.nombre} - {self.caracteristicas}"

    def eliminar_raza(self):
        self.nombre = None
        self.caracteristicas = None
