"""
Ejercicio 13
Escribir un programa que pregunte por una muestra de números, separados por
comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
"""
import math

muestra = str(input("Introduzca una serie de números separados por comas: "))
lista_numeros = muestra.split(',')

media = 0

for i in lista_numeros:
    i = float(i)
    media += i

media = media/len(lista_numeros)

desviacion_tipica = 0

for i in lista_numeros:
    i = float(i)
    desviacion_tipica += (i-media)**2


desviacion_tipica = desviacion_tipica/len(lista_numeros)
desviacion_tipica = math.sqrt(desviacion_tipica)


print (f"La media de los números es {media} y la desviación típica es {desviacion_tipica}")