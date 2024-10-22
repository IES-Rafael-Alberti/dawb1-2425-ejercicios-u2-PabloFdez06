# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

def comprueba_parimpar(num: int) -> bool:
    if num % 2 == 0:
        return print("El número indicado es par")
    else:
        return print("El número indicado es impar")


def main():
    num = int(input("Introduce un número para saber si es par o impar: "))
    comprueba_parimpar(num)


if __name__ == "__main__":
    main()