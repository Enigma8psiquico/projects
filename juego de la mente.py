#!/usr/bin/env python
# juego mental parte 2 

try:
	import random as rd
	from dataclasses import dataclass
	import os
except:
	pass

@dataclass
class Inicio(object):
	"""docstring for Inicio"""
	def __init__(self):
		portada()
	# variables de entrada
		# declaracion de las variables heredadas
		a = rd.randint(1,100) 
		b = rd.randint(1,100)

		# elegir un problema al azar 
		maximo = 5
		minimo = 0
		opcion = rd.randint(1,4)
		cambio = rd.randint(-1,1)

		opcion = opcion +(cambio)
		if opcion == maximo:
			opcion = opcion - 1
		elif opcion == minimo:
			opcion = opcion + 1
			print(opcion)

		# respuesta
		if opcion == 1:
			suma(a,b) # ejecutamos la funcion con las variables heredadas 

		elif opcion == 2:
			resta(a,b)

		elif opcion == 3:
			division(a,b)

		elif opcion == 4:
			multiplicacion(a,b)

def portada():
	print("""
""\"Juegos mentales :3\"""

		""")

# --------- Funciones ......
def suma(a,b):
	c = a + b
	print(f"Cuanto es? {a} + {b} ")
	respuesta = int(input("Respuesta: "))
	if respuesta == c:
		print(f"Correcto!!")
		Inicio()
	else:
		print(f"Incorrecto la respuesta es {c}")
		suma(a,b)


def resta(a,b):
	c = a - b 
	print(f"Cuanto es? {a} - {b}")
	respuesta = int(input("Respuesta: "))
	if respuesta == c:
		print(f"Correcto!!")
		Inicio()
	else:
		print(f"Incorrecto la respuesta es {c}")
		resta(a,b)

def division(a,b): 
	c = a / b 
	print(f"Cuanto es? {a} / {b}")
	respuesta = float(input("Respuesta: "))
	if respuesta == c:
		print(f"Correcto!!")
		Inicio()
	else:
		print(f"Incorrecto la respuesta es {c}")
		division(a,b)

def multiplicacion(a,b):
	c = a * b 
	print(f"Cuanto es? {a} * {b}")
	respuesta = int(input("Respuesta: "))
	if respuesta == c:
		print(f"Correcto!!")
		Inicio()
	else:
		print(f"Incorrecto la respuesta es {c}")
		multiplicacion(a,b)




if __name__=="__main__":
	# 				ahi engresan las herencias -> () envia al __init__()
	Numeros = Inicio()