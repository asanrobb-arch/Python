"""
Ejercicio 10
Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es un número primo o no.
"""

entero = int(input("Introduzca un número entero: "))

num_divisores = 0
cont = 2

while cont < entero and num_divisores == 0:
    if (entero % cont == 0):
        num_divisores +=1
    cont += 1

if (num_divisores == 0 and entero != 1):
    print (f"El número {entero} es un número primo.")
else:
    print (f"El número {entero} no es un número primo.")