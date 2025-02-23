#Generar y analizar histogramas de datos

import numpy as np
import matplotlib.pyplot as plt

def generar_y_analizar_histograma():
    print("Generar y analizar un histograma de datos")

    n = int(input("Ingresa la cantidad de datos a generar: "))
    media = float(input("Ingresa la media de la distribución normal: "))
    desviacion = float(input("Ingresa la desviación estándar de la distribución normal: "))


    datos = np.random.normal(loc=media, scale=desviacion, size=n)

    plt.hist(datos, bins=20, edgecolor='red')  
    plt.title('Ejemplo de histograma')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.show()

    media_datos = np.mean(datos)
    mediana_datos = np.median(datos)
    desviacion_datos = np.std(datos)

    print(f"\nAnálisis de los datos generados:")
    print(f"Media: {media_datos}")
    print(f"Mediana: {mediana_datos}")
    print(f"Desviación estándar: {desviacion_datos}")
    print(f"Máximo: {np.max(datos)}")
    print(f"Mínimo: {np.min(datos)}")

generar_y_analizar_histograma()

