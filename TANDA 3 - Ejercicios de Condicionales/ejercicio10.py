"""
Ejercicio 10
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.

    ● Ingredientes vegetarianos: Pimiento y tofu.
    ● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y
en función de su respuesta le muestre un menú con los ingredientes disponibles
para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el
tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la
pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""

tipo_pizza = str(input("Introduzca si quiere una pizza vegetariana o no vegetariana: "))
tipo_pizza = tipo_pizza.lower()

if tipo_pizza ==  "vegetariana":
    ingrediente_vegetariano = str(input("Los ingredientes vegetarianos son pimiento y tofu, diga cual de ellos quiere: "))
    ingrediente_vegetariano = ingrediente_vegetariano.lower()

    print (f"Los ingredientes de tu pizza {tipo_pizza} son mozzarella, tomate y {ingrediente_vegetariano}")
elif tipo_pizza == "no vegetariana":
    ingrediente_no_vegetariano = str(input("Los ingredientes no vegetarianos son peperoni, jamón y salmón, diga cual de ellos quiere: "))
    ingrediente_no_vegetariano = ingrediente_no_vegetariano.lower()

    print (f"Los ingredientes de tu pizza {tipo_pizza} son mozzarella, tomate y {ingrediente_no_vegetariano}")