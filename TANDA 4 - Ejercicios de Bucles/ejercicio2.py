"""
Ejercicio 2
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos
los años que ha cumplido (desde 1 hasta su edad).
"""

edad = int(input("Introduzca su edad: "))
cont = 1

print ("Los años que ha cumplido son: ")

while cont <= edad:
    print (cont)
    cont = cont + 1