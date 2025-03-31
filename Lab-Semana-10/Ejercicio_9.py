#Implementación de múltiples paradigmas

# Paradigma Imperativo
numeros = [1, 2, 3, 4, 5]
producto = 1
for num in numeros:
    producto *= num
print("Producto de los números (Imperativo):", producto)

# Paradigma Estructurado
def encontrar_maximo(lista):
    maximo = lista[0]
    for num in lista:
        if num > maximo:
            maximo = num
    return maximo

print("Número máximo en la lista (Estructurado):", encontrar_maximo(numeros))

# Paradigma Modular
def promedio(lista):
    return sum(lista) / len(lista)

import operaciones_modulo  

print("Promedio de la lista (Modular):", operaciones_modulo.promedio(numeros))

# Paradigma Orientado a Objetos
class ListaNumeros:
    def __init__(self, lista):
        self.lista = lista

    def sumar_lista(self):
        return sum(self.lista)

    def mostrar_lista(self):
        print("Lista almacenada:", self.lista)

mis_numeros = ListaNumeros(numeros)
mis_numeros.mostrar_lista()
print("Suma de la lista (POO):", mis_numeros.sumar_lista())
