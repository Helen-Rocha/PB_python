#Implementar una agenda de contactos

agenda = {}

def mostrar_contactos():
    print("\nNombre".ljust(20) + "Número de contacto")
    print("- * 35")
    for nombre, numero in agenda.items():
        print(f"{nombre.ljust(20)}{numero}")

while True:
    print("\nOpciones:")
    print("1) Añadir nuevo contacto")
    print("2) Buscar contacto")
    print("3) Mostrar todos los contactos")
    print("4) Elimiar contacto")
    print("5) Salir")
    opcion = int(input("Ingresa la opción que desea:"))

    if opcion == 1:
        nombre = input("Nombre del contacto:")
        numero = input("Numero del contacto:")
        agenda[nombre] = numero
        print("Contacto añanido")

    elif opcion == 2:
        buscar_nombre = input("Nombre del contacto:")
        if buscar_nombre in agenda:   #verificar que el contacto exista
            print(f"Su número es {agenda[buscar_nombre]}")
        else:
            print("No se encontro el contacto")

    elif opcion == 3:
        if not agenda:  #Si la agenda esta vacía
            print("La agenda esta vacía")
        else:
            mostrar_contactos()

    elif opcion == 4:
        eliminar_contacto = input("Nombre del contacto que desea eliminar:")
        if eliminar_contacto in agenda:  #Verificar que exista
            agenda.pop(eliminar_contacto)
            print("El contacto se elimino")
        else:
            print("No existe el contacto")

    elif opcion == 5:
        print("Salir")
        break

    else:
        print("Opción no valida")

if __name__ == "__main__":
    main()