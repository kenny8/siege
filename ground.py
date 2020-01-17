import pygame
import game_functions as gf


class Ground(pygame.sprite.Sprite):
    def __init__(self, in_or_out_wall):
        super(Ground, self).__init__()
        self.in_or_out_wall = in_or_out_wall
        if in_or_out_wall == 1:
            self.image = gf.load_image('grass.png')
        elif in_or_out_wall == 0:
            self.image = gf.load_image('ground.png')
        elif in_or_out_wall == 2:
            self.image = gf.load_image('ground_wall.png')
        self.image = pygame.transform.scale(self.image, (
            int(float(self.image.get_width()) * 1.5), int(float(self.image.get_height()) * 1.5)))
        self.rect = self.image.get_rect()
        self.first_y = False
        self.end_y = False
        self.first_x = False
        self.end_x = False
