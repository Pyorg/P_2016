import pygame
import sys
import pygame.sprite as sprite

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
        pygame.display.flip()
        pygame.display.update()
        reloj.tick(10)

def main():
    
    pantalla = pygame.display.set_mode((900,600))
    fondo(pantalla)
    
if __name__ == '__main__': main()