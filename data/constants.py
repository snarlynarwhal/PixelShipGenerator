import os
import pygame
from pygame.locals import *


SCALE = 2

SHIPW = 50 * SCALE
SHIPH = 50 * SCALE

SCREENWIDTH = 400 * SCALE
SCREENHEIGHT = 300 * SCALE
SCREEN_SIZE = (SCREENWIDTH, SCREENHEIGHT)
CAPTION = 'Pixel Ship Generator'
FPS = 60

BLACK = (0, 0, 0)

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = "TRUE"
pygame.display.set_caption(CAPTION)
SCREEN = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE | DOUBLEBUF)
SCREEN_RECT = SCREEN.get_rect()


def scale(n):
    return n * SCALE