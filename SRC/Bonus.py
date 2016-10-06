import pygame
from os import path

img_dir = path.join(path.dirname(__file__), 'imagenes')

alto = 600

""" COLORES """

negro = (0, 0, 0)

powerup_images = {}
powerup_images['x2'] = pygame.image.load(path.join(img_dir, 'x2.png'))

class Bonus(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = 'x2'
        self.image = powerup_images[self.type]
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > alto:
            self.kill()