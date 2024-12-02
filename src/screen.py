class Screen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img1 = pygame.image.load(f"/assets/{Scene}.png")
        #self.img2 = pygame.image.load(f"/assets/{You_Lose}.png")
        
        self.img1 = pygame.transform.scale(self.img1, (width, height))
        #self.img2 = pygame.transform.scale(self.img2, (width, height))
        self.image = self.img1
        self.x = 0
        self.y = 0
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.topleft = (self.x, self.y)
        
    def event(self): 
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False