#Chelin Tutorials 29
#sitio web: http://chelintutorials.blogspot.com/

import pygame
from pygame.locals import *
import random
import FullScreen


class Recs(object):
    def __init__(self,numeroinicial):
        self.lista=[]
        for x in range(numeroinicial):
            #creo un rect random
            leftrandom=random.randrange(2,560)
            toprandom=random.randrange(-580,-10)
            width=random.randrange(10,30)
            height=random.randrange(15,30)
            self.lista.append(pygame.Rect(leftrandom,toprandom,width,height))
    def reagrear(self):
        for x in range(len(self.lista)):
            if self.lista[x].top>482:
                leftrandom=random.randrange(2,560)
                toprandom=random.randrange(-580,-10)
                width=random.randrange(10,30)
                height=random.randrange(15,30)
                self.lista[x]=(pygame.Rect(leftrandom,toprandom,width,height))

    def agregarotro(self):
        pass
    def mover(self):
        for rectangulo in self.lista:
            rectangulo.move_ip(0,2)
    def pintar(self,superficie):
        for rectangulo in self.lista:
            pygame.draw.rect(superficie,(100,200,10),rectangulo)

class Player(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen=imagen
        self.listaDisparos = []  # agregado

        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=(100,200)
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
        if self.rect.left < 0:
            vx=-vx
        self.rect.move_ip(vx,vy)

    def disparar(self, x, y):  # disparo
        proyectil = Proyectil(x,y)
        self.listaDisparos.append(proyectil) # se coloca un objeto en la Lista de disparos
    def dibujar(self, superficie):
        superficie.blit(self.imagen, self.rect)


    def update(self,superficie):
        superficie.blit(self.imagen,self.rect)




class Proyectil(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)

        self.imagenProyectil = pygame.image.load("Imagenes/disparoa.jpg")
        self.rect = self.imagenProyectil.get_rect()
        self.velocidadDisparo = 5
        self.rect.top = posy - 29
        self.rect.left = posx - 3
    def trayectoria(self):
        self.rect.top = self.rect.top - self.velocidadDisparo

    def dibujar(self, superficie):
        superficie.blit(self.imagenProyectil, self.rect)



def colision(player,recs):
    for rec in recs.lista:
        if player.rect.colliderect(rec):
            return True
    return False

def colision2(disparo,recs):
    for rec in recs.lista:
        if Proyectil.rect.colliderect(rec):
            return True
    return False



def main():
    import pygame

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
texto = font.render("S P A C E  T R E C K.", 1, color)
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
                pygame.quit()
                
            # Alterna entre 'pantalla completa' y 'ventana'.
            elif event.key == pygame.K_KP_ENTER:
                salir = True
#                 #falta poner la accion de comenza rel juego
#             elif event.key == pygame.K_BACKSPACE:
#                 pass
#                 #crear pantalla de opciones
            
                
            

#     pygame.time.wait(10)

    pygame.init()
    flags = pygame.FULLSCREEN | pygame.DOUBLEBUF
    pantalla = pygame.display.set_mode((800, 600), flags)
    
    salir=False
    reloj1= pygame.time.Clock()
    imagen1=pygame.image.load("nave.png").convert_alpha()
    # imagenProyectil = pygame.image.load("Imagenes/disparoa.jpg").convert_alpha  # nuevo
    imagenexplosion=pygame.image.load("explosion.png").convert_alpha()
    imagenfondo=pygame.image.load("fondo_converted.png").convert_alpha()
    pygame.mixer.music.load("Heavy.mp3")
    sonido1=pygame.mixer.Sound("Plane_Fly.mp3")
    recs1=Recs(25)

    #variables aux

    player1=Player(imagen1)
    vx,vy=0,0
    velocidad=10
    leftsigueapretada,rightsigueapretada,upsigueapretada,downsigueapretada=False,False,False,False
    colisiono=False

    pygame.mixer.music.play(2)

    while salir!=True:#LOOP PRINCIPAL
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
            if colisiono==False:
                if event.type == pygame.KEYDOWN:

                    if event.key == K_s:  # agregado
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

        if colision(player1,recs1):
            colisiono=True
            player1.imagen=imagenexplosion
            pygame.mixer.music.stop()
        if colisiono==False:
            recs1.mover()
            player1.mover(vx, vy)

        pantalla.blit(imagenfondo,(0,0))
        recs1.pintar(pantalla)
        player1.update(pantalla)

        player1.dibujar(pantalla)  # agregado
        if len(player1.listaDisparos) > 0:
            for x in player1.listaDisparos:
                x.dibujar(pantalla)  # se coloca el proyectil sobre la ventana del juego
                x.trayectoria()  # trayectoria del proyectil
                if x.rect.top < 20:
                    player1.listaDisparos.remove(x)   # elimino el proyectil

        pygame.display.update()
        recs1.reagrear()
    pygame.quit()

main()