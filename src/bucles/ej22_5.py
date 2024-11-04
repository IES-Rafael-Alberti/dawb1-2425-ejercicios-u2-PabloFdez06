# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

# # Formula para calcular El capital tras un año.
# # amount *= 1 + interest / 100
# # En donde:
# # - amount: Cantidad a invertir
# # - interest: Interes porcentual anual 

def invertir_numero(num, interest):
    amount = num
    amount *= 1 + interest / 100
    return amount
   

def pedir_num():

    num_correcto = False
    while not num_correcto:
        try:
            num = int(input("Indique una cantidad a invertir: "))
            if num < 0:
                num_correcto = False
                print(f"ERROR: El número debe ser positivo.")

            else:
                num_correcto = True

        except ValueError:
            print(f"ERROR de Formato!!!")

    return num

def pedir_interest():

    interest_correcto = False
    while not interest_correcto:
        try:
            interest = float(input("Indique el interes porcentual anual: "))
            if type(interest) != float:
                    print(f"ERROR: El número debe ser entero.")
            
            elif interest < 0:
                interest_correcto = False
                print(f"ERROR: El número debe ser positivo.")

            else:
                interest_correcto = True

        except ValueError:
            print(f"ERROR de Formato!!!")

    return interest

def main():
    num = pedir_num()
    interest = pedir_interest()
    print(invertir_numero(num, interest))


if __name__ == "__main__":
    main()

##### EJERCICIO SIN ACABAR, NO ENTIENDO BIEN EL ENUNCIADO #####