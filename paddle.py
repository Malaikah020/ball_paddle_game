
import pygame
class Paddle:
    def __init__(self, x:int, y:int, speed_x:int):
        # all private instances so they can only be called from a setter and getter
        self.__x = x
        self.__y = y
        self.__speed_x= speed_x
        self.__coordinates = [self.__x, self.__y]
        # no colour instance because colour will only be needed if in default 
    def __str__(self):
        desc = "The paddle start coordinates are %s and has a speed of : %s" % (self.__coordinates,self.__speed_x)
        return desc
    
    def draw(self, display):
        '''draw paddle with an image of a canon'''
        # if no image or image wrong have a default object
        try:
            imp = pygame.image.load("/Users/malaikahhafeez/Documents/programming_folder/121344326_finalproject/gui/canon.png")
            display.blit(imp, (self.__x, self.__y))
        except:
            pygame.draw.rect(display, ([247, 231, 109]), (self.__x,self.__y,40,40))
            
    def move(self,horizontal_bound, keys):
        '''this function can both move it right and left'''
        # move the paddle right and left with in horizontal bounds
        # stop moving when key released
        # if is the keys has left then paddle move left with minusing x by speed for x
    
        if keys[pygame.K_LEFT]:
            # if going left it must be above 0 otherwise it will stay 0
            self.__x -= self.__speed_x
            if self.__x <= 0:
                self.__x = 0
            
        # if is the keys has right then paddle move right with plusing x by speed for x
        if keys[pygame.K_RIGHT]:
            # if x has increased to horizontal bound make it stay as horizontal bound no more
            self.__x += self.__speed_x
            if self.__x > horizontal_bound-45:
                self.__x = horizontal_bound-45
            
        # save in instance for coordinates which will be used in get coordinates
        self.__coordinates[0] = self.__x
        
        
    def get_coordinates(self):
        '''used to get coordinates for x and y which are needed for bullet'''
        return self.__coordinates