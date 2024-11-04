# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1


def crear_piramide(numero):

    resto = (numero % 2)
    i = None
    
    piramide = ""
    secuencia = ""
    if resto == 0:
        for i in range(0, numero + 1,2):
            secuencia = str(i) + " " + secuencia 
            piramide = piramide + secuencia + "\n"

    else:
        for i in range(1, numero + 1,2):
            secuencia = str(i) + " " + secuencia 
            piramide = piramide + secuencia + "\n"

    return piramide




def pedir_numero():
    num_correcto = False
    while not num_correcto:
        try:
            num = int(input("Introduzca el número: "))
            if str(num).startswith("-"):
                raise ValueError
            else:
                num_correcto = True

                
        except ValueError:
            print(f"ERROR de Formato!!!")

    return num


def main():
    numero = pedir_numero()
    piramide = crear_piramide(numero)
    print(piramide)



if __name__ == "__main__":
    main()