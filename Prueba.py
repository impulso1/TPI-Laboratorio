import tkinter as tk
from tkinter import ttk


# Funciones de ejemplo para manejar cada acción
def view_list(entity):
    print(f"Ver lista de {entity}")
    # Aquí iría el código para mostrar la lista de la entidad seleccionada


def add_item(entity):
    print(f"Agregar {entity}")
    # Aquí iría el código para agregar un nuevo elemento de la entidad seleccionada


def edit_item(entity):
    print(f"Modificar {entity}")
    # Aquí iría el código para modificar un elemento existente de la entidad seleccionada


def delete_item(entity):
    print(f"Eliminar {entity}")
    # Aquí iría el código para eliminar un elemento de la entidad seleccionada


# Crear la ventana principal
root = tk.Tk()
root.title("Menú Principal")
root.geometry("800x600")

# Crear un frame principal
mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Crear botones para cada entidad y acción
entities = ["Razas", "Personas", "Vacunas"]

for idx, entity in enumerate(entities):
    # Botón para ver lista
    view_button = ttk.Button(mainframe, text=f"Ver {entity}", command=lambda e=entity: view_list(e))
    view_button.grid(row=idx, column=0, padx=5, pady=5)

    # Botón para agregar
    add_button = ttk.Button(mainframe, text=f"Agregar {entity}", command=lambda e=entity: add_item(e))
    add_button.grid(row=idx, column=1, padx=5, pady=5)

    # Botón para modificar
    edit_button = ttk.Button(mainframe, text=f"Modificar {entity}", command=lambda e=entity: edit_item(e))
    edit_button.grid(row=idx, column=2, padx=5, pady=5)

    # Botón para eliminar
    delete_button = ttk.Button(mainframe, text=f"Eliminar {entity}", command=lambda e=entity: delete_item(e))
    delete_button.grid(row=idx, column=3, padx=5, pady=5)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()