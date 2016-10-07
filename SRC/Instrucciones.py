import pygame
from pygame.locals import *

pygame.init()
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

def mostrarInstrucciones():
    while True:
        for e in pygame.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == pygame.K_m:
                return
        imagenInstrucciones = pygame.image.load("imagenes/creditos.png").convert_alpha()
        pantalla.blit(imagenInstrucciones,(0, 0))
        imagenTeclado = pygame.image.load("imagenes/teclado.png").convert_alpha()
        pantalla.blit(imagenTeclado,(100, 80))
        mostrarTexto(pantalla, "Battle Space", 20, 90, 20)
        mostrarTexto(pantalla, "M PARA REGRESAR", 20, 120, 550)
        mostrarTexto(pantalla, "FLECHAS << CONTROL NAVE", 30, 450, 300)
        mostrarTexto(pantalla, "S << DISPARAR", 30, 450, 340)
        mostrarTexto(pantalla, "M << SALIR DEL JUEGO | REGRESAR", 30, 450, 380)
        mostrarTexto(pantalla, "P << PAUSAR PARTIDA", 30, 450, 420)
        mostrarTexto(pantalla, "R << RESUMIR PARTIDA", 30, 450, 460)
        mostrarTexto(pantalla, "ESPACIO << NUEVA PARTIDA", 30, 450, 500)
        pygame.display.flip()
        clock.tick(60)