import pygame
import time
import sys
import os
#import time
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
        
        try:
            self.player = pygame.image.load("assets/player.png")
            self.player = pygame.transform.scale(self.player, (self.width, self.height))
        except pygame.error as e:
            print("Error loading player image:", e)
            pygame.quit()
            sys.exit()
        
        #self.player = pygame.image.load("assets/player.png")
        #self.player = pygame.transform.scale(self.player, (self.width, self.height))
        self.image = self.player
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.movement()
        self.correction()
        #self.checkCollision()
        self.rect.center = (self.x, self.y)
        #keys = pygame.key.get_pressed()
        
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
    
    
    #game_over = False    
    def checkCollision(self):
        car_check = pygame.sprite.spritecollide(self, car_group, False, pygame.sprite.collide_mask)
        if car_check:
            # Handle collision (e.g., game over)
            return True
        return False
            
            
                     
            
class Car(pygame.sprite.Sprite):
    def __init__(self, number): 
        super().__init__()
        if number == 1:
            self.x = 190
            try:
                self.image = pygame.image.load("assets/car2.png")
            except pygame.error as e:
                print("Error loading car2 image:", e)
                pygame.quit()
                sys.exit()
            self.speed = -4
        else:
            self.x = 460
            try:
                self.image = pygame.image.load("assets/car1.png")
            except pygame.error as e:
                print("Error loading car1 image:", e)
                pygame.quit()
                sys.exit()
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
        #while collision:
           # False

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
        #global SCORE, player
        flag_hit = pygame.sprite.spritecollide(self, player_group, False, pygame.sprite.collide_mask)
        if flag_hit: 
            window.fill('blue')
            font = pygame.font.SysFont(None, 55)
            text = font.render("You Win! Great Job!", True, ('pink'))
            window.blit(text, (170, 230))
            pygame.display.flip()
            clock.tick(60)
            
class Game:
    def __init__(self):
        self.isGameOver = False
        self.isGameWon = False
        
    def checkCollision(self):
        # Check if player collides with any car
        car_check = pygame.sprite.spritecollide(player, car_group, False, pygame.sprite.collide_mask)
        if car_check:
            self.isGameOver = True
        # Check if player reaches the flag
        flag_check = pygame.sprite.spritecollide(player, flag_group, False, pygame.sprite.collide_mask)
        if flag_check:
            self.isGameWon = True

    def displayLoseScreen(self):
        window.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 35)
        text = font.render("You Lose: Try Again Next Time!", True, (255, 0, 0))
        window.blit(text, (170, 230))

    def displayWinScreen(self):
        window.fill('blue')
        font = pygame.font.SysFont(None, 55)
        text = font.render("You Win! Great Job!", True, ('pink'))
        window.blit(text, (170, 230))

    def update(self):
        self.checkCollision()
        if self.isGameOver:
            self.displayLoseScreen()
        elif self.isGameWon:
            self.displayWinScreen()
        else:
            self.updateGame()
            self.renderGame()

    def updateGame(self):
        # Update game elements like cars, player, etc.
        pass

    def renderGame(self):
        # This function can be used for rendering active game elements
        print("Game is running...")




width = 640
height = 480

pygame.init()


window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Chicken Crossing: Will the Chicken Make it to the Other Side of the Road?')
clock = pygame.time.Clock()

bg = Screen()
screen_group = pygame.sprite.Group()
screen_group.add(bg)

game = Game()

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



#def mainloop(self):
   
 #Main Game Loop (unchanged except calling `game.update()`)
# Main Game Loop
running = True
print("Game started")  # Debugging print to ensure game has started
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.update()
    car_group.update()
    player_group.update()
    flag_group.update()
    screen_group.update()

    screen_group.draw(window)
    car_group.draw(window)
    player_group.draw(window)
    flag_group.draw(window)

    pygame.display.update()

    if game.isGameOver or game.isGameWon:
        break

pygame.quit()
sys.exit()

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
