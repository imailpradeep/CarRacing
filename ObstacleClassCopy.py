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
        

        # uploading a image for obstacle, if I don't put this here, I get the rectangle for the first cycle
        image1 = pygame.image.load("Obs1.png").convert_alpha()

        self.image = image1
        self.image = pygame.transform.scale(self.image, (50,50))

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        #pygame.draw.rect(self.image, RED, [0, 0, self.rect.width, self.rect.height], 3)
        

    def move(self, speed):
        self.rect.y += speed

        if self.rect.y > self.height:
            self.rect.y = -30
            self.rect.x = random.randint(self.width/5,self.width*4/5-70)

            # re uploading a image for obstacle so that it changes for every cycle 
            image1 = pygame.image.load("Obs1.png").convert_alpha()
            image2 = pygame.image.load("Obs2.png").convert_alpha()
            image3 = pygame.image.load("Obs3.png").convert_alpha()
            image4 = pygame.image.load("Obs4.png").convert_alpha()
            image5 = pygame.image.load("Obs5.png").convert_alpha()
            image6 = pygame.image.load("Obs6.png").convert_alpha()
            image7 = pygame.image.load("Obs7.png").convert_alpha()
            image8 = pygame.image.load("Obs8.png").convert_alpha()
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

            
            # to draw a rectangle around the obstacles
            pygame.draw.rect(self.image, RED, [0, 0, self.rect.width, self.rect.height], 3)

        
    def slant_move(self,speed):

        #speed = random.randint(3,6)
        self.speed = speed
        self.rect.y += self.speed
        self.rect.x += self.speed
        '''
        if (self.rect.x > (self.width*4/5 -70)):
            speed *= -1
            self.rect.x -= self.speed
            
                #self.rect.x += speed
            print(self.speed,self.rect.x)
        
        if (self.rect.x < (self.width*1/5)):
            self.speed *= -1
            #self.rect.x += speed
        
        if self.rect.y > self.height:
            self.rect.y = -30
            self.rect.x = random.randint(self.width/5,self.width*4/5-70)
        '''

