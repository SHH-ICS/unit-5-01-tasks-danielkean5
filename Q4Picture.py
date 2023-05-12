# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
import pygame, sys
from pygame.locals import QUIT

from pygame import Color, Rect
from pygame import draw
from pygame import display

SCREEN_SIZE = (500, 500)

pygame.init()
gameDisplay = display.set_mode(SCREEN_SIZE)

gameDisplay.fill(Color('lightblue'))
draw.rect(gameDisplay, Color('brown'), Rect(100, 300, 200, 200))
draw.polygon(gameDisplay, Color('brown'), [(100, 300), (300, 300), (200, 200)])
draw.rect(gameDisplay, Color('green'), Rect(0, 450, 500, 100))
draw.circle(gameDisplay, Color('yellow'), (450, 50), 50)
display.flip()
input("Press enter to exit")