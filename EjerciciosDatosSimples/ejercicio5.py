"""
Ejercicio 5
Escribir un programa que pregunte al usuario por el número de
horas trabajadas y el coste por hora. Después debe mostrar
por pantalla la paga que le corresponde.
"""

Horas = input("Introduzca el número de horas trabajadas: ")
Coste = input("Introduzca el coste por hora: ")

Paga = float(Horas) * float(Coste)

print(f"La paga que le corresponde es {Paga}€.")