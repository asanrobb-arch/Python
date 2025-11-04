"""
Ejercicio 12
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
muestre por pantalla el número de veces que aparece la letra en la frase.
"""

frase = str(input("Introduzca una frase: "))
letra = str(input("Introduzca una letra: "))

cont = 0
repeticiones = 0

while cont < len(frase):
    if (frase[cont] == letra):
        repeticiones += 1
    cont += 1

print (f"La letra '{letra}' aparece {repeticiones} veces en la frase '{frase}'.")