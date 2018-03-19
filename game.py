import pygame
import sys
import numpy.random
from time import sleep


def load_image(name):
    image = pygame.image.load(name)
    return image

img1 = pygame.transform.scale(load_image('pika-1.png'),(80,60))
img2 = pygame.transform.scale(load_image('pika-2.png'),(80,60))
img3 = pygame.transform.scale(load_image('pika-3.png'),(80,60))
img4 = pygame.transform.scale(load_image('pika-4.png'),(80,60))

stump = pygame.transform.scale(load_image('stump.png'),(150,120))


class pikaSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(pikaSprite,self).__init__()
        self.images = []
        self.images.append(img1)
        self.images.append(img2)
        self.images.append(img3)
        self.images.append(img4)
        
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(20,350,64,64)
        self.isjump = 0
        
    def jump(self):
        self.isjump = 1
    
    def update(self):
        """constantly updates the state of Pikachu"""
        sleep(.04)
        if not self.isjump:
            #iterates through the images within self.images
            #every time update() is called
            self.index+=1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
                

class stumpObstacle(pygame.sprite.Sprite):
    def __init__(self):
        super(stumpObstacle,self).__init__()
        self.image = stump
        self.rect = self.image.get_rect()
        self.rect.y = 335
        self.rect.x = 957
        
    def update(self):
        """constantly updates stump position"""
        self.rect.x -= 10

        
pygame.init()
pygame.display.set_caption('PikaRun')
background_image = pygame.transform.scale(pygame.image.load("background.jpg"),(957,512))
window = pygame.display.set_mode((957,512))
running = True

pikachu = pikaSprite()
group = pygame.sprite.Group(pikachu)

stump = stumpObstacle()
obstacles = pygame.sprite.Group(stump)

x = 0
x2 = -957
delay = 0
cur = 0  
jumpInt = 2 #the interval for each jump frame -- affects speed
jumpHeight = 22 #the height for each jump frame
     
   
def pikaMove():
    """constantly updates Pikachu and the display"""
    group.update()
    group.draw(window)
    pygame.display.flip()
    
    
while running:
    event = pygame.event.poll()
    key = pygame.key.get_pressed()
    
    #handles exiting the game
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)
    
    #handles a jump
    if key[pygame.K_SPACE] and not pikachu.isjump:
        pikachu.rect.y -= jumpHeight
        pikachu.isjump = 1
        cur = delay #current time captured when space bar pressed
        pikachu.image = pikachu.images[2] #image while airborne
    delay += 1
    #the if statements are an admittedly hacky way to get a smoother jump curve
    if pikachu.isjump and delay == (cur+jumpInt):
        pikachu.rect.y -= jumpHeight
    if pikachu.isjump and delay == (cur+jumpInt*2):
        pikachu.rect.y -= jumpHeight
    if pikachu.isjump and delay == (cur+jumpInt*3):
        pikachu.rect.y -= jumpHeight
    if pikachu.isjump and delay == (cur+jumpInt*4):
        pikachu.rect.y += jumpHeight
    if pikachu.isjump and delay == (cur+jumpInt*5):
        pikachu.rect.y += jumpHeight
    if pikachu.isjump and delay == (cur+jumpInt*6):
        pikachu.rect.y += jumpHeight
    if pikachu.isjump and delay == (cur+jumpInt*7):
        pikachu.rect.y += jumpHeight
        pikachu.isjump = 0 #jump completed
        
    #background image is two connected images
    window.blit(background_image, [-x, 0])
    window.blit(background_image, [-x2, 0])
    #moving the positions of the two background images
    if x < 957:
        x += 10
    else:
        x = -957
    if x2 < 957:
        x2+=10
    else:
        x2=-957
    
    obstacles.update()
    obstacles.draw(window)
    
    #constantly updating the display
    pikaMove()

