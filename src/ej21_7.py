
def pedir_renta() -> int:
    renta_correcta = False
    while not renta_correcta:
        try:
            renta = int(input("Introduzca su renta anual: "))
            renta_correcta = True
                
        except ValueError:
            print(f"ERROR de Formato!!!")

    return renta
    
def comprobar_impositivo(renta):
    impositivo = None

    if renta <= 10000: 
        impositivo = "5%"
    elif renta > 10000 or renta <= 20000:
        impositivo = "15%"
    elif renta > 20000 or renta <= 35000:
        impositivo = "20%"
    elif renta > 35000 or renta <= 60000:
        impositivo = "30%"
    elif renta > 60000:
        impositivo = "45%"

    return impositivo

    
def main():
    renta = pedir_renta()
    impositivo = comprobar_impositivo(renta)
    print(f"El impositivo para una renta igual a {renta} es de {impositivo}")

    return


if __name__ == "__main__":
    main()