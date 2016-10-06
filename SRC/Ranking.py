import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
from Puntuacion import actualizarMaximaPuntuacion

""" COLORES """

blanco = (255, 255, 255)

font_name = pygame.font.match_font('arial')

def get_key():
    while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass
    
def mostrarTexto(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, blanco)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def mostrarCaja(pantalla, mensaje): # Print a message in a box in the middle of the screen
    fontobject = pygame.font.Font(None, 35)
    pygame.draw.rect(pantalla, (0, 0, 0), ((pantalla.get_width() / 2) - 100, (pantalla.get_height() / 2) - 20,
                    200, 40), 0)
    pygame.draw.rect(pantalla, (246, 77, 77), ((pantalla.get_width() / 2) - 150, (pantalla.get_height() / 2) - 20,
                    300, 40), 3)
    mostrarTexto(pantalla, "Nuevo RECORD", 40, 900 / 2, 600 / 3)
    mostrarTexto(pantalla, "Ingresa tu nombre", 22, 900 / 2, 250)
    if len(mensaje) != 0:
        pantalla.blit(fontobject.render(mensaje, 1, (255,255,255)),
                ((pantalla.get_width() / 2) - 100, (pantalla.get_height() / 2) - 10))
    pygame.display.flip()

def traerNombre(pantalla, pregunta, puntaje): # ask(screen, question) -> answer
    pygame.font.init()
    current_string = []
    mostrarCaja(pantalla, pregunta + " " + string.join(current_string,"") + " - - - - - - - - - - -")
    while 1:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey == K_RETURN:
            break
        elif inkey == K_MINUS:
            current_string.append("_")
        elif inkey <= 127:
            current_string.append(chr(inkey))
        mostrarCaja(pantalla, pregunta + "" + string.join(current_string,""))
    actualizarMaximaPuntuacion(puntaje, string.join(current_string,""))
    return string.join(current_string,"")

def main():
    pantalla = pygame.display.set_mode((900,600))
    print traerNombre(pantalla, "", 5) + " was entered"

if __name__ == '__main__': main()