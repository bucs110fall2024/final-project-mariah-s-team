import pygame
import os
import pygame_menu
from controller import Controller
#import your controller
class Main(pygame.sprite.Sprite):
    width = 640
    height = 480
    def main():
        controller = Controller()
        controller.main.loop()
    
    
if __name__ == '__main__':
    Main()
