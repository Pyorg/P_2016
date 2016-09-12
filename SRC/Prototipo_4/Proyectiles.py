import pygame

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagenProyectil = pygame.image.load("Imagenes/disparoa.jpg")
        self.rect = self.imagenProyectil.get_rect()
        self.velocidadDisparo = 10
        self.rect.top = posy - 29
        self.rect.left = posx - 3

    def trayectoria(self):
        self.rect.top = self.rect.top - self.velocidadDisparo

    def dibujar(self, superficie):
        superficie.blit(self.imagenProyectil, self.rect)

def colision(player1, asteroide):
    for rec in asteroide.lista:
        if player1.rect.colliderect(rec):
            return True
    return False

def colision2(rect, asteroide):
    for rec in asteroide.lista:
        if proyectil.rect.colliderect(rec):
            return True
    return False
