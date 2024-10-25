# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.


def pedir_pizza():
    # pizza_normal = None
    # pizza_vegetariana = None

    pizza_correcta = False
    while not pizza_correcta:
        try:
            pizza = input("Escoja su preferencia, cual desea?\nNormal | Vegetariana: ").strip().lower()
            if pizza == "vegetariana":
                # pizza = pizza_vegetariana
                pizza_correcta = True
            elif pizza == "normal":
                # pizza = pizza_normal
                pizza_correcta = True

            else:
                raise ValueError
                
        except ValueError:
            print(f"Seleccione una pizza de la carta, por favor!!!")

    return pizza


def elegir_ingredientes(tipo_pizza):
    
    ingredientes_correctos = False
    while not ingredientes_correctos:
        try:
            if tipo_pizza == "normal":
                ingredientes = input("Elija uno de estos 3 ingredientes:\nPeperoni | Jamón | Salmón: ").strip().lower()
                if ingredientes == "peperoni" or ingredientes == "jamón" or ingredientes == "salmón":
                    ingredientes_correctos = True
                    pizza_definitiva = f"Tu pizza no es vegetariana, y como base lleva tomate y mozzarella más tu personal que es {ingredientes}"

                else:
                    raise ValueError
                            
            elif tipo_pizza == "vegetariana":
                ingredientes = input("Elija uno de estos 2 ingredientes:\nPimiento | tofu: ").strip().lower()
                if ingredientes == "pimiento" or ingredientes == "tofu":
                    ingredientes_correctos = True
                    pizza_definitiva = f"Tu pizza es vegetariana, y como base lleva tomate y mozzarella más tu personal que es {ingredientes}"

                else:
                    raise ValueError
        
        except ValueError:
            print(f"Introduzca un ingrediente válido por favor!!!")

    return pizza_definitiva





def main():
    tipo_pizza = pedir_pizza()
    pizza = elegir_ingredientes(tipo_pizza)
    print(pizza)


if __name__ == "__main__":
    main()