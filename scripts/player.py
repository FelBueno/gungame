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
          #*animate vars
          self.moving:bool = False
          self.index:int = 0
          self.lastpressed:str = 'd'

     def update(self, G:game, mira:cursor) -> None:
          '''update player
          :return None'''


          self.move(G)


     def draw(self, surface:screen) -> None:
          '''draw player
          :param surface: screen to draw player
          :return None'''

          surface.blit(self.image, self.rect)

     def move(self, G:game) -> None:
          '''move player
          :return None'''



          #não permite sair pra fora da tela
          if self.rect.right < 0:
               self.rect.right = W
          elif self.rect.left > W:
               self.rect.left = 0
          if self.rect.bottom < 0:
               self.rect.bottom = H - scalecordY(2)
          if self.rect.top > H:
               self.rect.top = 0

     def get_event(self, events:event, mira:cursor):

          #compatibilidade com controle
          if events.type == MOUSEBUTTONDOWN:
               mira.waitindex = 10
               mira.index = 1














P:Player = Player()
