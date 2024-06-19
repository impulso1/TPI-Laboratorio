# VistaRaza.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class VistaRaza(tk.Toplevel):
    def __init__(self, razas, controlador_raza):
        super().__init__()
        self.title("Razas")
        self.geometry("600x600")
        self.controlador_raza = controlador_raza

        label = tk.Label(self, text="Lista de Razas")
        label.pack(pady=10)

        self.listbox = tk.Listbox(self, width=80)
        self.listbox.pack()

        for raza in razas:
            self.listbox.insert(tk.END, str(raza))

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        crear_button = tk.Button(button_frame, text="Crear", command=self.crear_raza)
        crear_button.pack(side=tk.LEFT, padx=10)

        modificar_button = tk.Button(button_frame, text="Modificar", command=self.modificar_raza)
        modificar_button.pack(side=tk.LEFT, padx=10)

        eliminar_button = tk.Button(button_frame, text="Eliminar", command=self.eliminar_raza)
        eliminar_button.pack(side=tk.LEFT, padx=10)

        cerrar_button = tk.Button(self, text="Cerrar", command=self.cerrar_ventana)
        cerrar_button.pack(pady=10)

        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

    def crear_raza(self):
        self.mostrar_formulario_creacion()

    def mostrar_formulario_creacion(self):
        self.formulario_creacion = tk.Toplevel(self)
        self.formulario_creacion.title("Crear Raza")
        self.formulario_creacion.geometry("300x250")

        tk.Label(self.formulario_creacion, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self.formulario_creacion)
        self.nombre_entry.pack()

        tk.Label(self.formulario_creacion, text="Características:").pack()
        self.caracteristicas_entry = tk.Entry(self.formulario_creacion)
        self.caracteristicas_entry.pack()

        tk.Button(self.formulario_creacion, text="Aceptar", command=self.crear_nueva_raza).pack()

    def crear_nueva_raza(self):
        nombre = self.nombre_entry.get()
        caracteristicas = self.caracteristicas_entry.get()

        if nombre and caracteristicas:
            self.controlador_raza.crear_raza(nombre, caracteristicas)
            self.listbox.insert(tk.END, f"{nombre} - {caracteristicas}")
            self.formulario_creacion.destroy()
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def modificar_raza(self):
        index = self.listbox.curselection()
        if index:
            cod = int(index[0])
            raza = self.controlador_raza.buscar_raza(cod)
            if raza:
                self.mostrar_formulario_modificacion(raza, cod)

    def mostrar_formulario_modificacion(self, raza, cod):
        self.formulario_modificacion = tk.Toplevel(self)
        self.formulario_modificacion.title("Modificar Raza")
        self.formulario_modificacion.geometry("300x250")

        tk.Label(self.formulario_modificacion, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self.formulario_modificacion)
        self.nombre_entry.insert(0, raza.nombre)
        self.nombre_entry.pack()

        tk.Label(self.formulario_modificacion, text="Características:").pack()
        self.caracteristicas_entry = tk.Entry(self.formulario_modificacion)
        self.caracteristicas_entry.insert(0, raza.caracteristicas)
        self.caracteristicas_entry.pack()

        tk.Button(self.formulario_modificacion, text="Aceptar", command=lambda: self.actualizar_raza(cod)).pack()

    def actualizar_raza(self, cod):
        nombre = self.nombre_entry.get()
        caracteristicas = self.caracteristicas_entry.get()

        if nombre and caracteristicas:
            self.controlador_raza.listaRazas[cod].nombre = nombre
            self.controlador_raza.listaRazas[cod].caracteristicas = caracteristicas
            self.listbox.delete(cod)
            self.listbox.insert(cod, f"{nombre} - {caracteristicas}")
            self.formulario_modificacion.destroy()
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def eliminar_raza(self):
        index = self.listbox.curselection()
        if index:
            cod = int(index[0])
            if self.controlador_raza.eliminar_raza(cod):
                self.listbox.delete(index)

    def cerrar_ventana(self):
        self.guardar_y_cerrar()

    def guardar_y_cerrar(self):
        self.controlador_raza.guardar_archivo_razas()
        self.destroy()
