import pygame
import sys 
from pygame import *
pygame.init()

ancho = 600 
alto = 500
esmeralda = (87,181,198)
width = 5
height = 5
red = (13,0,0)
x = 50
y = 490
vel = 0
salto = 10
isjump = False 

ventana = pygame.display.set_mode((ancho,alto))

# bucle 
correr = True 
while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            exit()
    reloj = pygame.time.Clock()
    pulsacion = pygame.key.get_pressed()
    if pulsacion[K_a]:
        vel = -3
    if pulsacion[K_d]:
        vel = 3

    
    if pulsacion[K_SPACE]:
        isjump = True    

    if isjump:
        if salto >= -10:
            y -= (salto * abs(salto)) * 0.5
            salto -= 1
        else:
            salto = 10
            isjump = False
    x += vel
        
    
    ventana.fill(esmeralda)
    pygame.draw.rect(ventana,red,(x,y,5,5))


    reloj.tick(30)
    pygame.display.update()