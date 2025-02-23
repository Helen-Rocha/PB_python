#Simular el lanzamiento de un dado y ua moneda

#Moneda
import random as rnd

valor = rnd.random()

if valor > 0.50:
    print("La moneda cayó en aguila")
else:
    print("La moneda cayó en sol")

#Dado

dado = rnd.randint(1,6)

if dado == 1:
    print(" El dado cayo en uno")
if dado == 2:
    print("El dado cayo en dos")
if dado == 3:
    print("El dado cayo en tres")
if dado == 4:
    print("El dado cayo en cuatro")
if dado == 5:
    print("El dado cayo en cinco")
if dado == 6:
    print("El dado cayo en seis")
