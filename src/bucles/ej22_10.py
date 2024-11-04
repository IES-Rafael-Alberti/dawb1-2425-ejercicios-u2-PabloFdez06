def es_primo(n):

    if n <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Si  tiene un divisor, no es primo
    return True  # Si no tiene ningún divisor, es primo


def pedir_numero():

    numero_correcto = False
    while not numero_correcto:
        try:
            numero = int(input("Introduce un número: "))

            if type(numero) != int:
                print(f"ERROR: El número debe ser entero.")

            elif numero < 0:
                numero_correcto = False
                print(f"ERROR: El número debe ser positivo.")

            else:
                numero_correcto = True

        except ValueError:
            print(f"ERROR de Formato!!!")

    return numero

def main():

    numero = pedir_numero()
    
    if es_primo(numero):
        print(f"{numero} es un número primo.")

    else:
        print(f"{numero} no es un número primo.")

if __name__ == "__main__":
    main()