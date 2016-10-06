import pygame
from os import path

img_dir = path.join(path.dirname(__file__), 'imagenes')

alto = 600

""" COLORES """

negro = (0, 0, 0)

escudo_anim = {}
escudo_anim['escudo'] = []
for i in range(7):
    filename = '0{}.gif'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert_alpha()
    img.set_colorkey(negro)
    img_azul = pygame.transform.scale(img, (90, 90))
    escudo_anim['escudo'].append(img_azul)

class Escudos(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.type = 'escudo'
        self.image = escudo_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75
        self.speedy = 3

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame > 6:
                self.frame = 0
            else:
                center = self.rect.center
                self.image = escudo_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
        self.rect.y += self.speedy
        if self.rect.top > alto:
            self.kill()