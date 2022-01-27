from typing import Text
import pygame
from pygame import font
from pygame.constants import TEXTINPUT
import webbrowser
from main import *
# constantes

WIDTH = 720
HEIGHT = 720

FPS = 5
#classes

class Button(object):
    

    def __init__(self, position, size, color, text):

        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = pygame.Rect((0,0), size)

        font = pygame.font.SysFont('Corbel', 32)
        text = font.render(text, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = self.rect.center
        

        self.image.blit(text, text_rect)

        # set after centering text
        self.rect.topleft = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)

def MenuScreen(screen):
    font = pygame.font.SysFont("comicsansms", 72)
    text = font.render("RASENDE ROBOTER", True, (112, 148, 124))
    buttonStart = Button((400, 250), (200, 100), (192,192,192), "Start")
    buttonQuit = Button((400, 650), (200, 100), (192,192,192), "Quit")
    buttonRules = Button((400,450), (200,100), (192,192,192),"Rules")
    
    
    # - mainloop -
    
    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if buttonStart.is_clicked(event):
                #ici on va mettre le jeu
                game()
                
                

            if buttonRules.is_clicked(event):
                # go to stage2
                webbrowser.open("https://fr.wikipedia.org/wiki/Ricochet_Robots")
                
                
            if buttonQuit.is_clicked(event):
                # exit
                pygame.quit()
                exit()

        # - draws -

        screen.fill((60,25,63))    
        buttonStart.draw(screen)
        buttonQuit.draw(screen)
        buttonRules.draw(screen)
        screen.blit(text,(150,100))
        
        
        pygame.display.flip()

        # - FPS -

        clock.tick(FPS)

# --- main ---



# - init -

pygame.init()
screen = pygame.display.set_mode((1000,950),pygame.RESIZABLE)  
pygame.display.set_caption('Rasende Roboter')

# - start -

MenuScreen(screen)


# - end -

pygame.quit()