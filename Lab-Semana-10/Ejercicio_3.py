#Gestión de contactos con tuplas y estructuras anidadas

class Gestion_de_contactos:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, numero, correo):
        contacto = (nombre, numero, correo)
        self.contactos.append(contacto)
        print(f"Contacto '{nombre}' agregado.")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto[0] == nombre:
                print(f"Contacto encontrado: Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")
                return
        print(f"No se encontro '{nombre}'")

    def listar_contactos(self):
        if not self.contactos:
            print("No hay contactos guardados.")
            return
        contactos_ordenados = sorted(self.contactos, key=lambda x: x[0])
        print("Lista de contactos ordenados alfabéticamente:")
        for contacto in contactos_ordenados:
            print(f"Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")

def menu():
    gestion = Gestion_de_contactos()
    while True:
        print("\n1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Lista de contactos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nombre = input("Nombre: ")
            numero = input("Número: ")
            correo = input("Correo: ")
            gestion.agregar_contacto(nombre, numero, correo)
        elif opcion == '2':
            nombre = input("Ingrese el nombre que busca: ")
            gestion.buscar_contacto(nombre)
        elif opcion == '3':
            gestion.listar_contactos()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()