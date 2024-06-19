class VistaFichaMedica:
    def mostrar_ficha_medica(self, ficha_medica):
        print(ficha_medica)
    
    def obtener_detalle(self):
        fecha = input("Ingrese la fecha del detalle: ")
        descripcion = input("Ingrese la descripción del detalle: ")
        return fecha, descripcion

    def seleccionar_indice(self):
        return int(input("Ingrese el índice del detalle: "))
