"""
Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan
que no es del día tiene un descuento del 60%. Escribir un
programa que comience leyendo el número de barras vendidas
que no son del día. Después el programa debe mostrar el
precio habitual de una barra de pan, el descuento que se le
hace por no ser fresca y el coste final total.
"""

Pan = input("Introduzca el número de barras de pan vendidas que no son del día: ")

Descuento = 3.49*0.4
Coste = float(Pan)*Descuento

print(f"El precio habitual de una barra de pan es de 3.49€, al no ser fresca se le hace un descento del 60% quedándose el precio en {Descuento:.2f}.")
print(f"El coste final de todas las barras con su descuento es de {Coste}")