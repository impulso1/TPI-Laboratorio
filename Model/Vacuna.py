class Vacuna:
    def __init__(self, nombre, fecha_ven, dosis, costo, observaciones):
        self.nombre=nombre
        self.fecha_ven=fecha_ven
        self.dosis=dosis
        self.costo=costo
        self.observaciones=observaciones
        
    def __str__(self):
        return f"{self.nombre} - {self.fecha_ven} - {self.dosis} - {self.costo} - {self.observaciones}"

    def __repr__(self):
        return f"{self.nombre} - {self.fecha_ven} - {self.dosis} - {self.costo} - {self.observaciones}"
