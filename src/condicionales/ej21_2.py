# Escribir un programa que almacene la cadena de caracteres contrasenia en una variable, pregunte al usuario por la contrasenia e imprima por pantalla si la contrasenia introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.


def almacenar_contrasenia():
    contraseña = "contraseña"

    return contraseña

def comprobar_contrasenia(valor):
    contraseña = almacenar_contrasenia()
    if contraseña == valor:
        return "Contraseña Correcta!"
    else:
        return "Contraseña incorrecta...!"



def main():
    preg_contraseña = input("Introduzca una contraseña: ").lower()
    comprobacion = comprobar_contrasenia(preg_contraseña)
    print(comprobacion)


if __name__ == "__main__":
    main()