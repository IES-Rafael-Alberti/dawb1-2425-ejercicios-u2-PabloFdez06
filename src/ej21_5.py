# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

def comprobacion_tributaria(edad: int, ingresos:float):
    if edad > 16 and ingresos >= 1000:
        return print("Cumples los requisitos necesarios para tributar!")
    else:
        return print("No cumples los requisitos necesarios para tributar! FELICIDADES.")



def main():
    edad = int(input("Introduce tu edad: "))
    ingresos = float(input("Intruduce tus ingresos mensuales: "))
    comprobacion_tributaria(edad, ingresos)


if __name__ == "__main__":
    main()