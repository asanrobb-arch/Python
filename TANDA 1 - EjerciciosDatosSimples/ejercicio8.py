"""
Ejercicio 8
Escribir un programa que pida al usuario dos números enteros
y muestre por pantalla la <n> entre <m> da un cociente <c>
y un resto <r> donde <n> y <m> son los números introducidos
por el usuario, y <c> y <r> son el cociente y el resto de la
división entera respectivamente.
"""

N = input("Introduzca el dividendo de la división: ")
M = input("Introduzca el divisor de la división: ")

C = float(N)/float(M)
R = float(N)%float(M)

print(f"La división {N} entre {M} da un cociente {C} y un resto {R}.")