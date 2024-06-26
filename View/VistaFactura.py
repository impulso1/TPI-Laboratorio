import tkinter as tk
from tkinter import ttk

class VistaFactura(tk.Toplevel):
    def __init__(self, controlador_factura):
        super().__init__()
        self.title("Facturas")
        self.geometry("400x400")
        self.controlador_factura = controlador_factura

        label = tk.Label(self, text="Seleccionar Factura:")
        label.pack(pady=10)

        self.fechas_combobox = ttk.Combobox(self)
        self.fechas_combobox.pack(pady=10)
        self.fechas_combobox.bind("<<ComboboxSelected>>", self.mostrar_factura_seleccionada)

        self.texto_factura = tk.Text(self, height=15, width=60)
        self.texto_factura.pack(pady=10)

        cerrar_button = tk.Button(self, text="Cerrar", command=self.cerrar_ventana)
        cerrar_button.pack(pady=10)

        self.mostrar_ventana()

    def mostrar_ventana(self):
        self.controlador_factura.cargar_archivo_facturas()
        fechas_facturas = self.controlador_factura.obtener_fechas_facturas()
        self.fechas_combobox["values"] = fechas_facturas
        if fechas_facturas:
            self.fechas_combobox.current(0)
            self.mostrar_factura_seleccionada()

        self.wait_window()

    def mostrar_factura_seleccionada(self, event=None):
        index_seleccionado = self.fechas_combobox.current()
        factura_seleccionada = self.controlador_factura.obtener_factura_por_fecha(index_seleccionado)

        self.texto_factura.delete(1.0, tk.END)
        if factura_seleccionada:
            self.texto_factura.insert(tk.END, str(factura_seleccionada))
        else:
            self.texto_factura.insert(tk.END, "No se encontró la factura seleccionada.")

    def cerrar_ventana(self):
        self.destroy()
