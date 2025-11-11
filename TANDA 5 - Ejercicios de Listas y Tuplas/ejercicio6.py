"""
Ejercicio 6
Escribir un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
nota que ha sacado en cada asignatura y elimine de la lista las asignaturas
aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el
usuario tiene que repetir.
"""
asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
notas = [0,0,0,0,0]

cont = 0
while (cont < len(asignaturas)):
    notas[cont] = int(input(f"Introduzca la nota que ha sacado en {asignaturas[cont]}: "))
    
    cont += 1

print ("Las asignaturas que debe repetir son: ")
cont = 0
while (cont < len(asignaturas)):
    if (notas[cont] < 5):
        print (asignaturas[cont], end=", ")

    cont += 1

print ("\n")