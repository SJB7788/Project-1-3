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
text_surface = test_font.render("TEST", False, 'Green')

snail_surface = pygame.image.load('Pygame 2nd Project/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (700, 300))

player_surface = pygame.image.load('Pygame 2nd Project/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (5, 5))
    snail_rect.left -= 5
    if snail_rect.right < 0:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    player_rect.left += 1
    screen.blit(player_surface, player_rect)

    pygame.display.update()
    clock.tick(60)