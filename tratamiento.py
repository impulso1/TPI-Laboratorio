class Tratamiento:
    def __init__(self, descripcion, costo, duracion, indicaciones):
        self._descripcion = descripcion
        self._costo = costo
        self._duracion = duracion
        self._indicaciones = indicaciones

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        if isinstance(value, str) and value.strip() != "":
            self._descripcion = value
        else:
            raise ValueError("La descripción debe ser una cadena de caracteres no vacía")

    @property
    def costo(self):
        return self._costo

    @costo.setter
    def costo(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._costo = value
        else:
            raise ValueError("El costo debe ser un número positivo")

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._duracion = value
        else:
            raise ValueError("La duración debe ser un número positivo")

    @property
    def indicaciones(self):
        return self._indicaciones

    @indicaciones.setter
    def indicaciones(self, value):
        if isinstance(value, str) and value.strip() != "":
            self._indicaciones = value
        else:
            raise ValueError("Las indicaciones deben ser una cadena de caracteres no vacía")

    def calcular_costo(self):
        # Aquí puedes agregar lógica adicional para calcular el costo si es necesario
        return self._costo

    def eliminar_tratamiento(self):
        self._descripcion = ""
        self._costo = 0
        self._duracion = 0
        self._indicaciones = ""
