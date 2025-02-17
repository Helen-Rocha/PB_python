#Encontrar el mayor entre tres números dados
n1 = int(input("Ingrese un numero:"))
n2 = int(input("Ingrese otro numero:"))
n3 = int(input("Ingrese otro mas:"))

if (n1 > n2) and (n1 > n3):
    print("El numero", n1, "es el mayor")
elif (n2 > n3):
    print("El numero", n2, "es el mayor")
else:
    print("el numero", n3, "es el mayor")