"""
Ejercicio 6
Escribir un programa que pida al usuario que introduzca una frase en la consola y
una vocal, y después muestre por pantalla la misma frase pero con la vocal
introducida en mayúscula.
"""

frase = str(input("Introduzca una frase: "))
vocal = str(input("Introduzca una vocal que este dentro de la frase: "))

print (frase.replace(vocal,vocal.upper()))