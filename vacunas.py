class Vacunas:
    def __int__(self,nombre,dosis,fecha_elaboracion,fecha_vencimiento,fabricante,costo,prospecto):
        self.nombre = nombre
        self.dosis = dosis
        self.fecha_elaboracion = fecha_elaboracion
        self.fecha_vencimiento = fecha_vencimiento
        self.fabricante = fabricante
        self.costo = costo
        self.prospecto = prospecto

    def get_nombre(self):
        return self.nombre
    def set_nombre(self,nombre):
        self.nombre = nombre
    def get_dosis(self):
        return self.dosis
    def set_dosis(self,dosis):
        self.dosis= dosis
    def get_fecha_elaboracion(self):
        return self.fecha_elaboracion
    def set_fecha_elaboracion(self,fecha_elaboracion):
        self.fecha_elaboracion=fecha_elaboracion
    def get_fecha_vencimiento(self):
        return self.fecha_vencimiento
    def set_fecha_vencimiento(self,fecha_vencimiento):
        self.fecha_vencimiento=fecha_vencimiento
    def get_fabricante(self):
        return self.fabricante
    def set_fabricante(self,fabricante):
        self.fabricante=fabricante
    def get_costo(self):
        return self.costo
    def set_costo(self,costo):
        self.costo=costo
    def get_prospecto(self):
        return self.prospecto
    def set_prospecto(self,prospecto):
        self.prospecto= prospecto