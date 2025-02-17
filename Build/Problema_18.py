#Resolver ecuaciones cuadraticas
def resolver_ecuaciones_cuadraticas(a, b, c):
   
   discriminante = b**2 - 4*a*c
   
   raiz1 = (-b + discriminante) / (2 * a)
   raiz2 = (-b - discriminante) / (2 * a)
   return raiz1, raiz2

try:
   a = float(input("Introduce el coeficiente a: "))
   b = float(input("Introduce el coeficiente b: "))
   c = float(input("Introduce el coeficiente c: "))
   if a == 0:
       print("El valor de 'a' no puede ser cero en una ecuación cuadrática.")
   else:
       raiz1, raiz2 = resolver_ecuaciones_cuadraticas(a, b, c)
       print(f"Las soluciones son: {raiz1} y {raiz2}")
except ValueError:
   print("Por favor, ingresa valores numéricos válidos para los coeficientes.")