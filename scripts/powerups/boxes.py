from typing import Any
import pygame
from scripts.consts import *
from scripts.player import P
from scripts.ProjPlayer import ProjPlayer
from random import choice, randint
import math


pygame.init()

class Box(pygame.sprite.Sprite):
     def __init__(self) -> None:
          ''''''
          pygame.sprite.Sprite.__init__(self)

          spr:image = pygame.image.load("sprites/powerups/boxes.png")
          self.sprites:list = [] 

          for i in range(5):
               self.image:image = spr.subsurface((14*i,0),(13,13))
               self.image:image = pygame.transform.scale(self.image, (13*REDOBJ, 13*REDOBJ))
               self.sprites.append(self.image)
          
          self.index:int = randint(0,4)
          self.image:image = self.sprites[self.index]
          self.rect = self.image.get_rect()
          self.rect.center = randint(0,W), randint(0,H) 

          self.lifetime:int = randint(60,360)

     def update(self, display:screen) -> None:
          self.lifetime -= 1

          txt = fontSmall.render(f"{int(self.lifetime/60)}", False, WHITE)    
          txt_rect = txt.get_rect()
          xpos = (self.rect.centerx - txt_rect.width)
          display.blit(txt, (xpos, self.rect.top))

          if self.lifetime <= 0:
               self.kill()









