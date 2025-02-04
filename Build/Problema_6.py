#Calcular el interés compuesto dado un capital, tasa y tiempo
cap=int(input("Ingrese su capital:"))
tasa=float(input("Ingrese la tasa de interés (0 a 1):"))
tiempo=int(input("Ingrese el tiempo:"))
inte_comp=cap*(1+tasa)**tiempo
print("El interes compuesto es:" ,inte_comp)