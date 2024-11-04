# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto.

def pedir_num():

    num_correcto = False
    while not num_correcto:
        try:
            num = int(input("Número > "))
            num_correcto = True

            if num < 0:
                 num_correcto = False
                 raise ValueError


        except ValueError:
                print(f"ERROR: La entrada no es correcta")

    return num


def cuenta_atras(numero):
    
    secuencia = ""
    for i in range(numero, -1, -1):
        secuencia += str(i) + ", "
        
    print(secuencia[:-2])



def main():
    numero = pedir_num()
    cuenta_atras(numero)

if __name__ == "__main__":
    main()
