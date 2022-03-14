import os
import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((800, 1000))

#cat_tail
ellipse(screen, (0, 0, 0), (600, 520, 500, 250), 2)
#main
rect(screen, (139, 69, 19), (0, 0, 800, 500))
rect(screen, (205, 133, 63), (0, 500, 800, 500))
#window
rect(screen, (176, 224, 230), (500, 20, 270, 420))
rect(screen, (0, 191, 255), (510, 30, 115, 110))
rect(screen, (0, 191, 255), (645, 30, 115, 110))
rect(screen, (0, 191, 255), (510, 150, 115, 280))
rect(screen, (0, 191, 255), (645, 150, 115, 280))
#cat_main
ellipse(screen, (119, 136, 153),(100, 520, 500, 250 ))
ellipse(screen, (0, 0, 0),(100, 520, 500, 250 ), 2)
#cat_right_hand
ellipse(screen, (119, 136, 153),(60, 620, 60, 80 ))
ellipse(screen, (0, 0, 0),(60, 620, 60, 80 ), 2)
#cat_left_hand
ellipse(screen, (119, 136, 153),(110, 680, 100, 60 ))
ellipse(screen, (0, 0, 0),(110, 680, 100, 60 ), 2)
#cat_head
circle(screen, (119, 136, 153), (130, 600), 80, 0)
circle(screen, (0, 0, 0), (130, 600), 80, 2)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
