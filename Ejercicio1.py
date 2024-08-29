class Consultorio: #clase perro con su contructor y funcion de mostrar info
    def __init__(self, nombre, edad, direccion, peso,fecha):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.peso = peso
        self.fecha = fecha
        self.estado = "No atendido"

    def mostrar_info(self): #funcion para hacer el formato en el que se imprime la info 
        print("------------------------ Paciente de el hospital Bloom -------------------------")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Direccion: {self.direccion}")
        print(f"Peso(kg): {self.peso}")
        print(f"Estado: {self.estado}" )
        print(f"Fecha de consulta: {self.fecha}")
        print("-" * 30)

def ingresar_datos():  # Función para hacer los inputs del usuario 
    nombre = input("Ingrese el nombre: ")
    for paciente in pacientes:
        if paciente.nombre == nombre:
            paciente.estado = "Sala de espera"
            print("Usted ya tiene una consulta previa. Por favor, espere en la sala de espera.")
            return 
    edad = input("Ingrese la edad: ")
    direccion = input("Ingrese su direccion: ")
    peso = input("Ingrese su peso en Kilogramos: ")
    fecha = input("Ingrese la fecha de la consulta")
    nuevo_paciente = Consultorio(nombre, edad, direccion, peso, fecha)
    pacientes.append(nuevo_paciente)
    return nuevo_paciente 

def mostrar_paciente(): #funcion para mostrar los usuarios que han prestado libros que estan en la lista global 
    print("\nPaciente registrado:")
    for paciente in pacientes:
        paciente.mostrar_info()

def menu_principal(): #funcion para el menu principal
    while True:
        print("Seleccione la opción que desea realizar:")
        print("1. Registrar paciente")
        print("2. Mostrar paciente")
        print("3. Salir")
        opcion = int(input("Ingrese el número correspondiente a la opción que desea realizar: "))

        if opcion == 1:
            ingresar_datos()
        elif opcion == 2:
            mostrar_paciente()
        elif opcion == 3:
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Lista global para almacenar los pacientes
pacientes = []

# Ejecutar el menú principal
menu_principal()