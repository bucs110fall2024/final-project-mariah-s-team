# #import pygame

# #class Flag(pygame.sprite.Sprite):
#     #def __init__(self, width, height, player_group):
#         super().__init__()
#         self.width = width
#         self.height = height

#         self.image = pygame.image.load('assets/green flag.png')
#         self.visible = True
#         self.x = 580
#         self.y = height / 2
#         self.image = pygame.transform.scale(self.image, (50, 100))  # Scale to fit
#         self.rect = self.image.get_rect()
#         self.mask = pygame.mask.from_surface(self.image)
        
#         self.player_group = player_group

#     def update(self):
#         if self.visible:
#             self.collision()
#             self.rect.center = (self.x, self.y)

#     def collision(self):
#         flag_hit = pygame.sprite.spritecollide(self, self.player_group, False, pygame.sprite.collide_mask)
#         if flag_hit:
#             window.fill('blue')
#             font = pygame.font.SysFont(None, 55)
#             text = font.render("You Win! Great Job!", True, ('pink'))
#             window.blit(text, (170, 230))
#             pygame.display.flip()
#             clock.tick(60)
