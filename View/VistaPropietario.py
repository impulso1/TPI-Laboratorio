# VistaPropietarios.py
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class VistaPropietarios(tk.Toplevel):
    def __init__(self, propietarios, controlador_propietario):
        super().__init__()
        self.title("Propietarios")
        self.geometry("600x600")
        self.controlador_propietario = controlador_propietario

        label = tk.Label(self, text="Lista de Propietarios")
        label.pack(pady=10)

        self.listbox = tk.Listbox(self, width=80)
        self.listbox.pack()

        for propietario in propietarios:
            self.listbox.insert(tk.END, str(propietario))

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        crear_button = tk.Button(button_frame, text="Crear", command=self.crear_propietario)
        crear_button.pack(side=tk.LEFT, padx=10)

        modificar_button = tk.Button(button_frame, text="Modificar", command=self.modificar_propietario)
        modificar_button.pack(side=tk.LEFT, padx=10)

        eliminar_button = tk.Button(button_frame, text="Eliminar", command=self.eliminar_propietario)
        eliminar_button.pack(side=tk.LEFT, padx=10)

        cerrar_button = tk.Button(self, text="Cerrar", command=self.cerrar_ventana)
        cerrar_button.pack(pady=10)

        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

    def crear_propietario(self):
        self.mostrar_formulario_creacion()

    def mostrar_formulario_creacion(self):
        self.formulario_creacion = tk.Toplevel(self)
        self.formulario_creacion.title("Crear Propietario")
        self.formulario_creacion.geometry("300x200")

        tk.Label(self.formulario_creacion, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self.formulario_creacion)
        self.nombre_entry.pack()

        tk.Label(self.formulario_creacion, text="Apellido:").pack()
        self.apellido_entry = tk.Entry(self.formulario_creacion)
        self.apellido_entry.pack()

        tk.Label(self.formulario_creacion, text="Teléfono:").pack()
        self.telefono_entry = tk.Entry(self.formulario_creacion)
        self.telefono_entry.pack()

        tk.Label(self.formulario_creacion, text="Email:").pack()
        self.email_entry = tk.Entry(self.formulario_creacion)
        self.email_entry.pack()

        tk.Button(self.formulario_creacion, text="Aceptar", command=self.crear_nuevo_propietario).pack()

    def crear_nuevo_propietario(self):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        telefono = self.telefono_entry.get()
        email = self.email_entry.get()

        if nombre and apellido and telefono and email:
            self.controlador_propietario.nuevo_propietario(nombre, apellido, telefono, email)
            self.listbox.insert(tk.END, f"{nombre} {apellido} - {telefono} - {email}")
            self.formulario_creacion.destroy()
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def modificar_propietario(self):
        index = self.listbox.curselection()
        if index:
            cod = int(index[0]) + 1
            propietario = self.controlador_propietario.buscar_objeto(cod)
            if propietario:
                self.mostrar_formulario_modificacion(propietario, cod)

    def mostrar_formulario_modificacion(self, propietario, cod):
        self.formulario_modificacion = tk.Toplevel(self)
        self.formulario_modificacion.title("Modificar Propietario")
        self.formulario_modificacion.geometry("300x200")

        tk.Label(self.formulario_modificacion, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self.formulario_modificacion)
        self.nombre_entry.insert(0, propietario.nombre)
        self.nombre_entry.pack()

        tk.Label(self.formulario_modificacion, text="Apellido:").pack()
        self.apellido_entry = tk.Entry(self.formulario_modificacion)
        self.apellido_entry.insert(0, propietario.apellido)
        self.apellido_entry.pack()

        tk.Label(self.formulario_modificacion, text="Teléfono:").pack()
        self.telefono_entry = tk.Entry(self.formulario_modificacion)
        self.telefono_entry.insert(0, propietario.telefono)
        self.telefono_entry.pack()

        tk.Label(self.formulario_modificacion, text="Email:").pack()
        self.email_entry = tk.Entry(self.formulario_modificacion)
        self.email_entry.insert(0, propietario.mail)
        self.email_entry.pack()

        tk.Button(self.formulario_modificacion, text="Aceptar", command=lambda: self.actualizar_propietario(cod)).pack()

    def actualizar_propietario(self, cod):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        telefono = self.telefono_entry.get()
        email = self.email_entry.get()

        if nombre and apellido and telefono and email:
            self.controlador_propietario.modificar_propietario(cod, 1, nombre)
            self.controlador_propietario.modificar_propietario(cod, 2, apellido)
            self.controlador_propietario.modificar_propietario(cod, 3, telefono)
            self.controlador_propietario.modificar_propietario(cod, 4, email)
            self.listbox.delete(cod - 1)
            self.listbox.insert(cod - 1, f"{nombre} {apellido} - {telefono} - {email}")
            self.formulario_modificacion.destroy()
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def eliminar_propietario(self):
        index = self.listbox.curselection()
        if index:
            cod = int(index[0]) + 1
            propietario = self.controlador_propietario.buscar_objeto(cod)
            if propietario:
                self.controlador_propietario.listaPropietarios.remove(propietario)
                self.listbox.delete(index)

    def cerrar_ventana(self):
        self.controlador_propietario.guardar_archivo_propietarios()
        self.destroy()
