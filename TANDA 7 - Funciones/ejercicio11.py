"""
Ejercicio 11
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario
con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el
diccionario generado con la función anterior y devuelva una tupla con la palabra más
repetida y su frecuencia.
"""

frase = "Buenos días a todos todos"
div = frase.split(" ")
dic = {}

for i in div:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

print(dic)