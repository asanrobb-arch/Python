"""
Ejercicio 8
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un
palíndromo.
"""

palabra = str(input("Introduzca una palabra: "))

palabra_al_reves = palabra[::-1]

if palabra == palabra_al_reves:
    print (f"La palabra {palabra} es un palíndromo porque del revés es {palabra_al_reves}.")
else:
    print (f"La palabra {palabra} no es un palíndromo porque del revés es {palabra_al_reves}.")