import tkinter as tk
from tkinter import messagebox


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
            self.listbox.insert(tk.END, str(diagnostico))

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        crear_button = tk.Button(button_frame, text="Crear", command=self.crear_diagnostico)
        crear_button.pack(side=tk.LEFT, padx=10)

        modificar_button = tk.Button(button_frame, text="Modificar", command=self.modificar_diagnostico)
        modificar_button.pack(side=tk.LEFT, padx=10)

        eliminar_button = tk.Button(button_frame, text="Eliminar", command=self.eliminar_diagnostico)
        eliminar_button.pack(side=tk.LEFT, padx=10)

        cerrar_button = tk.Button(self, text="Cerrar", command=self.cerrar_ventana)
        cerrar_button.pack(pady=10)

        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

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

        tk.Label(self.formulario_creacion, text="Tratamiento:").pack()
        self.tratamiento_entry = tk.Entry(self.formulario_creacion)
        self.tratamiento_entry.pack()

        tk.Label(self.formulario_creacion, text="Observaciones:").pack()
        self.observaciones_entry = tk.Entry(self.formulario_creacion)
        self.observaciones_entry.pack()

        tk.Button(self.formulario_creacion, text="Aceptar", command=self.crear_nuevo_diagnostico).pack()

    def crear_nuevo_diagnostico(self):
        nombre = self.nombre_entry.get()
        sintomas = self.sintomas_entry.get()
        tratamiento = self.tratamiento_entry.get()
        observaciones = self.observaciones_entry.get()

        if nombre and sintomas and tratamiento and observaciones:
            self.controlador_diagnostico.nuevo_diagnostico(nombre, sintomas, tratamiento, observaciones)
            self.listbox.insert(tk.END, f"{nombre} - {sintomas} - {tratamiento} - {observaciones}")
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
        self.nombre_entry = tk.Entry(self.formulario_modificacion)
        self.nombre_entry.insert(0, diagnostico.get_nombre())
        self.nombre_entry.pack()

        tk.Label(self.formulario_modificacion, text="Síntomas:").pack()
        self.sintomas_entry = tk.Entry(self.formulario_modificacion)
        self.sintomas_entry.insert(0, diagnostico.get_sintomas())
        self.sintomas_entry.pack()

        tk.Label(self.formulario_modificacion, text="Tratamiento:").pack()
        self.tratamiento_entry = tk.Entry(self.formulario_modificacion)
        self.tratamiento_entry.insert(0, diagnostico.get_tratamiento())
        self.tratamiento_entry.pack()

        tk.Label(self.formulario_modificacion, text="Observaciones:").pack()
        self.observaciones_entry = tk.Entry(self.formulario_modificacion)
        self.observaciones_entry.insert(0, diagnostico.get_observaciones())
        self.observaciones_entry.pack()

        tk.Button(self.formulario_modificacion, text="Aceptar", command=lambda: self.actualizar_diagnostico(cod)).pack()

    def actualizar_diagnostico(self, cod):
        nombre = self.nombre_entry.get()
        sintomas = self.sintomas_entry.get()
        tratamiento = self.tratamiento_entry.get()
        observaciones = self.observaciones_entry.get()

        if nombre and sintomas and tratamiento and observaciones:
            self.controlador_diagnostico.modificar_diagnostico(cod, nombre, sintomas, tratamiento, observaciones)
            self.listbox.delete(cod - 1)
            self.listbox.insert(cod - 1, f"{nombre} - {sintomas} - {tratamiento} - {observaciones}")
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
        self.controlador_diagnostico.guardar_archivo_diagnosticos()
        self.destroy()
