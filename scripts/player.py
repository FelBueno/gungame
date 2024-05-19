from typing import Any
import pygame
from scripts.consts import *
import math


pygame.init()

class Player(pygame.sprite.Sprite):
     def __init__(self) -> None:
          '''game's player'''
          pygame.sprite.Sprite.__init__(self)

          self.sprite = []
          spr = pygame.image.load("sprites/Player.png")

          for i in range(4):
               image = spr.subsurface((7*i, 0), (6, 6))
               image = pygame.transform.scale(image, (6*REDOBJ*2, 6*REDOBJ*2))
               self.sprite.append(image)

          # rect
          self.image = self.sprite[0]
          self.rect = self.image.get_rect()
          self.rect.center = W/2, H/2

          # var
          self.new_x, self.new_y = self.rect.center
          self.speedx, self.speedy = REDOBJ, REDOBJ
          self.gunid:int = 0
          self.guntype:str = "pistols"
          self.countdown:int = 0
          self.ammor:dict[str,int] = {
               "pistols": [8, 6, 12, 5, 10, 6, 10, 10]
               }
          self.maxammor:dict[str,int] = {
               "pistols": [8, 6, 12, 5, 10, 6, 10, 10]
               }
          
          self.Hp:int = 20



     def update(self) -> None:
          '''update player
          :return None'''
          self.countdown -= 1


          # não permite sair pra fora da tela
          if self.rect.right < 0:
               self.rect.right = W
          elif self.rect.left > W:
               self.rect.left = 0
          if self.rect.bottom < 0:
               self.rect.bottom = H - scalecordY(2)
          elif self.rect.top > H:
               self.rect.top = 0

          # Move o jogador para as novas coordenadas
          self.move()

     def draw(self, surface: screen) -> None:
          '''draw player
          :param surface: screen to draw player
          :return None'''

          surface.blit(self.image, self.rect)

     def move(self) -> None:
          '''move player
          :return None'''
          #efeito de atrito
          self.speedy *= 0.9
          self.speedx *= 0.9

          self.rect.x += self.speedx
          self.rect.y += self.speedy

     def get_event(self, events: event, mira: cursor):
          # compatibilidade com controle
          if events.type == MOUSEBUTTONDOWN:
               if self.countdown <= 0:
                    if self.ammor[self.guntype][self.gunid] > 0:
                         self.ammor[self.guntype][self.gunid] -= 1
                         self.setcountdown()
                         # Calcula a distância entre o jogador e o cursor
                         distance_x = mira.rect.centerx - self.rect.centerx
                         distance_y = mira.rect.centery - self.rect.centery
                         distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

                         # Calcula as coordenadas da ponta final do vetor na direção oposta com metade da distância
                         if distance != 0:
                              self.new_x = self.rect.centerx - (distance_x / distance) 
                              self.new_y = self.rect.centery - (distance_y / distance)

                              self.setspeed()
          #quando tecla é pressionada
          elif events.type == KEYDOWN:
               if events.key == K_r:
                    if self.countdown <= 0:
                         self.setcountdown()
                         self.ammor[self.guntype][self.gunid] = self.maxammor[self.guntype][self.gunid]
               elif events.key == K_m:
                    if self.gunid == len(self.ammor[self.guntype]) -1:
                         self.gunid:int = 0
                    else:
                         self.gunid += 1
               elif events.key == K_PLUS:
                    if self.gunid == 0:
                         len(self.ammor[self.guntype]) -1
                    else:
                         self.gunid -= 1

     def setspeed(self) -> None:
          '''set player's speed
          :return None'''

          if self.guntype == "pistols":
               match self.gunid:
                    case 0:
                         spd:float = REDOBJ / 2
                    case 1:
                         spd:float = REDOBJ * 5
                    case 2:
                         spd:float = REDOBJ * 2
                    case 3:
                         spd:float = REDOBJ * 4
                    case 4:
                         spd:float = REDOBJ * 2.5
                    case 5:
                         spd:float = REDOBJ * 3.5
                    case 6:
                         spd:float = REDOBJ * 4
                    case 7:
                         spd:float = REDOBJ * 2.2
                    case _:
                         raise NotImplementedError(IndexError)





          if self.new_x >= self.rect.centerx:
               self.speedx = spd
          elif self.new_x < self.rect.centerx:
               self.speedx = -spd

          if self.new_y >= self.rect.centery:
               self.speedy = spd
          elif self.new_y < self.rect.centery:
               self.speedy = -spd

     def setcountdown(self) -> None:
          '''set player's countdown
          :return None'''
          if self.guntype == "pistols":
               match self.gunid:
                    case 0:
                         ctd:int = 50
                    case 1:
                         ctd:int = 70
                    case 2:
                         ctd:int = 40
                    case 3:
                         ctd:int = 45
                    case 4:
                         ctd:int = 40
                    case 5:
                         ctd:int = 50
                    case 6:
                         ctd:int = 45
                    case 7:
                         ctd:int = 35
                    case _:
                         raise NotImplementedError(IndexError)
                    
          self.countdown:int = ctd








P:Player = Player()
