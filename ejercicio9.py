"""
Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a
invertir, el interés anual y el número de años, y muestre por
pantalla el capital obtenido en la inversión.
"""

cantidad = input("Introduzca la cantidad a invertir: ")
interes = input("Introduzca el interés anual: ")
tiempo = input("Introduzca el tiempo en años: ")

RESULTADO = float(cantidad)*float(tiempo)*(float(interes)/ 100)

print(f"El capital obtenido en la inversión es de: {RESULTADO}")