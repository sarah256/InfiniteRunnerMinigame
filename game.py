import pygame
import sys
import threading
from threading import Thread
from time import sleep

def load_image(name):
    image = pygame.image.load(name)
    return image

img1 = pygame.transform.scale(load_image('pika-1.png'),(80,60))
img2 = pygame.transform.scale(load_image('pika-2.png'),(80,60))
img3 = pygame.transform.scale(load_image('pika-3.png'),(80,60))
img4 = pygame.transform.scale(load_image('pika-4.png'),(80,60))

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
        
    
    def update(self):
        """iterates through the images within self.images"""
        #pygame.time.delay(200)
        sleep(.2)
        self.index+=1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        
        
pygame.init()
pygame.display.set_caption('PikaRun')
background_image = pygame.transform.scale(pygame.image.load("background.jpg"),(957,512))
window = pygame.display.set_mode((957,512))
running = True

pikachu = pikaSprite()
group = pygame.sprite.Group(pikachu)
x = 0
x2 = -957

        
        
def pikaMove():
    group.update()
    group.draw(window)
    pygame.display.flip()
    
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)
    window.blit(background_image, [-x, 0])
    window.blit(background_image, [-x2, 0])
    if x < 957:
        x += 5
    else:
        x = -957
    if x2 < 957:
        x2+=5
    else:
        x2=-957
    Thread(target = pikaMove()).start()
