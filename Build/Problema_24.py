#Calcular la suma de una serie numérica
 
def suma_de_serie():
    print("Calcular la suma de una serie numérica")
    
    n = int(input("Ingresa el número de términos en la serie: "))
    
    suma = 0
    
    for i in range(n):
        valor = float(input(f"Ingrese el término {i+1}: "))
        suma += valor
    
    print(f"La suma de los términos de la serie es: {suma}")

suma_de_serie()
