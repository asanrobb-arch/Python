"""
Ejercicio 7
Escribir un programa que cree un diccionario simulando una cesta de la compra. El
programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta
que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la
compra y el coste total, con el siguiente formato
"""

compra = {}

num = 1
suma = 0

while num==1:
    articulo = str(input("Introduzca un artículo: "))
    precio = float(input("Introduzca su precio: "))

    compra[articulo] = precio

    suma += precio

    continuar = input("¿Quiere continuar? [S|N]: ")

    if continuar.title() == 'N':
        num = 0
    
print ("------LISTA DE LA COMPRA------")
print ("Artículo                Precio")
print ("------------------------------")

for i in compra:
    print (f"{i}                       {compra[i]}")  