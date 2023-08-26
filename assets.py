#Importing_Variables
import pygame
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("assets/enemy/enemy.png")
        self.image=pygame.transform.rotozoom(self.image,0,10)
        self.rect=self.image.get_rect(center=(randint(0,1368),475))

