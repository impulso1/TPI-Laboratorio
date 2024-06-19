import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class VistaGeneral(tk.Frame):
    def __init__(self, master=None, controlador_general=None):
        super().__init__(master)
        self.master = master
        self.controlador_general = controlador_general
        self.master.geometry("1132x700")
        self.master.title("Vista General")
        self.master.resizable(False, False)  # Deshabilitar el cambio de tamaño

        # Columna izquierda con la imagen de fondo
        left_frame = tk.Frame(self.master, width=432, height=700)
        left_frame.pack(side=tk.LEFT)
        banner_image = tk.PhotoImage(file="Resources/banner.png")
        banner_label = tk.Label(left_frame, image=banner_image)
        banner_label.image = banner_image  # Keep a reference to the image to prevent garbage collection
        banner_label.pack()

        # Columna derecha
        right_frame = tk.Frame(self.master, width=700, height=700)
        right_frame.pack(side=tk.LEFT, padx=50)  # Ajusta el padx para mover la columna derecha más a la izquierda

        # Definir las fuentes
        bold_font = tkFont.Font(family="Arial", size=22, weight="bold")
        italic_font = tkFont.Font(family="Arial", size=16, slant="italic")

        # Título grande en negritas
        welcome_label = tk.Label(right_frame, text="Bienvenido a la Veterinaria de las Sierras", font=bold_font)
        welcome_label.pack(pady=20)

        # Subtítulo más pequeño en itálica
        system_label = tk.Label(right_frame, text="Sistema de gestión veterinaria", font=italic_font)
        system_label.pack(pady=10)

        # Botón "Generar consulta"
        generarconsulta_button = tk.Button(right_frame, text="GENERAR CONSULTA",
                                           command=lambda: self.controlador_general.abrir_vista_consulta(self.master),
                                           font=(bold_font, 12), width=20, height=2)
        generarconsulta_button.pack(pady=10)

        # Etiqueta sobre el Combobox
        info_label = tk.Label(right_frame, text="Ver/Modificar información de:", font=("Arial", 12))
        info_label.pack(pady=10)

        # Combobox con ancho de 100px
        self.selected_option = tk.StringVar(value="Mascotas (Activas)")  # Selección por defecto
        self.combobox = ttk.Combobox(right_frame, textvariable=self.selected_option, values=[
            "Mascotas (Activas)",
            "Tratamientos",
            "Diagnosticos",
            "Vacunas",
            "Razas",
            "Veterinarios",
            "Clientes (Propietarios)"
        ], width=20)
        self.combobox.pack(pady=10)

        # Botón "Aceptar" con ancho de 100px
        accept_button = tk.Button(right_frame, text="Aceptar",
                                  command=lambda: self.controlador_general.aceptar_accion(self), font=("Arial", 12),
                                  width=10)

        accept_button.pack(pady=10)

        self.pack()

