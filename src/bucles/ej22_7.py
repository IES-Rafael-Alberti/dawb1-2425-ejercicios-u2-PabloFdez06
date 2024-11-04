# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.


def tabla_multiplicacion():
    for i in range(1, 11):
        print(f"10 x {i} = {10 * i}")

def main():
    tabla_multiplicacion()


if __name__ == "__main__":
    main()