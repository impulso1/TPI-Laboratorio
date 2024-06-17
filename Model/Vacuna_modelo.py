class Vacuna:
    def __init__(self,nombre,fecha_ven,dosis,costo,observaciones):
        self.nombre=nombre
        self.fecha_ven=fecha_ven
        self.dosis=dosis
        self.costo=costo
        self.observaciones=observaciones
        
    def __str__(self):
        return f"Nombre: {self.nombre} Fecha de Vencimiento: {self.fecha_ven} Dosis: {self.dosis} Costo: {self.costo} Observaciones: {self.observaciones}"
    
    def __repr__(self):
        return f"Nombre: {self.nombre} Fecha de Vencimiento: {self.fecha_ven} Dosis: {self.dosis} Costo: {self.costo} Observaciones: {self.observaciones}"