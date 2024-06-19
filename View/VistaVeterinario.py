import tkinter as tk
from tkinter import messagebox

class VistaVeterinarios(tk.Toplevel):
    def __init__(self, veterinarios, controlador_veterinario):
        super().__init__()
        self.title("Veterinarios")
        self.geometry("600x600")
        self.controlador_veterinario = controlador_veterinario

        label = tk.Label(self, text="Lista de Veterinarios")
        label.pack(pady=10)

        self.listbox = tk.Listbox(self, width=80)
        self.listbox.pack()

        for veterinario in veterinarios:
            self.listbox.insert(tk.END, str(veterinario))

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        crear_button = tk.Button(button_frame, text="Crear", command=self.crear_veterinario)
        crear_button.pack(side=tk.LEFT, padx=10)

        modificar_button = tk.Button(button_frame, text="Modificar", command=self.modificar_veterinario)
        modificar_button.pack(side=tk.LEFT, padx=10)

        eliminar_button = tk.Button(button_frame, text="Eliminar", command=self.eliminar_veterinario)
        eliminar_button.pack(side=tk.LEFT, padx=10)

        cerrar_button = tk.Button(self, text="Cerrar", command=self.cerrar_ventana)
        cerrar_button.pack(pady=10)

        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

    def crear_veterinario(self):
        self.mostrar_formulario_creacion()

    def mostrar_formulario_creacion(self):
        self.formulario_creacion = tk.Toplevel(self)
        self.formulario_creacion.title("Crear Veterinario")
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

        tk.Label(self.formulario_creacion, text="Matrícula:").pack()
        self.matricula_entry = tk.Entry(self.formulario_creacion)
        self.matricula_entry.pack()

        tk.Button(self.formulario_creacion, text="Aceptar", command=self.crear_nuevo_veterinario).pack()

    def crear_nuevo_veterinario(self):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        telefono = self.telefono_entry.get()
        email = self.email_entry.get()
        matricula = self.matricula_entry.get()

        if nombre and apellido and telefono and email and matricula:
            self.controlador_veterinario.nuevo_veterinario(nombre, apellido, telefono, email, matricula)
            self.listbox.insert(tk.END, f"{nombre} {apellido} - {telefono} - {email} - {matricula}")
            self.formulario_creacion.destroy()
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def modificar_veterinario(self):
        index = self.listbox.curselection()
        if index:
            cod = int(index[0]) + 1
            veterinario = self.controlador_veterinario.buscar_objeto(cod)
            if veterinario:
                self.mostrar_formulario_modificacion(veterinario, cod)

    def mostrar_formulario_modificacion(self, veterinario, cod):
        self.formulario_modificacion = tk.Toplevel(self)
        self.formulario_modificacion.title("Modificar Veterinario")
        self.formulario_modificacion.geometry("300x200")

        tk.Label(self.formulario_modificacion, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self.formulario_modificacion)
        self.nombre_entry.insert(0, veterinario.nombre)
        self.nombre_entry.pack()

        tk.Label(self.formulario_modificacion, text="Apellido:").pack()
        self.apellido_entry = tk.Entry(self.formulario_modificacion)
        self.apellido_entry.insert(0, veterinario.apellido)
        self.apellido_entry.pack()

        tk.Label(self.formulario_modificacion, text="Teléfono:").pack()
        self.telefono_entry = tk.Entry(self.formulario_modificacion)
        self.telefono_entry.insert(0, veterinario.telefono)
        self.telefono_entry.pack()

        tk.Label(self.formulario_modificacion, text="Email:").pack()
        self.email_entry = tk.Entry(self.formulario_modificacion)
        self.email_entry.insert(0, veterinario.email)
        self.email_entry.pack()

        tk.Label(self.formulario_modificacion, text="Matrícula:").pack()
        self.matricula_entry = tk.Entry(self.formulario_modificacion)
        self.matricula_entry.insert(0, veterinario.matricula)
        self.matricula_entry.pack()

        tk.Button(self.formulario_modificacion, text="Aceptar", command=lambda: self.actualizar_veterinario(cod)).pack()

    def actualizar_veterinario(self, cod):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        telefono = self.telefono_entry.get()
        email = self.email_entry.get()
        matricula = self.matricula_entry.get()

        if nombre and apellido and telefono and email and matricula:
            self.controlador_veterinario.modificar_veterinario(cod, nombre, apellido, telefono, email, matricula)
            self.listbox.delete(cod - 1)
            self.listbox.insert(cod - 1, f"{nombre} {apellido} - {telefono} - {email} - {matricula}")
            self.formulario_modificacion.destroy()
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def eliminar_veterinario(self):
        index = self.listbox.curselection()
        if index:
            cod = int(index[0]) + 1
            veterinario = self.controlador_veterinario.buscar_objeto(cod)
            if veterinario:
                self.controlador_veterinario.listaVeterinarios.remove(veterinario)
                self.listbox.delete(index)

    def cerrar_ventana(self):
        self.controlador_veterinario.guardar_archivo_veterinarios()
        self.destroy()
