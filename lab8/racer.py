#Imports
import pygame
import sys
import random
import time
from pygame.locals import *

# Initialization
pygame.init()

done = False

# Settings up FPS
FPS = 60
FramePerSec = pygame.time.Clock()


# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other variables use for this program
WIDTH = 400
HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0


# Settings up fonts
font = pygame.font.SysFont('Verdana', 60)
font_small = pygame.font.SysFont('Verdana', 20)
game_over = font.render('Game over', True, BLACK)

background = pygame.image.load('media/AnimatedStreet.png')

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('media/mentcar.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('media/porshe1.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160, 500)

    def move(self):
        press_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if press_keys[K_LEFT]:
                self.rect.move_ip(-7, 0)
        if self.rect.right < WIDTH:
            if press_keys[K_RIGHT]:
                self.rect.move_ip(7, 0)

    def collect_coin(self, coins):
        collisions = pygame.sprite.spritecollide(self, coins, True)
        for coin in collisions:
            return True
        return False



class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("media/free-icon-dollar-coin-9787486.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)

#Setting up sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

#crating sprites group
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    DISPLAYSURF.blit(background, (0, 0))
    coin_scores = font_small.render(str(COIN_SCORE), True, BLACK)
    DISPLAYSURF.blit(coin_scores, (370, 8))
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    if P1.collect_coin(coins):
        COIN_SCORE += 1
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('media/crash.wav').play()
        time.sleep(0.5)


        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    pygame.display.update()
    FramePerSec.tick(FPS)