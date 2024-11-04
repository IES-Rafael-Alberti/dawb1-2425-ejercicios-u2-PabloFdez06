# Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"


def obtener_contraseña_correcta():

    return "contraseña"

def verificar_contraseña(contraseña_ingresada, contraseña_correcta):

    try:
        if contraseña_ingresada != contraseña_correcta:
            raise NameError("Incorrect Password!!")
        
        print("Contraseña correcta. Bienvenido!")

    except NameError as e:
        print(e)

def main():
    contraseña_correcta = obtener_contraseña_correcta()
    
    contraseña_ingresada = input("Ingresa la contraseña: ")
    
    verificar_contraseña(contraseña_ingresada, contraseña_correcta)

if __name__ == "__main__":
    main()
