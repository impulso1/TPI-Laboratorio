import os
from Model.Factura import Factura
from collections import defaultdict

class ControladorFactura:
    def __init__(self):
        self.listaFacturas = []

    def cargar_archivo_facturas(self):
        archivo = "Resources/facturas.txt"
        if os.path.exists(archivo):
            with open(archivo, "r") as file:
                lineas = file.read().split("##########")
            self.listaFacturas = [Factura.from_string(factura) for factura in lineas if factura.strip()]
        else:
            self.listaFacturas = []

    def obtener_fechas_facturas(self):
        contador_por_fecha = defaultdict(int)
        fechas_facturas = []
        for factura in self.listaFacturas:
            contador_por_fecha[factura.fecha] += 1
            fechas_facturas.append(f"Factura {contador_por_fecha[factura.fecha]} - {factura.fecha}")
        return fechas_facturas

    def obtener_factura_por_fecha(self, index):
        if index < len(self.listaFacturas):
            return self.listaFacturas[index]
        return None
