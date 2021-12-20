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
    global closeCalls
    # to write the score
    Distance, Hits,closeCalls = 0,0,0.0
    
        
    # upload back ground
    background = pygame.image.load("backgrounds/forest.jpg").convert_alpha()
    background = pygame.transform.scale(background, (SCREEN_LENGTH,SCREEN_HEIGHT))
    # background image
    screen.blit(background, (0, 0))

    # STANDARD load images and resize thems
    car = pygame.image.load("PlayerCars/car1.png")
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

    #to animate the stearing of car
    global position
    position = 9 #this is the rest position of steering in our case
    wheelList= []

    wheelList.append(pygame.image.load('steerings/steer9L.png'))
    wheelList.append(pygame.image.load('steerings/steer8L.png'))
    wheelList.append(pygame.image.load('steerings/steer7L.png'))
    wheelList.append(pygame.image.load('steerings/steer6L.png'))
    wheelList.append(pygame.image.load('steerings/steer5L.png'))
    wheelList.append(pygame.image.load('steerings/steer4L.png'))
    wheelList.append(pygame.image.load('steerings/steer3L.png'))
    wheelList.append(pygame.image.load('steerings/steer2L.png'))
    wheelList.append(pygame.image.load('steerings/steer1L.png'))
    wheelList.append(pygame.image.load('steerings/steer.png'))
    wheelList.append(pygame.image.load('steerings/steer1R.png'))
    wheelList.append(pygame.image.load('steerings/steer2R.png'))
    wheelList.append(pygame.image.load('steerings/steer3R.png'))
    wheelList.append(pygame.image.load('steerings/steer4R.png'))
    wheelList.append(pygame.image.load('steerings/steer5R.png'))
    wheelList.append(pygame.image.load('steerings/steer6R.png'))
    wheelList.append(pygame.image.load('steerings/steer7R.png'))
    wheelList.append(pygame.image.load('steerings/steer8R.png'))
    wheelList.append(pygame.image.load('steerings/steer9R.png'))

    def releasedStearing(): #when not holding either LEFT or RIGHT key to stear the car, then stear should get back to start state
        global position
        if(position < 9):
            position += 0.25
        if(position > 9):
            position -= 0.25


    def text():
        global TimeElapsed, Hits, start_time, current_time,closeCalls
        

        #if(Obs1.rect.width // 2 >0):
            #print(Obs1.rect.width //2)
            
        current_time = int(time.time())
        TimeElapsed = current_time - start_time
        
        #Title board
        font= pygame.font.SysFont('CalibriBold', 50, False, False)
        text = font.render("SPEEDY BLUE", True, BLUE)
        screen.blit(text,[SCREEN_LENGTH//2 - 150,25])
        
        #Score board
        font= pygame.font.SysFont('Calibri', 25, False, False) # font for score board
        text2 = font.render("TimeElapsed = " + str(TimeElapsed), True, WHITE)
        screen.blit(text2,[SCREEN_LENGTH - 200,30])
        
        text3 = font.render("Hits = " + str(Hits), True, WHITE)
        screen.blit(text3,[SCREEN_LENGTH - 200,10])

        #closeCalls
        font= pygame.font.SysFont('Calibri', 25, False, False)
        text4 = font.render("CloseCallBONUS= " +str(closeCalls),True, WHITE)
        screen.blit(text4,[SCREEN_LENGTH - 250,60])

        return TimeElapsed




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
            question() # needed otherwise the sprites do not appear below script
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

    ZigZagSpeed = 5 # for level 3
    carSpeed = 5
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

        
        # to change the position of the car
        keys = pygame.key.get_pressed()

        #animate the steering and change the position of car
        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            if keys[pygame.K_LEFT]:
                playerCar.moveLeft(carSpeed)
                if position > 0:
                    position -= 0.25
                else:#limit/stop the steering wheel rotation
                    position = 0
                    
            elif keys[pygame.K_RIGHT]:
                playerCar.moveRight(carSpeed)
                if position < len(wheelList)-1:
                    position += 0.25
                else:#limit/stop the steering wheel rotation
                    position = len(wheelList)-1

        else:#else: get back to initial state of steering wheel
            releasedStearing()



        if keys[pygame.K_UP]:
            playerCar.moveForward(carSpeed)
        if keys[pygame.K_DOWN]:
            playerCar.moveBackward(carSpeed)

        # to change the speed if required
        if keys[pygame.K_LCTRL]:
            carSpeed -= 0.05
        if keys[pygame.K_LSHIFT]:
            carSpeed += 0.05


        # call text function                  
        text()

        #PlayerCar's mid point in Vector form
        vect1 = pygame.math.Vector2((playerCar.rect.x+(45//2),playerCar.rect.y+(70//2))) 

        # change obstacle co-ordinates
        if TimeElapsed <= 10:
            a= pygame.math.Vector2(Obs1.move(3))
            b= pygame.math.Vector2(Obs2.move(3))
            c= pygame.math.Vector2(Obs3.move(3))
            d= pygame.math.Vector2(Obs4.move(3))

            obs_list= [a,b,c,d] #list of pygame's Vector2
            for vect2 in obs_list:
                #if car is not colliding(False) and the closeCall condidtion is met then, Increment Bonus score
                if(pygame.sprite.spritecollideany(playerCar, obstacle_sprite_group)):
                    break
                elif(vect1.distance_to(vect2) < 65): #closeCall condition
                    closeCalls += 0.0005
                    print(closeCalls)
                    

        # for Level 2
        if TimeElapsed > 10 and TimeElapsed < 20:
            # Obs1.move(3)
            # Obs2.move(3)
            # Obs3.move(4)
            # Obs4.move(5)
            # Obs5.move(5)
            # Obs6.move(6)
            a= pygame.math.Vector2(Obs1.move(3))
            b= pygame.math.Vector2(Obs2.move(3))
            c= pygame.math.Vector2(Obs3.move(4))
            d= pygame.math.Vector2(Obs4.move(5))
            e= pygame.math.Vector2(Obs5.move(5))
            f= pygame.math.Vector2(Obs6.move(6))

            obs_list= [a,b,c,d,e,f]
            for vect2 in obs_list:
                for vect2 in obs_list:
                    #if car is not colliding(False) and the closeCall condidtion is met then, Increment Bonus score
                    if(pygame.sprite.spritecollideany(playerCar, obstacle_sprite_group)):
                        break
                    elif(vect1.distance_to(vect2) < 65): #closeCall condition
                        closeCalls += 0.005 #Increment Score faster in LEVEL-2
                        print(closeCalls)
            
        
        # for Level 3
        if TimeElapsed >= 20:
        
            a= pygame.math.Vector2(Obs1.move(3))
            b= pygame.math.Vector2(Obs2.move(4))
            c= pygame.math.Vector2(Obs3.move(5))
            d= pygame.math.Vector2(Obs4.move(6))
            e= pygame.math.Vector2(Obs5.move(7))
            f= pygame.math.Vector2(Obs6.move(8))
            ZigZagSpeed = Obs7.slant_move(ZigZagSpeed)
            ZigZagSpeed = Obs8.slant_move(ZigZagSpeed) 

            obs_list= [a,b,c,d,e,f]
            for vect2 in obs_list:
                for vect2 in obs_list:
                    #if car is not colliding(False) and the closeCall condidtion is met then, Increment Bonus score
                    if(pygame.sprite.spritecollideany(playerCar, obstacle_sprite_group)):
                        break
                    elif(vect1.distance_to(vect2) < 65): #closeCall condition 
                        closeCalls += 0.05 #Increment Score faster in LEVEL-3
                        print(closeCalls)
            

        #collision 
        if pygame.sprite.spritecollideany(playerCar, obstacle_sprite_group):
            
            pause=True 
            #Instruction board
            question()
            paused()
            # all_sprites_list.empty();

        # draw the sprites
        all_sprites_list.update() 
        all_sprites_list.draw(screen)

        #draw the steer, using "int" to slow down the animation speed
        #e.g, int(0.1) to int(0.9)=0, we will get a new int value after 9th loop(helps to slow animation speed)
        screen.blit(pygame.transform.scale(wheelList[int(position)],(80,80)),(600,600))
        
        #STANDARD speed of loop
        clock.tick(FPS)

        #STANDARD Update the screen
        pygame.display.update()
        pygame.display.flip()

main()
