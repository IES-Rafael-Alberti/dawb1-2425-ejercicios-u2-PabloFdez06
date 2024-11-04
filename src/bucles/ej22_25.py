# Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.

def obtener_palabras(frase: str):
    return frase.split()


def contar_palabras(palabras: int):
    return len(palabras)


def palabra_mas_larga(palabras: str):

    palabra_larga = palabras[0] 
    for palabra in palabras:
        if len(palabra) > len(palabra_larga):
            palabra_larga = palabra 
    return palabra_larga

def main():
    frase = input("Ingresa una frase: ")

    palabras = obtener_palabras(frase)
    cantidad_palabras = contar_palabras(palabras)
    palabra_larga = palabra_mas_larga(palabras)

    print(f"La palabra más larga es: '{palabra_larga}'")
    print(f"La cantidad de palabras es: {cantidad_palabras}")

if __name__ == "__main__":
    main()
