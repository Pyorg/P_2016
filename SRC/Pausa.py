import pygame
from pygame.locals import *

pygame.init()

""" COLORES """

blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarillo = (255, 255, 0)

def pausa(pantalla):
    running = True
    while running:
        #pantalla.fill(negro)
        pygame.display.update()
        for event in pygame.event.get():
            if event.key == pygame.K_r:
                return False
        