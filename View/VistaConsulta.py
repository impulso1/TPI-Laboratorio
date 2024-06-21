import tkinter as tk
from tkinter import ttk
from datetime import datetime


class VistaConsulta(tk.Toplevel):
    def __init__(self, master=None, controlador_consulta=None):
        super().__init__(master)
        self.controlador_consulta = controlador_consulta
        self.title("Generar Consulta")
        self.geometry("600x950")
        self.resizable(False, False)  # Evitar que la ventana cambie de tamaño

        # Fecha de hoy
        self.fecha_label = tk.Label(self, text=f"Fecha: {datetime.now().strftime('%Y-%m-%d')}")
        self.fecha_label.pack(pady=10)

        # Combobox para elegir mascota
        self.mascota_label = tk.Label(self, text="Seleccionar Mascota:")
        self.mascota_label.pack(pady=5)

        self.mascotas = self.controlador_consulta.obtener_nombres_mascotas()
        self.mascota_combobox = ttk.Combobox(self, values=self.mascotas)
        self.mascota_combobox.pack(pady=5)
        self.mascota_combobox.bind("<<ComboboxSelected>>", self.actualizar_dueno_mascota)

        # Cuadro de texto para mostrar el dueño de la mascota
        self.dueno_label = tk.Label(self, text="Dueño de la Mascota:")
        self.dueno_label.pack(pady=5)
        self.dueno_text = tk.Entry(self, state='readonly', width=60)
        self.dueno_text.pack(pady=5)

        # Combobox para elegir veterinario
        self.veterinario_label = tk.Label(self, text="Seleccionar Veterinario:")
        self.veterinario_label.pack(pady=5)

        self.veterinarios = self.controlador_consulta.obtener_nombres_veterinarios()
        self.veterinario_combobox = ttk.Combobox(self, values=self.veterinarios)
        self.veterinario_combobox.pack(pady=5)
        self.veterinario_combobox.bind("<<ComboboxSelected>>", self.actualizar_matricula_veterinario)

        # Cuadro de texto para mostrar la matrícula del veterinario
        self.matricula_label = tk.Label(self, text="Matrícula del Veterinario:")
        self.matricula_label.pack(pady=5)
        self.matricula_text = tk.Entry(self, state='readonly', width=60)
        self.matricula_text.pack(pady=5)

        # Diagnóstico
        self.diagnostico_label = tk.Label(self, text="Seleccionar Diagnóstico:")
        self.diagnostico_label.pack(pady=5)

        self.diagnosticos = self.controlador_consulta.obtener_nombres_diagnosticos()
        self.diagnostico_combobox = ttk.Combobox(self, values=self.diagnosticos)
        self.diagnostico_combobox.pack(pady=5)
        self.diagnostico_combobox.bind("<<ComboboxSelected>>", self.mostrar_tratamiento_relacionado)

        # Cuadro de texto para mostrar el tratamiento relacionado
        self.tratamiento_text = tk.Text(self, height=8, width=60, state='disabled')  # Aumentar el tamaño
        self.tratamiento_text.pack(pady=5)

        # Checkboxes para vacunas
        self.vacunas_label = tk.Label(self, text="Vacunas:")
        self.vacunas_label.pack(pady=5)

        self.vacunas_frame = tk.Frame(self)
        self.vacunas_frame.pack(pady=5)

        self.vacunas = self.controlador_consulta.obtener_nombres_vacunas()
        self.vacunas_vars = {}

        for vacuna in self.vacunas:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(self.vacunas_frame, text=vacuna, variable=var, command=self.actualizar_costo)
            chk.pack(anchor='w')
            self.vacunas_vars[vacuna] = var

        # Etiqueta para mostrar el costo total
        self.costo_consulta_label = tk.Label(self, text="Costo Consulta: $50.00")
        self.costo_consulta_label.pack(pady=10)

        # Etiqueta para mostrar el costo total
        self.costo_total_label = tk.Label(self, text="Costo Total: $50.00")
        self.costo_total_label.pack(pady=10)

        # Observaciones
        self.observaciones_label = tk.Label(self, text="Observaciones:")
        self.observaciones_label.pack(pady=5)
        self.observaciones_text = tk.Text(self, height=4, width=60)
        self.observaciones_text.pack(pady=5)

        # Botón para guardar consulta
        self.guardar_button = tk.Button(self, text="Guardar Consulta", command=self.guardar_consulta)
        self.guardar_button.pack(pady=10)

    def actualizar_dueno_mascota(self, event):
        mascota = self.mascota_combobox.get()
        dueno = self.controlador_consulta.obtener_dueno_por_mascota(mascota)
        self.dueno_text.config(state='normal')
        self.dueno_text.delete(0, tk.END)
        if dueno:
            self.dueno_text.insert(0, dueno)
        else:
            self.dueno_text.insert(0, "No encontrado")
        self.dueno_text.config(state='readonly')

    def actualizar_matricula_veterinario(self, event):
        veterinario = self.veterinario_combobox.get()
        matricula = self.controlador_consulta.obtener_matricula_por_veterinario(veterinario)
        self.matricula_text.config(state='normal')
        self.matricula_text.delete(0, tk.END)
        if matricula:
            self.matricula_text.insert(0, matricula)
        else:
            self.matricula_text.insert(0, "No encontrada")
        self.matricula_text.config(state='readonly')

    def mostrar_tratamiento_relacionado(self, event):
        diagnostico = self.diagnostico_combobox.get()
        tratamiento = self.controlador_consulta.obtener_tratamiento_por_diagnostico(diagnostico)
        self.tratamiento_text.config(state='normal')
        self.tratamiento_text.delete("1.0", tk.END)
        self.tratamiento_text.insert(tk.END, tratamiento)
        self.tratamiento_text.config(state='disabled')

    def actualizar_costo(self):
        costo_general_consulta = 50  # Costo general de la consulta
        costo_total = costo_general_consulta  # Inicializar con el costo de la consulta
        costo_vacunas = sum(
            [float(self.controlador_consulta.obtener_costo_vacuna(vacuna)) for vacuna, var in self.vacunas_vars.items()
             if var.get()])
        costo_total += costo_vacunas  # Sumar el costo de las vacunas seleccionadas
        self.costo_total_label.config(text=f"Costo Total: ${costo_total:.2f}")

    def guardar_consulta(self):
        mascota = self.mascota_combobox.get()
        veterinario = self.veterinario_combobox.get()
        diagnostico = self.diagnostico_combobox.get()
        tratamiento = self.tratamiento_text.get("1.0", tk.END).strip()
        observaciones = self.observaciones_text.get("1.0", tk.END).strip()
        vacunas_seleccionadas = [vacuna for vacuna, var in self.vacunas_vars.items() if var.get()]

        self.controlador_consulta.guardar_consulta(mascota, veterinario, diagnostico, tratamiento,
                                                   vacunas_seleccionadas, observaciones)
        self.destroy()
