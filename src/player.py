#Rectangle: w, h, pos 
#surface: contains rect, has image
import pygame
import os
height = 480
width = 640
class Player(pygame.sprite.Sprite): 
    def __init__(self,name):
        super().__init__()
        
        self.x = 50
        self.y = height / 2
        self.size = 'small'
        self.width = 100
        self.height = 50
        self.speed = 4
        self.player = pygame.image.load(os.path.join('assets', 'car1.png')).convert()
        self.player = pygame.transform.scale(self.player, self.width, self.height)
        self.image = self.player
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = (self.x, self.y)
        keys = pygame.key.get_pressed()

        #if keys[pygame.K_LEFT]:
            #self.rect.x -= self.speed 
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_UP]:
            self.rect.y -= self.speed
        elif keys[pygame.K_DOWN]:
            self.rect.y += self.speed
    def draw(self):
        pygame.time.Clock.tick(60)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
    def correction(self):
        if self.x - self.width / 2 < 0:
            self.x = self.width / 2 
        elif self.x + self.width / 2 > width:
            self.x = width - self.width / 2
        elif self.y - self.height / 2 < 0:
            self.y = self.height / 2 
        elif self.y + self.height / 2 > height:
            self.y = height - self.height / 2
            
        Player.update()



        
