# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.


def division(num1, num2):
    division_correcta = num1 // num2
    if comprobar_numeros(num2) == True:
        return division_correcta




def comprobar_numeros(nume2):

    if nume2 == 0:
        print("Error, el divisor no puede ser igual a 0")
    else:
        return True
    



def main():
    
    num1 = int(input("Ingrese el número de la división: "))
    num2 = int(input("Ingrese el divisor: "))
    resultado = division(num1, num2)


    print(f"El resultado de la división es: {resultado}")





if __name__ == "__main__":
    main()