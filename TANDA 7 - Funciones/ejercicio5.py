"""
Ejercicio 5
Escribir una función que calcule el área de un círculo y otra que calcule el volumen
de un cilindro usando la primera función.
"""

def area (r):
    calculo = 3.14 * (r ** 2)

    return calculo

def volumen (r,h):
    base = area(r)
    calculo = base * h

    return calculo

radio = float(input("Introduce el radio del círculo: "))
altura = float(input("Introduce la altura del cilindro: "))

print(f"El área del círculo es = {area(radio)}.")
print(f"El volumen del cilindro es = {volumen(radio,altura)}.")