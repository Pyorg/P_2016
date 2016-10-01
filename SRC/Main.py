import pygame
import random
from Bonus import Bonus
from os import path

from pygame.locals import *

from Misil import Misil
from Puntuacion import actualizarMaximaPuntuacion,\
    traerMaximaPuntuacion,\
    traerMaximoJugador
from Explosion import Explosion
from Meteoritos import Meteoritos
from Ranking import traerNombre
from Fondo import fondo

img_dir = path.join(path.dirname(__file__), 'imagenes')

pygame.init()

listaEnemigo = []
lista = []

""" DEFINICIONES GLOBALES """

ancho = 900
alto = 600
tiempoBonus = 240
FPS = 60
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Battle Space")
clock = pygame.time.Clock()

""" COLORES """

blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarillo = (255, 255, 0)

font_name = pygame.font.match_font('arial')

def mostrarTexto(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, blanco)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
    
def pantallaPrincipal():
    imagenMenu = pygame.image.load("imagenes/menu.png").convert_alpha()
    pantalla.blit(imagenMenu,(0,0))
    mostrarTexto(pantalla, "Battle Space", 64, 900 / 2, 600 / 4)
    mostrarTexto(pantalla, "Flechas para moverse, S para disparar", 22, 900 / 2, 600 / 2)
    mostrarTexto(pantalla, "Presione cualquier tecla para comenzar ! Escape para salir", 18, 900 / 2, 600 * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
                if event.key == K_ESCAPE:
                    pygame.quit()
                    
def pantallaFinal():
    mostrarTexto(pantalla, "GAME OVER", 64, 900 / 2, 600 / 4)
    mostrarTexto(pantalla, "JUGAR DE NUEVO (ENTER)", 28, 900 / 2, 600 / 2)
    mostrarTexto(pantalla, "SALIR (ESCAPE)", 50, 900 / 2, 600 * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                if event.type == pygame.KEYUP:
                    waiting = False
                    
def mostrarVidas(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)

def nuevosMeteoritos():
    m = Meteoritos()
    conjuntoSprites.add(m)
    meteoritos.add(m)
    
    
""" CLASE PLAYER """

class Player(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen = imagen
        self.shield = 0
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_time = pygame.time.get_ticks()

        self.listaDisparos = []

        self.rect = self.imagen.get_rect()
        self.rect.top,self.rect.left = (500,200)
        
    def mover(self, vx, vy):
        self.rect.move_ip(vx,vy)
        if self.rect.left < 8: # LIMITE IZQUIERDO
            self.rect.left = 8
        if self.rect.left >= 835: # LIMITE DERECHO
            self.rect.left = 835
        if self.rect.top <= 7: # LIMITE SUPERIOR
            self.rect.top = 7
        if self.rect.top >= 530: # LIMITE INFERIOR
            self.rect.top = 530
        self.rect.move_ip(vx,vy)
        
    def update(self):
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > tiempoBonus:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = ancho / 2
            self.rect.bottom = alto - 10
        
    def powerup(self):
        self.power += 1
        
    def disparar(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                misil = Misil(self.rect.centerx, self.rect.top)
                conjuntoSprites.add(misil)
                misiles.add(misil)
                #shoot_sound.play()
            if self.power >= 2:
                misil1 = Misil(self.rect.left, self.rect.centery)
                misil2 = Misil(self.rect.right, self.rect.centery)
                conjuntoSprites.add(misil1)
                conjuntoSprites.add(misil2)
                misiles.add(misil1)
                misiles.add(misil2)
                self.power = 1
                #shoot_sound.play()

    def dibujar(self, superficie):
        superficie.blit(self.imagen, self.rect)

    def actualizar(self,superficie):
        superficie.blit(self.imagen,self.rect)
        
    """ OCULTA LA NAVE TEMPORALMENTE """   
    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (ancho - 20, alto + 200)
        
""" FIN CLASE PLAYER """
    
puntaje = 0
fuentePuntaje = pygame.font.SysFont("Arial", 20)
record = traerMaximaPuntuacion()
nombre = traerMaximoJugador()
puntuacion = fuentePuntaje.render("RECORD: " + nombre + " >>>> " + str(record), 1, (255, 255, 255))
posx = 100
vx,vy = 0,0
velocidad = 5 # CONTROLA VELOCIDAD DE LA NAVE
leftsigueapretada, rightsigueapretada, upsigueapretada, downsigueapretada = False, False, False, False
colisiono = False

""" RECURSOS """

imagenfondo = pygame.image.load("imagenes/fondo.png").convert_alpha()
nave = pygame.image.load("imagenes/nave.png").convert_alpha()
sonido1 = pygame.mixer.Sound("imagenes/Plane_Fly.mp3")
pygame.mixer.music.load("sonidos/fondo.wav")

pygame.mixer.music.play()

puntaje = 0
    
game_over = True
running = True

""" LOOP DEL JUEGO """
while running:

        if game_over:
            pantallaPrincipal()
            conjuntoSprites = pygame.sprite.Group()
            player1 = Player(nave)
            misiles = pygame.sprite.Group()
            bonus = pygame.sprite.Group()
            meteoritos = pygame.sprite.Group()
            for i in range(8):
                nuevosMeteoritos()
        
        keystate = pygame.key.get_pressed()
        game_over = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    
                    
            if colisiono == False:
                if event.type == pygame.KEYDOWN:
                    if event.key == K_s:
                        player1.disparar()
                        sonidoDisparo = pygame.mixer.Sound("sonidos/disparo.wav")
                        sonidoDisparo.play()

                    if event.key == pygame.K_LEFT:
                        leftsigueapretada = True
                        vx =- velocidad
                    
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada = True
                        vx = velocidad
                    
                    if event.key == pygame.K_UP:
                        upsigueapretada = True
                        vy =- velocidad
                        
                    if event.key == pygame.K_DOWN:
                        downsigueapretada = True
                        vy = velocidad

                if event.type == pygame.KEYUP:
                    
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada=False
                        if rightsigueapretada:vx=velocidad
                        else:vx=0
                        
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada=False
                        if leftsigueapretada:vx=-velocidad
                        else:vx=0
                        
                    if event.key== pygame.K_UP:
                        upsigueapretada=False
                        if downsigueapretada:vy=velocidad
                        else:vy=-0
                        
                    if event.key == pygame.K_DOWN:
                        downsigueapretada=False
                        if upsigueapretada:vy=-velocidad
                        else:vy=0

        """ MANTIENE EL BUCLE FUNCIONANDO ADECUADAMENTE """
        clock.tick(FPS) 
        
        conjuntoSprites.update()
        
        """ CONTROLA COLISION MISIL - METEORITO """
        
        hits = pygame.sprite.groupcollide(meteoritos, misiles, True, True)
        for hit in hits:
            puntaje += 50
            mostrarPuntaje = fuentePuntaje.render("PUNTAJE: " + str(puntaje), 1, (255, 255, 255))
            #random.choice(expl_sounds).play()
            expl = Explosion(hit.rect.center, 'lg')
            conjuntoSprites.add(expl)
            if random.random() > 0.9:
                bn = Bonus(hit.rect.center)
                conjuntoSprites.add(bn)
                bonus.add(bn)
            nuevosMeteoritos()
        
        """ CONTROLA COLISION JUGADOR - METEORITO """
        hits = pygame.sprite.spritecollide(player1, meteoritos, True, pygame.sprite.collide_circle)
        for hit in hits:
            expl = Explosion(hit.rect.center, 'sm')
            conjuntoSprites.add(expl)
            nuevosMeteoritos()
            if player1.shield <= 0:
                #player_die_sound.play()
                death_explosion = Explosion(player1.rect.center, 'player')
                conjuntoSprites.add(death_explosion)
                player1.hide()
                player1.lives -= 1
            if player1.lives == 0:
                if puntaje > int(record):
                    traerNombre(pantalla, "", puntaje)
                pantalla.fill((0,0,0))
                pantallaFinal()
                
        """ CONTROLA COLISION JUGADOR - BONUS """        
        hits = pygame.sprite.spritecollide(player1, bonus, True)
        for hit in hits:
            if hit.type == 'x2':
                player1.powerup()
                player1.lives += 1

        if colisiono == False:
            player1.mover(vx, vy)
        
        pantalla.blit(imagenfondo,(0,0))
        player1.actualizar(pantalla)

        if puntaje > record:
            actualizarMaximaPuntuacion(puntaje) 
        conjuntoSprites.draw(pantalla)
        mostrarVidas(pantalla, 20, 50, player1.lives, pygame.image.load("Imagenes/vidas.png").convert_alpha())
        mostrarTexto(pantalla, "PUNTAJE: " + str(puntaje), 20, 70, 20)
        pantalla.blit(puntuacion, (650, 20))
        pygame.display.flip()
        
pygame.quit()