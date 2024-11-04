# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios.
# Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una 
# tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable	0.4
# Meritorio	0.6 o más

# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.


# PUNTUACION = 0.0, 0.4, 0.6


def pedir_puntuacion():
    # puntuacion = input("Indique su puntuación de este año: ")
    # return puntuacion

    punt_correcta = False
    while not punt_correcta:
        try:
            puntuacion = float(input("Indique su puntuación de este año: "))
            if puntuacion == 0.0 or puntuacion == 0.4 or puntuacion == 0.6:
                punt_correcta = True
            else:
                punt_correcta = False
                print(f"ERROR: El número ha de estar entre los valores | 0.0 | 0.4 | 0.6 |")
                
        except ValueError:
            print(f"ERROR de Formato!!!")

    return puntuacion


def comprobar_nivel(puntuacion):
        if puntuacion == 0.0:
            puntuacion2 = "Tu puntuacion de este año es inaceptable"
        
        elif puntuacion == 0.4:
            puntuacion2 = f"Tu puntuación de este año es aceptable, recibiras: {2400*0.4}€"
            
        
        elif puntuacion >= 0.6:
            puntuacion2 = f"Tu puntuación de este año es aceptable, recibiras: {2400*0.6}€"

        return puntuacion2




def main():
    puntuacion = pedir_puntuacion()
    puntuacion2 = comprobar_nivel(puntuacion)
    print(f"Con un total de puntuación de: {puntuacion}... {puntuacion2}")

    return


if __name__ == "__main__":
    main()