
class Tratamiento:
    def __init__(self, diagnostico, descripcion, duracion, indicaciones):
        self.diagnostico = diagnostico
        self.descripcion = descripcion
        self.duracion = duracion
        self.indicaciones = indicaciones

    def __str__(self):
        return f"{self.diagnostico} - {self.descripcion} - {self.duracion} - {self.indicaciones}"

    def __repr__(self):
        return f"{self.diagnostico} - {self.descripcion} - {self.duracion} - {self.indicaciones}"

