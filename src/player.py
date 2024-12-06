# import pygame

# class Player(pygame.sprite.Sprite):
#     def __init__(self, width, height):
#         super().__init__()

#         self.x = 50
#         self.y = height / 2
#         self.size = 'small'
#         self.speed = 5
#         self.width = 100
#         self.height = 50
        
#         self.player_image = pygame.image.load("assets/player.png")
#         self.player_image = pygame.transform.scale(self.player_image, (self.width, self.height))
#         self.image = self.player_image
#         self.rect = self.image.get_rect()
#         self.mask = pygame.mask.from_surface(self.image)

#     def update(self):
#         self.movement()
#         self.correction()
#         self.rect.center = (self.x, self.y)

#     def movement(self):
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT]:
#             self.x -= self.speed
#         if keys[pygame.K_RIGHT]:
#             self.x += self.speed
#         if keys[pygame.K_UP]:
#             self.y -= self.speed
#         if keys[pygame.K_DOWN]:
#             self.y += self.speed

#     def correction(self):
#         if self.x - self.width / 2 < 0:
#             self.x = self.width / 2
#         elif self.x + self.width / 2 > self.width:
#             self.x = self.width - self.width / 2
#         elif self.y - self.height / 2 < 0:
#             self.y = self.height / 2
#         elif self.y + self.height / 2 > self.height:
#             self.y = self.height - self.height / 2
