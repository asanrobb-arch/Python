"""
Ejercicio 3
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla todos los números impares desde 1 hasta ese número separados por
comas.
"""

numero = int(input("Introduzca un número positivo: "))
x = 1

while x <= numero:
    if (x%2) != 0:
        if x == numero:
            print (x)
        else:
            print (x, ", ")
    x = x + 1