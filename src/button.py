import pygame
#Fonction permettant de créer des boutons sur Pygame
def button(screen, position, text,color):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (0, 0, 0))
    x, y, w , h = text_render.get_rect()
    x, y = position
   
    pygame.draw.rect(screen, color, (x, y, w , h))
    return screen.blit(text_render, (x, y))