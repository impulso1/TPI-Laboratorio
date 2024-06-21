class Raza:
    def __init__(self, nombre, caracteristicas):
        self.nombre = nombre
        self.caracteristicas = caracteristicas

    def __str__(self):
        return f"nombre: {self.nombre}, características: {self.caracteristicas}"

    def __repr__(self):
        return (f"Raza(nombre = {self.nombre}, caracteristicas = {self.caracteristicas})")

    def eliminarRaza(self):
        self.nombre = None
        self.caracteristicas = None