# Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.

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

def mostrar_numero(numero: str):
    suma = 0
    for digitos in numero:
        suma += int(digitos)
    print(f"{suma}")

# def mostrar_numeros_pares(numero):
#     contador = 0
#     num_par = (int(numero) % 2)
#     while num_par == 0:
#         contador = contador + 1
#         return contador
    
def es_par(numero) -> bool:
    return numero % 2 == 0

        
    
def main():
    cont_pares = 0
    numero = 0
    while numero != -1:

        numero = pedir_num()
        if numero != -1:
            mostrar_numero(str(numero))
            if es_par(numero):
                cont_pares += 1

    print(f"Has ingresado un total de {cont_pares} números pares.")


if __name__ == "__main__":
    main()