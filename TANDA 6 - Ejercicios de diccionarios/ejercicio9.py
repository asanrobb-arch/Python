"""
Ejercicio 9
Escribir un programa que gestione las facturas pendientes de cobro de una
empresa. Las facturas se almacenarán en un diccionario donde la clave de cada
factura será el número de factura y el valor el coste de la factura. El programa debe
preguntar al usuario si quiere añadir una nueva factura, pagar una existente o
terminar. Si desea añadir una nueva factura se preguntará por el número de factura
y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará
por el número de factura y se eliminará del diccionario. Después de cada operación
el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la
cantidad pendiente de cobro.
"""

facturas = {}
cobrado = 0
pendiente = 0

continuar = True

while continuar:
    opcion = input("\n¿Qué quieres hacer? Añadir (A), Pagar (P), Terminar (T): ")
    opcion = opcion.upper()

    if opcion == 'A':
        num_factura = input("Introduce el número de factura: ")
        coste = float(input("Introduce el coste de la factura: "))
        facturas[num_factura] = coste

    elif opcion == 'P':
        num_factura = input("Introduce el número de factura a pagar: ")
        if num_factura in facturas:
            cobrado += facturas[num_factura]
            del facturas[num_factura]
        else:
            print("Esa factura no existe.")

    elif opcion == 'T':
        continuar = False
    
    pendiente = 0
    for i in facturas:
        pendiente += facturas[i]
        
    if continuar:
        print(f"   --> Recaudado: {cobrado} €")
        print(f"   --> Pendiente de cobro: {pendiente} €")

print("\nPrograma terminado.")