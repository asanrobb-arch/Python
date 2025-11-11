"""
Ejercicio 7
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las
letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista
resultante.
"""
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numero_letras = len (abecedario)
abecedario_nuevo = []

cont = 0

while (cont < numero_letras):
    if ((cont+1) % 3 != 0):
        abecedario_nuevo.append(abecedario[cont])
    cont += 1

print (abecedario_nuevo)