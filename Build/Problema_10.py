#Leer, escribir y modificar un archivo de texto
ruta = r"texto_prueba.txt"
def leer():
    with open(ruta, "r") as archivo:
        contenido = archivo.read()
        print(contenido)

leer()
with open(ruta, "w") as archivo:
    archivo.write("Hola chicos desde python!!     ")

leer()
with open(ruta, "a") as archivo:
    archivo.write("\nAprendiendo en python      ")

leer()