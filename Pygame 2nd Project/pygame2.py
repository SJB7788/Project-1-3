import random
from secrets import choice
import pygame
from sys import exit
from random import randint
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('Pygame 2nd Project/graphics/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('Pygame 2nd Project/graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('Pygame 2nd Project/graphics/Player/jump.png')

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (100, 300))
        self.gravity = 0
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
    
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()
        
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'fly':
            fly_1 = pygame.image.load('Pygame 2nd Project/graphics/Fly/Fly1.png').convert_alpha()
            fly_2 = pygame.image.load('Pygame 2nd Project/graphics/Fly/Fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210

        else:
            snail_1 = pygame.image.load('Pygame 2nd Project/graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('Pygame 2nd Project/graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (random.randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    
    def update(self):
        self.animation_state()
        self.rect.x -= OB_SPEED
        self.destory()
    
    def destory(self):
        if self.rect.x <= -100:
            self.kill()

def display_score():
    time = int(pygame.time.get_ticks()/1000) - int(start_time/1000)
    score_surf = test_font.render(f'Score: {time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (WIDTH/2, 50))
    screen.blit(score_surf, score_rect)
    return time

"""def obstacle_movement(obstacle_list):
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
"""
def collisions():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True

def player_animation():
    global player_surface, player_index

    if player_rect.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]
        
#screen/window
WIDTH = 800
HEIGHT = 400
OB_SPEED = 6
SCORE_TALLY = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snail Jump")
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pygame 2nd Project/font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load('Pygame 2nd Project/graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('Pygame 2nd Project/graphics/ground.png').convert_alpha()

# Enemy
snail_frame_1 = pygame.image.load('Pygame 2nd Project/graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('Pygame 2nd Project/graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

fly_frame_1 = pygame.image.load('Pygame 2nd Project/graphics/Fly/Fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('Pygame 2nd Project/graphics/Fly/Fly2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

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

game_message = test_font.render('Press S to play', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 300))

obstacle_rate = 1200

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, obstacle_rate)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 300)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

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
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
                
            """if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]
            
            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]"""
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and game_active == False:
                    game_active = True
                    start_time = pygame.time.get_ticks()

    # game
    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()

        if int(score) >= SCORE_TALLY:
            OB_SPEED += 10
            SCORE_TALLY += 10
            if SCORE_TALLY == 20:
                pygame.time.set_timer(obstacle_timer, 1100)
            if SCORE_TALLY == 50:
                pygame.time.set_timer(obstacle_timer, 800)
            if SCORE_TALLY == 60:
                OB_SPEED = 6
            if SCORE_TALLY == 100:
                break

        #sprites
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()        

        game_active = collisions()

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

        OB_SPEED = 6
        SCORE_TALLY = 10

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message,score_message_rect)


    pygame.display.update()
    clock.tick(60)