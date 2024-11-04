# Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

def pedir_entrada():
    suma = 0
    negativos = 0
    entra_bucle = True

    while entra_bucle:
        try:
            num = int(input("Números > "))

            if num == 0: 
                entra_bucle = False
            elif num < 0:
                negativos += num  
            
            else:
                suma += num

        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    mostrar_eco(suma)


def mostrar_eco(total):
    print(f"El total de los números introducidos es: {total}")


def main():
    pedir_entrada()


if __name__ == "__main__":
    main()