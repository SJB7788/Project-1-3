import pygame
from sys import exit
from random import randint
pygame.init()

def display_score():
    time = int(pygame.time.get_ticks()/1000) - int(start_time/1000)
    score_surf = test_font.render(f'Score: {time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (WIDTH/2, 50))
    screen.blit(score_surf, score_rect)
    return time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 10

            if obstacle_rect.bottom == 300: 
                screen.blit(snail_surface, obstacle_rect)
            else: screen.blit(fly_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        
        return obstacle_list
    else: 
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def player_animation():
    global player_surface, player_index

    if player_rect.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index =    0
        player_surface = player_walk[int(player_index)]
        
#screen/window
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snail Jump")
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pygame 2nd Project/font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('Pygame 2nd Project/graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('Pygame 2nd Project/graphics/ground.png').convert_alpha()

"""score_surface = test_font.render("TEST", False, (64, 64, 64))
score_rect = score_surface.get_rect(center = (400, 50))"""

# Enemy
snail_surface = pygame.image.load('Pygame 2nd Project/graphics/snail/snail1.png').convert_alpha()
fly_surface = pygame.image.load('Pygame 2nd Project/graphics/Fly/Fly1.png').convert_alpha()

obstacle_rect_list = []

player_walk_1 = pygame.image.load('Pygame 2nd Project/graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('Pygame 2nd Project/graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('Pygame 2nd Project/graphics/Player/jump.png')

player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

player_stand = pygame.image.load('Pygame 2nd Project/graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale(player_stand, (108, 124))
player_stand_rect = player_stand.get_rect(center = (400, 200))

game_name = test_font.render('Snail Jump', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 110))

game_message = test_font.render('Press space to play', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 300))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 800)

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
            
            if event.type == obstacle_timer:
                if randint(0, 2):
                    obstacle_rect_list.append(snail_surface.get_rect(midbottom = (randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surface.get_rect(midbottom = (randint(900, 1100), 210)))
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active == False:
                    game_active = True
                    start_time = pygame.time.get_ticks()
        
    
    # game
    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        """pygame.draw.rect(screen, '#c0e8ec', score_rect)
        screen.blit(score_surface, score_rect)"""
        score = display_score()

        #snail/enemy
        """snail_rect.left -= 10
        if snail_rect.right < 0:
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)
"""
        #player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        player_animation()
        screen.blit(player_surface, player_rect)
        
        game_active = collisions(player_rect, obstacle_rect_list)
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

    # game over 
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        score_message = test_font.render(f'Your Score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 330))

        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message,score_message_rect)


    pygame.display.update()
    clock.tick(60)