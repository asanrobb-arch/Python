"""
Ejercicio 6
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y
el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y
los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un
programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
que le corresponde.
"""

nombre = str(input("Introduzca su nombre: "))
genero = str(input("Introduzca si es hombre o mujer: "))

nombre = nombre.title()
genero = genero.lower()

grupo = "ERROR"

if (genero == "mujer" and nombre < 'M') or (genero == "hombre" and nombre > 'N'):
    grupo = "A"
else:
    grupo = "B"

print (f"Su grupo es: {grupo}")

