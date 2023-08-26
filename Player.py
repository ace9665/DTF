import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("assets/player/sMan1.png")
        self.image=pygame.transform.rotozoom(self.image,0,10)
        self.rect=self.image.get_rect(center=(684,475))

    def player_input(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x+=2
        elif keys[pygame.K_LEFT]:
            self.rect.x-=2

    def update(self):
        self.player_input()