# Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.

def pedir_num():

    num_correcto = False
    while not num_correcto:
        try:
            num = int(input("Número > "))
            if type(num) != int:
                print(f"ERROR: El número debe ser entero.")

            elif num < 0:
                num_correcto = False
                print(f"ERROR: El número debe ser positivo.")

            else:
                num_correcto = True

        except ValueError:
            print(f"ERROR de Formato!!!")

    mostrar_numero(num)

def mostrar_numero(numero: str):
    numero = str(numero).split()
    print(f"{numero}")


def main():
    pedir_num()

if __name__ == "__main__":
    main()