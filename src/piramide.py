def pedir_num():

    num_correcto = False
    while not num_correcto:
        try:
            num = int(input("Indique su número: "))
            if type(num) != int:
                print(f"ERROR: El número debe ser entero.")

            elif num < 0:
                num_correcto = False
                print(f"ERROR: El número debe ser positivo.")
            
            elif num > 100:
                num_correcto = False
                print(f"ERROR: El número debe estar entre 0 y 100.")
                
            else:
                num_correcto = True

        except ValueError:
            print(f"ERROR de Formato!!!")

    return num

def serie_num(num: int, secuencia: str):
    # piramide = ""
    secuencia = ""

    for i in range(num, -1, -1):
        suma = total(i, num)
        secuencia = str(i) + " + " + secuencia
        # piramide = piramide + secuencia + "\n"

        print(f"{i} => {secuencia} = {str(suma)}")




def total(i, num):
    for j in range(i, num):
        num += j
    return num
        




def main():
    # suma = ""
    secuencia = ""
    # cont = 0
    num = pedir_num()
    #print(total(num, suma,cont))
    serie_num(num,secuencia)




if __name__ == "__main__":
    main()