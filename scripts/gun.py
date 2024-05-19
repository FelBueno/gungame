from typing import Any
import pygame
from scripts.consts import *
from scripts.player import P
from scripts.ProjPlayer import ProjPlayer
import math


pygame.init()

class Guns(pygame.sprite.Sprite):
     def __init__(self) -> None:
          '''game's player'''
          pygame.sprite.Sprite.__init__(self)

          self.sprite:dict[str, list] = {
               "pistols": []
               
          }
          self.loadpistoll()


          # rect
          self.img = self.sprite["pistols"][0]
          self.image = self.sprite["pistols"][0]
          self.rect = self.image.get_rect()
          self.rect.center = P.rect.center

          #vars
          self.gox: int = 1
          self.countdown:int = 0
          self.angle:int = 0

     def update(self, display: pygame.display) -> None:

          mouse_x, mouse_y = pygame.mouse.get_pos()

          # Calcular o vetor direção para o mouse
          dx:float = mouse_x - self.rect.centerx
          dy:float = mouse_y - self.rect.centery


          if mouse_x >= P.rect.x:
               self.gox:int = 1
               # Calcular o ângulo
               self.angle = math.degrees(math.atan2(-dy, dx))

               # Rotação do sprite para encarar o mouse
               self.image = pygame.transform.rotate(self.sprite[P.guntype][P.gunid], self.angle)
               self.rect = self.image.get_rect()


               self.rect.right = P.rect.right
               self.rect.bottom = P.rect.centery
               display.blit(self.image, (self.rect.right, self.rect.centery))
          elif mouse_x < P.rect.x:
               self.gox = -1
               # Calcular o ângulo e adicionar 180 graus
               self.angle = math.degrees(math.atan2(dy, dx)) + 180

               # Rotação do sprite para encarar o mouse
               self.image = pygame.transform.rotate(self.sprite[P.guntype][P.gunid], self.angle)
               self.rect = self.image.get_rect()

               self.image = pygame.transform.flip(self.image, True, False)
               self.rect.right = P.rect.left
               self.rect.bottom = P.rect.centery
               display.blit(self.image, (self.rect.left, self.rect.centery))

          

          # Desenhar a arma na tela


          self.countdown -= 1

     def get_event(self, events: event):
          # compatibilidade com controle
          if events.type == pygame.MOUSEBUTTONDOWN:
               
               if P.countdown <= 0:
                    if P.ammor[P.guntype][P.gunid] > 0:
                         # Calcula a distância entre o jogador e o cursor
                         if self.gox == -1:
                              pjp = ProjPlayer(self.rect.left, self.rect.top, self.angle, self.gox)
                         elif self.gox == 1:
                              pjp = ProjPlayer(self.rect.right, self.rect.top, self.angle, self.gox)

                         ProjPGroup.add(pjp)



     def loadpistoll(self) -> None:
          '''load sprite
          :return None'''
          spr = pygame.image.load("sprites/guns/revolvers.png")
          for i in range(2):
               image = spr.subsurface((12*i, 12), (12, 11))
               image = pygame.transform.scale(image, (12*REDOBJ, 11*REDOBJ))
               self.sprite["pistols"].append(image)

          for i in range(2):
               image = spr.subsurface((13*i, 0), (12, 11))
               image = pygame.transform.scale(image, (12*REDOBJ, 11*REDOBJ))
               self.sprite["pistols"].append(image)
          
          image = spr.subsurface((26, 0), (15, 11))
          image = pygame.transform.scale(image, (15*REDOBJ, 11*REDOBJ))
          self.sprite["pistols"].append(image)

          image = spr.subsurface((42, 0), (11, 11))
          image = pygame.transform.scale(image, (11*REDOBJ, 11*REDOBJ))
          self.sprite["pistols"].append(image)

          image = spr.subsurface((54, 0), (14, 11))
          image = pygame.transform.scale(image, (14*REDOBJ, 11*REDOBJ))
          self.sprite["pistols"].append(image)


          image = spr.subsurface((24, 11), (12, 11))
          image = pygame.transform.scale(image, (12*REDOBJ, 11*REDOBJ))
          self.sprite["pistols"].append(image)
     


Gun:Guns = Guns()






