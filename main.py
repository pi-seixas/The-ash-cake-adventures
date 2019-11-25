import pygame
from pygame.locals import *
import json

from components import components
from screens import screens

with open('history.json', encoding='utf-8') as json_file:
    history = json.load(json_file)

pygame.init()

widthScreen, heightScreen = 900, 600
screen = pygame.display.set_mode((widthScreen, heightScreen), 0,32)
pygame.display.set_caption('The Game')
font = pygame.font.SysFont("consolas", 25)

component = components(screen, font)
screens = screens(screen, font, widthScreen, heightScreen)

game = True


def quitgame():
    global game
    game = False

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            quitgame()
        
    page = screens.page
            
    if page == "menu":
        screens.menu()
        
    elif page == 'tutorial':
        screens.tutorial()

    elif page == 'exit':
        quitgame()
        
    elif page == 'pause':
        screens.pause()
    
    elif page == 'gameover':
        screens.gameover()
        
    elif page == 'game':
        screens.game()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                screens.page = "pause"

    pygame.display.update()
pygame.display.quit()
quitgame()


