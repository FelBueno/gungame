from typing import Any
import pygame
from pygame.locals import *
from scripts.consts import *
from scripts.player import P
from scripts.particles import Particle
from random import randint

pygame.init()

class Attacker(pygame.sprite.Sprite):
     def __init__(self) -> None:
          pygame.sprite.Sprite.__init__(self)

          self.sprite:list = []
          enemy = randint(0,1)
          if enemy == 0:
               spr = pygame.image.load("sprites/enemys/mafagafo.png")
               
               for i in range(2):
                    self.image = spr.subsurface((7*i,0),(6,10))
                    self.image = pygame.transform.scale(self.image,(6*REDOBJ*2,10*REDOBJ*2))
                    self.sprite.append(self.image)

               self.hp:int = 5
               self.dmg:int = 3
          elif enemy == 1:
               spr = pygame.image.load("sprites/enemys/mossmonster.png")
               
               for i in range(3):
                    self.image = spr.subsurface((7*i,0),(6,6))
                    self.image = pygame.transform.scale(self.image,(6*REDOBJ*2,6*REDOBJ*2))
                    self.sprite.append(self.image)
               
               self.hp:int = 1
               self.dmg:int = 1
          
          self.rect = self.image.get_rect()

          r = randint(0,3)
          if r == 0:
               minY = -scalecordY(10)
               maxY = H + scalecordY(10)
               self.rect.center = -scalecordX(10), randint(minY,maxY)
          elif r == 1:
               minY = -scalecordY(10)
               maxY = H + scalecordY(10)
               self.rect.center = W + scalecordX(10), randint(minY,maxY)
          elif r == 2:
               minX = -scalecordX(10)
               maxX = W + scalecordX(10)
               self.rect.center = randint(minX,maxX), H + scalecordY(10)
          elif r == 3:
               minX = -scalecordX(10)
               maxX = W + scalecordX(10)
               self.rect.center = randint(minX,maxX), -scalecordY(10)

          self.dir = 1

          
          #vars
          self.speed:float = REDOBJ /5
          self.spd:float = self.speed
          self.img = self.image
          self.waitattack:int = 50
          self.canwalk:bool = True
          self.index:int = 0



     def update(self) -> None:
          self.walk()  
          
          self.waitattack -= 1

          if self.hp <= 0:
               self.kill()

          if self.dir == -1:
               self.image = pygame.transform.flip(self.img, True, False) 
          else:
               self.image = self.img

          col:colision = pygame.sprite.spritecollide(self, ProjPGroup, True)
          if col:
               for i in range(10):
                    dmg:Particle = Particle(self.rect.centerx, self.rect.centery, RED)
                    ParticlesGroup.add(dmg)
               for bl in col:
                    self.hp -= bl.dmg

     def walk(self) -> None:
          if self.rect.centerx < P.rect.centerx:
               self.dir = 1
               self.rect.centerx += self.speed
          elif self.rect.centerx > P.rect.centerx:
               self.dir = -1
               self.rect.centerx -= self.speed
          if self.rect.centery < P.rect.centery:
               self.rect.centery += self.speed
          elif self.rect.centery > P.rect.centery:
               self.rect.centery -= self.speed













