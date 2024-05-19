import pygame
from pygame.locals import *
from scripts.consts import *
from random import randint

pygame.init()

class Particle(pygame.sprite.Sprite):
    def __init__(self, x:float, y:float, color:tuple[int] = (0,0,0), tamanho:tuple[float] = (4,4), lifetime:int = 90, fade:bool = True) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((tamanho[0], tamanho[1])) 
        self.image.fill(color) 
        self.rect = self.image.get_rect(center=(x, y))
        self.vx = (randint(-5, 5))
        self.vy = (randint(0, 5))
        self.gravity = 0.1
        self.life = lifetime
        self.maxlife = lifetime

        self.fade = fade

    def update(self) -> None:
        self.vx *= 0.9
        self.vy += self.gravity
        self.rect.x += self.vx
        self.rect.y += self.vy
        self.life -= 1

        if self.fade:
            alpha = max(0, int((self.life / self.maxlife) * 255))
            self.image.set_alpha(alpha)

        if self.life <= 0:
            self.kill()