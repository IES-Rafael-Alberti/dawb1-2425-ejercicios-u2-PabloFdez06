# Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.

import os
import time
OPCIONES = 1, 2, 3


def limpiar():
    os.system("cls")




def menu_programa():

    valor_correcto = False
    while not valor_correcto:
        time.sleep(0.5)
        print("1- Comenzar programa.\n2- Imprimir listado\n3- Finalizar programa.\n")
        time.sleep(0.5)
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




def main():
    opcion = menu_programa()
    opcionc = False

    while opcionc is not True:
        if opcion == 1:
            print("Buenas, has escogido la opción 1!")

        elif opcion == 2:
            print("Buenas, has escogido la opción 2!")

        
    if opcion == 3:
        print("Programa Finalizado.")
            
            
## SIN FINALIZAR BUCLE DEL MAIN ##

if __name__ == "__main__":
    main()