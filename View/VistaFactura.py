class FacturaVista:

    def mostrar_factura(self):
        cliente = self.factura.get_cliente()
        consulta = self.factura.get_consulta()


        apellido_cliente = cliente.get_apellido()
        nombre_cliente = cliente.get_nombre()
        nombre_mascota = cliente.get_mascota().get_nombre()

        costos_vacunas = []
        for i, detalle in enumerate(consulta.get_vacunas(), start=1):
            vacuna = detalle.get_vacuna()
            costo_vacuna = vacuna.get_costo()
            costos_vacunas.append(costo_vacuna)


        costo_total = self.factura.get_costoTotal()


        fecha_consulta = consulta.get_fecha().strftime("%d/%m/%Y")


        print("Factura")
        print(f"Cliente: {apellido_cliente}, {nombre_cliente}")
        print(f"Mascota: {nombre_mascota}")
        print(f"Fecha de la Consulta: {fecha_consulta}")
        print(f"Tratamiento: {consulta.get_tratamiento().get_costo()}")
        print("Vacunas:")
        for i, costo_vacuna in enumerate(costos_vacunas):
            print(f"Vacuna {i + 1}: {costo_vacuna}")
        print(f"Costo Total: ${costo_total}")
