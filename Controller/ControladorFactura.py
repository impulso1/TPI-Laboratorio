# ControladorFactura.py
from Model.Factura import Factura

class ControladorFactura:
    def __init__(self):
        self.listaFacturas = []

    def crear_factura(self, cliente, consulta):
        factura = Factura(cliente, consulta)
        self.listaFacturas.append(factura)

    def mostrar_facturas(self):
        for factura in self.listaFacturas:
            factura.mostrar_factura()
