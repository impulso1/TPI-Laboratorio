class VistaMascota:
    @staticmethod
    def mostrar_mascota(mascota):
        if mascota:
            print(
                f"Nombre: {mascota.nombre}, Especie: {mascota.especie}, Raza: {mascota.raza.nombre if mascota.raza else 'Sin raza'}, Estado: {mascota.estado}, Propietario: {mascota.propietario}")
        else:
            print("Mascota no registrada")

    @staticmethod
    def mostrar_todas_las_mascotas(mascotas: list):
        for mascota in mascotas:
            VistaMascota.mostrar_mascota(mascota)
