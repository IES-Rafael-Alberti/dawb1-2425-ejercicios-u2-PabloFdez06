# Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados


def pedir_entrada():
    #entradas = None
    entra_bucle = True

    while entra_bucle:
        nums = str(input("Números > "))

        if nums == 0:
            entra_bucle = False
        
        else:
            for num in nums:
                print(num)
    
    #mostrar_eco(entradas)



def mostrar_eco(texto: str):
    print("ECO USUARIO: \n" + str(texto))



def main():
    pedir_entrada()


if __name__ == "__main__":
    main()

    ##### SIN ACABAR #####