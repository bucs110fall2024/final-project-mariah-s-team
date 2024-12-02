import pygame 
import pygame_menu
from src.player import Player
from src.cars import Cars
#from src.redcar import RedCar
from src.screen import Screen
width = 640
height = 480

class Controller(pygame.sprite.Sprite):
 
  def __init__(self, name):
    self.player = Player()
    self.cars = Cars()
    self.screen = Screen()
    
    #bg = Screen()

    #setup pygame data
    
  def mainloop(self):
    
    running = True
    while running: 
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
    Screen.fill((0, 255, 0))
  
  ### below are some sample loop states ###

  def menuloop(self):
    start = True
    while start:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()
      Screen.fill('white')
      largeText = pygame.font.Font('freesanbold.ttf', 115)
      TextSurf, TextRect = ("Chicken Crossing: Will the Chicken Make it to the Other Side of the Road?", largeText)
      TextRect.center = ((width/2), (height/2))
      Screen.bilt(TextSurf, TextRect)
      pygame.display.update()
      pygame.time.Clock.tick(15)
      #event loop

      #update data

      #redraw
      
  def gameloop(self):

    #window_width = 640
    #window_height = 480
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Chicken Crossing: Will the chicken make it to the other side?')
    self.background_image = pygame.image.load(f"/assets/Scene.png").convert()
    clock = pygame.time.Clock() 
    
    run = True
    while run:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
  
      screen.fill((0, 255, 0))
      pygame.display.update()
      pygame.quit()

  #def mad():
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
    #if pygame.sprite.spritecollide(player, cars, False):
      #print("You Lost!")
          
    #self.screen.fill('black') 
      #game_over_text = font.render("Game Over", True, red)
    #pygame.display.flip()

    font = pygame.font.Font(None, 74)
    Screen.fill('black') 
    game_over_text = font.render("Game Over", True, 'red')
    Screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - game_over_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)

# Function to display play again button
  def play_again_button():
    font = pygame.font.Font(None, 74)
    button_rect = pygame.Rect(width // 2 - 100, height // 2 + 50, 200, 50)
    pygame.draw.rect(Screen, 'white', button_rect)
    button_text = font.render("Play Again", True, 'black')
    Screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))
    pygame.display.flip()
    return button_rect
  
    running = True
    game_over = False
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
          if play_again_button().collidepoint(event.pos):
            game_over = False
      #event loop

      #update data

      #redraw
pygame.quit()