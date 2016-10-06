# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

""" COLORES """

blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarillo = (255, 255, 0)

def mostrarTexto(surf, text, size, x, y):
    font = pygame.font.Font('fuentes/spin_cycle.ttf', 90)
    text_surface = font.render(text, True, blanco)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

class Menu:
    
    def __init__(self, opciones):
        self.opciones = opciones
        self.font = pygame.font.Font('fuentes/spin_cycle.ttf', 40)
        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self): # ALTERA EL VALOR DE 'SELF.SELECCIONADO' CON LOS DIRECCIONALES

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
                
                titulo, funcion = self.opciones[self.seleccionado]
                print "Selecciona la opcion '%s'." %(titulo)
                return funcion() # INVOCA A LA FUNCION ASOCIADA A LA OPCION

        # VERIFICA QUE EL CURSOS SE ENCUENTRE ENTRE LAS OPCIONES PERMITIDAS
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        # INDICA SI EL USUARIO MANTIENE PULSADA ALGUNA TECLA
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]


    def imprimir(self, screen):
        total = self.total
        indice = 0
        altura_de_opcion = 80
        x = 390
        y = 200
        
        for (titulo, funcion) in self.opciones:
            if indice == self.seleccionado:
                color = (200, 0, 0)
            else:
                color = (255, 255, 255)

            imagen = self.font.render(titulo, 1, color)
            posicion = (x, y + altura_de_opcion * indice)
            indice += 1
            screen.blit(imagen, posicion)

def comenzar_nuevo_juego():
    print " Funcion que muestra un nuevo juego."
    return True;

def mostrar_opciones():
    print " Funcion  que muestra otro menu de opciones."

def creditos():
    print " Funcion que muestra los creditos del programa."

def salir_del_programa():
    import sys
    print " Gracias por utilizar este programa."
    sys.exit(0)
    
def menu(pantalla):
    salir = False
    opciones = [
        ("Jugar", comenzar_nuevo_juego),
        ("Opciones", mostrar_opciones),
        ("Creditos", creditos),
        ("Salir", salir_del_programa)
        ]

    pygame.font.init()
    fondo = pygame.image.load("imagenes/menu.png").convert()
    menu = Menu(opciones)

    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True

        pantalla.blit(fondo, (0, 0))
        mostrarTexto(pantalla, "BATTLE SPACE", 64, 900 / 2, (600 / 6) - 35)
        if menu.actualizar() == True:
            return False
        menu.imprimir(pantalla)

        pygame.display.flip()
        pygame.time.delay(10)