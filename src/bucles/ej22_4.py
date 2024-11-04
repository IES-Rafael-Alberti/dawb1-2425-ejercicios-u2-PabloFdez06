# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

def serie_edad(edad):

    for i in range(edad, -1, -1):
        if i == 0:
            print(i)
        else:
            print(i, end=", ")
   

def pedir_edad():

    edad_correcto = False
    while not edad_correcto:
        try:
            edad = int(input("Indique su edad: "))
            if type(edad) != int:
                print(f"ERROR: El número debe ser entero.")

            elif edad < 0:
                edad_correcto = False
                print(f"ERROR: El número debe ser positivo.")

            else:
                edad_correcto = True

        except ValueError:
            print(f"ERROR de Formato!!!")

    return edad

def main():
    edad = pedir_edad()
    serie_edad(edad)


if __name__ == "__main__":
    main()