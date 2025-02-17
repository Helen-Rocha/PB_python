#Verificar si es pálindromo.
def es_palindromo(frase):
    frase = frase.lower()
    frase = frase.replace("á", "a")
    frase = frase.replace("é", "e")
    frase = frase.replace("í", "i")
    frase = frase.replace("ó", "o")
    frase = frase.replace("ú", "u")
    frase = frase.replace(" ", "")

    a = 0
    b = len(frase) - 1

    for i in range(0, len(frase)):
        if frase[a] == frase[b]:
            a += 1
            b -= 1
        else:
            return False
    return True

frase = input("Ingrese una palabra o frase:")

if es_palindromo(frase):
    print("Es palindromo")
else:
    print("No es palindromo")