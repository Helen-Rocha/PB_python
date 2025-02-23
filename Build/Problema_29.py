#Generar y analizar datos estadísticos

import numpy as np
import matplotlib.pyplot as plt

def generar_y_analizar_datos():
    print("Generación y análisis de datos estadísticos")
    
    n = int(input("Ingresa la cantidad de datos a generar: "))
    media = float(input("Ingresa la media de la distribución normal: "))
    desviacion = float(input("Ingresa la desviación estándar de la distribución normal: "))

    datos = np.random.normal(loc=media, scale=desviacion, size=n)

    media_datos = np.mean(datos) 
    mediana_datos = np.median(datos)  
    desviacion_datos = np.std(datos) 
    varianza_datos = np.var(datos) 
    max_datos = np.max(datos)
    min_datos = np.min(datos)  

    print(f"\nAnálisis de los datos generados:")
    print(f"Media: {media_datos}")
    print(f"Mediana: {mediana_datos}")
    print(f"Desviación estándar: {desviacion_datos}")
    print(f"Varianza: {varianza_datos}")
    print(f"Máximo: {max_datos}")
    print(f"Mínimo: {min_datos}")

    plt.hist(datos, bins=20, edgecolor='black')  
    plt.title('Histograma de la Distribución Normal')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.show()

generar_y_analizar_datos()