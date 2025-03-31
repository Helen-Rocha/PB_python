#Calculadora de estadísticas

import math

def calcular_estadisticas(*args):
    if len(args) == 0:
        print("No se ingresaron números.")
        return None

    promedio = sum(args) / len(args)

    numeros_ordenados = sorted(args)
    n = len(numeros_ordenados)
    if n % 2 == 0:
        mediana = (numeros_ordenados[n // 2 - 1] + numeros_ordenados[n // 2]) / 2
    else:
        mediana = numeros_ordenados[n // 2]

    varianza = sum((x - promedio) ** 2 for x in args) / len(args)
    desviacion_estandar = math.sqrt(varianza)

    return promedio, mediana, desviacion_estandar

def main():
    try:
        numeros = input("Ingrese los números deseados separados por espacios: ").split()
        numeros = list(map(float, numeros))
        promedio, mediana, desviacion_estandar = calcular_estadisticas(*numeros)
        print(f"Promedio: {promedio}")
        print(f"Mediana: {mediana}")
        print(f"Desviación Estándar: {desviacion_estandar}")
    except ValueError:
        print("Por favor, ingrese solo números válidos.")

if __name__ == "__main__":
    main()
