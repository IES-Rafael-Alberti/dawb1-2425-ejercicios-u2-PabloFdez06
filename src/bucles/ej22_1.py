# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def multiplicar_palabra(palabra):
    for _ in range(10):
        print(palabra)




def main():
    palabra = input("Introduzca la palabra: ")
    multiplicar_palabra(palabra)

if __name__ == "__main__":
    main()