import os, sys
import pygame
from pygame.locals import *
from helpers import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'



  
class PyManMain:    
        def __init__(self, width=640,height=480):
                """Initialize"""
                """Initialize PyGame"""
                pygame.init()
                """Set the window Size"""
                self.width = width
                self.height = height
                
                """Create the Screen"""
                self.screen = pygame.display.set_mode((self.width
                                               , self.height))
        def MainLoop(self):
            """This is the Main Loop of the Game"""
            """Load All of our Sprites"""
            self.LoadSprites();
            while 1:
                for event in pygame.event.get():        
                    if event.type == pygame.QUIT: 
                         sys.exit()
                    elif event.type == KEYDOWN:
                         if ((event.key == K_RIGHT)
                         or (event.key == K_LEFT)
                         or (event.key == K_UP)
                         or (event.key == K_DOWN)):
                             self.snake.move(event.key)
            
            self.pellet_sprites.draw(self.screen)
            self.snake_sprites.draw(self.screen)
            pygame.display.flip()
        def LoadSprites(self):
            """Load the sprites that we need"""
            self.snake = Snake()
            self.snake_sprites = pygame.sprite.RenderPlain((self.snake))
            """figure out how many pellets we can display"""
            nNumHorizontal = int(self.width/64)
            nNumVertical = int(self.height/64)       
            """Create the Pellet group"""
            self.pellet_sprites = pygame.sprite.Group()
            """Create all of the pellets and add them to the 
            pellet_sprites group"""
            for x in range(nNumHorizontal):
                    for y in range(nNumVertical):
                        self.pellet_sprites.add(Pellet(pygame.Rect(x*64, y*64, 64, 64)))
            
class Snake(pygame.sprite.Sprite):
    """This is our snake that will move around the screen"""
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('snake.png',-1)
        self.pellets = 0
    def move(self, key):
	    xMove = 0;
	    yMove = 0;
    
	    if (key == K_RIGHT):
	        xMove = self.x_dist
	    elif (key == K_LEFT):
	        xMove = -self.x_dist
	    elif (key == K_UP):
	        yMove = -self.y_dist
	    elif (key == K_DOWN):
	        yMove = self.y_dist
	    self.rect.move_ip(xMove,yMove);
        
class Pellet(pygame.sprite.Sprite):
        
    def __init__(self, rect=None):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('pellet.png',-1)
        if rect != None:
            self.rect = rect


    
if __name__ == "__main__":
        MainWindow = PyManMain()
        MainWindow.MainLoop()
