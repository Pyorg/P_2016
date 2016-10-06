import pygame
import random
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
from Bonus import Bonus
from Vidas import Vidas
from Menu import menu
from Pausa import pausa
from Escudo import Escudos

img_dir = path.join(path.dirname(__file__), 'imagenes')

pygame.init()

listaEnemigo = []
lista = []

pygame.mixer.set_num_channels(50)

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

def mostrarTexto(surf, text, size, x, y):
    font = pygame.font.Font('fuentes/spin_cycle.ttf', size)
    text_surface = font.render(text, True, blanco)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
    
def pantallaPrincipal():
    imagenMenu = pygame.image.load("imagenes/menu.png").convert_alpha()
    pantalla.blit(imagenMenu,(0,0))
    pygame.mixer.music.load('sonidos/menu.mp3')
    pygame.mixer.music.play()
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
    if fondo(pantalla):
        return True
                    
def mostrarVidas(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)
        
def mostrarBarraProteccion(surf, x, y, nivelEscudo):
    ancho_barra = 100
    alto_barra = 10
    llenar = nivelEscudo
    outline_rect = pygame.Rect(x, y, ancho_barra, alto_barra)
    llenar_barra = pygame.Rect(x, y, llenar, alto_barra)
    pygame.draw.rect(surf, verde, llenar_barra)
    pygame.draw.rect(surf, blanco, outline_rect, 2)

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
                sonidoDisparo1 = pygame.mixer.Sound("sonidos/laser4.wav")
                sonidoDisparo1.play()
            if self.power >= 2:
                misil1 = Misil(self.rect.left, self.rect.centery)
                misil2 = Misil(self.rect.right, self.rect.centery)
                conjuntoSprites.add(misil1)
                conjuntoSprites.add(misil2)
                misiles.add(misil1)
                misiles.add(misil2)
                self.power = 1
                sonidoDisparo2 = pygame.mixer.Sound("sonidos/laser8.wav")
                sonidoDisparo2.play()

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

""" RECURSOS """

imagenfondo = pygame.image.load("imagenes/fondo.png").convert_alpha()
nave = pygame.image.load("imagenes/nave.png").convert_alpha()
sonido1 = pygame.mixer.Sound("imagenes/Plane_Fly.mp3")

puntaje = 0
nivelEscudo = 0
rangoMeteoritos = 8
    
game_over = True
running = True
inicio = True

def getready(pantalla):
    ready = pygame.mixer.Sound(path.join('sonidos','getready.ogg'))
    ready.play()
    for i in range(100):
        pantalla.fill(negro)
        mostrarTexto(pantalla, "GET READY!", 40, ancho/2, alto/2)
        pygame.display.update()

""" LOOP DEL JUEGO """
while running:
    
        if inicio:
            #pantallaPrincipal()
            pygame.mixer.music.load('sonidos/menu.mp3')
            pygame.mixer.music.play(-1)
            if menu(pantalla) == False:
                inicio = False
            pygame.mixer.music.stop()
            mostrarTexto(pantalla, "GET READY!", 40, ancho/2, alto/2)
            inicio = False

        if game_over:
            pygame.mixer.music.stop()
            getready(pantalla)
            puntaje = 0
            nivelEscudo = 0
            fuentePuntaje = pygame.font.Font('fuentes/spin_cycle.ttf', 20)
            record = traerMaximaPuntuacion()
            nombre = traerMaximoJugador()
            puntuacion = fuentePuntaje.render("RECORD: " + nombre + " >>>> " + str(record), 1, (255, 255, 255))
            posx = 100
            vx, vy = 0,0
            velocidad = 5 # CONTROLA VELOCIDAD DE LA NAVE
            leftsigueapretada, rightsigueapretada, upsigueapretada, downsigueapretada = False, False, False, False
            colisiono = False
            pygame.mixer.music.load('sonidos/fondo.wav')
            pygame.mixer.music.play(-1)
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
                if event.key == K_p:
                    pausa(pantalla)
                    
                    
            if colisiono == False:
                if event.type == pygame.KEYDOWN:
                    if event.key == K_s:
                        player1.disparar()

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
            sonidoExplosion = pygame.mixer.Sound("sonidos/explosion.wav")
            sonidoExplosion.play()
            puntaje += 50
            mostrarPuntaje = fuentePuntaje.render("PUNTAJE: " + str(puntaje), 1, (255, 255, 255))
            expl = Explosion(hit.rect.center, 'lg')
            conjuntoSprites.add(expl)
            if random.random() > 0.9:
                if random.random() > 0.5:
                    bn = Bonus(hit.rect.center)
                    conjuntoSprites.add(bn)
                    bonus.add(bn)
                else:
                    if random.random() > 0.5:
                        bn = Vidas(hit.rect.center, 'azul')
                        conjuntoSprites.add(bn)
                        bonus.add(bn)
                    else:
                        bn = Escudos(hit.rect.center, 'escudo')
                        conjuntoSprites.add(bn)
                        bonus.add(bn)
            nuevosMeteoritos()
        
        """ CONTROLA COLISION JUGADOR - METEORITO """
        hits = pygame.sprite.spritecollide(player1, meteoritos, True, pygame.sprite.collide_circle)
        for hit in hits:
            expl = Explosion(hit.rect.center, 'sm')
            conjuntoSprites.add(expl)
            nuevosMeteoritos()
            if player1.shield == 0:
                death_explosion = Explosion(player1.rect.center, 'player')
                conjuntoSprites.add(death_explosion)
                sonidoExplosion1 = pygame.mixer.Sound("sonidos/explosion.wav")
                sonidoExplosion1.play()
                player1.hide()
                player1.lives -= 1
            else:
                player1.shield -= 1
                sonidoEscudo = pygame.mixer.Sound("sonidos/pierdeEscudo.ogg")
                sonidoEscudo.play()
                nivelEscudo -= 50
            if player1.lives == 0:
                if puntaje > int(record):
                    traerNombre(pantalla, "", puntaje)
                pantalla.fill((0,0,0))
                running = False
                if pantallaFinal():
                    running = True
                    game_over = True
                
        """ CONTROLA COLISION JUGADOR - BONUS """        
        hits = pygame.sprite.spritecollide(player1, bonus, True)
        for hit in hits:
            if hit.type == 'vidas':
                player1.lives += 1
                if player1.lives > 4:
                    player1.lives = 4
                else:
                    sonidoVida = pygame.mixer.Sound("sonidos/vida.wav")
                    sonidoVida.play()
            if hit.type == "x2":
                player1.powerup()
                sonidoX2 = pygame.mixer.Sound("sonidos/x2.wav")
                sonidoX2.play()
            if hit.type == "escudo":
                player1.shield += 1
                if player1.shield > 2:
                    player1.shield = 2
                else:
                    sonidoEscudo1 = pygame.mixer.Sound("sonidos/tomaEscudo.ogg")
                    sonidoEscudo1.play()
                if nivelEscudo < 100:
                    nivelEscudo += 50
                
        if colisiono == False:
            player1.mover(vx, vy)
        
        pantalla.blit(imagenfondo,(0,0))
        player1.actualizar(pantalla)

        if puntaje > record:
            actualizarMaximaPuntuacion(puntaje) 
        conjuntoSprites.draw(pantalla)
        mostrarVidas(pantalla, 20, 50, player1.lives, pygame.image.load("Imagenes/vidas.png").convert_alpha())
        mostrarBarraProteccion(pantalla, 20, 100, nivelEscudo)
        mostrarTexto(pantalla, "PUNTAJE: " + str(puntaje), 20, 100, 20)
        pantalla.blit(puntuacion, (570 , 20))
        pygame.display.flip()
        
pygame.quit()