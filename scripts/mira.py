from typing import Any
import pygame
from scripts.consts import *


pygame.init()

class Mira(pygame.sprite.Sprite):
     def __init__(self) -> None:
          '''game's palyer'''
          pygame.sprite.Sprite.__init__(self)
          self.sprites:list[image] = []
          spr:image = pygame.image.load("sprites/mira.png")

          for i in range(2):
               self.image:image = spr.subsurface((6*i,0),(5,5))
               self.image:image = pygame.transform.scale(self.image, (4*REDOBJ, 4*REDOBJ))
               self.sprites.append(self.image)

          self.image = self.sprites[0]
          self.rect = self.image.get_rect()
          self.rect.center = pygame.mouse.get_pos()

          #vars para animação
          self.angle:int = 0  
          self.scale_factor:int = 1  
          self.scale_increment:float = 0.01  
          self.waitindex:int = 0
          self.index:int = 0

     def update(self) -> None:
          self.waitindex -= 1
          if self.waitindex <= 0:
               self.index:int = 0

          #atualiza posição
          self.rect.center = pygame.mouse.get_pos()
          self.rotate()
          self.scale()
     
     def rotate(self):
          # Rotaciona a imagem em 1 grau
          self.angle = (self.angle + 1.5) % 360
          self.image = pygame.transform.rotate(self.sprites[self.index], self.angle)

     def scale(self):
          # Aumenta ou diminui o fator de escala até certo limite e depois inverte
          if self.scale_factor >= 1.5:
               self.scale_increment *= -1
          elif self.scale_factor <= 1:
               self.scale_increment *= -1

          self.scale_factor += self.scale_increment
          self.image = pygame.transform.scale(self.image, (int(self.rect.width * self.scale_factor), int(self.rect.height * self.scale_factor)))
     


M:Mira = Mira()
mira:group = pygame.sprite.Group()
mira.add(M)





