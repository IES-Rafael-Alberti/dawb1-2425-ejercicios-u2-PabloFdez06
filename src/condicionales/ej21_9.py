# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.


def pedir_edad():

    edad_correcta = False
    while not edad_correcta:
        try:
            edad = int(input("Indique su edad: "))
            if edad > 1 and edad < 100:
                edad_correcta = True
            else:
                edad_correcta = False
                print(f"ERROR: La edad debe estar entre 1 y 100")
                
        except ValueError:
            print(f"ERROR de Formato!!!")

    return edad


def precio_ticket(edad):
    if edad < 4:
        precio = "El cliente es menor de 4 años, podrá entrar gratis"

    elif edad > 4 and edad <= 18:
        precio = "El precio de la entrada será equivalente a 5€"

    else:
        precio = "El precio de la entrada será equivalente a 10€"

    return precio







def main():
    edad = pedir_edad()
    precio = precio_ticket(edad)
    print(f"Usted tiene {edad} Años: {precio}")


if __name__ == "__main__":
    main()