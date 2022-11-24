import time 
from plyer import notification 
if __name__ == '__main__':
	while True:
		notification.notify(
			title = "Alerta",
			message = "puto el que lo lea",
			timeout = 0.1
		)
		time.sleep(12334)
		continue


