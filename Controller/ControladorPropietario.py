from Model.Propietario import Propietario


class ControladorPropietario:
    def __init__(self):
        self.listaPropietarios = []

    def cargar_archivo_propietarios(self):
        with open("Resources/Propietarios.txt", "r") as file:
            renglones = file.readlines()
        for renglon in renglones:
            valores = renglon.strip().split(",")
            if len(valores) == 4:
                nombre, apellido, telefono, mail = valores
                self.listaPropietarios.append(Propietario(nombre, apellido, telefono, mail))

    def obtener_nombres_propietarios(self):
        return [str(propietario) for propietario in self.listaPropietarios]

    def nuevo_propietario(self, nombre, apellido, telefono, mail):
        self.listaPropietarios.append(Propietario(nombre, apellido, telefono, mail))

    def modificar_propietario(self, vet, opc, new):
        obj = self.buscar_objeto(vet)
        if opc == 1:
            obj.nombre = new
        elif opc == 2:
            obj.apellido = new
        elif opc == 3:
            obj.telefono = new
        elif opc == 4:
            obj.mail = new

    def buscar_objeto(self, cod):
        for i, propietario in enumerate(self.listaPropietarios, start=1):
            if i == int(cod):
                return propietario

    def buscar_propietario_por_nombre(self, nombre):
        for propietario in self.listaPropietarios:
            if propietario.nombre == nombre:
                return propietario
        return None

    def agregar_mascota(self, propietario, mascota):
        if mascota not in propietario.mascotas:
            propietario.mascotas.append(mascota)

    def mostrar_propietarios(self):
        return self.listaPropietarios

    def guardar_archivo_propietarios(self):
        with open("Resources/Propietarios.txt", "w") as file:
            for propietario in self.listaPropietarios:
                file.write(f"{propietario.nombre},{propietario.apellido},{propietario.telefono},{propietario.mail}\n")
