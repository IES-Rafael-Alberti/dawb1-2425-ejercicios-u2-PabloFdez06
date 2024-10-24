# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

def comprobar_edad(edad):
    if edad >= 18:
        return print("El sujeto es mayor de edad")
    # if edad < 0:
    #     raise ValueError("La edad no puede ser negativa.")
    # if edad == 0: 
    #     raise ValueError("La edad no puede ser 0.")
    # if edad > 125: 
    #     raise ValueError("La edad no puede ser mayor a 125.")   
    else:
        return print("El sujeto es menor de edad")
      

def main():
    edad = int(input("Introduce tu edad: "))
    comprobar_edad(edad)

if __name__ == "__main__":
    main()