import os

import pygame
import sys
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()
W = 600
H = 400

Surface = pygame.display.set_mode((W, H), 0, 32)
pygame.display.set_caption('Cold War 2: Putin Warfare Menu')

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

##def text_print(text,color1,color2,left,top,Font=basicFont):
##    text = Font.render(text,True,color1,color2)
##    text_rect = text.get_rect()
##    text_rect.top = top
##    text_rect.left = left
##    Surface.blit(text, text_rect)
game = True
mouse_pos = (0, 0)
mouse_click = (0, 0)
text1_bool = False
text2_bool = False
text3_bool = False
output = 'Welcome to Cold War 2: Putin Warfare'

while game == True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit(0)
        if event.type == MOUSEMOTION:
            mouse_pos = event.pos
        if event.type == MOUSEBUTTONUP:
            mouse_click = event.pos

    Surface.fill(BLACK)
    color = WHITE
    Font = pygame.font.SysFont('arial', 40)
    if text1_bool:
        color = RED
    text = Font.render('Play', True, color)
    text_rect = text.get_rect()
    text_rect.center = (W / 2, H / 5)
    if text_rect.collidepoint(mouse_click):
        os.system("python game.py")
        exit()


    if text_rect.collidepoint(mouse_pos):
        text1_bool = True
    else:
        text1_bool = False
    Surface.blit(text, text_rect)

    color = WHITE
    if text3_bool:
        color = RED

    Font = pygame.font.SysFont('arial', 40)
    text = Font.render('Quit', True, color)
    text_rect = text.get_rect()
    text_rect.center = (W / 2, H * 3 / 5)
    if text_rect.collidepoint(mouse_click):
        exit()
    if text_rect.collidepoint(mouse_pos):
        text3_bool = True
    else:
        text3_bool = False
    Surface.blit(text, text_rect)

    Font = pygame.font.SysFont('arial', 40)
    text = Font.render(output, True, BLUE)
    text_rect = text.get_rect()
    text_rect.center = (W / 2, H * 4 / 5)
    Surface.blit(text, text_rect)

    pygame.display.flip()
    mainClock.tick(100000)