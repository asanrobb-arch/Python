"""
Ejercicio 5
Escribir un programa que almacene en una lista los números del 1 al 10 y los
muestre por pantalla en orden inverso separados por comas.
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros.reverse()

cont = 0

while (cont < len(numeros)):
    if cont < len(numeros)-1:
        print (f"{numeros[cont]},", end=" ")
    else:
        print (numeros[cont], end="\n")
    cont += 1