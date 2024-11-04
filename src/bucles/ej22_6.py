# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

# *
# **
# ***
# ****
# *****

def serie_edad(edad):
    serie = ""

    for i in range(0, edad + 1, 1):
        serie = str(i) + " " + serie
        print(serie)
   

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