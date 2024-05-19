import pygame
from pygame.locals import *
from scripts.consts import *
from random import randint
import math

pygame.init()

class ProjPlayer(pygame.sprite.Sprite):
    def __init__(self, x:float, y:float, angle:float, gox:int, dmg:int, lifetime:int = 30, tipo:int = "normal") -> None:
        pygame.sprite.Sprite.__init__(self)

        # Carregando sprite
        self.image = pygame.image.load("sprites/Projectile.png")
        self.image = pygame.transform.scale(self.image, (2 * REDOBJ, 2 * REDOBJ))

        # Posicionando o sprite
        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.gox = gox
        self.dmg = dmg
        
        self.speed:float = REDOBJ * 5 * self.gox
        self.angle:float = angle

        self.time:int = lifetime

    def update(self) -> None:
        '''Atualização do projétil'''
        self.time -= 1

        if self.time < 0:
             self.kill()

        self.Move()

        if self.rect.right < 0:
            self.rect.right = W
        elif self.rect.left > W:
            self.rect.left = 0
        if self.rect.bottom < 0:
            self.rect.bottom = H - scalecordY(2)
        elif self.rect.top > H:
            self.rect.top = 0



    def Move(self) -> None:
        '''Movimentação'''
        # Calcular as componentes x e y do movimento com base no ângulo
        if self.gox == 1:
            dy = -math.sin(math.radians(self.angle)) * self.speed
        else:
            dy = math.sin(math.radians(self.angle)) * self.speed
        dx = math.cos(math.radians(self.angle)) * self.speed

        # Movimentar o projétil
        self.rect.x += dx
        self.rect.y += dy


        