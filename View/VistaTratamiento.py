import tkinter as tk
from tkinter import messagebox, ttk

class VistaTratamiento(tk.Toplevel):
    def __init__(self, tratamientos, controlador_tratamiento):
        super().__init__()
        self.title("Tratamientos")
        self.geometry("600x600")
        self.controlador_tratamiento = controlador_tratamiento

        label = tk.Label(self, text="Lista de Tratamientos")
        label.pack(pady=10)

        self.listbox = tk.Listbox(self, width=80)
        self.listbox.pack()

        for tratamiento in tratamientos:
            self.listbox.insert(tk.END, str(tratamiento))

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        crear_button = tk.Button(button_frame, text="Crear", command=self.crear_tratamiento)
        crear_button.pack(side=tk.LEFT, padx=10)

        modificar_button = tk.Button(button_frame, text="Modificar", command=self.modificar_tratamiento)
        modificar_button.pack(side=tk.LEFT, padx=10)

        eliminar_button = tk.Button(button_frame, text="Eliminar", command=self.eliminar_tratamiento)
        eliminar_button.pack(side=tk.LEFT, padx=10)

        mostrar_button = tk.Button(button_frame, text="Mostrar", command=self.mostrar_tratamiento_completo)
        mostrar_button.pack(side=tk.LEFT, padx=10)

        cerrar_button = tk.Button(self, text="Cerrar", command=self.cerrar_ventana)
        cerrar_button.pack(pady=10)

        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

    def crear_tratamiento(self):
        self.mostrar_formulario_creacion()

    def mostrar_formulario_creacion(self):
        self.formulario_creacion = tk.Toplevel(self)
        self.formulario_creacion.title("Crear Tratamiento")
        self.formulario_creacion.geometry("300x250")

        tk.Label(self.formulario_creacion, text="Diagnóstico:").pack()
        self.diagnostico_combobox = ttk.Combobox(self.formulario_creacion, values=self.controlador_tratamiento.obtener_lista_nombres_diagnosticos())
        self.diagnostico_combobox.pack()

        tk.Label(self.formulario_creacion, text="Descripción:").pack()
        self.descripcion_entry = tk.Entry(self.formulario_creacion)
        self.descripcion_entry.pack()

        tk.Label(self.formulario_creacion, text="Duración:").pack()
        self.duracion_entry = tk.Entry(self.formulario_creacion)
        self.duracion_entry.pack()

        tk.Label(self.formulario_creacion, text="Indicaciones:").pack()
        self.indicaciones_entry = tk.Entry(self.formulario_creacion)
        self.indicaciones_entry.pack()

        tk.Button(self.formulario_creacion, text="Aceptar", command=self.crear_nuevo_tratamiento).pack()

    def crear_nuevo_tratamiento(self):
        nombrediagnostico = self.diagnostico_combobox.get()
        descripcion = self.descripcion_entry.get()
        duracion = self.duracion_entry.get()
        indicaciones = self.indicaciones_entry.get()

        if nombrediagnostico and descripcion and duracion and indicaciones:
            self.controlador_tratamiento.nuevo_tratamiento(nombrediagnostico, descripcion, duracion, indicaciones)
            self.listbox.insert(tk.END, f"{nombrediagnostico} - {descripcion} - {duracion} - {indicaciones}")
            self.formulario_creacion.destroy()
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def modificar_tratamiento(self):
        index = self.listbox.curselection()
        if index:
            cod = int(index[0]) + 1
            tratamiento = self.controlador_tratamiento.buscar_objeto(cod)
            if tratamiento:
                self.mostrar_formulario_modificacion(tratamiento, cod)

    def mostrar_formulario_modificacion(self, tratamiento, cod):
        self.formulario_modificacion = tk.Toplevel(self)
        self.formulario_modificacion.title("Modificar Tratamiento")
        self.formulario_modificacion.geometry("300x250")

        tk.Label(self.formulario_modificacion, text="Diagnóstico:").pack()
        self.diagnostico_combobox = ttk.Combobox(self.formulario_modificacion, values=self.controlador_tratamiento.obtener_lista_nombres_diagnosticos())
        self.diagnostico_combobox.set(tratamiento.diagnostico.nombre)
        self.diagnostico_combobox.pack()

        tk.Label(self.formulario_modificacion, text="Descripción:").pack()
        self.descripcion_entry = tk.Entry(self.formulario_modificacion)
        self.descripcion_entry.insert(0, tratamiento.descripcion)
        self.descripcion_entry.pack()

        tk.Label(self.formulario_modificacion, text="Duración:").pack()
        self.duracion_entry = tk.Entry(self.formulario_modificacion)
        self.duracion_entry.insert(0, tratamiento.duracion)
        self.duracion_entry.pack()

        tk.Label(self.formulario_modificacion, text="Indicaciones:").pack()
        self.indicaciones_entry = tk.Entry(self.formulario_modificacion)
        self.indicaciones_entry.insert(0, tratamiento.indicaciones)
        self.indicaciones_entry.pack()

        tk.Button(self.formulario_modificacion, text="Aceptar", command=lambda: self.actualizar_tratamiento(cod)).pack()

    def actualizar_tratamiento(self, cod):
        nombrediagnostico = self.diagnostico_combobox.get()
        descripcion = self.descripcion_entry.get()
        duracion = self.duracion_entry.get()
        indicaciones = self.indicaciones_entry.get()

        if nombrediagnostico and descripcion and duracion and indicaciones:
            self.controlador_tratamiento.modificar_tratamiento(cod, nombrediagnostico, descripcion, duracion, indicaciones)
            self.listbox.delete(cod - 1)
            self.listbox.insert(cod - 1, f"{nombrediagnostico} - {descripcion} - {duracion} - {indicaciones}")
            self.formulario_modificacion.destroy()
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def eliminar_tratamiento(self):
        index = self.listbox.curselection()
        if index:
            cod = int(index[0]) + 1
            tratamiento = self.controlador_tratamiento.buscar_objeto(cod)
            if tratamiento:
                self.controlador_tratamiento.eliminar_tratamiento(tratamiento)
                self.listbox.delete(index)

    def cerrar_ventana(self):
        self.controlador_tratamiento.guardar_archivo_tratamientos()
        self.destroy()

    def mostrar_tratamiento_completo(self):
        index = self.listbox.curselection()
        if index:
            cod = int(index[0]) + 1
            tratamiento = self.controlador_tratamiento.buscar_objeto(cod)
            if tratamiento:
                self.mostrar_ventana_tratamiento_completo(tratamiento)

    def mostrar_ventana_tratamiento_completo(self, tratamiento):
        ventana_tratamiento = tk.Toplevel(self)
        ventana_tratamiento.title("Información del Tratamiento")
        ventana_tratamiento.geometry("1000x400")

        tk.Label(ventana_tratamiento, text="Descripción:").pack()
        tk.Label(ventana_tratamiento, text=tratamiento.descripcion).pack()

        tk.Label(ventana_tratamiento, text="Duración:").pack()
        tk.Label(ventana_tratamiento, text=tratamiento.duracion).pack()

        tk.Label(ventana_tratamiento, text="Indicaciones:").pack()
        tk.Label(ventana_tratamiento, text=tratamiento.indicaciones).pack()
