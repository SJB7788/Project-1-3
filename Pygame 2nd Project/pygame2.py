import pygame
from sys import exit
pygame.init()

#screen/window
WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tutorial")
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 200))
test_surface.fill('Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(test_surface, (0, 0))

    pygame.display.update()
    clock.tick(60)