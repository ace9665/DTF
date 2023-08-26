#Importing_Modules
import pygame
from sys import exit
from Player import Player
from assets import Enemy

#Initialising_Pygame
pygame.init()
clock=pygame.time.Clock()



#Variables
surf_ground=pygame.Surface([1368,22])
screen=pygame.display.set_mode((1368,700))

player=pygame.sprite.GroupSingle()
player.add(Player())
enemy=pygame.sprite.GroupSingle()
enemy.add(Enemy())
#Game_Loop
while True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    surf_ground.fill("#4A4A4A")
    screen.fill("#9B9B9B")
    screen.blit(surf_ground, (0, 550))
    player.draw(screen)
    enemy.draw(screen)
    player.update()




    #Updating_screen_after_every_frame
    pygame.display.update()
    #Fps_Count
    clock.tick(60)