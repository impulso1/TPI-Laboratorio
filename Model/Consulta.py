# Consulta.py
class Consulta:
    def __init__(self, fecha, veterinario, diagnostico, tratamiento, vacunas, observaciones):
        self.fecha = fecha
        self.veterinario = veterinario
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.vacunas = vacunas
        self.observaciones = observaciones

    def __str__(self):
        return f"{self.fecha} - {self.veterinario} - {self.diagnostico} - {self.tratamiento} - {self.vacunas} - {self.observaciones}"

    def __repr__(self):
        return f"{self.fecha} - {self.veterinario} - {self.diagnostico} - {self.tratamiento} - {self.vacunas} - {self.observaciones}"