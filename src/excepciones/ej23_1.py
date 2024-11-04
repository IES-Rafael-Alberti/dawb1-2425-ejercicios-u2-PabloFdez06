# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def validar_edad(edad: int):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    if edad == 0: 
        raise ValueError("La edad no puede ser 0.")
    if edad > 125: 
        raise ValueError("La edad no puede ser mayor a 125.")     


def comprobar_anios(valor: str) -> int:
        edad = None
        try:
            edad = int(valor)
            validar_edad(edad)
        except ValueError as e:
            if edad is None:
               print("ERROR! número incorrecto!.. Inténtalo otra vez")
            else:
                edad = None
                print(f"ERROR! {e}.. Inténtalo otra vez")

        return edad


def mostrar_anios(edad):
    for i in range(1, edad + 1):
        print (i)


def pedir_edad() -> int:
    edad = None
    while edad == None:
        valor = input("Introduzca su edad: ")
        edad = comprobar_anios(valor)

    return edad    


def main():
    edad = pedir_edad()
    mostrar_anios(edad)


if __name__ == "__main__":
    main()