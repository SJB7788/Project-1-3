import pygame
from sys import exit
pygame.init()

#screen/window
WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tutorial")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all out elements
    # update everything
    pygame.display.update()
    clock.tick(60)