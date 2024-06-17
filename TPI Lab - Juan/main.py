from propietario import Propietario, DetallePropietario, Mascota, Raza
from veterinario import Veterinario
from consulta import Consulta, DetalleConsulta, Vacuna, Tratamiento

from Controlador.factura_controlador import FacturaController


def main():

    raza = Raza()
    mascota = Mascota()
    detalle_propietario = DetallePropietario()
    propietario = Propietario()

    veterinario = Veterinario()

    tratamiento = Tratamiento()
    vacuna = Vacuna()
    detalle_consulta = DetalleConsulta()
    consulta = Consulta()

    factura_controller = FacturaController(cliente=propietario, veterinario=veterinario, consulta=consulta)

    factura_controller.mostrar_factura()


"""
def main():
    raza = Raza(nombre="Galgo", caracteristicas="cachorro")
    mascota = Mascota(nombre="Ojito", especie="Perro", raza=raza, estado="Sano")
    detalle_propietario = DetallePropietario(mascota=mascota)
    propietario = Propietario(detalle_propietario=detalle_propietario, apellido="González", nombre="Juan")

    veterinario = Veterinario(cuil=12345678)

    tratamiento = Tratamiento(descripcion="Tratamiento de alergia", costo=200.0, duracion="2 semanas", indicaciones="Administrar medicamento dos veces al día")
    vacuna = Vacuna(nombre="Vacuna A", fechaVenc="2025-06-01", dosis="1 ml", costo=50.0, observaciones="Primera dosis")
    detalle_consulta = DetalleConsulta(vacuna=vacuna)
    consulta = Consulta(fecha="2024-06-01", veterinario=veterinario, diagnostico="Alergia estacional", tratamiento=tratamiento, vacunas=[detalle_consulta], observaciones="Seguir tratamiento por 2 semanas")

    factura_controller = FacturaController(cliente=propietario, veterinario=veterinario, consulta=consulta)
    
    factura_controller.mostrar_factura()
"""

if __name__ == "__main__":
    main()
