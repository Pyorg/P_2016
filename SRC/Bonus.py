import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'imagenes')

alto = 600

""" COLORES """

negro = (0, 0, 0)

powerup_images = {}
powerup_images['shield'] = random.choice([pygame.image.load(path.join(img_dir, 'escudo.png')), 
                                          pygame.image.load(path.join(img_dir, 'escudo.png'))])
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
        if self.rect.top > alto:
            self.kill()
            
vidas_anim = {}
vidas_anim['azul'] = []
for i in range(6):
    filename = 'vidas0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(negro)
    img_azul = pygame.transform.scale(img, (75, 75))
    vidas_anim['azul'].append(img_azul)