import pygame
from pygame.locals import *
from scripts.consts import *
from scripts.particles import Particle
from random import randint, choice
import math

pygame.init()

class ProjPlayer(pygame.sprite.Sprite):
    def __init__(self, x:float, y:float, angle:float, gox:int, dmg:int, lifetime:int = 30, tipo:int = "normal", P:object = object()) -> None:
        pygame.sprite.Sprite.__init__(self)

        # Carregando sprite
        self.image = pygame.image.load("sprites/Projectile.png")
        self.image = pygame.transform.scale(self.image, (4 * REDOBJ, 4 * REDOBJ))

        # Posicionando o sprite
        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.gox = gox
        self.dmg = dmg
        
        self.speed:float = REDOBJ * 5 * self.gox
        self.angle:float = angle

        self.time:int = lifetime
        self.tipo:str = tipo
        "explosivo", "venenoso", "multi"
        if self.dmg <= 0:
            self.dmg = randint(1,4)
        self.P = P

    def update(self) -> None:
        '''Atualização do projétil'''
        self.time -= 1

        if self.time < 0:
             self.kill()

        self.Move()

        if self.rect.right < 0:
            self.rect.right = W
        elif self.rect.left > W:
            self.rect.left = 0
        if self.rect.bottom < 0:
            self.rect.bottom = H - scalecordY(2)
        elif self.rect.top > H:
            self.rect.top = 0

        if self.tipo == "explosivo":
            caminho:Particle = Particle(self.rect.centerx, self.rect.centery, YELLOW, (REDOBJ,REDOBJ), 60)
            ParticlesGroup.add(caminho)
        elif self.tipo == "venenoso":
            caminho:Particle = Particle(self.rect.centerx, self.rect.centery, GREEN, (REDOBJ,REDOBJ), 60)
            ParticlesGroup.add(caminho)
        
        pw = pygame.sprite.spritecollide(self, PowerupsGroup, True)
        if pw:
            for p in pw:
                match p.index:
                    case 0: #hp
                        if self.P.Hp + 3 <= 20:
                            self.P.Hp += 3
                        else:
                            self.P.Hp = 20
                    case 1: #+munição
                        self.P.canload[self.P.guntype][self.P.gunid] += 1 
                        self.P.ammor[self.P.guntype][self.P.gunid] = self.P.maxammor[self.P.guntype][self.P.gunid]
                    case 2: #muda arma
                        self.P.guntype = choice(["pistols","shotguns"])
                        self.P.gunid = randint(0, len(self.P.ammor[self.P.guntype])-1)
                    case 3: #mata algus inimigos
                        for en in EnemysGroup:
                            for i in range(10):
                                dmg:Particle = Particle(en.rect.centerx, en.rect.centery, RED)
                                ParticlesGroup.add(dmg)
                            en.kill()
                            if randint(0, 4) == 0:
                                break
                        
                    case 4: #random
                        r = randint(0,3)
                        if r == 0:
                            if self.P.Hp + 3 <= 20:
                                self.P.Hp += 3
                            else:
                                self.P.Hp = 20

                        elif r ==1: #+munição
                            self.P.canload[self.P.guntype][self.P.gunid] += 1 
                            self.P.ammor[self.P.guntype][self.P.gunid] = self.P.maxammor[self.P.guntype][self.P.gunid]
                        elif r ==2: #muda arma
                            self.P.guntype = choice(["pistols","shotguns"])
                            self.P.gunid = randint(0, len(self.P.ammor[self.P.guntype])-1)
                        elif r ==3: #mata algus inimigos
                            for en in EnemysGroup:
                                for i in range(10):
                                    dmg:Particle = Particle(en.rect.centerx, en.rect.centery, RED)
                                    ParticlesGroup.add(dmg)
                                en.kill()
                                if randint(0, 4) == 0:
                                    break


    def Move(self) -> None:
        '''Movimentação'''
        # Calcular as componentes x e y do movimento com base no ângulo
        if self.gox == 1:
            dy = -math.sin(math.radians(self.angle)) * self.speed
        else:
            dy = math.sin(math.radians(self.angle)) * self.speed
        dx = math.cos(math.radians(self.angle)) * self.speed

        # Movimentar o projétil
        self.rect.x += dx
        self.rect.y += dy


        