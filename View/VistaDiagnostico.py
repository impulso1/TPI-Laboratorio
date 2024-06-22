import tkinter as tk
from tkinter import messagebox, ttk

class VistaDiagnostico(tk.Toplevel):
    def __init__(self, diagnosticos, controlador_diagnostico):
        super().__init__()
        self.title("Diagnósticos")
        self.geometry("600x600")
        self.controlador_diagnostico = controlador_diagnostico

        label = tk.Label(self, text="Lista de Diagnósticos")
        label.pack(pady=10)

        self.listbox = tk.Listbox(self, width=80)
        self.listbox.pack()

        for diagnostico in diagnosticos:
            self.listbox.insert(tk.END, f"{diagnostico.nombre} - {diagnostico.sintomas} - {diagnostico.observaciones}")

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        crear_button = tk.Button(button_frame, text="Crear", command=self.crear_diagnostico)
        crear_button.pack(side=tk.LEFT, padx=10)

        modificar_button = tk.Button(button_frame, text="Modificar", command=self.modificar_diagnostico)
        modificar_button.pack(side=tk.LEFT, padx=10)

        eliminar_button = tk.Button(button_frame, text="Eliminar", command=self.eliminar_diagnostico)
        eliminar_button.pack(side=tk.LEFT, padx=10)

        mostrar_button = tk.Button(button_frame, text="Mostrar Tratamientos", command=self.mostrar_tratamientos)
        mostrar_button.pack(side=tk.LEFT, padx=5)

        cerrar_button = tk.Button(self, text="Cerrar", command=self.cerrar_ventana)
        cerrar_button.pack(pady=10)

        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

    def mostrar_tratamientos(self):
        seleccion = self.listbox.curselection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un diagnóstico.")
            return

        diagnostico_info = self.listbox.get(seleccion[0])
        nombre_diagnostico = diagnostico_info.split(" - ")[0]
        tratamientos = self.controlador_diagnostico.buscar_tratamiento_por_diagnostico(nombre_diagnostico)

        if not tratamientos:
            messagebox.showwarning("Advertencia", "No se encontraron tratamientos para el diagnóstico seleccionado.")
            return

        ventana_tratamientos = tk.Toplevel(self)
        ventana_tratamientos.title("Tratamientos")
        ventana_tratamientos.geometry("600x400")

        label = tk.Label(ventana_tratamientos, text=f"Tratamientos para {nombre_diagnostico}")
        label.pack(pady=10)

        self.tratamientos_combobox = ttk.Combobox(ventana_tratamientos, values=tratamientos)
        self.tratamientos_combobox.pack(pady=10)
        self.tratamientos_combobox.bind("<<ComboboxSelected>>", self.mostrar_descripcion_tratamiento)

        self.descripcion_tratamiento_text = tk.Text(ventana_tratamientos, height=8, width=60, state='disabled')
        self.descripcion_tratamiento_text.pack(pady=5)

    def mostrar_descripcion_tratamiento(self, event):
        tratamiento_nombre = self.tratamientos_combobox.get()
        descripcion = self.controlador_diagnostico.obtener_descripcion_tratamientos(tratamiento_nombre)
        self.descripcion_tratamiento_text.config(state='normal')
        self.descripcion_tratamiento_text.delete("1.0", tk.END)
        self.descripcion_tratamiento_text.insert(tk.END, descripcion)
        self.descripcion_tratamiento_text.config(state='disabled')

    def crear_diagnostico(self):
        self.mostrar_formulario_creacion()

    def mostrar_formulario_creacion(self):
        self.formulario_creacion = tk.Toplevel(self)
        self.formulario_creacion.title("Crear Diagnóstico")
        self.formulario_creacion.geometry("300x200")

        tk.Label(self.formulario_creacion, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self.formulario_creacion)
        self.nombre_entry.pack()

        tk.Label(self.formulario_creacion, text="Síntomas:").pack()
        self.sintomas_entry = tk.Entry(self.formulario_creacion)
        self.sintomas_entry.pack()

        tk.Label(self.formulario_creacion, text="Observaciones:").pack()
        self.observaciones_entry = tk.Entry(self.formulario_creacion)
        self.observaciones_entry.pack()

        tk.Button(self.formulario_creacion, text="Aceptar", command=self.crear_nuevo_diagnostico).pack()

    def crear_nuevo_diagnostico(self):
        nombre = self.nombre_entry.get()
        sintomas = self.sintomas_entry.get()
        observaciones = self.observaciones_entry.get()

        if nombre and sintomas and observaciones:
            self.controlador_diagnostico.nuevo_diagnostico(nombre, sintomas, observaciones)
            self.listbox.insert(tk.END, f"{nombre} - {sintomas} - {observaciones}")
            self.formulario_creacion.destroy()
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def modificar_diagnostico(self):
        index = self.listbox.curselection()
        if index:
            cod = int(index[0]) + 1
            diagnostico = self.controlador_diagnostico.buscar_objeto(cod)
            if diagnostico:
                self.mostrar_formulario_modificacion(diagnostico, cod)

    def mostrar_formulario_modificacion(self, diagnostico, cod):
        self.formulario_modificacion = tk.Toplevel(self)
        self.formulario_modificacion.title("Modificar Diagnóstico")
        self.formulario_modificacion.geometry("300x200")

        tk.Label(self.formulario_modificacion, text="Nombre:").pack()
        self.nombre_entry_mod = tk.Entry(self.formulario_modificacion)
        self.nombre_entry_mod.insert(0, diagnostico.nombre)
        self.nombre_entry_mod.pack()

        tk.Label(self.formulario_modificacion, text="Síntomas:").pack()
        self.sintomas_entry_mod = tk.Entry(self.formulario_modificacion)
        self.sintomas_entry_mod.insert(0, diagnostico.sintomas)
        self.sintomas_entry_mod.pack()

        tk.Label(self.formulario_modificacion, text="Observaciones:").pack()
        self.observaciones_entry_mod = tk.Entry(self.formulario_modificacion)
        self.observaciones_entry_mod.insert(0, diagnostico.observaciones)
        self.observaciones_entry_mod.pack()

        tk.Button(self.formulario_modificacion, text="Aceptar", command=lambda: self.modificar_diagnostico_confirmado(cod)).pack()

    def modificar_diagnostico_confirmado(self, cod):
        nombre = self.nombre_entry_mod.get()
        sintomas = self.sintomas_entry_mod.get()
        observaciones = self.observaciones_entry_mod.get()

        if nombre and sintomas and observaciones:
            self.controlador_diagnostico.modificar_diagnostico(cod, 1, nombre)
            self.controlador_diagnostico.modificar_diagnostico(cod, 2, sintomas)
            self.controlador_diagnostico.modificar_diagnostico(cod, 4, observaciones)
            self.listbox.delete(cod-1)
            self.listbox.insert(cod-1, f"{nombre} - {sintomas} - {observaciones}")
            self.formulario_modificacion.destroy()
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def eliminar_diagnostico(self):
        index = self.listbox.curselection()
        if index:
            cod = int(index[0]) + 1
            diagnostico = self.controlador_diagnostico.buscar_objeto(cod)
            if diagnostico:
                self.controlador_diagnostico.eliminar_diagnostico(diagnostico)
                self.listbox.delete(index)

    def cerrar_ventana(self):
        self.destroy()
