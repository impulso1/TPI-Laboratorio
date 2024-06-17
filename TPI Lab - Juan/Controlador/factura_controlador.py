from Modelo.factura_modelo import Factura
from Vista.factura_vista import FacturaVista

class FacturaController:
    def __init__(self, cliente, veterinario, consulta):
        self.factura = Factura(cliente, veterinario, consulta)
        self.vista = FacturaVista(self.factura)
    def mostrar_factura(self):
        self.vista.mostrar_factura()
