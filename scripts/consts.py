import pygame
from pygame.locals import *
from os import environ

pygame.init()

version:str = "0.0.1 alpha"

#Tela
environ["SDL_VIDEO_CENTERED"] = "1"
info = pygame.display.Info()
W:int = info.current_w
H:int = info.current_h

# Proporções para redimensionamento
W_RATIO: float = W / 1920  # Proporção da largura
H_RATIO: float = H / 1080  # Proporção da altura

# Função para redimensionar com base nas proporções
def scale(value:int) -> int:
    return int(value * min(W_RATIO, H_RATIO))

def scalecordX(x:float) -> int:
    '''Função para redimensionar coordenadas X
    :param: x: value to scale'''
    return int(x * W_RATIO)

def scalecordY(y:float) -> int:
    '''Função para redimensionar coordenadas Y
    :param: y: value to scale'''
    return int(y * H_RATIO)

REDOBJ: float = scale(5)


#tipos
type screen = any
type fonttype = any
type event = any
type clock = any
type color = tuple
type image = any
type player = object
type game = object
type joystick = any
type group = any
type cursor = object
type colision = any

#Fontes
fontSmall:fonttype = pygame.font.Font("joystix monospace.otf", scale(18))
font:fonttype = pygame.font.Font("joystix monospace.otf", scale(35))
fontBIG:fonttype = pygame.font.Font("joystix monospace.otf", scale(80))

#cores
WHITE:color = (255,255,255)
BLACK:color = (0,0,0)
RED:color = (255,0,0)
GREEN:color = (0,255,0)
BLUE:color = (0,0,255)
YELLOW:color = (255,255,0)
PURPLE:color = (255,0,255)
CYAN:color = (0,255,255)
DARKBLUE:color = (10, 10, 120)

#grupo de sprites
ProjPGroup:group = pygame.sprite.Group()
ParticlesGroup:group = pygame.sprite.Group()
UiGroup:group = pygame.sprite.Group()
EnemysGroup:group = pygame.sprite.Group()
PowerupsGroup:group = pygame.sprite.Group()
