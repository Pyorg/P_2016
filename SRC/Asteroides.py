import pygame
import random
from Proyectiles import Proyectil

class Asteroides(pygame.sprite.Sprite):
    def __init__(self,numeroinicial):
        pygame.sprite.Sprite.__init__(self)
        self.asteroide = pygame.image.load("Imagenes/rocas.png")
        self.lista = []
        self.angulo = .2

        for x in range(numeroinicial):
            #creo un rect random
            self.rectangulo = self.asteroide.get_rect()
            self.rectangulo.center = (random.randrange(2,890), random.randrange(-580,-10))
            print(self.rectangulo)
            
            #if self.lista != []:
             #   self.rectangulo.bottom > self.lista[-1].top is True
              #  overlap = 104 - 100
               # self.rectangulo.bottom = 104 - 4

                #self.rectangulo.right > self.lista[-1].left is True
                #overlap = 92 - 90
                #self.rectangulo.right = 92 - 2
                #print(self.rectangulo)
            
            self.lista.append(self.rectangulo)
        
        print(self.lista[-1])

    def mover(self, velocidad):
        for rectangulo in self.lista:
            rectangulo.move_ip(1, velocidad)

    def pintar(self,superficie):
        for rectangulo in self.lista:
            self.image = pygame.transform.rotate(self.asteroide, self.angulo)
            self.angulo += 0.22
            superficie.blit(self.image, rectangulo)

    def getLista(self):
        return self.lista
