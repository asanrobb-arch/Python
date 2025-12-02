"""
Ejercicio 9
Escribir un programa que pida al usuario una palabra y muestre por pantalla el
número de veces que contiene cada vocal.
"""

palabra = str(input("Introduzca una palabra: "))

conta = 0
conte = 0
conti = 0
conto = 0
contu = 0

for i in palabra:
    if i == 'a':
        conta += 1
    if i == 'e':
        conte += 1
    if i == 'i':
        conti += 1
    if i == 'o':
        conto += 1
    if i == 'u':
        contu += 1

print (f"La palabra {palabra} contiene {conta} número de veces la a, {conte} la e, {conti} la i, {conto} la o y {contu} la u.")