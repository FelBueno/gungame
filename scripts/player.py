from typing import Any
import pygame
from scripts.consts import *


pygame.init()

class Player(pygame.sprite.Sprite):
     def __init__(self) -> None:
          '''game's palyer'''
          pygame.sprite.Sprite.__init__(self)

          self.sprite:list = []
          spr:image = pygame.image.load("sprites/Player.png")

          for i in range(4):
               self.image:image = spr.subsurface((7*i,0),(6,6))
               self.image:image = pygame.transform.scale(self.image,(6*REDOBJ,6*REDOBJ))
               self.sprite.append(self.image)

          #rect
          self.image:image = self.sprite[0]
          self.spr:image  = self.sprite[0]
          self.rect = self.image.get_rect()
          self.rect.center = W/2, H/2

          #var
          self.speed:float = REDOBJ

     def update(self) -> None:
          '''update player
          :return None'''
          self.move()
          self.animate()

     def draw(self, surface:screen) -> None:
          '''draw player
          :param surface: screen to draw player
          :return None'''

          surface.blit(self.image, self.rect)

     def move(self) -> None:
          '''move player
          :return None'''
          keys = pygame.key.get_pressed()

          #move horizontal
          if keys[K_a]:
               self.rect.x -= self.speed 
          elif keys[K_d]:
               self.rect.x += self.speed 
          #move na vertical
          if keys[K_w]:
               self.rect.y -= self.speed 
          elif keys[K_s]:
               self.rect.y += self.speed 


          #não permite sair pra fora da tela
          if self.rect.right < 0:
               self.rect.right = W
          elif self.rect.left > W:
               self.rect.left = 0
          if self.rect.bottom < 0:
               self.rect.bottom = H - scalecordY(2)
          if self.rect.top > H:
               self.rect.top = 0



     def animate(self) -> None:
          '''animate player
          :return None'''
          pass















P:Player = Player()
