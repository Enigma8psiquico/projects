#!/usr/bin/env python
# chatbot
try:
	import speech_recognition as sr
	import pyttsx3
	import pywhatkit
except ImportError:
	import speech_recognition as sr
	import pyttsx3
	import pywhatkit


listener = sr.Recognizer()
name = "robert" # definir nombre 
engine = pyttsx3.init()
voices = engine.getProperty("voices")
# la colleccion [1] es para cambiar el tipo de voz
engine.setProperty("voice", voices[0].id)



# definimos metodo mostrar nuestro dialogo 
def talk(text):
	engine.say(text) 
	engine.runAndWait()




# funcion de escuchar 
def listen():
	try:
		with sr.Microphone() as source:
			print("Escuchando uwu")
			voice = listener.listen(source)
			rec = listener.recognize_google(voice)
			# validacion 
			rec = rec.lower()
			if name in rec: # si el nombre esta dentro de lo que dijimos 
				rec = rec.replace(name, " ") # reemplazamos el nombre por algo vacio
				print(rec)
				talk(rec)
	except:
		print("No entendi xd")
		pass
	return rec # retorna en el metodo listen

# funciones de que haremos 
def run():
	rec = listen()
	if "reproduce" in rec: 
		music = rec.replace("reproduce", "")
		talk(f"reproduciendo {music}")
		pywhatkit.playnoyt(music)

run()