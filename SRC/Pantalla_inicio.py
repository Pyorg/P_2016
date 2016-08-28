'''
Created on 27 ago. 2016

@author: carolina
'''
import pygame



salir = False
pygame.init()

# Define el modo pantalla completa como modo inicial.
flags = pygame.FULLSCREEN | pygame.DOUBLEBUF
screen = pygame.display.set_mode((800, 600), flags)

pygame.font.init()
font = pygame.font.Font(None, 70)
color = (155, 55, 25)
msg = font.render("INTERGALACTIKA.", 1, color)
screen.blit(msg, (150, 100))

# Texto en pantalla
pygame.font.init()
font = pygame.font.Font(None, 50)
color = (255, 255, 255)

#ponemos el nombre a la ventana del juego 
pygame.display.set_caption("Super Juego de Seminario UNLa")

# Imprime en pantalla los mensajes de ayuda
msg = font.render("Pulse 'q' para salir.", 1, color)
screen.blit(msg, (150, 200))
msg = font.render("Pulse 'enter' para jugar.", 1, color)
screen.blit(msg, (150, 250))
msg = font.render("Pulse 'espacio' para opciones.", 1, color)
screen.blit(msg, (150, 300))

# Muestra los cambios en pantalla
pygame.display.flip()

while not salir:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Permite terminar el programa
            if event.key == pygame.K_q:
                salir = True
            # Alterna entre 'pantalla completa' y 'ventana'.
            elif event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()

    pygame.time.wait(10)