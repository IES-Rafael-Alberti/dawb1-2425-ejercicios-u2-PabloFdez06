# Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.

# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

def pedir_frase():

    frase = input("Introduzca una frase: ").strip().lower()
    return frase

def pedir_letra():

    letra = input("Introduzca una letra: ").strip().lower()
    return letra

def contar_letras(frase, letra):

    contador = 0

    for letras in frase:
        if letras == letra:
            contador += 1

    print(f"La letra ingresada se repite en total {contador} veces.")




def main():
    frase = pedir_frase()
    letra = pedir_letra()
    contar_letras(frase, letra)


if __name__ == "__main__":
    main()