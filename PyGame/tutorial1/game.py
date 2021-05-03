import pygame
import object
import world

# initialize pygame
pygame.init()

# initialize globals
# TODO read from settings file
t = 0.00
dt = 0.01
RES_X = 640
RES_Y = 480
APP_NAME = "Space Invaders"
APP_ICON_PATH = "res/ufo.png"
APP_ICON = pygame.image.load(APP_ICON_PATH)
FPS = 60

# create the screen and parameters
screen = pygame.display.set_mode((RES_X, RES_Y))
pygame.display.set_caption(APP_NAME)
pygame.display.set_icon(APP_ICON)

# player
player = object.RenderedObject(image='res/player-small.png')

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((100, 100, 100))
    player.render(screen)
    pygame.display.update()
