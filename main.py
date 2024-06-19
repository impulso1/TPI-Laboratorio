from Controller.ControladorGeneral import ControladorGeneral
from tkinter import Tk

if __name__ == "__main__":
    root = Tk()
    controlador_general = ControladorGeneral()
    vista_general = controlador_general.iniciar(root)

