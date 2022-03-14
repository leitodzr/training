import os
import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((800, 1000))


#main
rect(screen, (139, 69, 19), (0, 0, 800, 500))
rect(screen, (205, 133, 63), (0, 500, 800, 500))
#window
rect(screen, (176, 224, 230), (500, 20, 270, 420))
rect(screen, (0, 191, 255), (510, 30, 115, 110))
rect(screen, (0, 191, 255), (645, 30, 115, 110))
rect(screen, (0, 191, 255), (510, 150, 115, 280))
rect(screen, (0, 191, 255), (645, 150, 115, 280))
#cat_tail
ellipse(screen, (119, 136, 153), (520, 600, 350, 80), 0)
ellipse(screen, (0, 0, 0), (520, 600, 350, 80), 2)
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
#cat_foot
circle(screen, (119, 136, 153), (530, 730), 80, 0)
circle(screen, (0, 0, 0), (530, 730), 80, 2)
ellipse(screen, (119, 136, 153),(560, 750, 50, 100 ))
ellipse(screen, (0, 0, 0),(560, 750, 50, 100 ), 2)
#cat_ear_left
pygame.draw.polygon(screen, (119, 136, 153), ((50, 510), (90, 542), (60, 570)))
pygame.draw.polygon(screen, (0, 0, 0), ((50, 510), (90, 542), (60, 570)), 2)
pygame.draw.polygon(screen, (252, 190, 182), ((57, 520), (83, 542), (65, 560)))
pygame.draw.polygon(screen, (0, 0, 0), ((57, 520), (83, 542), (65, 560)), 3)
#cat_ear_right
pygame.draw.polygon(screen, (119, 136, 153), ((190, 510), (160, 542), (198, 570)))
pygame.draw.polygon(screen, (0, 0, 0), ((190, 510), (160, 542), (198, 570)), 2)
pygame.draw.polygon(screen, (252, 190, 182), ((187, 520), (168, 542), (194, 562)))
pygame.draw.polygon(screen, (0, 0, 0), ((187, 520), (168, 542), (194, 562)), 2)
#cat_eye_left
circle(screen, (93, 161, 48), (90, 600), 20)
circle(screen, (0, 0, 0), (90, 600), 20, 2)
ellipse(screen, (0, 0 ,0), (95, 583, 5, 35 ))
#cat_eye_right
circle(screen, (93, 161, 48), (167, 600), 20)
circle(screen, (0, 0, 0), (167, 600), 20, 2)
ellipse(screen, (0, 0 ,0), (170, 583, 5, 35 ))
#cat_nose
polygon(screen, (252, 190, 182), ((120, 620), (140, 620), (130, 635)))
polygon(screen, (0, 0, 0), ((120, 620), (140, 620), (130, 635)), 2)
line(screen, (0, 0, 0), (130, 635), (130, 650), 2)
arc(screen, (0, 0, 0), (110, 50, 130, 670), 3.14, 2*3.14)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
