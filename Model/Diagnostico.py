class Diagnostico:
    def __init__(self, nombre, sintomas, tratamiento, observaciones):
        self.nombre = nombre
        self.sintomas = sintomas
        self.tratamiento = tratamiento
        self.observaciones = observaciones

    def __str__(self):
        return f"{self.nombre} - {self.sintomas} - {self.tratamiento} - {self.observaciones}"

    def __repr__(self):
        return f"{self.nombre} - {self.sintomas} - {self.tratamiento} - {self.observaciones}"

    # Métodos getter y setter para 'nombre'
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, value):
        if isinstance(value, str) and value.strip() != "":
            self.nombre = value
        else:
            raise ValueError("El nombre debe ser una cadena de caracteres no vacía")

    # Métodos getter y setter para 'sintomas'
    def get_sintomas(self):
        return self.sintomas

    def set_sintomas(self, value):
        if isinstance(value, str) and value.strip() != "":
            self.sintomas = value
        else:
            raise ValueError("Los síntomas deben ser una cadena de caracteres no vacía")

    # Métodos getter y setter para 'tratamiento'
    def get_tratamiento(self):
        return self.tratamiento

    def set_tratamiento(self, value):
        if isinstance(value, str) and value.strip() != "":
            self.tratamiento = value
        else:
            raise ValueError("El tratamiento debe ser una cadena de caracteres no vacía")

    # Métodos getter y setter para 'observaciones'
    def get_observaciones(self):
        return self.observaciones

    def set_observaciones(self, value):
        if isinstance(value, str) and value.strip() != "":
            self.observaciones = value
        else:
            raise ValueError("Las observaciones deben ser una cadena de caracteres no vacía")
