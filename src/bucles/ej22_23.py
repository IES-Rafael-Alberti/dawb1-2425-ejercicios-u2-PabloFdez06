# Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.

# Ejemplo de ejecución:
# Libro: Los 3 mosqueteros
# Libro: Historia de 2 ciudades
# Libro: /
# Línea completa. Aparecen 2 dígitos numéricos.
# Libro: 20000 leguas de viaje submarino
# Libro: El señor de los anillos
# Libro: /
# Línea completa. Aparecen 5 dígitos numéricos.
# Libro: 20 años después
# Libro: *
# Fin. Se leyeron 2 líneas completas.


def ingresa_valor():

    valor_correcto = False
    while not valor_correcto:
            valor = input("Libro: ").strip()
            valor_correcto = True


    return valor

def comprueba_si_hay_fin_o_linea(compr_valor: str):

    comprobacion = False

    while not comprobacion:
        if compr_valor == "/":
            print("Línea completa. Aparecen 5 dígitos numéricos.")
            comprobacion = True
            ingresa_valor()

        if compr_valor == "*":
            print("Línea completa. Aparecen 5 dígitos numéricos.")
            comprobacion = True

        else: 
            comprobacion = True
        
    return compr_valor
            


def informar_lineas(digitos):
    pass


def main():
    valor = ingresa_valor()
    comprueba_si_hay_fin_o_linea(valor)
    compr_valor = comprueba_si_hay_fin_o_linea()
    informar_lineas(compr_valor)

if __name__ == "__main__":
    main()


#### PREGUNTAR EN CLASE ####