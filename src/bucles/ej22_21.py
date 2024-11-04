# Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.


def pedir_entrada():
    suma = 0
    entra_bucle = True

    while entra_bucle:
        try:
            num = int(input("Números > "))

            if num == 0: 
                entra_bucle = False
            
            elif num < 0:
                raise ValueError("Ingrese un monto positivo porfavor!")
            
            else:
                suma += num

        except ValueError:
            print(f"ERROR DE FORMATO")

    mostrar_eco(suma)


def mostrar_eco(total):
    print(f"La suma total de los números introducidos es: {total}")


def main():
    pedir_entrada()


if __name__ == "__main__":
    main()