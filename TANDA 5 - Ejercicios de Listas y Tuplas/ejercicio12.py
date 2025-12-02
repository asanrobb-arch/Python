"""
Ejercicio 12
Escribir un programa que almacene las matrices
en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando
cada vector fila en una lista.
"""

matriz1 = ((1,2,3),
           (4,5,6))

matriz2 = ((-1,0),
           ( 0,1),
           ( 1,1))

print ("La multiplicación de lass matrices es: ")

multiplicacion = []

for i in range(len(matriz1)):
    fila = []
    for j in range(len(matriz2[0])):
        multiplicacion_fila = 0
        for k in range(len(matriz2)):
            multiplicacion_fila += matriz1[i][k] * matriz2[k][j]
        fila.append(multiplicacion_fila)
    multiplicacion.append(fila)

for fila in multiplicacion:
    print(fila)