"""
Ejercicio 6
Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo, de altura el número introducido.
*
**
***
****
*****
"""

entero = int(input("Introduzca un número entero: "))

cont = 1

while cont <= entero:
    print ("*"*cont)
    cont += 1