import tkinter as tk
from tkinter import ttk

class VistaFichaMedica(tk.Toplevel):
    def __init__(self, mascotas, controlador_ficha_medica):
        super().__init__()
        self.title("Fichas Médicas")
        self.geometry("400x400")
        self.controlador_ficha_medica = controlador_ficha_medica
        self.mascotas = mascotas

        label = tk.Label(self, text="Seleccionar Mascota:")
        label.pack(pady=10)

        self.mascotas_combobox = ttk.Combobox(self, values=mascotas)
        self.mascotas_combobox.pack(pady=10)

        self.mascotas_combobox.bind("<<ComboboxSelected>>", self.mostrar_fechas_fichas)

        self.fechas_combobox = ttk.Combobox(self)
        self.fechas_combobox.pack(pady=10)

        self.fechas_combobox.bind("<<ComboboxSelected>>", self.mostrar_ficha_seleccionada)

        self.lista_fichas = tk.Listbox(self, height=10, width=60)
        self.lista_fichas.pack(pady=10)

        cerrar_button = tk.Button(self, text="Cerrar", command=self.cerrar_ventana)
        cerrar_button.pack(pady=10)

        self.mostrar_ventana()

    def mostrar_ventana(self):
        self.wait_window()

    def mostrar_fechas_fichas(self, event=None):
        mascota_seleccionada = self.mascotas_combobox.get()

        # Cargar las fichas médicas de la mascota seleccionada
        self.controlador_ficha_medica.cargar_archivo_fichas_medicas(mascota_seleccionada)

        fechas_fichas = self.controlador_ficha_medica.obtener_fechas_fichas_por_mascota(mascota_seleccionada)
        if fechas_fichas:
            self.fechas_combobox["values"] = fechas_fichas
            self.fechas_combobox.current(0)
            self.mostrar_ficha_seleccionada()
        else:
            self.fechas_combobox["values"] = ["Sin ficha médica disponible"]
            self.fechas_combobox.current(0)
            self.lista_fichas.delete(0, tk.END)
            self.lista_fichas.insert(tk.END, "Sin ficha médica disponible")

    def mostrar_ficha_seleccionada(self, event=None):
        if self.fechas_combobox.get() == "Sin ficha médica disponible":
            self.lista_fichas.delete(0, tk.END)
            self.lista_fichas.insert(tk.END, "Sin ficha médica disponible")
            return

        mascota_seleccionada = self.mascotas_combobox.get()
        fecha_seleccionada = self.fechas_combobox.get()
        ficha_seleccionada = self.controlador_ficha_medica.obtener_ficha_por_fecha_mascota(fecha_seleccionada, mascota_seleccionada)

        self.lista_fichas.delete(0, tk.END)
        if ficha_seleccionada:
            self.lista_fichas.insert(tk.END, f"Fecha: {ficha_seleccionada.fecha}")
            self.lista_fichas.insert(tk.END, f"Veterinario: {ficha_seleccionada.veterinario}")
            self.lista_fichas.insert(tk.END, f"Diagnóstico: {ficha_seleccionada.diagnostico}")
            self.lista_fichas.insert(tk.END, f"Tratamiento: {ficha_seleccionada.tratamiento}")
            self.lista_fichas.insert(tk.END, f"Descripción: {ficha_seleccionada.descripcion}")
            self.lista_fichas.insert(tk.END, f"Duración: {ficha_seleccionada.duracion}")
            self.lista_fichas.insert(tk.END, f"Indicaciones: {ficha_seleccionada.indicaciones}")
            self.lista_fichas.insert(tk.END, f"Vacunas: {', '.join(ficha_seleccionada.vacunas)}")
            self.lista_fichas.insert(tk.END, f"Observaciones: {ficha_seleccionada.observaciones}")
        else:
            self.lista_fichas.insert(tk.END, "No se encontró ficha médica para la fecha seleccionada.")

    def cerrar_ventana(self):
        self.destroy()
