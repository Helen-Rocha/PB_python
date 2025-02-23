#Implementar funciones recursivas
#Función Factorial y fibonacci

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def menu():
    print("Elige una opción:")
    print("1. Calcular Factorial")
    print("2. Calcular Fibonacci")
    
    opcion = int(input("Ingresa el número de la opción que deseas ejecutar: "))
    
    if opcion == 1:
        numero = int(input("Ingresa un número para calcular su factorial: "))
        resultado = factorial(numero)
        print(f"El factorial de {numero} es {resultado}")
    
    elif opcion == 2:
        numero = int(input("Ingresa el índice de Fibonacci que deseas calcular: "))
        resultado = fibonacci(numero)
        print(f"El número de Fibonacci en la posición {numero} es {resultado}")
    
    else:
        print("Opción no válida. Intenta nuevamente.")

menu()
