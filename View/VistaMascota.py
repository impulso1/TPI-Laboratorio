# VistaMascota.py
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class VistaMascota(tk.Toplevel):
    def __init__(self, mascotas, controlador_mascota, controlador_raza, controlador_propietario):
        super().__init__()
        self.title("Mascotas")
        self.geometry("600x600")
        self.controlador_mascota = controlador_mascota
        self.controlador_raza = controlador_raza
        self.controlador_propietario = controlador_propietario

        label = tk.Label(self, text="Lista de Mascotas")
        label.pack(pady=10)

        self.listbox = tk.Listbox(self, width=80)
        self.listbox.pack()

        for mascota in mascotas:
            self.listbox.insert(tk.END, str(mascota))

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        crear_button = tk.Button(button_frame, text="Crear", command=self.crear_mascota)
        crear_button.pack(side=tk.LEFT, padx=10)

        modificar_button = tk.Button(button_frame, text="Modificar", command=self.modificar_mascota)
        modificar_button.pack(side=tk.LEFT, padx=10)

        eliminar_button = tk.Button(button_frame, text="Eliminar", command=self.eliminar_mascota)
        eliminar_button.pack(side=tk.LEFT, padx=10)

        cerrar_button = tk.Button(self, text="Cerrar", command=self.cerrar_ventana)
        cerrar_button.pack(pady=10)

        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

    def crear_mascota(self):
        self.mostrar_formulario_creacion()

    def mostrar_formulario_creacion(self):
        self.formulario_creacion = tk.Toplevel(self)
        self.formulario_creacion.title("Crear Mascota")
        self.formulario_creacion.geometry("300x250")

        tk.Label(self.formulario_creacion, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self.formulario_creacion)
        self.nombre_entry.pack()

        tk.Label(self.formulario_creacion, text="Especie:").pack()
        self.especie_entry = tk.Entry(self.formulario_creacion)
        self.especie_entry.pack()

        tk.Label(self.formulario_creacion, text="Raza:").pack()
        razas_disponibles = [raza.nombre for raza in self.controlador_raza.listaRazas]
        self.raza_combobox = ttk.Combobox(self.formulario_creacion, values=razas_disponibles)
        self.raza_combobox.pack()

        tk.Label(self.formulario_creacion, text="Estado:").pack()
        self.estado_entry = tk.Entry(self.formulario_creacion)
        self.estado_entry.pack()

        tk.Label(self.formulario_creacion, text="Propietario:").pack()
        propietarios_disponibles = self.controlador_propietario.obtener_nombres_propietarios()
        self.propietario_combobox = ttk.Combobox(self.formulario_creacion, values=propietarios_disponibles)
        self.propietario_combobox.pack()

        tk.Button(self.formulario_creacion, text="Aceptar", command=self.crear_nueva_mascota).pack()

    def crear_nueva_mascota(self):
        nombre = self.nombre_entry.get()
        especie = self.especie_entry.get()
        raza = self.raza_combobox.get()
        estado = self.estado_entry.get()
        propietario = self.propietario_combobox.get()

        if nombre and especie and raza and estado:
            self.controlador_mascota.crear_mascota(nombre, especie, raza, estado, propietario)
            self.listbox.insert(tk.END, f"{nombre} - {especie} - {raza} - {estado} - {propietario}")
            self.formulario_creacion.destroy()
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def modificar_mascota(self):
        index = self.listbox.curselection()
        if index:
            cod = int(index[0]) + 1
            mascota = self.controlador_mascota.buscar_mascota(cod)
            if mascota:
                self.mostrar_formulario_modificacion(mascota, cod)

    def mostrar_formulario_modificacion(self, mascota, cod):
        self.formulario_modificacion = tk.Toplevel(self)
        self.formulario_modificacion.title("Modificar Mascota")
        self.formulario_modificacion.geometry("300x250")

        tk.Label(self.formulario_modificacion, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self.formulario_modificacion)
        self.nombre_entry.insert(0, mascota.nombre)
        self.nombre_entry.pack()

        tk.Label(self.formulario_modificacion, text="Especie:").pack()
        self.especie_entry = tk.Entry(self.formulario_modificacion)
        self.especie_entry.insert(0, mascota.especie)
        self.especie_entry.pack()

        tk.Label(self.formulario_modificacion, text="Raza:").pack()
        razas_disponibles = [raza.nombre for raza in self.controlador_raza.listaRazas]
        self.raza_combobox = ttk.Combobox(self.formulario_modificacion, values=razas_disponibles)
        self.raza_combobox.set(mascota.raza.nombre if mascota.raza else '')
        self.raza_combobox.pack()

        tk.Label(self.formulario_modificacion, text="Estado:").pack()
        self.estado_entry = tk.Entry(self.formulario_modificacion)
        self.estado_entry.insert(0, mascota.estado)
        self.estado_entry.pack()

        tk.Label(self.formulario_modificacion, text="Propietario:").pack()
        propietarios_disponibles = self.controlador_propietario.obtener_nombres_propietarios()
        self.propietario_combobox = ttk.Combobox(self.formulario_modificacion, values=propietarios_disponibles)
        self.propietario_combobox.set(mascota.propietario)
        self.propietario_combobox.pack()

        tk.Button(self.formulario_modificacion, text="Aceptar", command=lambda: self.actualizar_mascota(cod)).pack()

    def actualizar_mascota(self, cod):
        nombre = self.nombre


    def eliminar_mascota(self):
        index = self.listbox.curselection()
        if index:
            cod = int(index[0]) + 1
            mascota = self.controlador_mascota.buscar_mascota(cod)
            if mascota:
                self.controlador_mascota.eliminar_mascota(mascota)
                self.listbox.delete(index)

    def cerrar_ventana(self):
        self.guardar_y_cerrar()

    def guardar_y_cerrar(self):
        self.controlador_mascota.guardar_archivo_mascotas()
        self.destroy()
