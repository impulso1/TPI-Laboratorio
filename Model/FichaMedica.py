class FichaMedica:
    def __init__(self, fecha, mascota, veterinario, diagnostico, tratamiento, descripcion, duracion, indicaciones, vacunas, observaciones):
        self.fecha = fecha
        self.mascota = mascota
        self.veterinario = veterinario
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.descripcion = descripcion
        self.duracion = duracion
        self.indicaciones = indicaciones
        self.vacunas = vacunas
        self.observaciones = observaciones

    @classmethod
    def from_string(cls, s):
        datos = s.strip().split("\n")
        fecha = datos[0].split(": ")[1]
        mascota = datos[1].split(": ")[1]
        veterinario = datos[2].split(": ")[1]
        diagnostico = datos[3].split(": ")[1]
        tratamiento = datos[4].split(": ")[1]
        descripcion = datos[5].split(": ")[1]
        duracion = datos[6].split(": ")[1]
        indicaciones = datos[7].split(": ")[1]
        vacunas = datos[8].split(": ")[1].split(", ")
        observaciones = datos[9].split(": ")[1]
        return cls(fecha, mascota, veterinario, diagnostico, tratamiento, descripcion, duracion, indicaciones, vacunas, observaciones)


    def __str__(self):
        return f"{self.fecha} - {self.mascota} - {self.veterinario} - {self.diagnostico} - {self.tratamiento} - {self.vacunas} - {self.observaciones}"

    def __repr__(self):
        return f"{self.fecha} - {self.mascota} - {self.veterinario} - {self.diagnostico} - {self.tratamiento} - {self.vacunas} - {self.observaciones}"
