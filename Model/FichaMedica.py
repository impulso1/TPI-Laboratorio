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
    def from_string(cls, ficha_string):
        lines = ficha_string.strip().split('\n')
        data = {}
        for line in lines:
            key, value = line.split(':', 1)
            data[key.strip()] = value.strip()
        return cls(
            fecha=data.get('Fecha', ''),
            mascota=data.get('Mascota', ''),
            veterinario=data.get('Veterinario', ''),
            diagnostico=data.get('Diagnóstico', ''),
            tratamiento=data.get('Tratamiento', ''),
            descripcion=data.get('Descripción', ''),
            duracion=data.get('Duración', ''),
            indicaciones=data.get('Indicaciones', ''),
            vacunas=data.get('Vacunas', '').split(', '),
            observaciones=data.get('Observaciones', '')
        )


    def __str__(self):
        return f"{self.fecha} - {self.mascota} - {self.veterinario} - {self.diagnostico} - {self.tratamiento} - {self.vacunas} - {self.observaciones}"

    def __repr__(self):
        return f"{self.fecha} - {self.mascota} - {self.veterinario} - {self.diagnostico} - {self.tratamiento} - {self.vacunas} - {self.observaciones}"
