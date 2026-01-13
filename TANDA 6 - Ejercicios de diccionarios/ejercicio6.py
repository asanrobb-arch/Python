"""
Ejercicio 6
Escribir un programa que cree un diccionario vacío y lo vaya llenado con
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo
electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato
debe imprimirse el contenido del diccionario.
"""

preguntas = ['nombre', 'edad', 'sexo', 'teléfono', 'correo electrónico']

usuario = {}

for dato in preguntas:
    respuesta = input(f"Introduzca su {dato}: ")
    usuario[dato] = respuesta
    print(usuario)