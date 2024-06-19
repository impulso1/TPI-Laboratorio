# Factura.py
from datetime import datetime
from Model.Consulta import Consulta

class Factura:
    def __init__(self, cliente, consulta):
        self.__cliente = cliente
        self.__consulta = consulta  # Relación con Consulta
        self.__fecha = datetime.now()
        self.__total = self.calcular_total()

    def calcular_total(self):
        total = 0
        if self.__consulta.get_tratamiento():
            total += self.__consulta.get_tratamiento().calcular_costo()
        return total

    def mostrar_factura(self):
        print(f"Factura\nFecha: {self.__fecha}")
        print(f"Cliente: {self.__cliente}")
        print(f"Consulta: {self.__consulta}")
        print(f"Total: {self.__total}")

    def __str__(self):
        return (f"Factura(Cliente: {self.__cliente}, Consulta: {self.__consulta}, Total: {self.__total})")

    def __repr__(self):
        return self.__str__()
