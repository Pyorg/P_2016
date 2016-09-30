import pygame
from os import path

img_dir = path.join(path.dirname(__file__), 'imagenes')

""" COLORES """

negro = (0, 0, 0)

imagenMisil = pygame.image.load(path.join(img_dir, "misil.png"))

class Misil(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagenMisil
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()