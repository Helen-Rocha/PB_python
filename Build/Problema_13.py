#Convertir una temperatura entre distintas escalas
def convertir_temperatura(valor, escala_origen, escala_destino):
   if escala_origen == escala_destino:
       return valor
   
   if escala_origen == 'F':
       valor = (valor - 32) * 5 / 9
   elif escala_origen == 'K':
       valor = valor - 273.15
   
   if escala_destino == 'F':
       return (valor * 9 / 5) + 32
   elif escala_destino == 'K':
       return valor + 273.15
   else:
       return valor

print("Conversor de temperaturas entre Celsius (C), Fahrenheit (F) y Kelvin (K)")
try:
   temperatura = float(input("Ingresa la temperatura: "))
   escala_origen = input("Ingresa la escala de origen (C, F, K): ").upper()
   escala_destino = input("Ingresa la escala de destino (C, F, K): ").upper()
   if escala_origen not in ('C', 'F', 'K') or escala_destino not in ('C', 'F', 'K'):
       print("Error: Escala no válida. Usa C, F o K.")
   else:
       resultado = convertir_temperatura(temperatura, escala_origen, escala_destino)
       print(f"{temperatura}°{escala_origen} equivale a {resultado:.2f}°{escala_destino}")
except ValueError:
   print("Error: Ingresa un número válido para la temperatura.")