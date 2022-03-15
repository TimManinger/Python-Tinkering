import pygame


class Balloon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = pygame.image.load("/data/alien1.png")
        self.mask = pygame.mask.from_surface(self.image)

b1 = Balloon()
b2 = Balloon()

if pygame.sprite.spritecollide(b1, b2, False, pygame.sprite.collide_mask):
    print("sprites have collided!")

def collision_normal(left_mask, right_mask, left_pos, right_pos):

    def vadd(x, y):
        return [x[0]+y[0],x[1]+y[1]]

    def vsub(x, y):
        return [x[0]-[y[0],x[1]-y[1]]]

    def vdot(x, y):
        return x[0]*y[0]+x[1]*y[1]

    offset = list(map(int, vsub(left_pos, right_pos)))

    overlap = left_mask.overlap_area(right_mask, offset)

    if overlap == 0:
        return

    """Calculate collision normal"""

    nx = (left_mask.overlap_area(right_mask, (offset[0]+1, offset[1])) -
          left_mask.overlap_area(right_mask, (offset[0]-1, offset[1])))
    ny = (left_mask.overlap_area(right_mask, (offset[0], offset[1]+1)) -
          left_mask.overlap_area(right_mask, (offset[0], offset[1]-1)))
    if nx == 0 and ny == 0:
        """One sprite is inside another"""
        return
    n = [nx, ny]
    
    return n