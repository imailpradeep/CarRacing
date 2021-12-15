# delete the image of car and obstacles in each cycle to make it faster

import pygame, sys, random, time
from CarClassCopy import SpeedyBlue
from ObstacleClassCopy import Obstacle


pygame.init()

# STANDARD Time variables
clock = pygame.time.Clock()
FPS = 60

#STANDARD colors
GREEN=(0,200,0)
RED=(250,0,0)
BLUE=(0,0,250)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (77,77,77)
PINK = (255,100,100)
CYAN = (0, 160, 233)

# STANDARD screen window dimensions
SCREEN_LENGTH = 700
SCREEN_HEIGHT = 700

# STANDARD make screen window and caption
screen=pygame.display.set_mode((SCREEN_LENGTH,SCREEN_HEIGHT))
pygame.display.set_caption('SPEEDY BLUE')

# function to move background
bg_y1 = 0
bg_y2 = 700

# to write the score
Distance, Hits = 0,0
start_time = int(time.time())

def main():
    global Distance # so that I can use it 
    # to write the score
    Distance, Hits = 0,0
    
        
    # upload back ground
    background = pygame.image.load("background.jpg").convert_alpha()
    background = pygame.transform.scale(background, (SCREEN_LENGTH,SCREEN_HEIGHT))
    # background image
    screen.blit(background, (0, 0))

    # STANDARD load images and resize thems
    car = pygame.image.load("car1.png")
    #car = pygame.transform.scale(car, (70, 70))
    # STANDARD set icon on the window
    pygame.display.set_icon(car)

    # make player car
    playerCar = SpeedyBlue()
    playerCar.rect.x = SCREEN_LENGTH/2 - 30
    playerCar.rect.y = SCREEN_HEIGHT - 80

    # make obstacle car and add it into a list
    Obs1 = Obstacle(random.randint(SCREEN_LENGTH/5,SCREEN_LENGTH*3/5),random.randint(-700,0),SCREEN_LENGTH, SCREEN_HEIGHT)
    Obs2 = Obstacle(random.randint(SCREEN_LENGTH/5,SCREEN_LENGTH*3/5),random.randint(-100,0),SCREEN_LENGTH, SCREEN_HEIGHT)
    Obs3 = Obstacle(random.randint(SCREEN_LENGTH/5,SCREEN_LENGTH*3/5),random.randint(-300,0),SCREEN_LENGTH, SCREEN_HEIGHT)
    Obs4 = Obstacle(random.randint(SCREEN_LENGTH/5,SCREEN_LENGTH*3/5),random.randint(-500,0),SCREEN_LENGTH, SCREEN_HEIGHT)
    Obs5 = Obstacle(random.randint(SCREEN_LENGTH/5,SCREEN_LENGTH*3/5),random.randint(-150,-100),SCREEN_LENGTH, SCREEN_HEIGHT)
    Obs6 = Obstacle(random.randint(SCREEN_LENGTH/5,SCREEN_LENGTH*3/5),random.randint(-100,-80),SCREEN_LENGTH, SCREEN_HEIGHT)
    Obs7 = Obstacle(random.randint(SCREEN_LENGTH/5,SCREEN_LENGTH*3/5),random.randint(-150,-100),SCREEN_LENGTH, SCREEN_HEIGHT)
    Obs8 = Obstacle(random.randint(SCREEN_LENGTH/5,SCREEN_LENGTH*3/5),random.randint(-100,-80),SCREEN_LENGTH, SCREEN_HEIGHT)
            
    obstacle_sprite_group = pygame.sprite.Group()

    obstacle_sprite_group.add(Obs1)
    obstacle_sprite_group.add(Obs2)
    obstacle_sprite_group.add(Obs3)
    obstacle_sprite_group.add(Obs4)
    obstacle_sprite_group.add(Obs5)
    obstacle_sprite_group.add(Obs6)
    obstacle_sprite_group.add(Obs7)
    obstacle_sprite_group.add(Obs8)
    

    # list of all sprites - obstacles and players
    all_sprites_list = pygame.sprite.Group()

    # Add the car to the list of objects
    all_sprites_list.add(playerCar)
    all_sprites_list.add(Obs1)
    all_sprites_list.add(Obs2)
    all_sprites_list.add(Obs3)
    all_sprites_list.add(Obs4)
    all_sprites_list.add(Obs5)
    all_sprites_list.add(Obs6)
    all_sprites_list.add(Obs7)
    all_sprites_list.add(Obs8)


    def text():
        global Distance, Hits, start_time, current_time
        
        current_time = int(time.time())
        Distance = current_time - start_time
        
        #Title board
        font= pygame.font.SysFont('CalibriBold', 50, False, False)
        text = font.render("SPEEDY BLUE", True, BLUE)
        screen.blit(text,[SCREEN_LENGTH//2 - 150,25])
        
        #Score board
        font= pygame.font.SysFont('Calibri', 25, False, False) # font for score board
        text2 = font.render("Distance = " + str(Distance), True, WHITE)
        screen.blit(text2,[SCREEN_LENGTH - 200,30])
        
        text3 = font.render("Hits = " + str(Hits), True, WHITE)
        screen.blit(text3,[SCREEN_LENGTH - 200,10])

        return Distance




    def question():
        font= pygame.font.SysFont('Calibri', 50, False, False)
        line1 = font.render('Spacebar to unpause', True, CYAN)
        line2 = font.render('OR', True, CYAN)
        line3 = font.render('"r" to restart', True, CYAN)
        line4 = font.render('"esc" to quit', True, CYAN)
        screen.blit(line1,[SCREEN_LENGTH/5,SCREEN_HEIGHT//2 - 100])                    
        screen.blit(line2,[SCREEN_LENGTH/2 - 20,SCREEN_HEIGHT//2 - 50])
        screen.blit(line3,[SCREEN_LENGTH/5 + 80,SCREEN_HEIGHT//2])
        screen.blit(line2,[SCREEN_LENGTH/2 - 20,SCREEN_HEIGHT//2 + 50])
        screen.blit(line4,[SCREEN_LENGTH/5 + 80,SCREEN_HEIGHT//2+100])
        pygame.display.flip()
        
        

    # STANDARD quit function           
    def quit():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                    sys.exit()

    # to pause the game on collision
    def paused():
        global pause, Hits, start_time, Distance, current_time
        while pause:
            question()
            all_sprites_list.update()
            all_sprites_list.draw(screen)
            for event in pygame.event.get():
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_SPACE):
                        pause = False
                        Hits += 1
                    if(event.key == pygame.K_r):
                        Hits = 0
                        start_time = int(time.time())
                        main()
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        pygame.quit()
                        sys.exit()
                        
                        
    def Redraw_Window():
        global bg_y1, bg_y2
        bg_y1 += 1
        bg_y2 += 1
        
        screen.blit(background, (0,bg_y1))  # draws our first bg image
        screen.blit(background, (0,bg_y2))
        if bg_y1 >= 700: 
            bg_y1 = -700
        if bg_y2 >= 700: 
            bg_y2 = -700 
                              
                    
    #STANDARD game loop


    global pause
    run = True
    while run:
        quit()

        #screen.blit(background, (0, 0))
        Redraw_Window()

        # make road with tow white rectangles as road partition 
        pygame.draw.rect(screen, GREY,(int(SCREEN_LENGTH/5), 0, int(SCREEN_LENGTH*3/5),SCREEN_HEIGHT))
        pygame.draw.rect(screen, WHITE,(int(SCREEN_LENGTH*2/5), 0, 3 ,SCREEN_HEIGHT))
        pygame.draw.rect(screen, WHITE,(int(SCREEN_LENGTH*3/5), 0, 3 ,SCREEN_HEIGHT))

        
        # to change the position of the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerCar.moveLeft(3)
        if keys[pygame.K_RIGHT]:
            playerCar.moveRight(3)
        if keys[pygame.K_UP]:
            playerCar.moveForward(3)
        if keys[pygame.K_DOWN]:
            playerCar.moveBackward(3)
        # to change the speed if required
        if keys[pygame.K_LCTRL]:
            speed -= 0.05
        if keys[pygame.K_LSHIFT]:
            speed += 0.05

        # change obstacle co-ordinates
        Obs1.move(3)
        Obs2.move(3)
        Obs3.move(3)
        Obs4.move(3)

        # call text function                  
        text()
        
        # for Level 2
        if Distance > 5 and Distance < 10:
            Obs3.move(4)
            Obs4.move(5)
            Obs5.move(5)
            Obs6.move(6)
        
        # for Level 3
        if Distance >= 10:
            Obs1.move(3)
            Obs2.move(4)
            Obs3.move(5)
            Obs4.move(6)
            Obs5.move(7)
            Obs6.move(8)
            Obs7.slant_move(4)
            Obs8.slant_move(5)              
              
                
        # collision
        if pygame.sprite.spritecollideany(playerCar, obstacle_sprite_group):
            pause=True 
            #Instruction board
            question()
            paused()

        # draw the sprites
        all_sprites_list.update()
        all_sprites_list.draw(screen)

        #STANDARD speed of loop
        clock.tick(FPS)

        #STANDARD Update the screen
        pygame.display.update()
        pygame.display.flip()

main()
