# Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.

def pedir_num():

    num_correcto = False
    while not num_correcto:
        try:
            num = int(input("Número > "))
            num_correcto = True

        except ValueError:
            print(f"ERROR: La entrada no es correcta")

    return num


def main():
    pedir_num()

if __name__ == "__main__":
    main()

