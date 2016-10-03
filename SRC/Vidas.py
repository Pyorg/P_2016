import pygame
from os import path

img_dir = path.join(path.dirname(__file__), 'imagenes')

alto = 600

""" COLORES """

negro = (0, 0, 0)

vidas_anim = {}
vidas_anim['azul'] = []
for i in range(6):
    filename = 'vidas0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert_alpha()
    img.set_colorkey(negro)
    img_azul = pygame.transform.scale(img, (50, 50))
    vidas_anim['azul'].append(img_azul)

class Vidas(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.type = 'vidas'
        self.image = vidas_anim[self.size][0]
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
            if self.frame > 5:
                self.frame = 0
            else:
                center = self.rect.center
                self.image = vidas_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
        self.rect.y += self.speedy
        if self.rect.top > alto:
            self.kill()