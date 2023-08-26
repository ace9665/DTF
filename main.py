#Importing_Modules
import pygame
from sys import exit

#Initialising_Pygame
pygame.init()
clock=pygame.time.Clock()

#Variables
surf_ground=pygame.Surface([1368,20])
screen=pygame.display.set_mode((1368,700))
screen.fill("#9B9B9B")
#Game_Loop
while True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    surf_ground.fill("#4A4A4A")
    screen.blit(surf_ground,(0,550))

    pygame.display.update()
    clock.tick(60)