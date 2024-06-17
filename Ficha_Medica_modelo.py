class Detalle_Ficha_Medica:
    def __init__(self, fecha, descripcion):
        self.fecha = fecha
        self.descripcion = descripcion
    
    def __str__(self):
        return f"Detalle_Ficha_Medica(fecha={self.fecha}, descripcion={self.descripcion})"

class Ficha_Medica:
    def __init__(self, mascota):
        self.mascota = mascota  # Este será un objeto de la clase Mascota
        self.detalles = []

    def agregar_detalle(self, detalle):
        self.detalles.append(detalle)  # Este será un objeto de la clase Detalle_Ficha_Medica

    def eliminar_detalle(self, indice):
        if 0 <= indice < len(self.detalles):
            del self.detalles[indice]
        else:
            print("Índice fuera de rango.")

    def editar_detalle(self, indice, nuevo_detalle):
        if 0 <= indice < len(self.detalles):
            self.detalles[indice] = nuevo_detalle
        else:
            print("Índice fuera de rango.")

    def __str__(self):
        detalles_str = "\n".join(str(detalle) for detalle in self.detalles)
        return f"Ficha_Medica de {self.mascota}\nDetalles:\n{detalles_str}"
