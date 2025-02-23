#Implementar y operar con matrices

import numpy as np

def ingresar_matriz(nombre):
    filas = int(input(f"Ingresa el número de filas de la matriz {nombre}: "))
    columnas = int(input(f"Ingresa el número de columnas de la matriz {nombre}: "))
    matriz = []
    print(f"Ingrese los elementos de la matriz {nombre} ({filas}x{columnas}):")
    
    for i in range(filas):
        fila = list(map(int, input(f"Ingrese los elementos de la fila {i+1}, separados por espacios: ").split()))
        matriz.append(fila)
    
    return matriz

def mostrar_matriz(matriz, nombre):
    print(f"Matriz {nombre}:")
    for fila in matriz:
        print(fila)

print("Ingresa la matriz A:")
A = ingresar_matriz('A')

print("Ingresa la matriz B:")
B = ingresar_matriz('B')

mostrar_matriz(A, 'A')
mostrar_matriz(B, 'B')

def operaciones_matrices():
    print("Operaciones con matrices:")
    print("1) Sumar matrices")
    print("2) Restar matrices")
    print("3) Multiplicar matrices")
    print("4) Transponer una matriz")
    
operacion =  input("Selecciona la operación: ")
if operacion == '1':
        print (A + B)