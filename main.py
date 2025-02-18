# how to play? press right and left to move paddle and space to shoot bullet
# must have 4 python files called main.py, paddle.py, bullet.py, bubble.py
# must have 3 images called bullet.png, boat.png and canon.png

# must import the classes to create instances 
from bubble import Bubble
from paddle import Paddle
from bullet import Bullet

# import pygame library
import pygame


 
        
# create a diplay window of my choice 
pygame.init()
DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 600
DISPLAY_SIZE = [DISPLAY_WIDTH, DISPLAY_HEIGHT]
display = pygame.display.set_mode(DISPLAY_SIZE)

 # checks for collisions
def collision_check(BUB, BUL):
    if BUB.get_y() + 5 > BUL.get_y() and BUB.get_y() - 5 < BUL.get_y() + 5:
        # if collided change speed in bullet class which is basically a setter to increment by one
        BUL.speed_change(4,18)
        # also change to a bigger size image 
        BUB.change_size()  
        # relocate when hit
        BUB.relocate(DISPLAY_WIDTH, DISPLAY_HEIGHT)  
        
# three main colour used to create design 
# blue for background
blue = [56, 179, 255]
# cream for line
cream = (242, 237, 216)
# red for stop
red = [255, 0, 0]

# these are all used to create the instances----------------------------------------------------
# circle
bub_x = DISPLAY_WIDTH//2
bub_y = DISPLAY_HEIGHT//2
space_needed = 45
speed_y = 1
speed_x = 1

# paddle cordinated to start for x and y
pad_x = DISPLAY_WIDTH//2 
pad_y = DISPLAY_HEIGHT-50

# bullet coordinates
Bul_x = DISPLAY_WIDTH*-1
Bul_y = DISPLAY_HEIGHT*-1
# speed 
speed =  6
bul_speed =  5
# ----------------------------------------------------------------------------------------------

        
        # the bullet should change speed  when the bullet collides with the bubble
        
clock = pygame.time.Clock()

# instances created for the three main elements of the game--------------------------------------
Bub = Bubble(bub_x,bub_y,space_needed,speed_x,speed_y)
pad = Paddle(pad_x,pad_y, speed)
bul = Bullet(pad_x,pad_y-30,bul_speed)
# -----------------------------------------------------------------------------------------------

# print the sting representation for the instance of bub,pad,bul in class Bubble,Paddle and Bullet
print(Bub)
print(pad)
# print(bul)

# the game while loop run as long as run_game is True
run_game = True
while run_game:
    # display is coloued blue 
    
    display.fill(blue)
    # line----------------------------------------------------------------------------------------
    # this is drawing a line which the bubble should not pass and the paddle is underneath
    # variable used to make a line and a certain position 
    # proportional to the display height and width
    line_x1 =0
    line_y1 = 4/5*DISPLAY_HEIGHT
    line_x2 = DISPLAY_WIDTH
    line_y2 = 4/5*DISPLAY_HEIGHT
    
    # draw line with 5 thickness
    pygame.draw.line(display, cream, [line_x1, line_y1], [line_x2, line_y2], 5)
    # ---------------------------------------------------------------------------------------------
    # draw the bub instance using the class function draw with one parameter display
    Bub.draw(display, 0)
    # move that bubble inside the display 
    # not past the line_y2 which is the vertical bound
    # the bubble also need the horizontal bound 
        #which is the display_width and the lenth of the picture
    Bub.move(line_y2,DISPLAY_WIDTH)
    
    
    # Draw the paddle using class function draw with one parameter display
    pad.draw(display)
    
    # get a list of all the key pressed to make the paddle move
    keys = pygame.key.get_pressed()
    # move that paddle inside the display HORIZONTALLY ONLY
    # param display_width is the horizonal bound so it doesn't go off screen and keys is a list of all keys pressed
    pad.move(DISPLAY_WIDTH, keys)
    
    # bullet---------------------------------------------------------------------------
    # draw bullet on display
    bul.draw(display)
    # get list of coordinates using get coordinates from paddle
    info = pad.get_coordinates()
    # move bullet with paddle coordinates also places behind so it looks like it is coming out of the canon like it does in real life
    bul.move(info)
    # draw paddle on top of bullet
    pad.draw(display)
    
    collision_check(Bub, bul)
            
    # keep the game going as long as no one has exited the display window by pressing the x button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        # trigger = True for bullet if pressing space--------------------------------------
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                bul.set_triggered(True)  
    
        # ----------------------------------------------------------------------------------    
    
    clock.tick(40)
    pygame.display.update()
    # ---- update framerate
    

pygame.quit()
quit()

# references
# used https://www.geeksforgeeks.org/python-display-images-with-pygame/ for images in pygame
# used https://www.pythonforbeginners.com/basics/how-to-detect-keypress-in-python to learn how key.pressed function works