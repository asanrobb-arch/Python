"""
Ejercicio 2
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono
y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje
<nombre> tiene <edad> años, vive en <dirección> y su número de
teléfono es <teléfono>.
"""

usuario = {}

usuario['nombre'] = input("Intrduzca su nombre: ")
usuario['edad'] = input("Introduzca su edad: ")
usuario['dirección'] = input("Introduzca su dirección: ")
usuario['teléfono'] = input("Introduzca su número de teléfono: ")

print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['dirección']} y su número de teléfono es {usuario['teléfono']}.")