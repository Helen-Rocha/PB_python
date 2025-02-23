#Generar números aleatorios
import random
import math


def generar_numeros():
    print("Selecciona la distribución:")
    print("1) Distribución Uniforme")
    print("2) Distribución Normal")
    print("3) Distribución Binomial")
    print("4) Distribución Poisson")
    
    seleccion = input("Ingresa el número de la distribución: ")
    
    size = int(input("¿Cuántos números deseas generar? "))
    
    if seleccion == '1':  
        a = float(input("Ingresa el valor mínimo (a): "))
        b = float(input("Ingresa el valor máximo (b): "))
        numeros = [random.uniform(a, b) for _ in range(size)]
        print("Números aleatorios (Uniforme):", numeros)
        
    elif seleccion == '2':  
        mu = float(input("Ingresa la media (mu): "))
        sigma = float(input("Ingresa la desviación estándar (sigma): "))
        numeros = [random.gauss(mu, sigma) for _ in range(size)]
        print("Números aleatorios (Normal):", numeros)
        
    elif seleccion == '3':  
        n = int(input("Ingresa el número de intentos (n): "))
        p = float(input("Ingresa la probabilidad de éxito (p): "))
        numeros = [random.betavariate(p, 1 - p) for _ in range(size)] 
        print("Números aleatorios (Binomial):", numeros)
        
    elif seleccion == '4':  
        lam = float(input("Ingresa el parámetro lambda (λ): "))
        numeros = [random.poisson(lam) for _ in range(size)]  
        print("Números aleatorios (Poisson):", numeros)
        
    else:
        print("Selección no válida.")


generar_numeros()
