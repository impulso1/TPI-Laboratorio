class DiagnosticoView:
    def mostrar_diagnostico(self, diagnostico):
        print(f"Nombre: {diagnostico.get_nombre()}")
        print(f"Sintomas: {diagnostico.get_sintomas()}")
        tratamiento = diagnostico.get_tratamiento()
        print("Tratamiento:")
        print(f"  Descripción: {tratamiento.descripcion}")
        print(f"  Costo: {tratamiento.costo}")
        print(f"  Duración: {tratamiento.duracion}")
        print(f"  Indicaciones: {tratamiento.indicaciones}")
        print(f"Observaciones: {diagnostico.get_observaciones()}")
        print("\n")

    def mostrar_todos_diagnosticos(self, diagnosticos):
        for i, diagnostico in enumerate(diagnosticos):
            print(f"Diagnóstico {i + 1}:")
            self.mostrar_diagnostico(diagnostico)

    def obtener_datos_diagnostico(self):
        nombre = input("Ingrese el nombre del diagnóstico: ")
        sintomas = input("Ingrese los síntomas: ")
        descripcion_tratamiento = input("Ingrese la descripción del tratamiento: ")
        costo_tratamiento = float(input("Ingrese el costo del tratamiento: "))
        duracion_tratamiento = float(input("Ingrese la duración del tratamiento: "))
        indicaciones_tratamiento = input("Ingrese las indicaciones del tratamiento: ")
        observaciones = input("Ingrese las observaciones: ")
        return nombre, sintomas, descripcion_tratamiento, costo_tratamiento, duracion_tratamiento, indicaciones_tratamiento, observaciones

    def mostrar_menu(self):
        print("1. Agregar diagnóstico")
        print("2. Ver diagnóstico")
        print("3. Actualizar diagnóstico")
        print("4. Eliminar diagnóstico")
        print("5. Ver todos los diagnósticos")
        print("6. Salir")
