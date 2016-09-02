'''
Created on 27 ago. 2016

@author: carolina
'''
import pygame
from pygame.locals import *



salir = False
pygame.init()





# Define el modo pantalla completa como modo inicial.
flags = pygame.FULLSCREEN | pygame.DOUBLEBUF
screen = pygame.display.set_mode((800, 600), flags)

imagenfondo=pygame.image.load("NoMansSky_SpaceStation.png").convert_alpha()
screen.blit(imagenfondo,(0,0))

#musica del juego
pygame.mixer.music.load("hoarse_space_cadet.ogg")
pygame.mixer.music.play(2)
##

pygame.font.init()


font = pygame.font.Font(None, 90)
color = (12, 90, 235)
texto = font.render("SPACE TRECK.", 1, color)
screen.blit(texto, (250, 50))

# Texto en pantalla
pygame.font.init()
font = pygame.font.Font(None, 50)
color = (226, 226, 176)


#ponemos el nombre a la ventana del juego 
pygame.display.set_caption("Super Juego de Seminario UNLa")

# Imprime en pantalla los mensajes de ayuda
texto = font.render("Pulse 'q' para salir.", 1, color)
screen.blit(texto, (50, 400))
texto = font.render("Pulse 'enter' para jugar.", 1, color)
screen.blit(texto, (50, 450))
texto = font.render("Pulse 'espacio' para opciones.", 1, color)
screen.blit(texto, (50, 500))

# Muestra los cambios en pantalla
pygame.display.flip()

while not salir:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Permite terminar el programa
            if event.key == pygame.K_q:
                salir = True
            # Alterna entre 'pantalla completa' y 'ventana'.
            elif event.key == pygame.K_KP_ENTER:
                salir = True
                #falta poner la accion de comenza rel juego
            elif event.key == pygame.K_BACKSPACE:
                pass
                #crear pantalla de opciones
            
                
            

    pygame.time.wait(10)
    
