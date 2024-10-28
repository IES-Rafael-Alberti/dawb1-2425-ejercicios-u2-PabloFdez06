# Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.

import os
import time

def limpiar():
    os.system("cls")


def menu_programa():
    OPCIONES = 1, 2, 3
    valor_correcto = False
    while not valor_correcto:
        time.sleep(0.5)
        print("1- Comenzar programa.\n2- Imprimir listado\n3- Finalizar programa.\n")
        time.sleep(1)
        try:
            valor = int(input("Selección > "))
            if type(valor) != int:
                print(f"ERROR: Escoja una de las 3 opciónes aportadas")

            elif valor not in OPCIONES:
                valor_correcto = False
                print(f"ERROR: Escoja una de las 3 opciónes aportadas")

            else:
                valor_correcto = True

        except ValueError:
            print(f"ERROR de Formato!!!")

    return valor


def seleccion_menu():

    pass


def main():
    menu_programa()
    limpiar()

if __name__ == "__main__":
    main()