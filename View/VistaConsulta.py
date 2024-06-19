import tkinter as tk
from tkinter import ttk
from datetime import datetime


class VistaConsulta(tk.Toplevel):
    def __init__(self, master=None, controlador_consulta=None):
        super().__init__(master)
        self.controlador_consulta = controlador_consulta
        self.title("Generar Consulta")
        self.geometry("500x500")

        # Fecha de hoy
        self.fecha_label = tk.Label(self, text=f"Fecha: {datetime.now().strftime('%Y-%m-%d')}")
        self.fecha_label.pack(pady=10)

        # Combobox para elegir veterinario
        self.veterinario_label = tk.Label(self, text="Seleccionar Veterinario:")
        self.veterinario_label.pack(pady=5)

        self.veterinarios = self.controlador_consulta.obtener_nombres_veterinarios()
        self.veterinario_combobox = ttk.Combobox(self, values=self.veterinarios)
        self.veterinario_combobox.pack(pady=5)

        # Diagnóstico
        self.diagnostico = self.controlador_consulta.obtener_nombres_diagnosticos()
        self.diagnostico_combobox = ttk.Combobox(self, values=self.diagnostico)
        self.diagnostico_combobox.pack(pady=5)

        # Tratamiento
        self.tratamiento = self.controlador_consulta.obtener_descripcion_tratamientos()
        self.tratamiento_combobox = ttk.Combobox(self, values=self.diagnostico)
        self.tratamiento_combobox.pack(pady=5)

        # Checkboxes para vacunas
        self.vacunas_label = tk.Label(self, text="Vacunas:")
        self.vacunas_label.pack(pady=5)

        self.vacunas_frame = tk.Frame(self)
        self.vacunas_frame.pack(pady=5)

        self.vacunas = self.controlador_consulta.obtener_nombres_vacunas()
        self.vacunas_vars = {}

        for vacuna in self.vacunas:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(self.vacunas_frame, text=vacuna, variable=var)
            chk.pack(anchor='w')
            self.vacunas_vars[vacuna] = var

        # Observaciones
        self.observaciones_label = tk.Label(self, text="Observaciones:")
        self.observaciones_label.pack(pady=5)
        self.observaciones_text = tk.Text(self, height=3, width=40)
        self.observaciones_text.pack(pady=5)

        # Botón para guardar consulta
        self.guardar_button = tk.Button(self, text="Guardar Consulta", command=self.guardar_consulta)
        self.guardar_button.pack(pady=10)

    def guardar_consulta(self):
        veterinario = self.veterinario_combobox.get()
        diagnostico = self.diagnostico_text.get("1.0", tk.END).strip()
        tratamiento = self.tratamiento_text.get("1.0", tk.END).strip()
        observaciones = self.observaciones_text.get("1.0", tk.END).strip()
        vacunas_seleccionadas = [vacuna for vacuna, var in self.vacunas_vars.items() if var.get()]

        self.controlador_consulta.guardar_consulta(veterinario, diagnostico, tratamiento, vacunas_seleccionadas,
                                                   observaciones)
        self.destroy()
