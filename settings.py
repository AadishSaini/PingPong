import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()

FONT_NAME = 'arial'

# window dimensions
WIDTH = 860
HEIGHT = 620
FPS = 100

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)

# fonts
##SCORE AND TEXT##
score_value = 0
score_value2 = 0
font = pygame.font.Font('./fonts/FreightSansBold.otf', 32)
textx = 10
texty = 10

##Game Over Text##
over_font = pygame.font.Font('./fonts/FreightSansBold.otf', 64)

# bg image
bg = pygame.image.load("./img/bg.png")
