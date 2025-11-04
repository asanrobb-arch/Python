"""
Ejercicio 13
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta
que el usuario escriba “salir” que terminará.
"""

escribir = str(input())

while escribir != "salir":
    print (escribir)
    escribir = str(input())