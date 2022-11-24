
#!/usr/bin/env python
	
from pynput import keyboard as kb
def pulsacion(tecla):
	print(f"se ha pulsado{str(tecla)} ")

with kb.Listener(pulsacion) as pulsar:
	pulsar.join()