# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

def pedir_num():

    num_correcto = False
    while not num_correcto:
        try:
            num = int(input("Número > "))
            if type(num) != int:
                print(f"ERROR: El número debe ser entero.")

            elif num < -1:
                num_correcto = False
                print(f"ERROR: El número debe ser positivo.")

            else:
                num_correcto = True

        except ValueError:
            print(f"ERROR de Formato!!!")

    return num


def contar_impares(numero):
    resultado = ""
    for i in range(1, numero + 1): 
        if i % 2 == 1:
            resultado += str(i) + ", " 
    
    print(resultado[:-2])
            

        
    
def main():

    numero = pedir_num()
    contar_impares(numero)


if __name__ == "__main__":
    main()