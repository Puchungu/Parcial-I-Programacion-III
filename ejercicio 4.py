class Vehiculo:
    def __init__(self, tipo_de_carro, marca_del_carro, modelo, costo_al_dia):
        self.tipo_de_carro = tipo_de_carro
        self.marca_del_carro = marca_del_carro
        self.modelo = modelo
        self.costo_al_dia = costo_al_dia
        self.disponible = True

    def __str__(self):
        disponibilidad = "Está disponible" if self.disponible else "No está disponible"
        return f"{self.tipo_de_carro} - {self.marca_del_carro} {self.modelo} - ${self.costo_al_dia} por día ({disponibilidad})"


class Cliente:
    def __init__(self, nombre_del_cliente, dui):
        self.nombre_del_cliente = nombre_del_cliente
        self.dui = dui

    def __str__(self):
        return f"Nombre: {self.nombre_del_cliente}, DUI: {self.dui}"


class Renta:
    def __init__(self):
        self.vehiculos = []

    def registrar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"Vehículo {vehiculo} registrado con éxito.")

    def alquilar_vehiculo(self, cliente, tipo_de_carro, dias):
        for vehiculo in self.vehiculos:
            if vehiculo.tipo_de_carro == tipo_de_carro and vehiculo.disponible:
                vehiculo.disponible = False
                costo_total = vehiculo.costo_al_dia * dias
                print(f"\nFactura para {cliente}")
                print(f"Vehículo alquilado: {vehiculo}")
                print(f"Número de días: {dias}")
                print(f"Subtotal alquiler: ${costo_total}")
                print("¡Gracias por su renta!")
                return

        print("Vehículo no disponible o tipo de vehículo no encontrado.")

    def mostrar_vehiculos(self):
        print("\nVehículos disponibles:")
        for vehiculo in self.vehiculos:
            print(vehiculo)


if __name__ == "__main__":
    # Creamos la instancia de la empresa que renta
    renta = Renta()

    # Registramos los carros 
    vehiculo1 = Vehiculo(tipo_de_carro="Sedán", marca_del_carro="Toyota", modelo="Camry", costo_al_dia=40)
    vehiculo2 = Vehiculo(tipo_de_carro="SUV", marca_del_carro="Honda", modelo="CR-V", costo_al_dia=60)
    vehiculo3 = Vehiculo(tipo_de_carro="Camioneta", marca_del_carro="Ford", modelo="F-150", costo_al_dia=70)

    renta.registrar_vehiculo(vehiculo1)
    renta.registrar_vehiculo(vehiculo2)
    renta.registrar_vehiculo(vehiculo3)

    # Mostramos los carros disponibles
    renta.mostrar_vehiculos()

    # Mostramos alquilar de un carro
    nombre_cliente = input("\nIngrese el nombre del cliente: ")
    dui_cliente = input("Ingrese el DUI del cliente: ")
    tipo_vehiculo = input("Ingrese el tipo de vehículo que desea alquilar (Sedán, SUV, Camioneta): ")
    dias = int(input("Ingrese el número de días de alquiler: "))

    cliente = Cliente(nombre_del_cliente=nombre_cliente, dui=dui_cliente)
    renta.alquilar_vehiculo(cliente, tipo_vehiculo, dias)

    # Mostramos carros después del alquilarlo 
    renta.mostrar_vehiculos()




    #Este código define un sistema simple de alquiler de vehículos. Incluye la capacidad de registrar vehículos, alquilarlos a clientes, y mostrar la disponibilidad de vehículos. El bloque principal del script maneja la interacción con el usuario para registrar vehículos, alquilar uno y mostrar la disponibilidad antes y después de cada alquiler.
