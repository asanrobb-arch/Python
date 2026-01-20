"""
Ejercicio 8
Escribir un programa que cree un diccionario de traducción español-inglés. El
usuario introducirá las palabras en español e inglés separadas por dos puntos, y
cada par <palabra>:<traducción> separados por comas. El programa debe
crear un diccionario con las palabras y sus traducciones. Después pedirá una frase
en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra
no está en el diccionario debe dejarla sin traducir.
"""
traducciones = {'hola': 'hello', 
                'perro': 'dog', 
                'gato': 'cat', 
                'es': 'is', 
                'rojo': 'red', 
                'casa': 'house',
                'el': 'the',
                'la': 'the'
                }

frase = input("Introduce una frase en español: ")
palabras = frase.split()

print("\nTraducción:")

for palabra in palabras:
    if palabra in traducciones:
        print(traducciones[palabra], end=" ")
    else:
        print(palabra, end=" ")

print("\n")