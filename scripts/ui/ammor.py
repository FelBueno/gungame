from typing import Any
import pygame
from pygame.locals import *
from scripts.consts import *
from scripts.player import P
from scripts.particles import Particle
from random import randint

pygame.init()

class AmmorBar(pygame.sprite.Sprite):
     def __init__(self) -> None:
          pygame.sprite.Sprite.__init__(self)

          #sprites
          spr = pygame.image.load("sprites/ui/ammorUI.png")
          self.sprite:list = []

          for i in range(5):
               self.image = spr.subsurface((14*i,0),(13,7))
               self.image = pygame.transform.scale(self.image,(13*REDOBJ*1.5,7*REDOBJ*1.5))
               self.sprite.append(self.image)

          #rect
          self.image = self.sprite[0]
          self.rect = self.image.get_rect()
          self.rect.center = scalecordX(125), scalecordY(35)

          self.porcent75:int = int(P.ammor[P.guntype][P.gunid] * 0.75)
          self.porcent50:int = int(P.ammor[P.guntype][P.gunid] * 0.5)
          self.porcent25:int = int(P.ammor[P.guntype][P.gunid] * 0.25)
          self.porcent10:int = int(P.ammor[P.guntype][P.gunid] * 0.1)
          self.time:int = 30
          self.originalx:float = self.rect.centerx

     def update(self, display:pygame.display) -> None:
          #update class e desenha na tela
          mpos = pygame.mouse.get_pos()

          self.porcent75:int = int(P.maxammor[P.guntype][P.gunid] * 0.75)
          self.porcent50:int = int(P.maxammor[P.guntype][P.gunid] * 0.5)
          self.porcent25:int = int(P.maxammor[P.guntype][P.gunid] * 0.25)
          self.porcent10:int = int(P.maxammor[P.guntype][P.gunid] * 0.1)
          
          # Verifique se o mouse está dentro do retângulo do objeto
          if self.rect.collidepoint(mpos):
               #desenha txt na tela
               Txt = font.render(f"{P.ammor[P.guntype][P.gunid]}/{P.maxammor[P.guntype][P.gunid]}", True, (255, 255, 255))
          
               display.blit(Txt, (self.rect.centerx, self.rect.bottom))
          
          txt = font.render(f"(x{P.canload[P.guntype][P.gunid]})", True, (255, 255, 255))
          display.blit(self.image, self.rect)
          display.blit(txt, (scalecordX(160), scalecordY(20)))

          if P.ammor[P.guntype][P.gunid] > self.porcent75:
               self.image = self.sprite[0]
          elif (P.ammor[P.guntype][P.gunid] > self.porcent50):
               self.image = self.sprite[1]
          elif (P.ammor[P.guntype][P.gunid] > self.porcent25):
               self.image = self.sprite[2]
          elif (P.ammor[P.guntype][P.gunid] > self.porcent10):
               self.image = self.sprite[3]
          elif (P.ammor[P.guntype][P.gunid] <= 0): 
               self.image = self.sprite[4]
               if self.time % 3 == 0:
                    color = YELLOW
                    tamanho = (randint(3,8),randint(3,8))
                    ammor = Particle(self.rect.centerx, self.rect.centery, color, tamanho, 30, fade = False)
                    ParticlesGroup.add(ammor)

               self.shake()

          self.time -= 1

          if P.ammor[P.guntype][P.gunid] <= 0:
               P.ammor[P.guntype][P.gunid] = 0
          
     def shake(self) -> None:
          '''Faz balançar'''
          if self.time <= 0:
               self.time:int = 30

          self.image = self.sprite[4]
          if self.time % 5 == 0:
               self.rect.centerx = self.originalx + scalecordX(2)
          elif self.time % 5 != 0:
               self.rect.centerx = self.originalx - scalecordX(2)


ammorBar:AmmorBar = AmmorBar()


