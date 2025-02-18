# import library for pygame
import pygame

# creat a class 
class Bullet:
    # create class instances that store the valued of the coordinates and spees and is_triggered
    def __init__(self, x:int, y:int, speed:int):
        # all private instances so they can only be called from a setter and getter
        self.__x = x 
        self.__y = y
        self.__coordinates = [self.__x, self.__y]
        self.__speed_y = speed
        self.__is_triggered = False
        # no colour instance because colour will only be needed if in default 
    def __str__(self):
        desc = "The Bullet start coordinates are %s and has a speed of : %s" % (self.__coordinates,self.__speed_y)
        return desc
    
    def draw(self, display):
       try:
        #    draw bullet from image 
            imp = pygame.image.load("/Users/malaikahhafeez/Documents/programming_folder/121344326_finalproject/gui/ball.png")
            display.blit(imp, (self.__coordinates))
       except:
        #    if something wrong use default s
           pygame.draw.rect(display, ([123, 247, 109]), (self.__x,self.__y,20,20))

# =========================================================
    def change_speed(self, lower_limit, upper_limit):
        pass
# ==========================================================
    def move(self, pos:list):
        # so when space is pressed trigger is True
        if self.__is_triggered:
            # this will decrease y by the number set by speed y(controls how fast it goes)
            # this will make it go up the display form the we want it to start
            self.__y = self.__y - self.__speed_y
            # to reset the position y must be less than 0 which is the top the display
            if self.__y <= -6:
                # reset it to the position of the paddle by matching x which is in pos list same with y
                self.__x = pos[0]
                self.__y = pos[1]
                # to make sure it doesn't keep moving after repositioning we set self.__is_triggered to False
                self.__is_triggered = False
        # if it is not shooting then the position of the bullet should be the same as the paddle
        else:
            # x and y are taken from the get_coordinates in paddle and used as a list to get x and y for bullet
            self.__x = pos[0]
            self.__y = pos[1]
        # and the cordinants are then saved and can be used in get_coordinates for the collision
        self.__coordinates = [self.__x, self.__y]
    
    def get_coordinates(self):
        '''need to get coordinates for collision'''
        return self.__coordinates
    
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    # setter for trigger
    def set_triggered(self, val:bool):
        if val == True:
            self.__is_triggered = True
        if val == False:
            self.__is_triggered = False
            
    # change speed;
    def speed_change(self, lower_limit, upper_limit):
        # so if the spped is lower than upper keep adding on
        if self.__speed_y < upper_limit:
            self.__speed_y = self.__speed_y + 1
        # but if it reached the upper limit go back to lower limit and than you can gradually speed upa again
        if self.__speed_y == upper_limit:
            self.__speed_y = lower_limit
