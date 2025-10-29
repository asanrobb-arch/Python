"""
Ejercicio 5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
año que dura la inversión.
"""

cantidad = float(input("Introduzca una cantidad a invertir: "))
interes = float(input("Introduzca el interés anual: "))
años = float(input("Introduzca el número de años: "))

cont = 1

while cont <= años:
    capital = cantidad * cont * (interes/100)

    print (f"El capital obtenido el año {cont} es de: {capital}€")

    cont += 1

