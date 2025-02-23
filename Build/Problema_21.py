#Calcular el área y volumen de distintas figuras geométricas.

import math

def area_cuadrado(lado):
    return lado ** 2

def area_circulo(radio):
    return math.pi * radio ** 2

def area_rectangulo(base, altura):
    return base * altura

def volumen_esfera(radio):
    return (4/3) * math.pi * radio ** 3

def volumen_cilindro(radio, altura):
    return math.pi * radio ** 2 * altura


def calcular():
    print("Selecciona la figura que desea calcular el área o el volumen:")
    print("1) Cuadrado")
    print("2) Círculo")
    print("3) Rectángulo")
    print("4) Esfera")
    print("5) Cilindro")
    
    seleccion = input("Ingresa el número de la figura: ")

    if seleccion == '1':  
        lado = float(input("Ingresa el lado del cuadrado: "))
        print(f"El área del cuadrado es: {area_cuadrado(lado)}")

    elif seleccion == '2': 
        radio = float(input("Ingresa el radio del círculo: "))
        print(f"El área del círculo es: {area_circulo(radio)}")

    elif seleccion == '3':  
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        print(f"El área del rectángulo es: {area_rectangulo(base, altura)}")

    elif seleccion == '4':  
        radio = float(input("Ingresa el radio de la esfera: "))
        print(f"El volumen de la esfera es: {volumen_esfera(radio)}")

    elif seleccion == '5': 
        radio = float(input("Ingresa el radio del cilindro: "))
        altura = float(input("Ingresa la altura del cilindro: "))
        print(f"El volumen del cilindro es: {volumen_cilindro(radio, altura)}")


    else:
        print("Selección no válida, por favor ingresa un número del 1 al 6.")


calcular()