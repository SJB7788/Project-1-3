import pygame
from sys import exit
pygame.init()

def display_score():
    time = int(pygame.time.get_ticks()/1000) - int(start_time/1000)
    score_surf = test_font.render(f'Score: {time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (WIDTH/2, 50))
    screen.blit(score_surf, score_rect)

#screen/window
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snail Jump")
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pygame 2nd Project/font/Pixeltype.ttf', 50)
game_active = True
start_time = 0

sky_surface = pygame.image.load('Pygame 2nd Project/graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('Pygame 2nd Project/graphics/ground.png').convert_alpha()

"""score_surface = test_font.render("TEST", False, (64, 64, 64))
score_rect = score_surface.get_rect(center = (400, 50))"""

snail_surface = pygame.image.load('Pygame 2nd Project/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (700, 300))

player_surface = pygame.image.load('Pygame 2nd Project/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

player_stand = pygame.image.load('Pygame 2nd Project/graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale(player_stand, (108, 124))
player_stand_rect = player_stand.get_rect(center = (400, 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN :
                if player_rect.collidepoint(event.pos):
                    player_gravity = - 20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300 :
                    player_gravity = - 20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active == False:
                    game_active = True
                    snail_rect.left = 800
                    start_time = pygame.time.get_ticks()
    
    # game
    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        """pygame.draw.rect(screen, '#c0e8ec', score_rect)
        screen.blit(score_surface, score_rect)"""
        display_score()

        #snail/enemy
        snail_rect.left -= 10
        if snail_rect.right < 0:
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)

        #player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        #collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    # game over 
    else:
        screen.fill((94, 129, 162))
    
        screen.blit(player_stand, player_stand_rect)


    pygame.display.update()
    clock.tick(60)