import pygame
#import os
#import pygame_menu
#from src.player import Player
#from src.controller import Controller
#import your controller
#width = 640
#height = 480

class Player(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        
        self.x = 50
        self.y = height / 2
        self.size = 'small'
        self.speed = 5
        self.width = 100
        self.height = 50
        
        self.player = pygame.image.load("assets/player.png")
        self.player = pygame.transform.scale(self.player, (self.width, self.height))
        self.image = self.player
        self.rect = self.image.get_rect()

    def update(self):
        self.movement()
        self.correction()
        self.rect.center = (self.x, self.y)
        keys = pygame.key.get_pressed()
        
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed 
        elif keys[pygame.K_RIGHT]:
            self.x += self.speed
        elif keys[pygame.K_UP]:
            self.y -= self.speed
        elif keys[pygame.K_DOWN]:
            self.y += self.speed
    def correction(self):
        if self.x - self.width / 2 < 0:
            self.x = self.width / 2 
        elif self.x + self.width / 2 > width:
            self.x = width - self.width / 2 #****
        elif self.y - self.height / 2 < 0:
            self.y = self.height / 2 
        elif self.y + self.height / 2 > height:
            self.y = height - self.height / 2
            
class Car(pygame.sprite.Sprite):
    def __init__(self, number): 
        super().__init__()
        if number == 1:
            self.x = 198
            self.image = pygame.image.load("assets/car1.png")
            self.speed = -4
        else:
            self.x = 460
            self.image = pygame.image.load("assets/car2.png")
            self.speed = 4
        
        self.y = height / 2 
        self.width = 100
        self.height = 150
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.size = 'small'
        
    def update(self):
        self.movement()
        self.rect.center = (self.x, self.y)
    def movement(self):
        self.y += self.speed
        
        if self.y - self.height / 2 < 0:
            self.y = self.height / 2
            self.speed *= -1
        elif self.y + self.height / 2 > height: 
            self.y = height - self.height / 2
            self.speed *= -1

class Screen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load('assets/Scene.png')
        self.img = pygame.transform.scale(self.img, (width, height))
        
        self.image = self.img 
        self.x = 0
        self.y = 0
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.topeleft = (self.x, self.y)

width = 640
height = 480

pygame.init()


window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Chicken Crossing: Will the Chicken Make it to the Other Side of the Road?')
clock = pygame.time.Clock()

bg = Screen()
screen_group = pygame.sprite.Group()
screen_group.add(bg)

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

car1 = Car(1)
car2 = Car(2)
car_group = pygame.sprite.Group()
car_group.add(car1, car2)
#def mainloop(self):
   
running = True 
while running: 
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
          running = False 
    screen_group.draw(window)
    
    player_group.draw(window)
    car_group.draw(window)
    player_group.update()
    car_group.update()
    screen_group.update()
    pygame.display.update()
    
pygame.quit()
   
    

      
pygame.quit()

#def main():
    
    #pygame.init()
    
   # controller = Controller()
    #controller.mainloop()
    
    #running = True
    #while running: 
      #  for event in pygame.event.get():
        #    if event.type == pygame.QUIT:
              #  running = False
        #window.fill((0, 255, 0))    
        #pygame.display.update()
          
    #pygame.quit()
        



        # show display
    
#main()
