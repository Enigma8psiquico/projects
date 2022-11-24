#!/usr/bin/env python
"""" juego de la vida"""
import time
import pygame 
import numpy as np

pygame.init()

width , height = 500, 500

screen = pygame.display.set_mode((width, height))

bg = 0, 0, 0

screen.fill(bg)

# paso 1 crear celdas 
nxC, nyC = 30,30

dimCW = width / nxC
dimCH = height / nyC

# estado de cada celdaa vivas = 1, muertas = 0
# estado de cada celdaa vivas = 1, muertas = 0
gameState = np.zeros((nxC, nyC))


# paso 3 creamos a una celula por ejemplo Pablo
gameState[15,13] = 1
gameState[15,14] = 1
gameState[15,15] = 1


gameState[21,21] = 1
gameState[22,22] = 1
gameState[22,23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1


while True:

	# nuevo estado 
	newGameState = np.copy(gameState)
	
	# limpiar la pantalla 
	screen.fill(bg) 

	# hacer que valla mas lento la cosa
	time.sleep(0.1)

	# registramos eventos del teclado y raton
	ev = pygame.event.get()

	for event in ev:
		mouseClick = pygame.mouse.get_pressed()

		if sum(mouseClick) > 0:
			posX, posY = pygame.mouse.get_pos()
			celX,celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
			newGameState[celX, celY] = 1




	for y in range(0, nxC):
		for x in range(0,nyC):
			nheight = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
					  gameState[(x)    % nxC, (y - 1) % nyC] + \
					  gameState[(x + 1)% nxC, (y - 1) % nyC] + \
					  gameState[(x - 1)% nxC, (y) % nyC] + \
					  gameState[(x + 1)% nxC, (y) % nyC] + \
					  gameState[(x - 1)% nxC, (y + 1) % nyC] + \
					  gameState[(x)    % nxC, (y + 1) % nyC] + \
					  gameState[(x + 1)% nxC, (y + 1) % nyC]

			# paso 2 crear las reglas de las celulas
			if gameState[x,y] == 0 and nheight == 3:
				newGameState[x,y] = 1

			elif gameState[x,y] == 1 and (nheight < 2 or nheight > 3):
				newGameState[x,y] = 0

			

			poly = [((x) * dimCW, y * dimCH),
					((x + 1) * dimCW, y * dimCH),
					((x + 1) * dimCW,(y+1)* dimCH),
					((x) * dimCW, (y+1) * dimCH)]


			# dibujamos las celdas para cada cuadrado
			if newGameState[x,y] == 0:
				pygame.draw.polygon(screen, (128, 128, 128), poly, 1)

			else:
				pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

	# actualizamos el estado del juego
	gameState = np.copy(newGameState)

	pygame.display.flip()