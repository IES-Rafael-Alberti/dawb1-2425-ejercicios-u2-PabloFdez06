# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.


def almacenar_contraseña(contraseña):
    contraseña = "contraseña"
    return contraseña

def pedir_contraseña(contraseña_usr):
    contraseña_usr = str(input("Introduce tu contraseña")).lower
    return contraseña_usr


def main():
    
    if contraseña_usr == contraseña:
        print("Felicidades, has adivinado la contraseña!")
    else:
        print("Contraseña incorrecta!")


    contraseña = almacenar_contraseña()
    contraseña_usr = pedir_contraseña()



if __name__ == "__main__":
    main()