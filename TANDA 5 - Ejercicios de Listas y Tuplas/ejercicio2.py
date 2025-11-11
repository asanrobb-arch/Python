"""
Ejercicio 2
Escribir un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por
pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada
una de las asignaturas de la lista.
"""
tupla = ("Matemáticas","Física","Química","Historia","Lengua")

cont = 0

while (cont < len(tupla)):
    print (f"Yo estudio {tupla[cont]}")

    cont += 1