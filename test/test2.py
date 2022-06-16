import random
from re import X
from secrets import choice
import pygame
from sys import exit
from random import randint
pygame.init()

WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test")

clock = pygame.time.Clock()
enemySPD = 5
bullet_location = 6

bullet_x = 630
bullet_y = 200

class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #Enemy
        hamza_1 = pygame.image.load('assets/hamza intensifies.png').convert_alpha() #dont forgte to cahnge it
        hamza_2 = pygame.image.load('assets/hamza intensifies 2.png').convert_alpha()
        hamza_1 = pygame.transform.scale(hamza_1, (146, 123))
        hamza_2 = pygame.transform.scale(hamza_2, (146, 123))
        self.frames = [hamza_1, hamza_2]
        self.animation_index = 0

        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (600, 150))
        

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    
    def phase_1(self):
        #Hamza movement
        global enemySPD
        if self.rect.x <= 100:
            enemySPD = enemySPD * -1
            self.rect.x += enemySPD
        if self.rect.x >= 1000:
            enemySPD = enemySPD * -1
            self.rect.x += enemySPD
        else: 
            self.rect.x += enemySPD

    def update(self):
        self.phase_1()
        self.animation_state()

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #Enemy
        bullet = pygame.image.load('assets/pewpew.jpg').convert_alpha()
        bullet = pygame.transform.scale(bullet, (50, 20))

        self.image = pygame.transform.rotate(bullet, 90)
        self.rect = self.image.get_rect(midbottom = (bullet_x, bullet_y))

    def location(self):
        #Hamza movement
        global bullet_location, bullet_x
        if bullet_x <= 200:
            bullet_location *= -1
            bullet_x = bullet_x + 100
            print(bullet_x)
        if bullet_x >= 1100:
            bullet_location *= -1
            bullet_x = bullet_x - 170
            print(bullet_x)
        else: 
            bullet_x += bullet_location

    def destroy(self):
        if self.rect.y >= 850:
            self.kill()
        
    def update(self):
        self.location()
        self.rect.y += 20
        self.destroy()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #player image
        

obstacle_group = pygame.sprite.Group()
obstacle_group.add(Obstacles(), Bullet())

game_active = True

#timer
bullet_timer = pygame.USEREVENT +1
pygame.time.set_timer(bullet_timer, 800)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == bullet_timer:
            obstacle_group.add(Bullet())
    
    if game_active:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 1200, 800))
        
        obstacle_group.draw(screen)
        obstacle_group.update()
    """bullet_group.draw(screen)
    bullet_group.update()
"""
    pygame.display.update()
    clock.tick(60)