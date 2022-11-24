"""
este codigo hace que se envien mensajes de txt por wasap aun falta hacer unos cuantos 
arreglos y modificaciones  pero esta bn 

"""

import time 
import pywhatkit # modulo para conectarse con wasap
import keyboard # este es para la comunicacion de el teclado
import os  
from datetime import datetime # este para saber la hora en que estamos 


try:
    
    hora = datetime.now() # solicita la hora
    min = datetime.now() # solicita los min
    hora_actual = int(hora.time().strftime("%H")) # almacena la hora como str luego lo convierte a int 
    min_actual = int(min.time().strftime("%M"))
    min_actual = int(min_actual+1) # al min le suma 1 
    pywhatkit.sendwhatmsg("+51902470198", 
    "ola puto",hora_actual,min_actual)
    print("abriendo ")
    print("enviado ")

except:
    print("no se pudo encontrar") # si esk ha habido algun problema 