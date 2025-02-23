#Simular una cuenta bancaria con depósitos y retiros

def mostrar_saldo(saldo):
    print(f"Tu saldo actual es: {saldo: .2f}$")

def depositar():
    monto = float(input("Ingrese el monto a depositar:"))
    if monto < 0:
        print("Cantidad invalida")
        return 0
    else:
        return monto
    
def retirar(saldo):
    monto = float(input("Ingrese el monto a retirar:"))
    if monto > saldo:
        print("Fondos insuficientes")
        return 0
    elif monto < 0:
        print("El monto debe ser mayor que 0")
        return 0
    else:
        return monto
    
def menu():
    saldo = 0
    en_ejecucion = True
    while en_ejecucion:
        print("\nCuenta bancaria")
        print("1) Mostrar saldo")
        print("2) Depositar")
        print("3) Retirar dinero")
        print("4) Salir")
        opcion = input("Ingrese una opción:")

        if opcion == 1:
            mostrar_saldo(saldo)
        elif opcion == 2:
            saldo += depositar()
        elif opcion == 3:
            saldo -= retirar(saldo)
        elif opcion == 4:
            en_ejecucion = False
            print("Buen día!")
        else:
            print("Opción no valida")

if __name__ == "__main__":
    menu()