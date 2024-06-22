import tkinter as tk
from tkinter import ttk
from datetime import datetime


class VistaConsulta(tk.Toplevel):
    def __init__(self, master=None, controlador_consulta=None):
        super().__init__(master)
        self.controlador_consulta = controlador_consulta
        self.title("Generar Consulta")
        self.geometry("900x700")
        self.resizable(False, False)  # Evitar que la ventana cambie de tamaño

        # Parte izquierda
        self.frame_izquierda = tk.Frame(self)
        self.frame_izquierda.pack(side=tk.LEFT, padx=20, pady=20)

        # Fecha de hoy
        self.fecha_label = tk.Label(self.frame_izquierda, text=f"Fecha: {datetime.now().strftime('%Y-%m-%d')}")
        self.fecha_label.pack(pady=10)

        # Combobox para elegir mascota
        self.mascota_label = tk.Label(self.frame_izquierda, text="Seleccionar Mascota:")
        self.mascota_label.pack(pady=5)

        self.mascotas = self.controlador_consulta.obtener_nombres_mascotas()
        self.mascota_combobox = ttk.Combobox(self.frame_izquierda, values=self.mascotas)
        self.mascota_combobox.pack(pady=5)
        self.mascota_combobox.bind("<<ComboboxSelected>>", self.actualizar_dueno_mascota)

        # Cuadro de texto para mostrar el dueño de la mascota
        self.dueno_label = tk.Label(self.frame_izquierda, text="Dueño de la Mascota:")
        self.dueno_label.pack(pady=5)
        self.dueno_text = tk.Entry(self.frame_izquierda, state='readonly', width=60)
        self.dueno_text.pack(pady=5)

        # Combobox para elegir veterinario
        self.veterinario_label = tk.Label(self.frame_izquierda, text="Seleccionar Veterinario:")
        self.veterinario_label.pack(pady=5)

        self.veterinarios = self.controlador_consulta.obtener_nombres_veterinarios()
        self.veterinario_combobox = ttk.Combobox(self.frame_izquierda, values=self.veterinarios)
        self.veterinario_combobox.pack(pady=5)
        self.veterinario_combobox.bind("<<ComboboxSelected>>", self.actualizar_matricula_veterinario)

        # Cuadro de texto para mostrar la matrícula del veterinario
        self.matricula_label = tk.Label(self.frame_izquierda, text="Matrícula del Veterinario:")
        self.matricula_label.pack(pady=5)
        self.matricula_text = tk.Entry(self.frame_izquierda, state='readonly', width=60)
        self.matricula_text.pack(pady=5)

        # Diagnóstico
        self.diagnostico_label = tk.Label(self.frame_izquierda, text="Seleccionar Diagnóstico:")
        self.diagnostico_label.pack(pady=5)

        self.diagnosticos = self.controlador_consulta.obtener_nombres_diagnosticos()
        self.diagnostico_combobox = ttk.Combobox(self.frame_izquierda, values=self.diagnosticos)
        self.diagnostico_combobox.pack(pady=5)
        self.diagnostico_combobox.bind("<<ComboboxSelected>>", self.cargar_tratamientos_relacionados)

        self.tratamiento_label = tk.Label(self.frame_izquierda, text="Seleccionar Tratamiento:")
        self.tratamiento_label.pack(pady=5)

        self.tratamientos_combobox = ttk.Combobox(self.frame_izquierda, values=[], state="readonly")
        self.tratamientos_combobox.pack(pady=5)
        self.tratamientos_combobox.bind("<<ComboboxSelected>>", self.mostrar_descripcion_tratamiento)

        self.descripcion_tratamiento_text = tk.Text(self.frame_izquierda, height=8, width=60, state='disabled')
        self.descripcion_tratamiento_text.pack(pady=5)

        # Observaciones
        self.observaciones_label = tk.Label(self.frame_izquierda, text="Observaciones:")
        self.observaciones_label.pack(pady=5)
        self.observaciones_text = tk.Text(self.frame_izquierda, height=5, width=60)
        self.observaciones_text.pack(pady=5)

        # Parte derecha
        self.frame_derecha = tk.Frame(self)
        self.frame_derecha.pack(side=tk.RIGHT, padx=20, pady=20)

        # Imagen
        self.imagen_label = tk.Label(self.frame_derecha)
        self.imagen_label.pack(pady=10)
        self.mostrar_imagen()

        # Checkboxes para vacunas
        self.vacunas_label = tk.Label(self.frame_derecha, text="Vacunas:")
        self.vacunas_label.pack(pady=5)

        self.vacunas_frame = tk.Frame(self.frame_derecha)
        self.vacunas_frame.pack(pady=5)

        self.vacunas = self.controlador_consulta.obtener_nombres_vacunas()
        self.vacunas_vars = {}

        for vacuna in self.vacunas:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(self.vacunas_frame, text=vacuna, variable=var, command=self.actualizar_costo)
            chk.pack(anchor='w')
            self.vacunas_vars[vacuna] = var

        # Etiqueta para mostrar el costo total
        self.costo_consulta_label = tk.Label(self.frame_derecha, text="Costo Consulta: $50.00")
        self.costo_consulta_label.pack(pady=10)

        # Etiqueta para mostrar el costo total
        self.costo_total_label = tk.Label(self.frame_derecha, text="Costo Total: $50.00")
        self.costo_total_label.pack(pady=10)

        # Botón para guardar consulta
        self.guardar_button = tk.Button(self.frame_derecha, text="Generar", command=self.guardar_consulta)
        self.guardar_button.pack(pady=10)

    def mostrar_imagen(self):
        imagen = tk.PhotoImage(file="Resources/Consulta.png")
        self.imagen_label.config(image=imagen)
        self.imagen_label.image = imagen

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
        tratamiento = self.descripcion_tratamiento_text.get("1.0", tk.END).strip()
        observaciones = self.observaciones_text.get("1.0", tk.END).strip()
        vacunas_seleccionadas = [vacuna for vacuna, var in self.vacunas_vars.items() if var.get()]

        costo_general_consulta = 50  # Costo general de la consulta
        costo_total = costo_general_consulta  # Inicializar con el costo de la consulta
        costo_vacunas = sum(
            [float(self.controlador_consulta.obtener_costo_vacuna(vacuna)) for vacuna, var in self.vacunas_vars.items()
             if var.get()])
        costo_total += costo_vacunas  # Sumar el costo de las vacunas seleccionadas

        self.controlador_consulta.guardar_consulta(mascota, veterinario, diagnostico, tratamiento,
                                                   vacunas_seleccionadas, observaciones, costo_total)
        self.destroy()

    def cargar_tratamientos_relacionados(self, event):
        diagnostico = self.diagnostico_combobox.get()
        tratamientos = self.controlador_consulta.tratamientos.buscar_tratamiento_por_diagnostico(diagnostico)
        if tratamientos:
            self.tratamientos_combobox.config(values=tratamientos, state="readonly")
            self.tratamientos_combobox.set('')
        else:
            self.tratamientos_combobox.config(values=[], state="readonly")
            self.descripcion_tratamiento_text.config(state='normal')
            self.descripcion_tratamiento_text.delete("1.0", tk.END)
            self.descripcion_tratamiento_text.insert(tk.END, "No se encontró tratamiento para el diagnóstico seleccionado")
            self.descripcion_tratamiento_text.config(state='disabled')

    def mostrar_descripcion_tratamiento(self, event):
        tratamiento = self.tratamientos_combobox.get()
        descripcion = self.controlador_consulta.obtener_descripcion_tratamientos(tratamiento)
        self.descripcion_tratamiento_text.config(state='normal')
        self.descripcion_tratamiento_text.delete("1.0", tk.END)
        self.descripcion_tratamiento_text.insert(tk.END, descripcion)
        self.descripcion_tratamiento_text.config(state='disabled')
