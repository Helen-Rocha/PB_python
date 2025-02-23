#Conversor de unidades

def metros_a_kilometros(metros):
    return metros / 1000

def kilometros_a_metros(kilometros):
    return kilometros * 1000

def gramos_a_kilogramos(gramos):
    return gramos / 1000

def kilogramos_a_gramos(kilogramos):
    return kilogramos * 1000

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def conversor_unidades():
    print("Conversor de Unidades")
    print("1. Metros a Kilómetros")
    print("2. Kilómetros a Metros")
    print("3. Gramos a Kilogramos")
    print("4. Kilogramos a Gramos")
    print("5. Celsius a Fahrenheit")
    print("6. Fahrenheit a Celsius")
    
    opcion = int(input("Elige el número de la conversión que deseas realizar: "))
    
    if opcion == 1:
        metros = float(input("Ingresa el valor en metros: "))
        resultado = metros_a_kilometros(metros)
        print(f"{metros} metros es igual a {resultado} kilómetros.")
    
    elif opcion == 2:
        kilometros = float(input("Ingresa el valor en kilómetros: "))
        resultado = kilometros_a_metros(kilometros)
        print(f"{kilometros} kilómetros es igual a {resultado} metros.")
    
    elif opcion == 3:
        gramos = float(input("Ingresa el valor en gramos: "))
        resultado = gramos_a_kilogramos(gramos)
        print(f"{gramos} gramos es igual a {resultado} kilogramos.")
    
    elif opcion == 4:
        kilogramos = float(input("Ingresa el valor en kilogramos: "))
        resultado = kilogramos_a_gramos(kilogramos)
        print(f"{kilogramos} kilogramos es igual a {resultado} gramos.")
    
    elif opcion == 5:
        celsius = float(input("Ingresa el valor en grados Celsius: "))
        resultado = celsius_a_fahrenheit(celsius)
        print(f"{celsius} grados Celsius es igual a {resultado} grados Fahrenheit.")
    
    elif opcion == 6:
        fahrenheit = float(input("Ingresa el valor en grados Fahrenheit: "))
        resultado = fahrenheit_a_celsius(fahrenheit)
        print(f"{fahrenheit} grados Fahrenheit es igual a {resultado} grados Celsius.")
    
    else:
        print("Opción no válida. Intenta nuevamente.")

conversor_unidades()