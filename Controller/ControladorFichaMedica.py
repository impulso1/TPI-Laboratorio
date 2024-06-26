from Model.FichaMedica import FichaMedica
import os

class ControladorFichaMedica:
    def __init__(self):
        self.listaFichasMedicas = []

    def cargar_archivo_fichas_medicas(self, nombre_mascota):
        nombre = nombre_mascota.split()[0]
        archivo = f"Resources/Mascotas/FichaMedica{nombre}.txt"
        if os.path.exists(archivo):
            with open(archivo, "r") as file:
                lineas = file.read().split("##########")
            self.listaFichasMedicas = [FichaMedica.from_string(ficha) for ficha in lineas if ficha]
        else:
            self.listaFichasMedicas = []

    def obtener_fechas_fichas_por_mascota(self, nombre_mascota):
        nombre_mascota_simple = nombre_mascota.split()[0]
        return [ficha.fecha for ficha in self.listaFichasMedicas if ficha.mascota.lower() == nombre_mascota_simple.lower()]

    def obtener_ficha_por_fecha_mascota(self, fecha, nombre_mascota):
        nombre_mascota_simple = nombre_mascota.split()[0]
        return next((ficha for ficha in self.listaFichasMedicas if ficha.fecha == fecha and ficha.mascota.lower() == nombre_mascota_simple.lower()), None)
