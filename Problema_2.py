operador = input("OPERADOR: (+,-,*,/) ")
num1 = float(input("num1: "))
num2 = float(input("num2: "))

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    resultado = num1 / num2
else:
    print("Operador imválido")

print(resultado)