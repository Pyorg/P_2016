import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'imagenes')

alto = 600

""" COLORES """

negro = (0, 0, 0)

powerup_images = {}
powerup_images['shield'] = pygame.image.load(path.join(img_dir, 'nave.png'))
powerup_images['x2'] = pygame.image.load(path.join(img_dir, 'x2.png'))

class Bonus(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'x2'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.top > alto:
            self.kill()