#Manejo de inventario con listas y diccionarios

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, categoria, precio, cantidad):
        if nombre in self.productos:
            print(f"El producto '{nombre}' ya existe. Actualizando cantidad.")
            self.productos[nombre]['cantidad'] += cantidad
        else:
            self.productos[nombre] = {'categoria': categoria, 'precio': precio, 'cantidad': cantidad}
            print(f"Producto '{nombre}' agregado con éxito.")

    def eliminar_producto(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]
            print(f"Producto '{nombre}' eliminado.")
        else:
            print(f"Producto '{nombre}' no encontrado.")

    def buscar_producto(self, nombre):
        if nombre in self.productos:
            print(f"Producto encontrado: {nombre}, {self.productos[nombre]}")
        else:
            print(f"Producto '{nombre}' no encontrado.")

    def mostrar_productos_ordenados(self):
        productos_ordenados = sorted(self.productos.items(), key=lambda x: x[1]['precio'])
        for nombre, datos in productos_ordenados:
            print(f"{nombre}: {datos}")

def menu():
    inventario = Inventario()
    while True:
        print("\n1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Buscar producto")
        print("4. Mostrar productos ordenados por precio")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nombre = input("Nombre del producto: ")
            categoria = input("Categoría: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            inventario.agregar_producto(nombre, categoria, precio, cantidad)
        elif opcion == '2':
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == '3':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '4':
            inventario.mostrar_productos_ordenados()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
