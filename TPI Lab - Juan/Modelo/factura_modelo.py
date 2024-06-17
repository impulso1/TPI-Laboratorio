from datetime import datetime

class Factura:
    def __init__(self, cliente, veterinario, consulta):
        self.__cliente = cliente
        self.__veterinario = veterinario
        self.__consulta = consulta
        self.__costoTotal = self.calcularCostoTotal(consulta)
        self.__fecha = datetime.now()

    def get_cliente(self):
        return self.__cliente

    def set_cliente(self, cliente):
        self.__cliente = cliente

    def get_veterinario(self):
        return self.__veterinario

    def set_veterinario(self, veterinario):
        self.__veterinario = veterinario

    def get_consulta(self):
        return self.__consulta

    def set_consulta(self, consulta):
        self.__consulta = consulta
        self.__costoTotal = self.calcularCostoTotal(consulta)

    def get_costoTotal(self):
        return self.__costoTotal

    def set_costoTotal(self, costoTotal):
        self.__costoTotal = costoTotal

    def get_fecha(self):
        return self.__fecha

    def set_fecha(self, fecha):
        self.__fecha = fecha



    def calcularCostoTotal(self, consulta):
        costo_total = 0


        for detalle in consulta.get_vacunas():
            costo_total += detalle.get_vacuna().get_costo()

        costo_total += consulta.get_tratamiento().get_costo()

        return costo_total

