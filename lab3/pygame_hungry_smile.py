import os
import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((600, 600))

#main circle
rect(screen, (165, 165, 165), (0, 0, 600, 600))
circle(screen, ('yellow'), (300, 300), 200, 0)
circle(screen, (0, 0, 0), (300, 300), 200, 3)
#left eyes
circle(screen, ('red'), (200, 250), 40, 0)
circle(screen, (0, 0, 0), (200, 250), 40, 3)
circle(screen, (0, 0, 0), (200, 250), 15, 0)
#right eyes
circle(screen, ('red'), (400, 250), 30, 0)
circle(screen, (0, 0, 0), (400, 250), 30, 3)
circle(screen, (0, 0, 0), (400, 250), 15, 0)
#mouth
rect(screen, (0, 0, 0), (200, 400, 200, 30))
#eyebrow - left
line(screen, (0, 0, 0), (130, 170), (250, 220), 20)
#eyebrow - right
line(screen, (0, 0, 0), (350, 235), (500, 165), 15)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
