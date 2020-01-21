# Professor Dave Toth wrote this code
# it will make it possible to play audio and run a servo at the same time

import pygame
import time
pygame.init()

music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
counter = 0
run = True
while run:
    print(counter) # servo code
    counter = counter + 1 # goes here!
    time.sleep(1)
pygame.quit()
