"""
Ejercicio 8
Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
"""

entero = int(input("Introduzca un número entero: "))

cont1 = 1

while cont1 <= entero:
    if (cont1 % 2 != 0):
        cont2 = cont1

        while cont2 >= 1:
            if (cont2 % 2 != 0):
                print (cont2, sep=" ", end=" ")
            cont2 -= 1
        
        print ("\n")
        
    cont1 += 1