"""
Ejercicio 11
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
una a una las letras de la palabra introducida empezando por la última.
"""

palabra = str(input("Introduzca una palabra: "))

cont = len(palabra) - 1

while cont >= 0:
    print (palabra[cont], sep=" ", end= " ")
    cont -= 1

print ("\n")