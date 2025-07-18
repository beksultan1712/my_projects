import pygame, sys
from pygame.locals import *
import random, time 

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

Blue = (0, 0, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Black = (0, 0, 0)
White = (255, 255, 255)

Screen_width = 400
Screen_height = 600
SPEED = 5
SCORE = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, Black)

background = pygame.image.load("AnimatedStreet.jpeg")

Displaysurf = pygame.display.set_mode((400, 600))
Displaysurf.fill(White)
pygame.display.set_caption("Fgame")

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.image = pygame.image.load("Enemy.png")
            self.rect = self.image.get_rect()
            self.rect.center = random.randint(40, Screen_width - 40), 0
            
      def move(self):
            global SCORE
            self.rect.move_ip(0, SPEED)
            if self.rect.bottom > 600:
                  SCORE += 1 
                  self.rect.top = 0
                  self.rect.center = random.randint(30, 370), 0

class Player(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.image = pygame.image.load("Player.png")
            self.rect = self.image.get_rect()
            self.rect.center = 160, 520

      def move(self):
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_UP]:
                  self.rect.move_ip(0, -5)
            if pressed_keys[K_DOWN]:
                  self.rect.move_ip(0, 5)
                  
            if self.rect.left > 0 and pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0) 
            if self.rect.right < Screen_width and pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
      for event in pygame.event.get():
            if event.type == INC_SPEED:
                  SPEED += 0.2

            if event.type == QUIT:
                  pygame.quit()
                  sys.exit()
                  
      Displaysurf.blit(background, (0, 0))
      scores = font_small.render(str(SCORE), True, Black )
      Displaysurf.blit(scores, (10, 10))
                       
      for entity in all_sprites:
            Displaysurf.blit(entity.image, entity.rect)
            entity.move()
            
      if pygame.sprite.spritecollideany(P1, enemies):
            pygame.mixer.Sound('crash.wav').play()
            time.sleep(0.5)

            Displaysurf.fill(Red)
            Displaysurf.blit(game_over, (30, 250))
                       
            pygame.display.update()
            for entity in all_sprites:
                  entity.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()

      pygame.display.update()
      FramePerSec.tick(FPS)

      
