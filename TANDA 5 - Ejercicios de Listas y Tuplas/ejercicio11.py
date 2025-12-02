"""
Ejercicio 11
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y
muestre por pantalla su producto escalar.
"""

vector1 = (1,2,3)
vector2 = (-1,0,2)

producto_escalar = (vector1[0]*vector2[0]) + (vector1[1]*vector2[1]) + (vector1[2]*vector2[2])

print (f"El producto escalar de los dos vectores es {producto_escalar}.")