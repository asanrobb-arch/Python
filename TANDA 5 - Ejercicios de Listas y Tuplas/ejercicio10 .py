"""
Ejercicio 10
Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46,
22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
"""

precios = (50,75,46,22,80,65,8)

mayor = precios[0]
menor = precios[0]

for precio in precios:
    if mayor < precio:
        mayor = precio
    if menor > precio:
        menor = precio

print (f"El numéro mayor es {mayor} y el menor es {menor}.")