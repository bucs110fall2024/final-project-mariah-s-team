import pygame
class Cars(pygame.sprite.Sprite): 
    def __init__(self, number): 
        super().__init__()
        if number == 1:
            self.x = 198
            self.image = pygame.image.load(f"/assets/{car2}.png")
            self.speed = -4
        else:
            self.x = 460
            self.image = pygame.image.load(f"/assets/{car1}.png")
            self.speed = 4
        
        self.y = height / 2 
        self.width = 100
        self.height = 150
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.size = 'small'

    def update(self):
        self.rect.center = (self.x, self.y)
        self.y += self.speed
        
        if self.y - self.height / 2 < 0:
            self.y = self.height / 2
            self.speed *= -1
        elif self.y + self.height / 2 > 0: 
            self.y = height - self.height / 2 
            self.speed *= -1
    
