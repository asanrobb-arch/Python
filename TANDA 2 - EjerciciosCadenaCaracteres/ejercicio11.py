"""
Ejercicio 11
Escribir un programa que pregunte el nombre el un producto, su precio y el número
de unidades y muestre por pantalla una cadena con el nombre del producto seguido
de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con
tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
"""

nombre = input ("Introduzca el nombre del producto: ")
precio = float(input ("Introduzca el precio del producto: "))
unidades = float(input ("Introduzca el número de unidades que quiere comprar: "))

print (f"El producto {nombre} tiene un precio de {precio:.2f} €/ud y el coste total es: {(precio*unidades):.2f}")

