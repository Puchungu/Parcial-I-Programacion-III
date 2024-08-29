listaTarjetas = []

class Tarjeta:
    def _init_(self, nombre, institucion, codigo, libro, fechaPrestamo, diasPrestamo):
        self.nombre = nombre
        self.institucion = institucion
        self.codigo = codigo
        self.libro = libro
        self.fechaPrestamo = fechaPrestamo
        self.diasPrestamo = int(diasPrestamo)

    def mostrarDatos(self):
        print("Nombre: ", self.nombre)
        print("Institución: ", self.institucion)
        print("Código: ", self.codigo)
        print("Libro: ", self.libro)
        print("Fecha de Préstamo: ", self.fechaPrestamo)
        print("Días de préstamo: ", self.diasPrestamo)

    def calcularDiastrans(self):
        diasTranscurridos= int(input("Ingrese el numero de dias desde el prestamo: "))
        if diasTranscurridos>self.diasPrestamo:
            print("Ha excedido el limite de prestamo, se ha aplicado una sancion")
        else: print("Aun se encuentra dentro de los dias disponibles de devolucion")
        

def nuevatar():
    nombre = input("Ingrese su nombre: ")
    institucion = input("Ingrese su Institución: ")
    codigo = input("Ingrese su código: ")
    resp = input("¿Desea prestar un libro? S/N: ").upper()
    if resp == "S":
        libro = input("Ingrese el nombre del libro: ")
        fechaPrestamo = input("Ingrese la fecha de préstamo (YYYY-MM-DD): ")
        diasPrestamo = input("Ingrese la cantidad de días de préstamo: ")
    else:
        libro = "Ninguno"
        fechaPrestamo = "Ninguno"
        diasPrestamo = "0"

    nuevaTarjeta = Tarjeta(nombre, institucion, codigo, libro, fechaPrestamo, diasPrestamo)
    nuevaTarjeta.mostrarDatos()
    listaTarjetas.append(nuevaTarjeta)
    return nuevaTarjeta

# Crear una nueva tarjeta de préstamo
tarjeta1 = nuevatar()

# Verificar si hay sanción al devolver el libro
tarjeta1.calcularDiastrans()

"""
Decidi hacerlo con clases debido a la flexibilidad que nos brindan en la reutilizacion del codigo y el orden que podemos tener con ellas, se soluciona de manera que compramos los dias transcurridos con los dias que el usuario 
presto el libro y de esta manera podemos determinar si el usuario se paso de dias de prestamo y aplicar la sancion
"""