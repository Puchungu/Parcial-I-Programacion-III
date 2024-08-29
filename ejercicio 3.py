class Habitacion:
    def __init__(self, tipo_de_habitacion, precio):
        self.tipo_de_habitacion = tipo_de_habitacion
        self.precio = precio

    def __str__(self):
        return f"{self.tipo_de_habitacion} - ${self.precio} por la noche"


class ServicioExtra:
    def __init__(self, nombre_servicio, costo):
        self.nombre_servicio = nombre_servicio
        self.costo = costo

    def __str__(self):
        return f"{self.nombre_servicio} - ${self.costo}"


class Cliente:
    def __init__(self, nombre_del_cliente, habitacion, noches, servicios_extra=None):
        self.nombre_del_cliente = nombre_del_cliente
        self.habitacion = habitacion
        self.noches = noches
        self.servicios_extra = servicios_extra if servicios_extra else []

    def calcular_total(self):
        total_habitacion = self.habitacion.precio * self.noches
        total_servicios = sum(servicio.costo for servicio in self.servicios_extra)
        return total_habitacion + total_servicios

    def mostrar_factura(self):
        print(f"\nFactura para {self.nombre_del_cliente}")
        print(f"Habitación: {self.habitacion}")
        print(f"Número de noches: {self.noches}")
        print(f"Subtotal habitación: ${self.habitacion.precio * self.noches}")
        
        if self.servicios_extra:
            print("Servicios extra:")
            for servicio in self.servicios_extra:
                print(f"  {servicio}")
            print(f"Subtotal servicios extra: ${sum(servicio.costo for servicio in self.servicios_extra)}")
        
        print(f"Total a pagar: ${self.calcular_total()}")


if __name__ == "__main__":
    # Creamos las habitaciones
    habitacion_simple = Habitacion("Habitación Simple", 50)
    habitacion_doble = Habitacion("Habitación Doble", 100)
    
    # Creamos los servicios extras
    piscina = ServicioExtra("Uso de la piscina", 10)
    golf = ServicioExtra("Uso de la cancha de golf", 5)

    # Pedimos los datos al usuario
    print("Bienvenido al sistema de reservas del hotel.")
    
    nombre_del_cliente = input("Ingrese el nombre del cliente: ")
    
    print("\nTipos de habitaciones disponibles:")
    print("1. Habitación Simple - $50 por noche")
    print("2. Habitación Doble - $100 por noche")
    seleccion_habitacion = input("Seleccione el tipo de habitación (1 o 2): ")
    
    if seleccion_habitacion == "1":
        habitacion_seleccionada = habitacion_simple
    elif seleccion_habitacion == "2":
        habitacion_seleccionada = habitacion_doble
    else:
        print("Selección no válida. Se seleccionará la habitación simple por defecto.")
        habitacion_seleccionada = habitacion_simple
    
    noches = int(input("Ingrese el número de noches: "))
    
    servicios_extra = []
    print("\nServicios extra disponibles:")
    print("1. Uso de la piscina - $10")
    print("2. Uso de la cancha de golf - $5")
    seleccion_servicios = input("Seleccione los servicios extra (separe con comas, ej. 1,2) o presione Enter para ninguno: ")
    
    if seleccion_servicios:
        seleccion_servicios = seleccion_servicios.split(",")
        if "1" in seleccion_servicios:
            servicios_extra.append(piscina)
        if "2" in seleccion_servicios:
            servicios_extra.append(golf)
    
    cliente = Cliente(
        nombre_del_cliente=nombre_del_cliente,
        habitacion=habitacion_seleccionada,
        noches=noches,
        servicios_extra=servicios_extra
    )

    # Aqui se muestra la factura
    cliente.mostrar_factura()

    



    #Este código es una implementación de un sistema de reservas para un hotel, donde se gestionan habitaciones, servicios extra y se calcula el costo total de una estancia
