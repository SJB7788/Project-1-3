from winsound import PlaySound
import pygame
from sys import exit
pygame.init()

#screen/window
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tutorial")
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pygame 2nd Project/font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('Pygame 2nd Project/graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('Pygame 2nd Project/graphics/ground.png').convert_alpha()

score_surface = test_font.render("TEST", False, (64, 64, 64))
score_rect = score_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load('Pygame 2nd Project/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (700, 300))

player_surface = pygame.image.load('Pygame 2nd Project/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        """if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                print("collision")"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('Jump')

        if event.type == pygame.KEYUP:
            print('key up')
            

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    screen.blit(score_surface, score_rect)

    snail_rect.left -= 5
    if snail_rect.right < 0:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    player_rect.left += 1
    screen.blit(player_surface, player_rect)

    """if player_rect.colliderect(snail_rect):
        print("collision")"""

    """mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())"""

    pygame.display.update()
    clock.tick(60)