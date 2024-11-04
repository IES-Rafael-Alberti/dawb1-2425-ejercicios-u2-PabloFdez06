# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

ABECEDARIO = "abcdefghijklmnñopqrstuvwxyz"
SEXO ="FM"


def asignar_grupo(inicial: str, sexo: str):

    if inicial < "m" and sexo == "F" or inicial > "n" and sexo == "M":
        return print("Perteneces el grupo A")
    else:
        return print("Perteneces al grupo B")



def pedir_nombre():
    nombre_correcto = False
    while not nombre_correcto:
        nombre = input("Introduzca su nombre: ").lower().strip()
        try:
            if nombre[:1] not in ABECEDARIO:
                raise ValueError("El nombre debe comenzar por una letra del abecedario!!!")
            nombre_correcto = True
        except ValueError as e:
            print(f"ERROR: {e}")
    
    return nombre



def pedir_sexo():
    sexo_correcto = False
    while not sexo_correcto:
        sexo = input("Con que genero se identifica?\nM | F:  ").upper().strip()
        try:
            if sexo not in SEXO:
                raise ValueError("El genero ha de ser masculino o femenino!!!!")
            sexo_correcto = True
        except ValueError as e:
            print(f"ERROR: {e}")

    return sexo

def main():

    nombre = pedir_nombre()
    sexo = pedir_sexo()
    asignar_grupo(nombre[:1], sexo)

    return

if __name__ == "__main__":
    main()


""" 
pertenece al grupo A si tiene un nombre anterior a la M(L) y es mujer 

posterior a la N(R) y es hombre,

SINO el resto pertenecera al grupo B """




