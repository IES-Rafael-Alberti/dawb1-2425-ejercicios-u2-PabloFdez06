# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

def pedir_palabra():

    palabra = input("Introduzca una palabra: ")
    return palabra

def mostrar_letras(palabra):

    for letra in palabra[::-1]:
        print(letra)



def main():
    palabra = pedir_palabra()
    mostrar_letras(palabra)


if __name__ == "__main__":
    main()