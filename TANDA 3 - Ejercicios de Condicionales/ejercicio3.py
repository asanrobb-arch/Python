"""
Ejercicio 3
Escribir un programa que pida al usuario dos números y muestre por pantalla su
división. Si el divisor es cero el programa debe mostrar un error.
"""

dividendo = float(input("Introduzca el dividendo de la división: "))
divisor = float(input("Introduzca el divisor de la división: "))

if divisor <= 0 or dividendo < 0:
    print ("No se puede realizar la operación.")
else:
    print (f"El resultado de la división es: {dividendo/divisor}.")