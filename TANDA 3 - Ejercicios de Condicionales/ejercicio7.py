"""
Ejercicio 7
Los tramos impositivos para la declaración de la renta en un determinado país son
los siguientes:
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla
el tipo impositivo que le corresponde.-
"""

renta = float(input("Introduzca su renta anual: "))

if renta < 10000:
    print ("Le corresponde un tipo impositivo de: 5%")
elif renta > 10000 and renta < 20000:
    print ("Le corresponde un tipo impositivo de: 15%")
elif renta > 20000 and renta < 35000:
    print ("Le corresponde un tipo impositivo de: 20%")
elif renta > 35000 and renta < 60000:
    print ("Le corresponde un tipo impositivo de: 30%")
else:
    print ("Le corresponde un tipo impositivo de: 45%")