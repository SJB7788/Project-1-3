import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 1000
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

BORDER = pygame.Rect(0, HEIGHT/2 - 10, WIDTH, 20)

#sound files
BULLET_HIT_SOUND = pygame.mixer.Sound('Pygame/assets/pacman_eatghost.wav')
BULLET_FIRE_SOUND = pygame.mixer.Sound('Pygame/assets/pacman_chomp.mp3')

PAC_FONT = pygame.font.Font('Pygame/assets/crackman.ttf', 20)
WIN_PAC_FONT = pygame.font.Font('Pygame/assets/crackman.ttf', 50)

PACMAN_SIZE = 55
RED_HIT = pygame.USEREVENT + 1
YELLOW_HIT = pygame.USEREVENT + 2

# adding the pacman image
PACMAN1_IMAGE = pygame.image.load('Pygame/assets/pacman.png')
PACMAN1 = pygame.transform.rotate(pygame.transform.scale(PACMAN1_IMAGE, (PACMAN_SIZE, PACMAN_SIZE)), 90) #change the width and the height of pacman

PACMAN2_IMAGE = pygame.image.load('Pygame/assets/pacman 2.png')
PACMAN2 = pygame.transform.rotate(pygame.transform.scale(PACMAN2_IMAGE, (PACMAN_SIZE, PACMAN_SIZE)), 270)

BACKGROUND_IMG = pygame.image.load('Pygame/assets/pacman background.png')

# Window Stuff
def window_custom(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(BACKGROUND_IMG, (0,0))
    pygame.draw.rect(WIN, BACKGROUND_COLOR, BORDER)

    red_health_text = PAC_FONT.render("HEALTH: " + str(red_health), 1, WHITE)
    yellow_health_text = PAC_FONT.render("HEALTH: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 20, HEIGHT/2 + 10))
    WIN.blit(yellow_health_text, (20, 20))

    WIN.blit(PACMAN1, (red.x, red.y))
    WIN.blit(PACMAN2, (yellow.x, yellow.y))   

    for bullet in red_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, WHITE, bullet)

    pygame.display.update()

# PACMAN 1 Controls
def pacman1_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_w] and red.y > HEIGHT/2 + 20: #UP
        red.y -= SPEED
    if keys_pressed[pygame.K_s] and red.y + red.height + SPEED < HEIGHT - 25: #DOWN
        red.y += SPEED
    if keys_pressed[pygame.K_a] and red.x - SPEED > 20: #LEFT
        red.x -= SPEED
    if keys_pressed[pygame.K_d] and red.x + red.width > 0 and red.x < WIDTH - red.width - 25: #RIGHT
        red.x += SPEED
# PACMAN 2 Controls
def pacman2_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_UP] and yellow.y > 35: #UP
        yellow.y -= SPEED
    if keys_pressed[pygame.K_DOWN] and yellow.y + yellow.height < HEIGHT/2 - 15: #DOWN
        yellow.y += SPEED
    if keys_pressed[pygame.K_LEFT] and yellow.x - SPEED > 20: #LEFT
        yellow.x -= SPEED
    if keys_pressed[pygame.K_RIGHT] and yellow.x + yellow.width > 0 and yellow.x < WIDTH - yellow.width - 25: #RIGHT
        yellow.x += SPEED

def handle_bullets(red_bullets, yellow_bullets, red, yellow):
    for bullet in red_bullets: #moving red bullet
        bullet.y -= BULLET_SPEED
        if yellow.colliderect(bullet): # colliding
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.y < 20:
            red_bullets.remove(bullet)

    for bullet in yellow_bullets:
        bullet.y += BULLET_SPEED
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.y > HEIGHT - 30:
            yellow_bullets.remove(bullet)

def winner(text):
    draw_text = WIN_PAC_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(1000)

def main():
    red = pygame.Rect(WIDTH/2 - PACMAN_SIZE/2, HEIGHT - PACMAN_SIZE - 30, PACMAN_SIZE, PACMAN_SIZE)
    yellow = pygame.Rect(WIDTH/2 - PACMAN_SIZE/2, 30, PACMAN_SIZE, PACMAN_SIZE)

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
                    bullet = pygame.Rect(red.x + red.width/2 - 5, red.y + red.height//2 - 5, 10, 30)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_KP1 and len(yellow_bullets) < AMMO_AMT:
                    bullet = pygame.Rect(yellow.x + yellow.width/2 - 5, yellow.y + yellow.height//2 - 5, 10, 30)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
        
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
    
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
        
        winner_text = ""

        if red_health <= 0:
            winner_text = "Gray Wins!"

        if yellow_health <= 0:
            winner_text = "Yellow Wins!"
        
        if winner_text != "":
            winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        pacman1_handle_movement(keys_pressed, red)
        pacman2_handle_movement(keys_pressed, yellow)

        handle_bullets(red_bullets, yellow_bullets, red, yellow)

        window_custom(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    pygame.quit()


if __name__ == '__main__':
    main()