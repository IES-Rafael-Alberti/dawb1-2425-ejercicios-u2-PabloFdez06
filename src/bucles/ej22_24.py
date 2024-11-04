# Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.


def pedir_num():

    num_correcto = False
    while not num_correcto:
        try:
            num = int(input("Número > "))
            if type(num) != int:
                print(f"ERROR: El número debe ser entero.")

            elif num < 0:
                num_correcto = False
                print(f"ERROR: El número debe ser mayor a 1")

            else:
                num_correcto = True

        except ValueError:
            print(f"ERROR de Formato!!!")

    return num

    
def es_primo(n):

    if n <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Si  tiene un divisor, no es primo
    return True  # Si no tiene ningún divisor, es primo

        
    
def main():
    cont_primos = 0
    numero = None
    while numero != 0:

        numero = pedir_num()
        if numero != -1:
            if es_primo(numero):
                cont_primos += 1

    print(f"Has ingresado un total de {cont_primos} números primos.")


if __name__ == "__main__":
    main()