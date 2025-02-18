# import pygame library
import pygame
# import random for relocation of bubble
import random
# create a class
class Bubble:

    def __init__(self, x:int, y:int, space:int, speed_y:int, speed_x:int):
        # all private instances so they can only be called from a setter and getter
        self.__x = x
        self.__y = y
        # this can be changed if picture has a greater width
        self.__extra_space = space
        self.__coordinates = [self.__x, self.__y]
        self.__speed_y = speed_y
        self.__speed_x = speed_x
        self.__size = 0
        # no colour instance because colour will only be needed if in default 
        
    # create string representation to show the speed because the higher the speed the harder the game
    def __str__(self):
        desc = "The bubble has a speed(higher the harder) of : %s and the position of start is x:%s , y:%s" % (self.__speed_x, self.__x, self.__y)
        return desc
    
    # draw function
    def draw(self, display, size = 0):
        '''this function takes one param and draw either a image if image named and is in the right file or
        a rectange as a default'''
        try:
            if self.__size == 0:
                imp = pygame.image.load("/Users/malaikahhafeez/Documents/programming_folder/121344326_finalproject/gui/boat.png")
                display.blit(imp, (self.__x, self.__y))
            # so now for increasing the size of the boat at collision use a different image
            if self.__size == 1:
                imp = pygame.image.load("/Users/malaikahhafeez/Documents/programming_folder/121344326_finalproject/gui/Bigboat.png")
                display.blit(imp, (self.__x, self.__y))
        except:
            # change extra space to the new size of the bubble
            pygame.draw.rect(display, ([231, 166, 237]), (self.__x,self.__y,self.__extra_space-20,self.__extra_space-20))
                


    def move(self, vertical_bound:int, horizontal_bound:int ):
        '''move the bubble diagnoanlly
            -must not move past vertical bound = the line
            -must relocate above the line when it hits the line
            -must not go off the screen on the sides
            -move diagonally both right and left'''
        # change the space needed to whatever the image is 
        horizontal_bound = horizontal_bound - self.__extra_space
        self.__y += self.__speed_y
        self.__x += self.__speed_x
        self.__coordinates = [self.__x,self.__y]
        if vertical_bound-self.__extra_space <= self.__y :
            # relocate by changing y to a random number above 10(not too close to ground) and below vertical_bound
            self.__y =  random.randint(10,vertical_bound)
            # relocate by changing x to a random number above 10 and below horizontal_bound
            self.__x =  random.randint(0,horizontal_bound)
        # if going to the sides
        if self.__x < 0 or self.__x>horizontal_bound:
            # multiply speed by -1 so if goes opposite direction cause moving right(+) will go left(-) and 
            # if left(-) then right(+) because -num * -1 = +
            self.__speed_x = self.__speed_x*-1
            # contanly add positive or gegative speed to the coordinates x and y
        
            
    
    
# use get coordinated for collision
    def get_coordinates(self):
        return self.__coordinates
    
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
    
# change size
    def change_size(self):
        '''because i was using images i didn't want to have upper and lower bounds because i would need 
        atleast more than 3 for it to make sense so i decided to do it a bit different so the draw is 
        affected by changing though i did this i could change it in the future when i have the amount
        of pictures by changing size a different way'''
        self.__size = 1
        self.__extra_space = 100
        
    def relocate(self, horizontal_bound, vertical_bound):
        '''to relocate the boat you just need to regenerate numbers within the bound for x and y'''
        self.__y =  random.randint(10,vertical_bound)
            # relocate by changing x to a random number above 10 and below horizontal_bound
        self.__x =  random.randint(0,horizontal_bound)