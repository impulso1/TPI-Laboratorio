class Factura:
    def __init__(self, fecha, veterinario, cliente, paciente, costo_total):
        self.fecha = fecha
        self.veterinario = veterinario
        self.cliente = cliente
        self.paciente = paciente
        self.costo_total = costo_total

    @classmethod
    def from_string(cls, factura_string):
        lines = factura_string.strip().split('\n')
        data = {}
        for line in lines:
            key, value = line.split(':', 1)
            data[key.strip()] = value.strip()
        return cls(
            fecha=data.get('Fecha', ''),
            veterinario=data.get('Veterinario', ''),
            cliente=data.get('Cliente', ''),
            paciente=data.get('Paciente', ''),
            costo_total=data.get('Costo total', '')
        )

    def __str__(self):
        return f"Fecha: {self.fecha}\nVeterinario: {self.veterinario}\nCliente: {self.cliente}\nPaciente: {self.paciente}\nCosto total: {self.costo_total}"

    def __repr__(self):
        return self.__str__()
