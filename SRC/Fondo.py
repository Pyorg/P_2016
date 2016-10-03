import pygame
import sys
import pygame.sprite as sprite

from pygame.locals import *
from pygame.constants import K_t

""" COLORES """

blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarillo = (255, 255, 0)

font_name = pygame.font.match_font('arial')

def fondo(pantalla):
    reloj = pygame.time.Clock()

    background = pygame.image.load('imagenes/sky.jpg')

    background_size = background.get_size()
    background_rect = background.get_rect()
    w, h = background_size
    x = 0
    y = 0

    x1 = 0
    y1 = -h

    running = True

    while running:
        pantalla.blit(background,background_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        y1 += 5
        y += 5
        pantalla.blit(background,(x,y))
        pantalla.blit(background,(x1,y1))
        if y > h:
            y = -h
        if y1 > h:
            y1 = -h
        mostrarTexto(pantalla, "GAME OVER", 64, 900 / 2, 600 / 4)
        mostrarTexto(pantalla, "JUGAR DE NUEVO (ENTER)", 28, 900 / 2, 600 / 2)
        mostrarTexto(pantalla, "SALIR (ESCAPE)", 50, 900 / 2, 600 * 3 / 4)
        pygame.display.flip()
        pygame.display.update()
        reloj.tick(10)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.key == K_t:
                return True
            if event.key == K_ESCAPE:
                pygame.quit()
    
    
def mostrarTexto(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, blanco)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def main():
    
    pantalla = pygame.display.set_mode((900,600))
    fondo(pantalla)
    
if __name__ == '__main__': main()