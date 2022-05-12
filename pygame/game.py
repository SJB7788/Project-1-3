import pygame
import os
pygame.font.init()

WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman Shooter")

FPS = 60
SPEED = 10
BULLET_SPEED = 15
AMMO_AMT = 5

BACKGROUND_COLOR = (42, 32, 127)
SKYBLUE = (3, 171, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255,255,0)

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 15, HEIGHT)

PAC_FONT = pygame.font.Font('Pygame/assets/crackman.ttf', 20)

PACMAN_SIZE = 55
RED_HIT = pygame.USEREVENT + 1
YELLOW_HIT = pygame.USEREVENT + 2

# adding the pacman image
PACMAN1_IMAGE = pygame.image.load('Pygame/assets/pacman.png')
PACMAN1 = pygame.transform.scale(PACMAN1_IMAGE, (PACMAN_SIZE, PACMAN_SIZE)) #change the width and the height of pacman

PACMAN2_IMAGE = pygame.image.load('Pygame/assets/pacman 2.png')
PACMAN2 = pygame.transform.rotate(pygame.transform.scale(PACMAN2_IMAGE, (PACMAN_SIZE, PACMAN_SIZE)), 180)

BACKGROUND_IMG = pygame.image.load('Pygame/assets/pacman background.png')
# Window Stuff
def window_custom(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(BACKGROUND_IMG, (0,0))
    pygame.draw.rect(WIN, BACKGROUND_COLOR, BORDER)

    red_health_text = PAC_FONT.render("HEALTH: " + str(red_health), 1, WHITE)
    yellow_health_text = PAC_FONT.render("HEALTH: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (20, 15))
    WIN.blit(yellow_health_text, (WIDTH - red_health_text.get_width() - 20, 15))

    WIN.blit(PACMAN1, (red.x, red.y))
    WIN.blit(PACMAN2, (yellow.x, yellow.y))   

    for bullet in red_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, WHITE, bullet)

    pygame.display.update()

# PACMAN 1 Controls
def pacman1_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_w] and red.y > 20: #UP
        red.y -= SPEED
    if keys_pressed[pygame.K_s] and red.y + red.height + SPEED < HEIGHT - 15: #DOWN
        red.y += SPEED
    if keys_pressed[pygame.K_a] and red.x - SPEED > 10: #LEFT
        red.x -= SPEED
    if keys_pressed[pygame.K_d] and red.x + red.width + SPEED < BORDER.x - 5: #RIGHT
        red.x += SPEED
# PACMAN 2 Controls
def pacman2_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_UP] and yellow.y > 20: #UP
        yellow.y -= SPEED
    if keys_pressed[pygame.K_DOWN] and yellow.y + yellow.height + SPEED < HEIGHT - 15: #DOWN
        yellow.y += SPEED
    if keys_pressed[pygame.K_LEFT] and yellow.x - SPEED > BORDER.x + BORDER.width: #LEFT
        yellow.x -= SPEED
    if keys_pressed[pygame.K_RIGHT] and yellow.x + SPEED < WIDTH - PACMAN_SIZE - 10: #RIGHT
        yellow.x += SPEED

def handle_bullets(red_bullets, yellow_bullets, red, yellow):
    for bullet in red_bullets: #moving red bullet
        bullet.x += BULLET_SPEED
        if yellow.colliderect(bullet): # colliding
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x > WIDTH - 50:
            red_bullets.remove(bullet)

    for bullet in yellow_bullets:
        bullet.x -= BULLET_SPEED
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x < 10:
            yellow_bullets.remove(bullet)

def winner():
    pass

def main():
    red = pygame.Rect(50, 300, PACMAN_SIZE, PACMAN_SIZE)
    yellow = pygame.Rect(900, 300, PACMAN_SIZE, PACMAN_SIZE)

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) #game is capped at 60FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN and len(red_bullets) < AMMO_AMT:
                if event.key == pygame.K_j:
                    bullet = pygame.Rect(red.x + red.width, red.y + red.height//2 - 5, 30, 10)
                    red_bullets.append(bullet)

                if event.key == pygame.K_KP1 and len(yellow_bullets) < AMMO_AMT:
                    bullet = pygame.Rect(yellow.x - yellow.width, yellow.y + yellow.height//2 - 5, 30, 10)
                    yellow_bullets.append(bullet)
        
            if event.type == RED_HIT:
                red_health -= 1
    
            if event.type == YELLOW_HIT:
                yellow_health -= 1
        
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"
            winner()
        
        if yellow_health <= 0:
            winner_text = "Red Wins!"
            winner()
        
        if winner_text != "":
            pass # someone won

        keys_pressed = pygame.key.get_pressed()
        pacman1_handle_movement(keys_pressed, red)
        pacman2_handle_movement(keys_pressed, yellow)



        handle_bullets(red_bullets, yellow_bullets, red, yellow)

        window_custom(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    pygame.quit()


if __name__ == '__main__':
    main()