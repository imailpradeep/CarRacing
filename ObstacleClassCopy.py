import pygame, random

RED=(250,0,0)

class Obstacle(pygame.sprite.Sprite):
         
    def __init__(self,obs_x, obs_y, SCREEN_LENGTH, SCREEN_HEIGHT):
        # Call the parent class (Sprite) constructor
        super().__init__()

        #Initialise attributes of the obstacle/rectangle to draw it.
        self.x = obs_x
        self.y = obs_y
        self.width = SCREEN_LENGTH
        self.height = SCREEN_HEIGHT

        # re uploading a image for obstacle so that it changes for every cycle 
        image1 = pygame.image.load("obstacles/Obs1.png").convert_alpha()
        image2 = pygame.image.load("obstacles/Obs2.png").convert_alpha()
        image3 = pygame.image.load("obstacles/Obs3.png").convert_alpha()
        image4 = pygame.image.load("obstacles/Obs4.png").convert_alpha()
        image5 = pygame.image.load("obstacles/Obs5.png").convert_alpha()
        image6 = pygame.image.load("obstacles/Obs6.png").convert_alpha()
        image7 = pygame.image.load("obstacles/Obs7.png").convert_alpha()
        image8 = pygame.image.load("obstacles/Obs8.png").convert_alpha()
        image_obstacle = []
        image_obstacle.append(image1)
        image_obstacle.append(image2)
        image_obstacle.append(image3)
        image_obstacle.append(image4)
        image_obstacle.append(image5)
        image_obstacle.append(image6)
        image_obstacle.append(image7)
        image_obstacle.append(image8)
        self.image = random.choice(image_obstacle)
        self.image = pygame.transform.scale(self.image, (50,50))
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y     

        pygame.draw.rect(self.image, RED, [0, 0, self.rect.width, self.rect.height], 3)
        

    def move(self, speed):
        self.rect.y += speed

        if self.rect.y > self.height:
            self.rect.y = -50
            self.rect.x = random.randint(self.width/5,self.width*4/5-70)

            # to draw a rectangle around the obstacles
            pygame.draw.rect(self.image, RED, [0, 0, self.rect.width, self.rect.height], 3)

        #50 is the width and the height of Obstacle'ss rect
        return (self.rect.x+(50//2),self.rect.y+(50//2))# returning the mid point of Obstacles's rect, to compare the distance for closeCalls 
           
    # causes obstacles to move in a zig-zag manner    
    def slant_move(self,speed):
        
        self.speed = speed
        #self.rect.x = random.randint(self.width/5,self.width*4/5-70)
        self.rect.x += self.speed # change X-coordinate

        # change Y-coordinate, negative speed also mooves the image downwards
        if self.speed >0:
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed

        # limits on side motion or X-coordinate
        if (self.rect.x > (self.width*4/5 -70)):
            self.speed *= -1
            self.rect.x += self.speed
                    
        if (self.rect.x < (self.width*1/5)):
            self.speed *= -1
            self.rect.x += self.speed
        
        if self.rect.y > self.height:
            self.rect.y = -30
            self.rect.x = random.randint(self.width/5,self.width*4/5-70)
        
        return self.speed
