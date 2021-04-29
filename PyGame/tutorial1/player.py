import pygame


class RenderedObject:
    """basic type for visible game objects"""
    def __init__(self, x=0, y=0, image='ufo.png', name='Object', desc='A basic rendered object.'):
        self.x = x
        self.y = y
        self.img = pygame.image.load(image)
        self.name = name
        self.desc = desc
