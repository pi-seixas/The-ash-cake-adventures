import pygame
from pygame.locals import *
import time

class components():
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.black = 0,0,0
        self.white = 255, 255, 255
        self.cinza = 255, 52, 52
        self.relogio = pygame.time   

    def botao(self, posX, posY, text):
        mouse = pygame.mouse.get_pos() 
        click = pygame.mouse.get_pressed()
        width, height = self.font.size(text)[0], self.font.size(text)[1]
             
        if posX+width/2 > mouse[0] > posX-width/2 and posY+height/2 > mouse[1] > posY-height/2:
            self.screen_text = self.font.render('{0}'.format(text), True, self.cinza)
            self.botaoDesign(posX,posY,width,height)
            self.screen.blit(self.screen_text, [posX-width/2, posY-height/2])
            if click[0] == 1:
                self.relogio.delay(200)
                return True
        else:
            self.botaoDesign(posX,posY,width,height)
            self.screen_text = self.font.render('{0}'.format(text), True, self.white)
            self.screen.blit(self.screen_text, [posX-width/2, posY-height/2])

    def botaoDesign(self, posX, posY, width, height):
        overExtH, overExtV = 12, 6
        overIntH, overIntV = 9, 3
        pygame.draw.polygon(self.screen, self.black, 
                            ((posX-width/2 -overExtH, posY-height/2 -overExtV), (posX+width/2 +overExtH, posY-height/2 -overExtV),
                             (posX+width/2 +overExtH, posY+height/2 +overExtV), (posX-width/2 -overExtH, posY+height/2 +overExtV)))
        pygame.draw.polygon(self.screen, (92,92,92),
                            ((posX-width/2 -overIntH, posY-height/2 -overIntV), (posX+width/2 +overIntH, posY-height/2 -overIntV),
                             (posX+width/2 +overIntH, posY+height/2 +overIntV), (posX-width/2 -overIntH, posY+height/2 +overIntV)))
    
    def quebraTexto(self, fala, font):
        falas = []
        
        vezes = int(font.size(fala)[0]/800)
        
        if font.size(fala)[0] > 800:
            lista = fala.split()
            
            for e in range(vezes):
                i = 1
                while font.size(" ".join(lista[0:-i]))[0] > 800:
                    i += 1
                
                falas.append(" ".join(lista[0:-i]))
                lista = lista[-i:]
                
            falas.append(" ".join(lista[-i:]))
                 
        else:
            falas.append(fala)
        
        return falas


            