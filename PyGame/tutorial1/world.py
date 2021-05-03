import pygame


class Time:
    """class to do the base simulation"""

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.t = 0.0
        self.dt = 0.01
        self.accumulator = 0.0


class Space:
    """class to hold the world coordinate system"""

    def __init__(self, x=10_000, y=10_000):
        self.size = (x, y)
        self.objects = ()
