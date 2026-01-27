"""
Ejercicio 3
Escribir una función que reciba un número entero positivo y devuelva su factorial.
"""

def factorial(num):
    num = abs(num)
    calculo = 1

    while num >= 1:
        calculo *= num
        num -= 1
    
    return calculo

numero = int(input("Introduzca un número entero positivo: "))
print(f"El factorial de {abs(numero)} es = {factorial(numero)}")