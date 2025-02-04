#Calcular factorial de un número
print("Ingrese un número")
num = int(input())
fact=1
for i in range(1, num+1):
    fact*=i
print("El factorial de",num, "es:", fact)