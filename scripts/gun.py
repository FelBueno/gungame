from typing import Any
import pygame
from scripts.consts import *
from scripts.player import P
from scripts.ProjPlayer import ProjPlayer
from random import choice, randint
import math


pygame.init()

class Guns(pygame.sprite.Sprite):
     def __init__(self) -> None:
          '''game's player'''
          pygame.sprite.Sprite.__init__(self)

          self.sprite:dict[str, list] = {
               "pistols": [],
               "shotguns": []
               
          }
          self.loadpistoll()
          self.loadshotguns()

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
                         self.fire()



     def loadpistoll(self) -> None:
          '''load sprite
          :return None'''
          spr = pygame.image.load("sprites/guns/revolvers.png")
          for i in range(2):
               image = spr.subsurface((12*i, 12), (12, 11))
               image = pygame.transform.scale(image, (12*REDOBJ/2, 11*REDOBJ/2))
               self.sprite["pistols"].append(image)

          for i in range(2):
               image = spr.subsurface((13*i, 0), (12, 11))
               image = pygame.transform.scale(image, (12*REDOBJ/2, 11*REDOBJ/2))
               self.sprite["pistols"].append(image)
          
          image = spr.subsurface((26, 0), (15, 11))
          image = pygame.transform.scale(image, (15*REDOBJ/2, 11*REDOBJ/2))
          self.sprite["pistols"].append(image)

          image = spr.subsurface((42, 0), (11, 11))
          image = pygame.transform.scale(image, (11*REDOBJ/2, 11*REDOBJ/2))
          self.sprite["pistols"].append(image)

          image = spr.subsurface((54, 0), (14, 11))
          image = pygame.transform.scale(image, (14*REDOBJ/2, 11*REDOBJ/2))
          self.sprite["pistols"].append(image)


          image = spr.subsurface((24, 11), (12, 11))
          image = pygame.transform.scale(image, (12*REDOBJ/2, 11*REDOBJ/2))
          self.sprite["pistols"].append(image)
     
     def loadshotguns(self) -> None:
          '''load sprite
          :return None'''
          spr = pygame.image.load("sprites/guns/shotguns.png")
          for i in range(5):
               image = spr.subsurface((40*i, 0), (39, 12))
               image = pygame.transform.scale(image, (39*REDOBJ/2, 12*REDOBJ/2))
               self.sprite["shotguns"].append(image)

          image = spr.subsurface((0, 13), (39, 12))
          image = pygame.transform.scale(image, (39*REDOBJ/2, 12*REDOBJ/2))
          self.sprite["shotguns"].append(image)

          for i in range(4):
               x = 34 * i
               image = spr.subsurface((x+40, 13), (33, 12))
               image = pygame.transform.scale(image, (33*REDOBJ/2, 12*REDOBJ/2))
               self.sprite["shotguns"].append(image)

     def fire(self) -> None:
          tipo = "normal"
          match P.guntype:
               case "pistols":
                    match P.gunid:
                         case 0:
                              lifetime = 25
                              dmg = 1
                         case 1:
                              lifetime = randint(40,90)
                              dmg = 0
                              tipo = choice(["normal", "explosivo", "venenoso", "multi", "more"])
                         case 2:
                              lifetime = 40
                              dmg = 1
                         case 3:
                              lifetime = 40
                              dmg = 3
                              tipo = "explosivo"
                         case 4:
                              lifetime = 50
                              dmg = 1
                         case 5:
                              lifetime = randint(40,50)
                              dmg = 1
                         case 6:
                              lifetime = randint(30,40)
                              dmg = 2
                         case 7:
                              lifetime = 40
                              dmg = 1
                              tipo = "venenoso"
               case "shotguns":
                    match P.gunid:
                         case 0:
                              lifetime = 20
                              dmg = 1
                         case 1:
                              lifetime = 30
                              dmg = 1
                         case 2:
                              lifetime = 25
                              dmg = 2
                         case 3:
                              lifetime = 40
                              dmg = 3
                              tipo = choice(["explosivo", "multi"])
                         case 4:
                              lifetime = 35
                              dmg = 3
                              tipo =  "explosivo"
                         case 5:
                              lifetime = 35
                              dmg = 2
                              tipo = "venenoso"
                         case 6:
                              lifetime = 20
                              dmg = 1
                         case 7:
                              lifetime = 30
                              dmg = 1
                         case 8:
                              lifetime = 25
                              dmg = 2
                         case 9:
                              lifetime = 40
                              dmg = 2
                              tipo = choice(["explosivo", "multi"])


          match P.guntype:
               case "pistols":
                    if P.gunid != 1:
                         if self.gox == -1:
                              pjp = ProjPlayer(self.rect.left, self.rect.top, self.angle, self.gox, dmg, lifetime, tipo)
                         elif self.gox == 1:
                              pjp = ProjPlayer(self.rect.right, self.rect.top, self.angle, self.gox, dmg, lifetime, tipo)

                         ProjPGroup.add(pjp)
                    else:
                         if tipo == "more":
                              tipo = "normal"
                              r = randint(0,5)
                              if r == 0:
                                   if self.gox == -1:
                                        pjp = ProjPlayer(self.rect.left, self.rect.top, self.angle, self.gox, dmg, lifetime, tipo)
                                        ProjPGroup.add(pjp)
                                        pjp = ProjPlayer(self.rect.left, self.rect.top, self.angle - 15, self.gox, dmg, lifetime, tipo)
                                        ProjPGroup.add(pjp)
                                        pjp = ProjPlayer(self.rect.left, self.rect.top, self.angle - 30, self.gox, dmg, lifetime, tipo)
                                        ProjPGroup.add(pjp)
                                        pjp = ProjPlayer(self.rect.left, self.rect.top, self.angle + 30, self.gox, dmg, lifetime, tipo)
                                        ProjPGroup.add(pjp)
                                        pjp = ProjPlayer(self.rect.left, self.rect.top, self.angle + 15, self.gox, dmg, lifetime, tipo)
                                        ProjPGroup.add(pjp)
                                   elif self.gox == 1:
                                        pjp = ProjPlayer(self.rect.right, self.rect.top, self.angle, self.gox, dmg, lifetime, tipo)
                                        ProjPGroup.add(pjp)
                                        pjp = ProjPlayer(self.rect.right, self.rect.top, self.angle - 15, self.gox, dmg, lifetime, tipo)
                                        ProjPGroup.add(pjp)
                                        pjp = ProjPlayer(self.rect.right, self.rect.top, self.angle - 30, self.gox, dmg, lifetime, tipo)
                                        ProjPGroup.add(pjp)
                                        pjp = ProjPlayer(self.rect.right, self.rect.top, self.angle + 30, self.gox, dmg, lifetime, tipo)
                                        ProjPGroup.add(pjp)
                                        pjp = ProjPlayer(self.rect.right, self.rect.top, self.angle + 15, self.gox, dmg, lifetime, tipo)
                                        ProjPGroup.add(pjp)
                              else:
                                   if self.gox == -1:
                                        pjp = ProjPlayer(self.rect.left, self.rect.top, self.angle, self.gox, dmg, lifetime, tipo)
                                        ProjPGroup.add(pjp)
                                        pjp = ProjPlayer(self.rect.left, self.rect.top, self.angle - 15, self.gox, dmg, lifetime, tipo)
                                        ProjPGroup.add(pjp)
                                        pjp = ProjPlayer(self.rect.left, self.rect.top, self.angle + 15, self.gox, dmg, lifetime, tipo)
                                        ProjPGroup.add(pjp)
                                   elif self.gox == 1:
                                        pjp = ProjPlayer(self.rect.right, self.rect.top, self.angle, self.gox, dmg, lifetime, tipo)
                                        ProjPGroup.add(pjp)
                                        pjp = ProjPlayer(self.rect.right, self.rect.top, self.angle - 15, self.gox, dmg, lifetime, tipo)
                                        ProjPGroup.add(pjp)
                                        pjp = ProjPlayer(self.rect.right, self.rect.top, self.angle + 15, self.gox, dmg, lifetime, tipo)
                                        ProjPGroup.add(pjp)
                         else: 
                              if self.gox == -1:
                                   pjp = ProjPlayer(self.rect.left, self.rect.top, self.angle, self.gox, dmg, lifetime, tipo)
                              elif self.gox == 1:
                                   pjp = ProjPlayer(self.rect.right, self.rect.top, self.angle, self.gox, dmg, lifetime, tipo)

                              ProjPGroup.add(pjp)          
               case "shotguns":
                    r:int = randint(0,9)
                    if r == 0:
                         if self.gox == -1:
                              pjp = ProjPlayer(self.rect.left, self.rect.top, self.angle, self.gox, dmg, lifetime, tipo)
                              ProjPGroup.add(pjp)
                              pjp = ProjPlayer(self.rect.left, self.rect.top, self.angle - 15, self.gox, dmg, lifetime, tipo)
                              ProjPGroup.add(pjp)
                              pjp = ProjPlayer(self.rect.left, self.rect.top, self.angle - 30, self.gox, dmg, lifetime, tipo)
                              ProjPGroup.add(pjp)
                              pjp = ProjPlayer(self.rect.left, self.rect.top, self.angle + 30, self.gox, dmg, lifetime, tipo)
                              ProjPGroup.add(pjp)
                              pjp = ProjPlayer(self.rect.left, self.rect.top, self.angle + 15, self.gox, dmg, lifetime, tipo)
                              ProjPGroup.add(pjp)
                         elif self.gox == 1:
                              pjp = ProjPlayer(self.rect.right, self.rect.top, self.angle, self.gox, dmg, lifetime, tipo)
                              ProjPGroup.add(pjp)
                              pjp = ProjPlayer(self.rect.right, self.rect.top, self.angle - 15, self.gox, dmg, lifetime, tipo)
                              ProjPGroup.add(pjp)
                              pjp = ProjPlayer(self.rect.right, self.rect.top, self.angle - 30, self.gox, dmg, lifetime, tipo)
                              ProjPGroup.add(pjp)
                              pjp = ProjPlayer(self.rect.right, self.rect.top, self.angle + 30, self.gox, dmg, lifetime, tipo)
                              ProjPGroup.add(pjp)
                              pjp = ProjPlayer(self.rect.right, self.rect.top, self.angle + 15, self.gox, dmg, lifetime, tipo)
                              ProjPGroup.add(pjp)
                    else:
                         if self.gox == -1:
                              pjp = ProjPlayer(self.rect.left, self.rect.top, self.angle, self.gox, dmg, lifetime, tipo)
                              ProjPGroup.add(pjp)
                              pjp = ProjPlayer(self.rect.left, self.rect.top, self.angle - 15, self.gox, dmg, lifetime, tipo)
                              ProjPGroup.add(pjp)
                              pjp = ProjPlayer(self.rect.left, self.rect.top, self.angle + 15, self.gox, dmg, lifetime, tipo)
                              ProjPGroup.add(pjp)
                         elif self.gox == 1:
                              pjp = ProjPlayer(self.rect.right, self.rect.top, self.angle, self.gox, dmg, lifetime, tipo)
                              ProjPGroup.add(pjp)
                              pjp = ProjPlayer(self.rect.right, self.rect.top, self.angle - 15, self.gox, dmg, lifetime, tipo)
                              ProjPGroup.add(pjp)
                              pjp = ProjPlayer(self.rect.right, self.rect.top, self.angle + 15, self.gox, dmg, lifetime, tipo)
                              ProjPGroup.add(pjp)






Gun:Guns = Guns()






