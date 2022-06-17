from pydoc import describe
import random
from re import X
from secrets import choice
from tkinter import EventType
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

obstacle_pos = 660
player_speed = 10

player_x = 600
player_y = 700
player_bullet_x = player_x

class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #Enemy
        hamza_1 = pygame.image.load('test/assets/hamza intensifies.png').convert_alpha() #dont forgte to cahnge it
        hamza_2 = pygame.image.load('test/assets/hamza intensifies 2.png').convert_alpha()
        hamza_1 = pygame.transform.scale(hamza_1, (146, 123))
        hamza_2 = pygame.transform.scale(hamza_2, (146, 123))
        self.frames = [hamza_1, hamza_2]
        self.animation_index = 0

        self.image = self.frames[self.animation_index]
        self.image_r = self.image.get_rect()
        self.rect = self.image.get_rect(midbottom = (600, 150))
        

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    
    def phase_1(self):
        #Hamza movement
        global enemySPD, obstacle_pos
        if self.rect.x <= 100:
            enemySPD = enemySPD * -1
            self.rect.x += enemySPD
        if self.rect.x >= 1000:
            enemySPD = enemySPD * -1
            self.rect.x += enemySPD
        else: 
            self.rect.x += enemySPD
            obstacle_pos = self.rect.x + 60

    def update(self):
        self.phase_1()
        self.animation_state()

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #Enemy
        bullet = pygame.image.load('test/assets/pewpew.jpg').convert_alpha()
        bullet = pygame.transform.scale(bullet, (50, 20))

        self.image = pygame.transform.rotate(bullet, 90)
        self.rect = self.image.get_rect(midbottom = (obstacle_pos, 200))

    def destroy(self):
        if self.rect.y >= 850:
            self.kill()
        
    def update(self):
        self.rect.y += 10
        self.destroy()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #player image
        xerath = pygame.image.load('test/assets/xerath.png')
        xerath_2 = pygame.image.load('test/assets/xerath 2.png')
        xerath = pygame.transform.rotate(xerath, 180)
        xerath_2 = pygame.transform.rotate(xerath_2, 180)
        xerath = pygame.transform.scale(xerath, (60, 100))
        xerath_2 = pygame.transform.scale(xerath_2, (60, 100))
        
        self.frames = [xerath, xerath_2]
        self.animation_index = 0

        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (600, 700))
        
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    
    def controls(self):
        global player_speed
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.rect.y >= 0: #up
            self.rect.y -= player_speed

        if keys[pygame.K_s] and self.rect.y <= 610: #down
            self.rect.y += player_speed
            
        if keys[pygame.K_d] and self.rect.x <= 1090: #right
            self.rect.x += player_speed
                
        if keys[pygame.K_a] and self.rect.x >= 0: #left
            self.rect.x -= player_speed


    def update(self):
        global player_x, player_y
        self.animation_state()
        self.controls()
        player_x = self.rect.x
        player_y = self.rect.y

class Player_bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bullet = pygame.image.load('test/assets/pewpew player.png')
        bullet = pygame.transform.scale(bullet, (50, 20))
        bullet = pygame.transform.rotate(bullet, 90)

        self.image = bullet
        self.image_r = self.image.get_rect()
        self.rect = self.image.get_rect(midbottom = (player_x + 30, 650))

    def destroy(self):
        col = self.rect.colliderect(ob.image_r)
        print(col)
    
    def update(self):
        self.destroy()
        self.rect.y -= 20



obstacle_group = pygame.sprite.Group()
obstacle_group.add(Obstacles())

player_group = pygame.sprite.Group()
player_group.add(Player())

p_bullet = Player_bullet()
ob = Obstacles()

sprite = pygame.sprite.Group()


game_active = True

#timer
bullet_timer = pygame.USEREVENT +1
pygame.time.set_timer(bullet_timer, 400)

player_bullet_timer = pygame.USEREVENT + 2
pygame.time.set_timer(player_bullet_timer, 800)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == bullet_timer:
            obstacle_group.add(Bullet())
        
        if event.type == player_bullet_timer:
            player_group.add(Player_bullet())
    
    if game_active:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 1200, 800))

        obstacle_group.draw(screen)
        obstacle_group.update()

        player_group.draw(screen)
        player_group.update()

        for player_group in pygame.sprite.groupcollide(obstacle_group, player_group, False, False):
            print(True)

    pygame.display.update()
    clock.tick(60)