import pygame
import random
from Proyectiles import Proyectil # importamos de esta forma la clase que esta en la misma carpeta Clases

class Asteroide(pygame.sprite.Sprite):
    def __init__(self,numeroinicial):
        pygame.sprite.Sprite.__init__(self)
        self.asteroide = pygame.image.load("Imagenes/icon.png")
        self.lista=[]
        self.angulo = .2

        for x in range(numeroinicial):
            #creo un rect random
            self.rectangulo = self.asteroide.get_rect()
            self.rectangulo.center = (random.randrange(2,890), random.randrange(-580,-10))
            self.lista.append(self.rectangulo)



    def mover(self, velocidad):
        for rectangulo in self.lista:
            rectangulo.move_ip(0, velocidad)

    def pintar(self,superficie):
        for rectangulo in self.lista:
            self.image = pygame.transform.rotate(self.asteroide, self.angulo)
            self.angulo += 0.22
            superficie.blit(self.image, rectangulo)

    def getLista(self):
        return self.lista
