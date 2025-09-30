"""
Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que
te ofrece el 4% de interés al año. Estos ahorros debido a
intereses, que no se cobran hasta finales de año, se te añaden
al balance final de tu cuenta de ahorros. Escribir un programa
que comience leyendo la cantidad de dinero depositada en la
cuenta de ahorros, introducida por el usuario. Después el
programa debe calcular y mostrar por pantalla la cantidad de
ahorros tras el primer, segundo y tercer año. Redondear cada
cantidad a dos decimales.
"""

cantidad = input("Introduzca la cantidad de dinero depositada en la cuenta de ahorros: ")

año1 = float(cantidad) - (float(cantidad)*1*(4/ 100))
año2 = float(cantidad) - (float(cantidad)*2*(4/ 100))
año3 = float(cantidad) - (float(cantidad)*3*(4/ 100))

print(f"La cantidad de ahorros después del primer año es de {año1:.2f}, después del segundo año es de {año2:.2f} y después del tercero {año3:.2f}")
