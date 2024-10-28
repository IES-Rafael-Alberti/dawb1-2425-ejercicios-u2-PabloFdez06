# Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

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

    return num

def pedir_entrada():
    suma = 0
    mayor = None
    entra_bucle = True

    while entra_bucle:
        try:
            num = pedir_num()

            if num == 0: 
                entra_bucle = False
            
            else:
                suma += num

                if mayor == None or num > mayor:
                    mayor = num

        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    mostrar_eco(suma, mayor)


def mostrar_eco(total, maximo):
    print(f"El total de los números introducidos es: {total}\nEl número máximo introducido es: {maximo}")


def main():
    pedir_entrada()

    
if __name__ == "__main__":
    main()