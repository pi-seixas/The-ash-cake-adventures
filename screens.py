import pygame
from pygame.locals import *

from components import components

import json
import time

with open('history.json') as json_file:
    history = json.load(json_file)

class screens():
    def __init__(self, screen, font, width, height):
        self.screen = screen
        self.font = font
        self.component = components(screen, font)
        self.widthScreen = width
        self.heightScreen = height
        self.titulo = "CRUZADORA"
        self.page = "menu"
        self.relogio = pygame.time.Clock()
        
        self.falas = True
        self.cont_fala = 0
        self.cont_screen = "1"
 
    
    def menu(self):
        #===Fundo===
        self.screen.blit(pygame.image.load("imagens/menu.jpg"), (0,0))
        
        #===Título===
        font = pygame.font.SysFont("comicsansms", 48)
        screen_text = font.render('{0}'.format(self.titulo), True, (255,255,255))
        self.component.botaoDesign(self.widthScreen*0.5, self.heightScreen*0.3, 
                                   font.size(self.titulo)[0], font.size(self.titulo)[1])
        
        self.screen.blit(screen_text, [self.widthScreen*0.5 - (font.size(self.titulo)[0])/2, 
                                       self.heightScreen*0.3 - (font.size(self.titulo)[1])/2])
        
        #===Botôes===
        if self.component.botao(self.widthScreen*0.25, self.heightScreen*0.6, 'Play'): self.page = 'game'
        if self.component.botao(self.widthScreen*0.5, self.heightScreen*0.6, 'Tutorial'): self.page = 'tutorial'
        if self.component.botao(self.widthScreen*0.75, self.heightScreen*0.6, 'Exit'): self.page = 'exit'
        
    def tutorial(self):
        self.screen.fill((0,0,0))
        screen_text = self.font.render('{0}'.format(history['tutorial']), True, (255,255,255))
        
        self.screen.blit(screen_text, [self.widthScreen*0.5 - (self.font.size(history['tutorial'])[0])/2, self.heightScreen*0.3 - (self.font.size(history['tutorial'])[1])/2])
        if self.component.botao(self.widthScreen*0.5, self.heightScreen*0.6, 'Voltar'): self.page = 'menu'
        
    def pause(self):
        posX, posY = 300, 200
        """
        pygame.draw.polygon(self.screen, (0,0,0), 
                            ((posX, posY), 
                             ((self.widthScreen/2 - posX) + self.widthScreen/2, posY),
                             ((self.widthScreen/2 - posX) + self.widthScreen/2, (self.heightScreen/2 - posY) + self.heightScreen/2), 
                             (posX/2, (self.heightScreen/2 - posY) + self.heightScreen/2)))
        """
        pygame.draw.polygon(self.screen, (92,92,92),
                            ((posX, posY), 
                             ((self.widthScreen/2 - posX) + self.widthScreen/2, posY),
                             ((self.widthScreen/2 - posX) + self.widthScreen/2, (self.heightScreen/2 - posY) + self.heightScreen/2), 
                             (posX, (self.heightScreen/2 - posY) + self.heightScreen/2)))
         
        #===Botôes===
        if self.component.botao(self.widthScreen*0.5, self.heightScreen*0.4, 'Resume'): self.page = 'game'
        if self.component.botao(self.widthScreen*0.5, self.heightScreen*0.5, 'Tutorial'): self.page = 'tutorial'
        if self.component.botao(self.widthScreen*0.5, self.heightScreen*0.6, 'Menu'): self.page = 'menu'
        
    def gameover(self):
        self.screen.fill((0,0,0))
        
        go = history["gameOver"]
        
        font = pygame.font.SysFont("consolas", 18)
        
        lista = self.component.quebraTexto(go, font)
        
        i=1
        for e in lista:
            screen_text = font.render('{0}'.format(e), True, (255,255,255))
            self.screen.blit(screen_text, [self.widthScreen*0.5 - font.size(e)[0]/2, 
                                           self.heightScreen*(0.1*i) - font.size(e)[1]/2])
            i += 0.5

        if self.component.botao(self.widthScreen*0.5, self.heightScreen*(0.7), "Menu"): self.page = 'menu'
        
    def game(self):
        
        hgs = history["gameScreens"]
        
        if hgs[self.cont_screen]["background"] == "":
            self.screen.fill((0,0,0))
        else:
            self.screen.blit(pygame.image.load(hgs[self.cont_screen]["background"]), (0,0))
        
        
        
        num_falas = len(hgs[self.cont_screen]["historia"])
            
        if self.falas:
            if self.cont_fala < num_falas:
                
                fala = hgs[self.cont_screen]["historia"][self.cont_fala]
                font = pygame.font.SysFont("consolas", 18)
                
                lista = self.component.quebraTexto(fala, font)
                
                i=1
                for e in lista:
                    screen_text = font.render('{0}'.format(e), True, (255,255,255))
                    self.screen.blit(screen_text, [self.widthScreen*0.5 - font.size(e)[0]/2, 
                                                   self.heightScreen*(0.1*i) - font.size(e)[1]/2])
                    i += 0.5
    
                if self.component.botao(self.widthScreen*0.5, self.heightScreen*0.75, "Próximo"): self.cont_fala += 1
            
        if self.cont_fala >= num_falas:
            self.falas = False
     
        perguntas = hgs[self.cont_screen]["pergunta"]
        
        if not self.falas:
            fala = hgs[self.cont_screen]["historia"][-1]
            font = pygame.font.SysFont("consolas", 18)
            lista = self.component.quebraTexto(fala, font)
            
            i=1
            for e in lista:
                screen_text = font.render('{0}'.format(e), True, (255,255,255))
                self.screen.blit(screen_text, [self.widthScreen*0.5 - font.size(e)[0]/2, 
                                               self.heightScreen*(0.1*i) - font.size(e)[1]/2])
                i += 0.5
            
            if len(hgs[self.cont_screen]["pergunta"]) != 0:
            
                for e in range(len(hgs[self.cont_screen]["pergunta"])):
                    if self.component.botao(self.widthScreen*0.5, self.heightScreen*(0.7+(e*0.1)), perguntas[e]): 
                        self.cont_screen = hgs[self.cont_screen]["local"][e]
                        self.falas = True
                        self.cont_fala = 0
            else:
                self.falas = True
                self.cont_fala = 0
                self.cont_screen = "1"
                self.page = 'gameover'
                       