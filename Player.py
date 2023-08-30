import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
#Loading_all_images
    #Walking_Frames
        walk_right1 = pygame.transform.rotozoom(pygame.image.load("assets/player/walk/playerRwalk1.png"),0,1.1)
        walk_right2 = pygame.transform.rotozoom(pygame.image.load("assets/player/walk/playerRwalk2.png"),0,1.1)
        walk_right3 = pygame.transform.rotozoom(pygame.image.load("assets/player/walk/playerRwalk3.png"),0,1.1)
        walk_left1 = pygame.transform.rotozoom(pygame.image.load("assets/player/walk/playerLwalk1.png"),0,1.1)
        walk_left2 = pygame.transform.rotozoom(pygame.image.load("assets/player/walk/playerLwalk2.png"),0,1.1)
        walk_left3 = pygame.transform.rotozoom(pygame.image.load("assets/player/walk/playerLwalk3.png"),0,1.1)
        shoot_right1= pygame.transform.rotozoom(pygame.image.load("assets/player/shoot/playerRshoot1.png"), 0, 1.1)
        shoot_right2= pygame.transform.rotozoom(pygame.image.load("assets/player/shoot/playerRshoot2.png"), 0, 1.1)
        shoot_left1=  pygame.transform.rotozoom(pygame.image.load("assets/player/shoot/playerLshoot1.png"), 0, 1.1)
        shoot_left2=  pygame.transform.rotozoom(pygame.image.load("assets/player/shoot/playerLshoot2.png"), 0, 1.1)
    #Shooting_Frames

        self.i=0
        self.index=0
        self.image=pygame.image.load("assets/player/walk/playerRwalk1.png")
        self.image=pygame.transform.rotozoom(self.image,0,1.1)
        self.rect=self.image.get_rect(center=(684,475))
        self.walk_right = [walk_right1, walk_right2, walk_right3]
        self.walk_left = [walk_left1, walk_left2, walk_left3]
        self.shoot_right=[shoot_right1,shoot_right2]
        self.shoot_left=[shoot_left1,shoot_left2]



    def player_input(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x+=2
        elif keys[pygame.K_LEFT]:
            self.rect.x-=2



    def animation_state(self):
        keys=pygame.key.get_pressed()
        keyup=pygame.KEYUP
        if keys[pygame.K_RIGHT]:
            self.index+=0.15
            if self.index>=len(self.walk_right): self.index=0
            self.image = self.walk_right[int(self.index)]
        elif keys[pygame.K_LEFT]:
            self.index += 0.15
            if self.index >= len(self.walk_left): self.index = 0
            self.image = self.walk_left[int(self.index)]
        if keys[pygame.K_RIGHT] or keyup==pygame.K_RIGHT:
            if keys[pygame.K_SPACE]:
                self.image=self.shoot_right[int(self.i)]






    def update(self):
        self.i+=1
        if self.i >= len(self.shoot_right): self.i = 0
        self.player_input()
        self.animation_state()