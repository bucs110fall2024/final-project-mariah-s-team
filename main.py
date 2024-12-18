import pygame
#from src.controller import Controller

width = 640
height = 480

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
         self.mask = pygame.mask.from_surface(self.image)

    def update(self):
         self.movement()
         self.correction()
         self.checkCollision()
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
            
    def checkCollision(self):
        car_check = pygame.sprite.spritecollide(self, car_group, False, pygame.sprite.collide_mask)
        if car_check:
            window.fill((0, 0, 0))
            font = pygame.font.SysFont(None, 35)
            text = font.render("You Lose: Try Again Next Time!", True, (255, 0, 0))
            window.blit(text, (170, 230))
            
                     
            
class Car(pygame.sprite.Sprite):
    def __init__(self, number): 
        super().__init__()
        if number == 1:
            self.x = 190
            self.image = pygame.image.load("assets/car2.png")
            self.speed = -4
        else:
            self.x = 460
            self.image = pygame.image.load("assets/car1.png")
            self.speed = 4
        
        self.y = height / 2 
        self.width = 100
        self.height = 150
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.size = 'small'
        self.mask = pygame.mask.from_surface(self.image)
        
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
        #collision = pygame.sprite.spritecollideany(self, player_group)
#         #while collision:
#            # False

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
        self.rect.topleft = (self.x, self.y)

class Flag(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/green flag.png')
        self.visable = True
        self.x = 580
        
        self.y = height / 2
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self):
        if self.visable:
            self.collision() 
            self.rect.center = (self.x, self.y)
            
    def collision(self):
        global SCORE, player
        flag_hit = pygame.sprite.spritecollide(self, player_group, False, pygame.sprite.collide_mask)
        if flag_hit: 
            window.fill('blue')
            font = pygame.font.SysFont(None, 55)
            text = font.render("You Win! Great Job!", True, ('pink'))
            window.blit(text, (170, 230))
            pygame.display.flip()
            clock.tick(60)
            
        

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

green_flag = Flag()
flag_group = pygame.sprite.Group()
flag_group.add(green_flag)
flags = [green_flag]



# #def mainloop(self):
   
running = True 
while running: 
   
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
           running = False 
    screen_group.draw(window)
    
    
    car_group.draw(window)
    player_group.draw(window)
    flag_group.draw(window)
    
    
    car_group.update()
    player_group.update()
    flag_group.update()
    
    screen_group.update()
    
    pygame.display.update()
    
pygame.quit()

#import pygame
#from controller import GameController

# Game setup
# width = 640
# height = 480
# pygame.init()

# window = pygame.display.set_mode((width, height))
# pygame.display.set_caption('Chicken Crossing: Will the Chicken Make it to the Other Side of the Road?')

# # Initialize the game controller
# controller = Controller(width, height, window)

# # Start the game
# controller.start()
