#Determinar si un número es par, impar o múltiplo de otro
num=int(input("Ingresa un número:"))
n=int(input("Ingrese otro número"))
if num % 2 == 0:
     print("El",num, "es número par")
else:
     print("El",num, "es número impar")

def calcular(x,y):
     if x % y == 0:
          print(f"{x} es multiplo de {y}")
     elif y % x == 0:
        print(f"{y} es multiplo de {x}")
     else:
        print("Los números no son multiplos")

calcular(num, n)
     