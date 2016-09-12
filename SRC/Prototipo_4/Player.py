import pygame
from Proyectiles import Proyectil # importamos de esta forma la clase que esta en la misma carpeta Clases

class Player(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen=imagen
        self.listaDisparos = []

        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=(500,200)
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
        if self.rect.left < 5:
            self.rect.left = 5
        if self.rect.left >= 870:
            self.rect.left = 870
        if self.rect.top <= 10:
            self.rect.top = 10
        if self.rect.top >= 570:
            self.rect.top = 570
        self.rect.move_ip(vx,vy)

    def disparar(self, x, y):  # disparo
        proyectil = Proyectil(x,y)
        self.listaDisparos.append(proyectil) # se coloca un objeto en la Lista de disparos

    def dibujar(self, superficie):
        superficie.blit(self.imagen, self.rect)

    def update(self,superficie):
        superficie.blit(self.imagen,self.rect)

