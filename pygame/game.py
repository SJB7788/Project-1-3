import pygame
import os

WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test")

FPS = 60
SPEED = 10

SKYBLUE = (3, 171, 255)
PACMAN_SIZE = 55
# adding the pacman image
PACMAN1_IMAGE = pygame.image.load('Pygame/assets/pacman.png')
PACMAN1 = pygame.transform.scale(PACMAN1_IMAGE, (PACMAN_SIZE, PACMAN_SIZE)) #change the width and the height of pacman

PACMAN2_IMAGE = pygame.image.load('Pygame/assets/pacman 2.png')
PACMAN2 = pygame.transform.rotate(pygame.transform.scale(PACMAN2_IMAGE, (PACMAN_SIZE, PACMAN_SIZE)), 180)

# PACMAN 1 Controls
def pacman1_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_w]: #UP
        red.y -= SPEED
    if keys_pressed[pygame.K_s]: #DOWN
        red.y += SPEED
    if keys_pressed[pygame.K_a]: #LEFT
        red.x -= SPEED
    if keys_pressed[pygame.K_d]: #RIGHT
        red.x += SPEED
# PACMAN 2 Controls
def pacman2_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_UP]: #UP
        yellow.y -= SPEED
    if keys_pressed[pygame.K_DOWN]: #DOWN
        yellow.y += SPEED
    if keys_pressed[pygame.K_LEFT]: #LEFT
        yellow.x -= SPEED
    if keys_pressed[pygame.K_RIGHT]: #RIGHT
        yellow.x += SPEED
# Window Stuff
def window_custom(red, yellow):
    WIN.fill(SKYBLUE)
    WIN.blit(PACMAN1, (red.x, red.y))
    WIN.blit(PACMAN2, (yellow.x, yellow.y))
    pygame.display.update()

def main():
    red = pygame.Rect(50, 300, PACMAN_SIZE, PACMAN_SIZE)
    yellow = pygame.Rect(900, 300, PACMAN_SIZE, PACMAN_SIZE)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) #game is capped at 60FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        pacman1_handle_movement(keys_pressed, red)
        pacman2_handle_movement(keys_pressed, yellow)
        window_custom(red, yellow)
    pygame.quit()

if __name__ == '__main__':
    main()