#Verificar si es un número primo
n=int(input("Ingresa un número"))
a=1
b=0
while a <= n:
    if n % a == 0:
        b=b+1
    a=a+1
if b==2:
    print("El número", n, "es primo")
else:
    print("El número", n, "no es primo")    