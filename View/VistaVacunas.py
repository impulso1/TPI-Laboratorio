import tkinter as tk
from tkinter import messagebox

class VistaVacunas(tk.Toplevel):
    def __init__(self, vacunas, controlador_vacuna):
        super().__init__()
        self.title("Vacunas")
        self.geometry("600x600")
        self.controlador_vacuna = controlador_vacuna

        label = tk.Label(self, text="Lista de Vacunas")
        label.pack(pady=10)

        self.listbox = tk.Listbox(self, width=80)
        self.listbox.pack()

        for vacuna in vacunas:
            self.listbox.insert(tk.END, str(vacuna))

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        crear_button = tk.Button(button_frame, text="Crear", command=self.crear_vacuna)
        crear_button.pack(side=tk.LEFT, padx=10)

        modificar_button = tk.Button(button_frame, text="Modificar", command=self.modificar_vacuna)
        modificar_button.pack(side=tk.LEFT, padx=10)

        eliminar_button = tk.Button(button_frame, text="Eliminar", command=self.eliminar_vacuna)
        eliminar_button.pack(side=tk.LEFT, padx=10)

        cerrar_button = tk.Button(self, text="Cerrar", command=self.cerrar_ventana)
        cerrar_button.pack(pady=10)

        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

    def crear_vacuna(self):
        self.mostrar_formulario_creacion()

    def mostrar_formulario_creacion(self):
        self.formulario_creacion = tk.Toplevel(self)
        self.formulario_creacion.title("Crear Vacuna")
        self.formulario_creacion.geometry("300x300")

        tk.Label(self.formulario_creacion, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self.formulario_creacion)
        self.nombre_entry.pack()

        tk.Label(self.formulario_creacion, text="Fecha de Vencimiento:").pack()
        self.fecha_ven_entry = tk.Entry(self.formulario_creacion)
        self.fecha_ven_entry.pack()

        tk.Label(self.formulario_creacion, text="Dosis:").pack()
        self.dosis_entry = tk.Entry(self.formulario_creacion)
        self.dosis_entry.pack()

        tk.Label(self.formulario_creacion, text="Costo:").pack()
        self.costo_entry = tk.Entry(self.formulario_creacion)
        self.costo_entry.pack()

        tk.Label(self.formulario_creacion, text="Observaciones:").pack()
        self.observaciones_entry = tk.Entry(self.formulario_creacion)
        self.observaciones_entry.pack()

        tk.Button(self.formulario_creacion, text="Aceptar", command=self.crear_nueva_vacuna).pack()

    def crear_nueva_vacuna(self):
        nombre = self.nombre_entry.get()
        fecha_ven = self.fecha_ven_entry.get()
        dosis = self.dosis_entry.get()
        costo = self.costo_entry.get()
        observaciones = self.observaciones_entry.get()

        if nombre and fecha_ven and dosis and costo and observaciones:
            self.controlador_vacuna.nuevo_vacuna(nombre, fecha_ven, dosis, costo, observaciones)
            self.listbox.insert(tk.END, f"{nombre} - {fecha_ven} - {dosis} - {costo} - {observaciones}")
            self.formulario_creacion.destroy()
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def modificar_vacuna(self):
        index = self.listbox.curselection()
        if index:
            cod = int(index[0]) + 1
            vacuna = self.controlador_vacuna.buscar_objeto(cod)
            if vacuna:
                self.mostrar_formulario_modificacion(vacuna, cod)

    def mostrar_formulario_modificacion(self, vacuna, cod):
        self.formulario_modificacion = tk.Toplevel(self)
        self.formulario_modificacion.title("Modificar Vacuna")
        self.formulario_modificacion.geometry("300x300")

        tk.Label(self.formulario_modificacion, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self.formulario_modificacion)
        self.nombre_entry.insert(0, vacuna.nombre)
        self.nombre_entry.pack()

        tk.Label(self.formulario_modificacion, text="Fecha de Vencimiento:").pack()
        self.fecha_ven_entry = tk.Entry(self.formulario_modificacion)
        self.fecha_ven_entry.insert(0, vacuna.fecha_ven)
        self.fecha_ven_entry.pack()

        tk.Label(self.formulario_modificacion, text="Dosis:").pack()
        self.dosis_entry = tk.Entry(self.formulario_modificacion)
        self.dosis_entry.insert(0, vacuna.dosis)
        self.dosis_entry.pack()

        tk.Label(self.formulario_modificacion, text="Costo:").pack()
        self.costo_entry = tk.Entry(self.formulario_modificacion)
        self.costo_entry.insert(0, vacuna.costo)
        self.costo_entry.pack()

        tk.Label(self.formulario_modificacion, text="Observaciones:").pack()
        self.observaciones_entry = tk.Entry(self.formulario_modificacion)
        self.observaciones_entry.insert(0, vacuna.observaciones)
        self.observaciones_entry.pack()

        tk.Button(self.formulario_modificacion, text="Aceptar", command=lambda: self.actualizar_vacuna(cod)).pack()

    def actualizar_vacuna(self, cod):
        nombre = self.nombre_entry.get()
        fecha_ven = self.fecha_ven_entry.get()
        dosis = self.dosis_entry.get()
        costo = self.costo_entry.get()
        observaciones = self.observaciones_entry.get()

        if nombre and fecha_ven and dosis and costo and observaciones:
            self.controlador_vacuna.modificar_vacuna(cod, nombre, fecha_ven, dosis, costo, observaciones)
            self.listbox.delete(cod - 1)
            self.listbox.insert(cod - 1, f"{nombre} - {fecha_ven} - {dosis} - {costo} - {observaciones}")
            self.formulario_modificacion.destroy()
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def eliminar_vacuna(self):
        index = self.listbox.curselection()
        if index:
            cod = int(index[0]) + 1
            vacuna = self.controlador_vacuna.buscar_objeto(cod)
            if vacuna:
                self.controlador_vacuna.eliminar_vacuna(vacuna)
                self.listbox.delete(index)

    def cerrar_ventana(self):
        self.controlador_vacuna.guardar_archivo_vacunas()
        self.destroy()
