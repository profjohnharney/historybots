import pygame
import time
pygame.init()

music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
counter = 0
run = True
while run:
    print(counter)
    counter = counter + 1
    time.sleep(1)
pygame.quit()
