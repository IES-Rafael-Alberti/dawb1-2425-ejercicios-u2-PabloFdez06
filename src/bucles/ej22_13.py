# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

def pedir_entrada():
    entradas = ""
    entra_bucle = True

    while entra_bucle:
        msj = input("> ")

        if msj == "salir":
            entra_bucle = False
        
        else:
            entradas += "- " + msj + "\n"
    
    mostrar_eco(entradas)



def mostrar_eco(texto: str):
    print("ECO USUARIO: \n" + texto.strip())



def main():
    pedir_entrada()


if __name__ == "__main__":
    main()