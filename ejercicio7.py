"""
Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y
estatura (en metros), calcule el índice de masa corporal y lo
almacene en una variable, y muestre por pantalla la frase Tu
índice de masa corporal es <imc> donde <imc> es el índice
de masa corporal calculado redondeado con dos decimales.
"""

peso = input("Introduzca su peso en kg: ")
altura = input("Introduzca su altura en m: ")

imc = float(peso)//float(altura)**2

print(f"Tu IMC es: {imc:.2f}")