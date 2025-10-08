"""
Ejercicio 9
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa
anterior para que también funcione cuando el día o el mes se introduzcan con un
solo carácter.
"""

fecha = input("Introduzca su fecha de nacimiento en formato dd/mm/aaaa: ")
separar = fecha.split("/")

print (f"Su fecha de nacimiento es el día {separar[0]} del mes {separar[1]} del año {separar[2]}.")
