"""
Ejercicio 7
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""

cont1 = 1
cont2 = 0

while cont1 <= 10:
    print (f"Tabla multiplicar número {cont1}:")

    cont2 = 0
    while cont2 <= 10:
        print (f"{cont1} x {cont2} = {cont1*cont2}")
        cont2 += 1

    cont1 += 1