import pygame
from scripts.consts import *
from scripts.player import P
from scripts.mira import mira, M
from scripts.enemys.attacker import Attacker
from scripts.ui.life import HpBar
from scripts.ui.ammor import ammorBar 
from scripts.gun import Gun
from random import randint

pygame.init()

UiGroup.add(HpBar, ammorBar)



class Game():
     def __init__(self) -> None:
          #tela e relógio
          self.screen:screen = pygame.display.set_mode((W,H))
          self.clock:clock = pygame.time.Clock()
          
          #outras vars
          self.rodando:bool = True
          self.pause:bool = False

          self.color:color = BLUE
          self.waitenemy:int = randint(30, 120)

          pygame.mouse.set_visible(False)

     def main(self):

          while self.rodando:
               self.screen.fill(self.color)
               for event in pygame.event.get():
                    if event.type == QUIT:
                         #quita do jogo
                         pygame.quit()
                         self.rodando:bool = False

                    #se tecla for clickada
                    elif event.type == KEYDOWN:
                         if event.key == K_DELETE:
                              #atalho pra quita do jogo
                              pygame.quit()
                              self.rodando:bool = False

                         elif event.key == K_ESCAPE:
                              #pausa o jogo
                              self.pause:bool = not self.pause

                         elif event.key == K_r:
                              if P.Hp <= 0:
                                   P.restart()

                    Gun.get_event(event)
                    P.get_event(event, M)

               #game code
               if P.Hp > 0:
                    self.ingame()
               else:
                    self.GameOver()
               mira.draw(self.screen)
               mira.update()

               pygame.display.update()
               self.clock.tick(60)

     def ingame(self) -> None:
          self.waitenemy -= 1

          if self.waitenemy <= 0:
               self.waitenemy:int = randint(60, 300)

               EnemysGroup.add(Attacker())

          P.draw(self.screen)
          P.update()

          Gun.update(self.screen)

          ProjPGroup.draw(self.screen)
          ProjPGroup.update()

          EnemysGroup.draw(self.screen)
          EnemysGroup.update()

          UiGroup.draw(self.screen)
          UiGroup.update(self.screen)

          ParticlesGroup.draw(self.screen)
          ParticlesGroup.update()

     def GameOver(self) -> None:
          '''game over
          :return None'''

          #Titlep.
          youdie = fontBIG.render("You", False, (255, 255, 255))
          youdie_rect = youdie.get_rect()
          xpos = (scalecordX(1500) - youdie_rect.width) // 2
          self.screen.blit(youdie, (xpos, scalecordY(72)))

          youdie = fontBIG.render("Died", False, (255, 0, 0))
          youdie_rect = youdie.get_rect()
          xpos = (scalecordX(2000) - youdie_rect.width) // 2
          self.screen.blit(youdie, (xpos, scalecordY(72)))
          
          Texto = font.render("Press R to restart", False, (255, 255, 255))
          Texto_rect = Texto.get_rect()
          xpos = (W - Texto_rect.width) // 2
          self.screen.blit(Texto, (xpos, scalecordY(1000)))


          UiGroup.draw(self.screen)
          UiGroup.update(self.screen) 

G:Game = Game()

if __name__ == "__main__":
     G.main()




