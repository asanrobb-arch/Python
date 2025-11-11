"""
Ejercicio 3
Escribir un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
nota que ha sacado en cada asignatura, y después las muestre por pantalla con el
mensaje En <asignatura> has sacado <nota> donde <asignatura> es
cada una des las asignaturas de la lista y <nota> cada una de las correspondientes
notas introducidas por el usuario.
"""
asignaturas = ("Matemáticas","Física","Química","Historia","Lengua")
notas = [0,0,0,0,0]

cont = 0

while (cont < len(asignaturas)):
    notas[cont] = int(input(f"Introduzca la nota que ha sacado en {asignaturas[cont]}: "))
    cont += 1

cont = 0

while (cont < len(asignaturas)):
    print (f"En {asignaturas[cont]} has sacado {notas[cont]}.")
    cont += 1