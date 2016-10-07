import pygame
import sys
import pygame.sprite as sprite

from pygame.locals import *

pygame.init() 

""" COLORES """

blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarillo = (255, 255, 0)

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
        mostrarTexto(pantalla, "GAME OVER", 60, 900 / 2, 600 / 4)
        mostrarTexto(pantalla, "JUGAR DE NUEVO >>> ESPACIO", 40,  900 / 2, 600 / 2)
        mostrarTexto(pantalla, "SALIR >>> M", 40, 900 / 2, 600 * 3 / 4)
        mostrarTexto(pantalla, "Battle Space", 20, 90, 20)
        pygame.display.flip()
        pygame.display.update()
        reloj.tick(10)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return True
                if event.key == K_m:
                    sys.exit()
                    pygame.quit()
    
    
def mostrarTexto(surf, text, tamanio, x, y):
    font = pygame.font.Font('fuentes/spin_cycle.ttf', tamanio)
    text_surface = font.render(text, True, blanco)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def main():
    
    pantalla = pygame.display.set_mode((900,600))
    fondo(pantalla)
    
if __name__ == '__main__': main()