"""
Ejercicio 10
Escribir un programa que pregunte por consola por los productos de una cesta de la
compra, separados por comas, y muestre por pantalla cada uno de los productos en
una línea distinta.
"""

cesta = input("Introduzca los productos a comprar separados por comas: ")
productos = cesta.split(",")

print ("Los productos que quiere comprar son: \n", *productos , sep ="\n")