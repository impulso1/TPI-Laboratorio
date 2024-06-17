class Diagnostico:
    def __init__(self, nombre, sintomas, tratamiento, observaciones):
        self._nombre = nombre
        self._sintomas = sintomas
        self._tratamiento = tratamiento
        self._observaciones = observaciones

    # Métodos getter y setter para 'nombre'
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, value):
        if isinstance(value, str) and value.strip() != "":
            self._nombre = value
        else:
            raise ValueError("El nombre debe ser una cadena de caracteres no vacía")

    # Métodos getter y setter para 'sintomas'
    def get_sintomas(self):
        return self._sintomas

    def set_sintomas(self, value):
        if isinstance(value, str) and value.strip() != "":
            self._sintomas = value
        else:
            raise ValueError("Los síntomas deben ser una cadena de caracteres no vacía")

    # Métodos getter y setter para 'tratamiento'
    def get_tratamiento(self):
        return self._tratamiento

    def set_tratamiento(self, value):
        if isinstance(value, str) and value.strip() != "":
            self._tratamiento = value
        else:
            raise ValueError("El tratamiento debe ser una cadena de caracteres no vacía")

    # Métodos getter y setter para 'observaciones'
    def get_observaciones(self):
        return self._observaciones

    def set_observaciones(self, value):
        if isinstance(value, str) and value.strip() != "":
            self._observaciones = value
        else:
            raise ValueError("Las observaciones deben ser una cadena de caracteres no vacía")


