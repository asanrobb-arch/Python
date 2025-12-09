"""
Ejercicio 3
Escribir un programa que guarde en un diccionario los precios de las frutas de la
tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el
precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe
mostrar un mensaje informando de ello.
    Fruta       Precio
    Plátano     1.35
    Manzana     0.80
    Pera        0.85
    Naranja     0.70
"""

frutas = {'Platano':1.35, 'Manzana':0.80, 'Pera':0.85, 'Naranja':0.70}

fruta = str(input("Introduzca una fruta: "))
fruta = fruta.title()
kilos = float(input("Introduzca el número de kilos: "))

if fruta in frutas:
    print(f"\nEl precio de {kilos} kg de {fruta.lower()} es de {kilos*frutas[fruta]} €.")
else:
    print("\nLa fruta no está en el diccionario.")