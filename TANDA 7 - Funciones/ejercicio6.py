"""
Ejercicio 6
Escribir una función que reciba una muestra de números en una lista y devuelva su
media.
"""

def media (lista):
    suma = 0

    for i in lista:
        suma += i
    
    resultado = suma / len(lista)
    return resultado

numeros = [1,2,3,4,5,6,7,8,9,10]

print (f"La media es = {media(numeros)}")