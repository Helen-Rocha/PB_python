#Vocales y consonantes
def contar_vocales_consonantes(texto):
   
   vocales = "AEIOUaeiouÁÉÍÓÚáéíóú"
   
   vocales_count = 0
   consonantes_count = 0
   
   for i in texto:
       if i.isalpha():  
           if i in vocales:
               vocales_count += 1
           else:
               consonantes_count += 1
   return vocales_count, consonantes_count

texto = input("Ingrese un texto: ")
vocales, consonantes = contar_vocales_consonantes(texto)
print(f"Vocales", vocales, "Consonantes", consonantes)