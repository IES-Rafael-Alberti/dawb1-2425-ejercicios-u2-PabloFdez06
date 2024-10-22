# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

def comprobar_nombres(nombre: str, sexo:str):
    nombre = str(nombre)
    sexo = str(sexo)

    if nombre < "l" and sexo == "F":
        return print("Perteneces el grupo A")
    elif nombre > "r" and sexo == "M":
        return print("Perteneces el grupo A")
    else:
        return print("Perteneces al grupo B")



def main():
    nombre = input("Introduzca su nombre: ").lower
    sexo = input("Introduzca con que genero se identefica\nM | F: ")
    comprobar_nombres(nombre, sexo)


if __name__ == "__main__":
    main()


""" 
pertenece al grupo A si tiene un nombre anterior a la M(L) y es mujer 

posterior a la N(R) y es hombre,

SINO el resto pertenecera al grupo B """