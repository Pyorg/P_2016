import pygame
from pygame.locals import *

pygame.init()
font = pygame.font.SysFont("Arial", 40)
clock = pygame.time.Clock()
ancho = 900
alto = 600
pantalla = pygame.display.set_mode((ancho, alto))

""" COLORES """

blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarillo = (255, 255, 0)


def mostrarTexto(surf, text, size, x, y):
    font = pygame.font.Font('fuentes/spin_cycle.ttf', size)
    text_surface = font.render(text, True, blanco)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def mostrarCreditos():

    
    credit_list = ["Maria Carolina Rozas", " ","Diego Leandro Zalazar Madeo", " ", "Agustin Trota", " ", "Alejandro Tomas Perez", " ",
                    "*** Seminario de Lenguajes ***", " ", "Universidad Nacional de Lanus - 2016"]
    screen_r = pantalla.get_rect()
    
    texts = []
    # we render the text once, since it's easier to work with surfaces
    # also, font rendering is a performance killer
    for i, line in enumerate(credit_list):
        s = font.render(line, 1, (255, 255, 255))
        # we also create a Rect for each Surface. 
        # whenever you use rects with surfaces, it may be a good idea to use sprites instead
        # we give each rect the correct starting position 
        r = s.get_rect(centerx = screen_r.centerx, y = screen_r.bottom + i * 45)
        texts.append((r, s))

    while True:
        for e in pygame.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == pygame.K_m:
                return

        #pantalla.fill((255, 255, 255))
        imagenMenu = pygame.image.load("imagenes/menu.png").convert_alpha()
        pantalla.blit(imagenMenu,(0,0))

        for r, s in texts:
            # now we just move each rect by one pixel each frame
            r.move_ip(0, -3)
            # and drawing is as simple as this
            pantalla.blit(s, r)

        # if all rects have left the screen, we exit
        if not screen_r.collidelistall([r for (r, _) in texts]):
            return
        
        mostrarTexto(pantalla, "M PARA REGRESAR", 20, 120, 550)

        # only call this once so the screen does not flicker
        pygame.display.flip()

        clock.tick(60)

if __name__ == '__main__':
    mostrarCreditos()