#Ordenamiento y busqueda

import random

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return quicksort(izquierda) + medio + quicksort(derecha)

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1  

numeros = [random.randint(1, 100) for _ in range(10)]
print("Lista original:", numeros)

numeros_ordenados = quicksort(numeros)
print("Lista ordenada:", numeros_ordenados)

num_buscar = int(input("Ingrese un número para buscar en la lista: "))
indice = busqueda_binaria(numeros_ordenados, num_buscar)

if indice != -1:
    print(f"El número {num_buscar} se encuentra en la posición {indice} de la lista ordenada.")
else:
    print(f"El número {num_buscar} no está en la lista.")
