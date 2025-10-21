"""
Ejercicio 1
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10
veces.
"""

palabra = str(input("Introduzca una palabra: "))
x = 1

while x <= 10:
    print (palabra, "\n")
    x = x+1