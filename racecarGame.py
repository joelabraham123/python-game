import pygame
import time
import random
pygame.init()           #initiates modules of pygame

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
green = (255,255,0)

dodge_color = (53,115,200)
car_width = 81
gameDisplay = pygame.display.set_mode((display_width,display_height))#setting resolution(width,height)
pygame.display.set_caption('Fate of the Furious')   #sets a caption
clock = pygame.time.Clock()         #setting frames per sec

carImg = pygame.image.load('raceCarnew.png')       #import an image

def things_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged: "+str(count),True,dodge_color)
    gameDisplay.blit(text,(0,0))
def things(thingx, thingy, thingw, thingh, color):      #create random things such as objects/car
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    
def car(x,y):
    gameDisplay.blit(carImg,(x,y))              #display image..blit places something on screen
def text_objects(text,font):
    textSurface = font.render(text,True,black)        #render is pygame method..true is antialiasing
    return textSurface, textSurface.get_rect()          #get rectangle around text to position text
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',70)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)    #draws textsurf message inside textrect block
    pygame.display.update()     #use this everytime to update every change
    time.sleep(2)       #show message for 2 secs
    game_loop()
    
def crash():
    message_display('Oops!!Crashed!')

#setting game loop for putting all logics of game
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.80)
    x_change = 0

    thing_startx = random.randrange(0, display_width)   #to generate origin place of things randomly
    thing_starty = -600
    thing_speed = 4         #thing moves 4 per frame
    thing_width = 100
    thing_height = 100
    dodged = 0
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():     #grabs any happening event..event handler loop
            if event.type == pygame.QUIT:      #if someone press red X to close                
                pygame.quit()                   #instead of gameExit = True 
                quit()
            if event.type == pygame.KEYDOWN:    #if a key was pressed
                if event.key == pygame.K_LEFT:  #responds to left arrow key
                    x_change = -5
                elif event.key == pygame.K_RIGHT:   #responds to right arrow key
                    x_change = 5
            if event.type == pygame.KEYUP:   #if key is released
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0        #if left or right key is released

        x += x_change       #to change car to new position
            #print(event)        #this will work only for a single frame
        gameDisplay.fill(green)     #background white

        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed         #add 7 pixels lower and redraw with each while iteration
        car(x,y)
        things_dodged(dodged)
        #for crash into boundaries
        if x > display_width - car_width or x < 0:
            crash()
        if thing_starty > display_height:       #if it reached bottom of screen
            thing_starty = 0 - thing_height     #start a new block from top
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1        #increase speed by 1 pixel with each dodge
            #thing_width += (dodged * 1.2)
        if y < thing_starty + thing_height:
            #print('y crossover')        #prints in console
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                #print ('xcrossover')
                crash()
        pygame.display.update()         #or pygame.display.flip()..flip updates everything but updates just the given parameter
        clock.tick(60)        #parameter is fps
game_loop()
pygame.quit()           #idle you have to close twice
quit()

        
         
