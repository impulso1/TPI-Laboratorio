

from controlador.diagnosticar import DiagnosticoController
from view.vista import DiagnosticoView

def main():
    controlador = DiagnosticoController()
    vista = DiagnosticoView()

    while True:
        vista.mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            datos = vista.obtener_datos_diagnostico()
            diagnostico = controlador.agregar_diagnostico(*datos)
            print("Diagnóstico agregado exitosamente.")
        elif opcion == "2":
            indice = int(input("Ingrese el índice del diagnóstico a ver: ")) - 1
            try:
                diagnostico = controlador.obtener_diagnostico(indice)
                vista.mostrar_diagnostico(diagnostico)
            except IndexError as e:
                print(e)
        elif opcion == "3":
            indice = int(input("Ingrese el índice del diagnóstico a actualizar: ")) - 1
            try:
                datos = vista.obtener_datos_diagnostico()
                diagnostico = controlador.actualizar_diagnostico(indice, *datos)
                print("Diagnóstico actualizado exitosamente.")
            except IndexError as e:
                print(e)
        elif opcion == "4":
            indice = int(input("Ingrese el índice del diagnóstico a eliminar: ")) - 1
            try:
                controlador.eliminar_diagnostico(indice)
                print("Diagnóstico eliminado exitosamente.")
            except IndexError as e:
                print(e)
        elif opcion == "5":
            vista.mostrar_todos_diagnosticos(controlador.diagnosticos)
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
