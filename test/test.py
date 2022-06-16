from time import time
import pygame
import random
pygame.font.init()
pygame.mixer.init()


WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test")

#COLORS
WHITE = (255, 255, 255)
DARKBLUE = (9, 23, 90)

FPS = 60

BACKGROUND = pygame.Rect((0,0), (1000, 600))
ENEMY = pygame.Rect(WIDTH/2 - 10, 100, 20, 20)
ENEMY_vel = 10

def window_settings():
    pygame.draw.rect(WIN, DARKBLUE, BACKGROUND)
    pygame.draw.rect(WIN, WHITE, ENEMY)
    
    pygame.display.update()


movement = [0, 1]

def enemy(counter):
    global ENEMY_vel
    ENEMY.x += ENEMY_vel
    if ENEMY.x - ENEMY.width < 0 or ENEMY.x + ENEMY.width > WIDTH:
        ENEMY_vel *= -1
    
        

def enemy_phase1():
    pass

def main():
    enemy_gun_box1 = pygame.Rect(0, 0, 50, 50)
    enemy_gun_box2 = pygame.Rect(100, 100, 50, 50)
    enemy_gun_box3 = pygame.Rect(200, 200, 50, 50)
    enemy_gun_box4 = pygame.Rect(300,300, 50, 50)
    enemy_gun_box5 = pygame.Rect(400, 400, 50, 50)
    enemy_gun_box6 = pygame.Rect(500, 500, 50, 50)
    enemy_gun_box7 = pygame.Rect(600, 600, 50, 50)
    enemy_gun_box8 = pygame.Rect(700, 700, 50, 50)
    enemy_gun_box9 = pygame.Rect(800, 800, 50, 50)
    enemy_gun_box10 = pygame.Rect(900, 900, 50, 50)
    enemy_gun_box11 = pygame.Rect(1000, 1000, 50, 50)

    clock = pygame.time.Clock()
    run = True
    
    #timer to count time
    time_delay = 1000
    timer_event = pygame.USEREVENT+1
    counter = 0
    pygame.time.set_timer(timer_event, time_delay)
  
    while run:
        clock.tick(FPS) #game is capped at 60FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == timer_event:
                counter += 1
                if counter % 2 == 0:
                    bullet1 = pygame.Rect()
                if counter % 2 == 1:
                    pass
        
        
        enemy(counter)
        window_settings()
     
main()
