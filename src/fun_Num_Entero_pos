# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def serie_edad(edad):

    for i in range(1, edad + 1):
        print(i)
   

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