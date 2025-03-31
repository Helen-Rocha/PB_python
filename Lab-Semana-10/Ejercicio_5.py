#Módulo para conversión de unidades

def main():
    while True:
        print("\nSeleccione una opción:")
        print("1. Convertir kilómetros a millas")
        print("2. Convertir celsius a fahrenheit")
        print("3. LConvertir litros a galones")
        opcion = input("Ingrese la opción deseada: ")

        if opcion == '1':
            valor = float(input("Ingrese kilómetros: "))
            print (valor * 0.621)
        elif opcion == '2':
            valor = float(input("Ingrese grados Celsius: "))
            print (valor * (9/5) + 32)
        elif opcion == '3':
            valor = float(input("Ingrese litros: "))
            print (valor * 0.264)
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
