#Sistema de gestión de vehículos

class Vehiculo:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Precio: ${self.precio}"


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, precio, num_puertas):
        super().__init__(marca, modelo, año, precio)
        self.num_puertas = num_puertas

    def mostrar_info(self):
        return super().mostrar_info() + f", Puertas: {self.num_puertas}"


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, precio, cilindrada):
        super().__init__(marca, modelo, año, precio)
        self.cilindrada = cilindrada

    def mostrar_info(self):
        return super().mostrar_info() + f", Cilindrada: {self.cilindrada}cc"
