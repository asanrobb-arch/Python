"""
Ejercicio 8
Escribir un programa que pregunte por consola el precio de un producto en euros
con dos decimales y muestre por pantalla el número de euros y el número de
céntimos del precio introducido.
"""

precio = input("Introduzca el precio de un producto en € con dos decimales: ")
partesPrecio = precio.split(".")

print (f"El producto cuesta {partesPrecio[0]} € y {partesPrecio[1]} cent.")