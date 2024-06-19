class VistaRaza:

    @staticmethod
    def mostrar_raza(raza):
        if raza:
            print(f"Nombre: {raza.nombre}, Características: {raza.caracteristicas}")
        else:
            print("Raza no encontrada")

    @staticmethod
    def mostrar_todas_las_razas(razas: list):
        for raza in razas:
            VistaRaza.mostrar_raza(raza)
            print('---')