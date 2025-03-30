#Análisis de texto con diccionarios y conjuntos

def analizar_texto(texto):
    #Primero convertir todo el texto a minúsculas y eliminar signos de puntuación
    import string
    texto_nuevo = texto.lower().translate(str.maketrans('', '', string.punctuation))
    
    palabras = texto_nuevo.split()
    
    total_palabras = len(palabras)
    palabras_unicas = set(palabras)
    
    #Cuantas veces se repiten las palabras 
    frecuencia_palabras = {}
    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1
    
    #Palabra más frecuente
    palabra_mas_frecuente = max(frecuencia_palabras, key=frecuencia_palabras.get)
    
    #Para mostrar los resultados
    print(f"Número total de palabras: {total_palabras}")
    print(f"Número de palabras únicas: {len(palabras_unicas)}")
    print("Frecuencia de cada palabra:")
    for palabra, frecuencia in frecuencia_palabras.items():
        print(f"{palabra}: {frecuencia}")
    print(f"La palabra más frecuente es '{palabra_mas_frecuente}' con {frecuencia_palabras[palabra_mas_frecuente]} apariciones.")

def main():
    texto = input("Ingrese un texto para analizar: ")
    analizar_texto(texto)

if __name__ == "__main__":
    main()
