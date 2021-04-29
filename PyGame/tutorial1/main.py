import pygame

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((640, 480))

# title and logo
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('player-small.png')
playerX = 320 - (playerImg.get_width() / 2)
playerY = 400 - (playerImg.get_height() / 2)


def player():
    screen .blit(playerImg, (playerX, playerY))


# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((100, 100, 100))
    player()
    pygame.display.update()
