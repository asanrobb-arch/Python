"""
Ejercicio 4
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre
por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es
el nombre del mes.
"""

meses =  {1:'enero',2:'febrero',3:'marzo',4:'abril',5:'mayo',6:'junio',7:'julio',8:'agosto',9:'septiembre',10:'octubre',11:'noviembre',12:'diciembre'}
fecha = str(input("Introduzca una fecha en formato dd/mm/aaaa: "))
fecha_partes = fecha.split('/')

fecha = {}
fecha['dd'] = int(fecha_partes[0])
fecha['mm'] = int(fecha_partes[1])
fecha['aaaa'] = int(fecha_partes[2])



print (f"Fecha: {fecha['dd']} de {meses[fecha['mm']]} de {fecha['aaaa']}.")