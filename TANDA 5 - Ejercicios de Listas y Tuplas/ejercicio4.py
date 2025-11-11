"""
Ejercicio 4
Escribir un programa que pregunte al usuario los números ganadores de la lotería
primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
a mayor.
"""

primitiva = input("Introduzca los números ganadores de la primitiva: ")
primitiva = primitiva.split(", ")
primitiva = sorted(primitiva)

print ("Los números ordenador de menor a mayor son: ")
print (primitiva)