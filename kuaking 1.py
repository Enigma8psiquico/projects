"""# consula el nombre de la maquina y la ip 
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(f"hostname: ", hostname)
print(f"ip: ", ip)


# escaner de puertos 
import sys
import socket

objetivo = socket.gethostbyname(input("ingrese la direccion ip"))
print("escaneando ..")

try:
	for port in range(1,150):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		resultado = s.connect_ex((objetivo, port))
		if resultado == 0:
			print(f"el puerto esta abierto {port}")
		s.close()
except Exception as e:
	print("saliendo")


# decimal a binario 
def binario(deciamal):
	binario = ""
	while deciamal // 2 != 0:
		binario = str(deciamal % 2) + binario
		deciamal = deciamal // 2

	return str(deciamal) + binario

numero = int(input("introduce el numero"))
print(binario(numero))
"""
# craakear contraseñas 
import hashlib

encontrada = 0
input_hash = input("ingrese la contraseña ")
pass_doc = input("ingrese el diccionario ")

try:
	pass_file = open(pass_doc, "r")
except Exception as e:
	print("error: ", pass_doc, "no ha sido hasheaada")

for palabra in pass_file:
	palabra_cifradaa = palabra.enconde("utf-8")
	palabra_hasheada = hashlib.md5(palabra_cifradaa.strip())
	digest = palabra_hasheada.hexdigest()

	if digest == input_hash:
		print("contraseña encontraadaa: ", palabra)
		encontrada = 1
		break

if not encontrada:
	print("no lo encontre")