try:
	from pygame import *
	import pygame
	pygame.init() 
	from sys import *
	import sys
except ImportError as e:
	from pygame import *
	import pygame
	pygame.init()
	from sys import *
	import sys


class Principal(object):
	"""docstring for Principal"""
	def __init__(self):
		self.ventana = display.set_mode((900,600))
		pass

	def bucle(self):
		correr = True
		while correr:
			self.ventana.fill((0,0,0))
			for self.evento in event.get():
				if self.evento.type == QUIT: sys.exit()
				self.correr = True





			pygame.display.update()
			pass
		pass


Principal = Principal()
Principal.bucle()	

if __name__ == "__main__":
    Principal()

