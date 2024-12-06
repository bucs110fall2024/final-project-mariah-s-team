# import pygame

# class Car(pygame.sprite.Sprite):
#     def __init__(self, number, width, height):
#         super().__init__()
#         self.width = width
#         self.height = height

#         if number == 1:
#             self.x = 190
#             self.image = pygame.image.load("assets/car2.png")
#             self.speed = -4
#         else:
#             self.x = 460
#             self.image = pygame.image.load("assets/car1.png")
#             self.speed = 4

#         self.y = height / 2
#         self.image = pygame.transform.scale(self.image, (100, 150))
#         self.rect = self.image.get_rect()
#         self.mask = pygame.mask.from_surface(self.image)

#     def update(self):
#         self.movement()
#         self.rect.center = (self.x, self.y)

#     def movement(self):
#         self.y += self.speed

#         if self.y - self.height / 2 < 0:
#             self.y = self.height / 2
#             self.speed *= -1
#         elif self.y + self.height / 2 > self.height:
#             self.y = self.height - self.height / 2
#             self.speed *= -1

