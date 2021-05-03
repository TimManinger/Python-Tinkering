import pygame


class RenderedObject:
    """basic type for visible game objects"""
    def __init__(self, x=0, y=0, rot=0, image='res/ufo.png', name='Object', desc='A basic rendered object.'):
        self.x = x
        self.y = y
        self.rot = rot
        self.img_loc = image
        self.img = pygame.image.load(image)
        self.name = name
        self.desc = desc

    def __str__(self):
        return f'{self.name} at {self.x},{self.y}'

    def __repr__(self):
        return f'RenderedObject({self.x},{self.y},{self.rot},{self.img_loc},{self.name},{self.desc})'

    def render(self, screen):
        r_img = pygame.transform.rotate(self.img, self.rot)
        screen.blit(r_img, (self.x, self.y))

    def center(self):
        x = self.x - (self.img.get_width() / 2)
        y = self.y - (self.img.get_height() / 2)
        return x, y
