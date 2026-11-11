import pygame

#Basic Pygame setup from documentation
pygame.init()
screen = pygame.display.set_mode((512, 512))
clock = pygame.time.Clock()
running = True

while running:
    #Handles the quit game event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((128,0,128)) #Background color

    #Chess board setup
    for row in range(8):
        for col in range(8):
            color = (255,255,255) if (row + col) % 2 == 0 else (0,0,0)
            pygame.draw.rect(screen, color, pygame.Rect(col*64, row*64, 64, 64))

    #Chess Pieces
    _images = {}
    def load_image(name):
        if name not in _images:
            _images[name] = pygame.image.load(name).convert_alpha()
        return _images[name]
    
    class pawn(pygame.sprite.Sprite):
        def __init__(self, col, row, color):
            pygame.sprite.Sprite.__init__(self)
            self.color = color
            self.image = load_image(f"{color}_Pawn.png")
            self.rect = self.image.get_rect(topleft=(col*64, row*64))
        def move(self):
            pass
 
    pawns = pygame.sprite.Group()
    pawns.add(pawn(0,1,"Black"))

    #Place Pieces on the board
    pawns.draw(screen)
    
    pygame.display.flip() #Updates the display

    clock.tick(60) #60. FPS