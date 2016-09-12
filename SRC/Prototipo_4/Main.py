import pygame
from pygame.locals import *
import random

from Player import Player
# from Enemigo import Alien
from Rocas import Asteroide
from Proyectiles import Proyectil

listaEnemigo = []
lista = []

def colision(player1, asteroide):
    for rec in asteroide.lista:
        if player1.rect.colliderect(rec):
            return True
    return False

def colision2(rect, asteroide):
    for rec in asteroide.lista:
        if proyectil.rect.colliderect(rec):
            return True
    return False








def main():
    import pygame

    pygame.init()
    pantalla=pygame.display.set_mode((900,600))
    salir=False
    reloj1= pygame.time.Clock()
    imagen1=pygame.image.load("Imagenes/nave.png").convert_alpha()
    imagenexplosion=pygame.image.load("Imagenes/explosion.png").convert_alpha()
    imagenfondo=pygame.image.load("Imagenes/fondo.png").convert_alpha()
    pygame.mixer.music.load("Imagenes/Heavy.mp3")
    sonido1=pygame.mixer.Sound("Imagenes/Plane_Fly.mp3")
    asteroide=Asteroide(11)
    posx = 100
    #enemigo = Enemigo(posx, 100, 40, "Imagenes/spyder.png")  # carga las imagenes de los invasores con sus parametros segun la clase Invasor

    #variables aux

    player1=Player(imagen1)
    vx,vy=0,0
    velocidad=10
    leftsigueapretada,rightsigueapretada,upsigueapretada,downsigueapretada=False,False,False,False
    colisiono=False

    pygame.mixer.music.play(2)

    while salir!=True:  # loop para eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
                #sys.exit(0)
            if colisiono==False:
                if event.type == pygame.KEYDOWN:

                    if event.key == K_s:
                        x, y = player1.rect.center
                        player1.disparar(x,y)

                    if event.key == pygame.K_LEFT:
                        leftsigueapretada=True
                        vx=-velocidad
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada=True
                        vx=velocidad
                    if event.key== pygame.K_UP:
                        upsigueapretada=True
                        vy=-velocidad
                        sonido1.play()
                    if event.key == pygame.K_DOWN:
                        downsigueapretada=True
                        vy=velocidad

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada=False
                        if rightsigueapretada:vx=velocidad
                        else:vx=0
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada=False
                        if leftsigueapretada:vx=-velocidad
                        else:vx=0
                    if event.key== pygame.K_UP:
                        upsigueapretada=False
                        if downsigueapretada:vy=velocidad
                        else:vy=-0
                    if event.key == pygame.K_DOWN:
                        downsigueapretada=False
                        if upsigueapretada:vy=-velocidad
                        else:vy=0

        reloj1.tick(20)

        if colision(player1,asteroide):
            colisiono=True
            player1.imagen=imagenexplosion
            pygame.mixer.music.stop()
        if colisiono==False:
            asteroide.mover(2)  # le pasamos la velocidad como parametro
            player1.mover(vx, vy)

        pantalla.blit(imagenfondo,(0,0))
        asteroide.pintar(pantalla)
        player1.update(pantalla)

        player1.dibujar(pantalla)  # agregado
        if len(player1.listaDisparos) > 0:
            for x in player1.listaDisparos:
                x.dibujar(pantalla)  # se coloca el proyectil sobre la ventana del juego
                x.trayectoria()  # trayectoria del proyectil
                if x.rect.top < 20:
                    player1.listaDisparos.remove(x)   # elimino el proyectil


        for x in player1.listaDisparos:
            x.dibujar(pantalla)  # se coloca el proyectil sobre la ventana del juego
            x.trayectoria()  # trayectoria del proyectil
            for a in asteroide.getLista():
                if x.rect.colliderect(a):
                    #numero = x.collidelist(asteroide.getLista())
                    asteroide.lista.remove(a)
                    #asteroide.getLista().eliminar #pop(numero)
                    player1.listaDisparos.remove(x)

        pygame.display.update()
        #enemigo.cargarEnemigos()
        #recs1.reagrear()
    pygame.quit()

main()
