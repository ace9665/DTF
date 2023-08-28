#Importing_Variables
import pygame
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
#Loading all images
    # Loading_Right_walk_frames
        walk_right1 = pygame.transform.rotozoom(pygame.image.load("assets/enemy/enemyRwalk1.png"), 0, 1.1)
        walk_right2 = pygame.transform.rotozoom(pygame.image.load("assets/enemy/enemyRwalk2.png"), 0, 1.1)
        walk_right3 = pygame.transform.rotozoom(pygame.image.load("assets/enemy/enemyRwalk3.png"), 0, 1.1)
    # Loading_Left_walk_frames
        walk_left1 = pygame.transform.rotozoom(pygame.image.load("assets/enemy/enemyLwalk1.png"), 0, 1.1)
        walk_left2 = pygame.transform.rotozoom(pygame.image.load("assets/enemy/enemyLwalk2.png"), 0, 1.1)
        walk_left3 = pygame.transform.rotozoom(pygame.image.load("assets/enemy/enemyLwalk3.png"), 0, 1.1)

        self.image=pygame.image.load("assets/enemy/enemyRwalk1.png")
        self.image=pygame.transform.rotozoom(self.image,0,1.1)
        self.rect=self.image.get_rect(center=(randint(0,1368),475))
        self.index=0
        self.walkR = [walk_right1, walk_right2, walk_right3]  # list of all right walk frames
        self.walkL = [walk_left1, walk_left2, walk_left3]  # list of all left walk frames
#Defines_enemy_movement
    def enemy_movement(self):
        if self.rect.x==self.rect.x+2:
            self.index+=0.15
            if self.index>=len(self.walkR): self.index=0
            self.walkR[int(self.index)]
        elif self.rect.x== self.rect.x-2:
            self.index += 0.15
            if self.index >= len(self.walkL): self.index = 0
            self.walkL[int(self.index)]

#Update method to update all methods inside the game
    def update(self):
        self.enemy_movement()
        self.enemy_ai()

    def enemy_ai(self):
        if randint(0,2):
            self.rect.x=self.rect.x+2
        else:
            self.rect.x=self.rect.x-2