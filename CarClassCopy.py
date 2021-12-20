import pygame

RED=(250,0,0)

class SpeedyBlue(pygame.sprite.Sprite):
     
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Instead we could load a proper picture of a car...
        self.image = pygame.image.load("PlayerCars/car1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (45, 70))
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
        pygame.draw.rect(self.image, RED, [0, 0, self.rect.width, self.rect.height], 3)

    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
 
    def moveForward(self, pixels): 
        self.rect.y -= pixels
 
    def moveBackward(self, pixels): 
        self.rect.y += pixels
