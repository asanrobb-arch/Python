"""
Ejercicio 10
Escribir un programa que permita gestionar la base de datos de clientes de una
empresa. Los clientes se guardarán en un diccionario en el que la clave de cada
cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre,
dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se
trata de un cliente preferente. El programa debe preguntar al usuario por una opción
del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4)
Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la
opción elegida el programa tendrá que hacer lo siguiente:

    1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.

    2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
    
    3. Preguntar por el NIF del cliente y mostrar sus datos.

    4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre.

    5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.

    6. Terminar el programa.
"""

clientes = {}
opcion = ""

while opcion != "6":
    print("\n--- MENÚ DE GESTIÓN DE CLIENTES ---")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")
    
    opcion = input("Elija una opción (1-6): ")

    if opcion == "1":
        nif = input("Introduce el NIF del cliente: ")
        nombre = input("Nombre: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        vip = input("¿Es cliente preferente? (S/N): ").upper()
        
        datos = {
            'nombre': nombre,
            'dirección': direccion,
            'teléfono': telefono,
            'correo': correo,
            'preferente': vip == 'S'
        }
        
        clientes[nif] = datos
        print(f"Cliente {nombre} añadido correctamente.")

    elif opcion == "2":
        nif = input("Introduce el NIF del cliente a eliminar: ")
        if nif in clientes:
            del clientes[nif]
            print("Cliente eliminado.")
        else:
            print("No existe ningún cliente con ese NIF.")

    elif opcion == "3":
        nif = input("Introduce el NIF del cliente a mostrar: ")
        if nif in clientes:
            print(f"\nDatos del cliente {nif}:")
            for clave, valor in clientes[nif].items():
                print(f"{clave.title()}: {valor}")
        else:
            print("Cliente no encontrado.")

    elif opcion == "4":
        print("\n--- LISTA DE TODOS LOS CLIENTES ---")
        for nif in clientes:
            nombre_cliente = clientes[nif]['nombre']
            print(f"NIF: {nif} - Nombre: {nombre_cliente}")

    elif opcion == "5":
        print("\n--- LISTA DE CLIENTES PREFERENTES ---")
        for nif in clientes:
            if clientes[nif]['preferente']:
                print(f"NIF: {nif} - Nombre: {clientes[nif]['nombre']}")

    elif opcion == "6":
        print("Finalizando programa...")
    
    else:
        print("Opción no válida.")