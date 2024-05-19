import pygame
from scripts.consts import *
from scripts.player import P
from scripts.mira import mira, M
from scripts.gun import Gun

pygame.init()

class Game():
     def __init__(self) -> None:
          #tela e relógio
          self.screen:screen = pygame.display.set_mode((W,H))
          self.clock:clock = pygame.time.Clock()
          
          #outras vars
          self.rodando:bool = True
          self.pause:bool = False

          self.color:color = BLUE
          

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

                    Gun.get_event(event)
                    P.get_event(event, M)

               #game code
               self.ingame()
               mira.draw(self.screen)
               mira.update()

               pygame.display.update()
               self.clock.tick(60)

     def ingame(self) -> None:

          P.draw(self.screen)
          P.update()

          Gun.update(self.screen)

          ProjPGroup.draw(self.screen)
          ProjPGroup.update()


G:Game = Game()

if __name__ == "__main__":
     G.main()




