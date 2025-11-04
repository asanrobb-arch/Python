"""
Ejercicio 9
Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
correcta.
"""

contraseña = str("contraseña")

introducir_contraseña = str(input("Introduzca la contraseña: "))

while introducir_contraseña != contraseña:
    print ("Error, contraseña incorrecta.")
    introducir_contraseña = str(input("Introduzca la contraseña de nuevo: "))