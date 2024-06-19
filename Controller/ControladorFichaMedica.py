from Model.FichaMedica import FichaMedica

class ControladorFichaMedica:
    def __init__(self):
        self.listaFichas = []

    def cargar_archivo_fichas(self):
        with open("Resources/FichasMedicas.txt", "r") as file:
            renglones = file.readlines()
        for renglon in renglones:
            datos = renglon.strip().split(",")
            self.listaFichas.append(FichaMedica(*datos))

    def crear_ficha(self, *datos):
        self.listaFichas.append(FichaMedica(*datos))

    def buscar_ficha(self, cod):
        for i, ficha in enumerate(self.listaFichas, start=1):
            if i == int(cod):
                return ficha

    def eliminar_ficha(self, cod):
        if 0 <= cod < len(self.listaFichas):
            del self.listaFichas[cod]
            return True
        return False

    def guardar_archivo_fichas(self):
        with open("Resources/FichasMedicas.txt", "w") as file:
            for ficha in self.listaFichas:
                file.write(f"{ficha}\n")

    def mostrar_fichas(self):
        for ficha in self.listaFichas:
            print(ficha)
