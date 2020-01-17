import pygame
import game_functions as gf


class Wall(pygame.sprite.Sprite):
    def __init__(self, wall_up, door=False):
        super(Wall, self).__init__()
        self.wall_up = wall_up
        self.door = door
        self.door_open = False
        if self.wall_up:
            self.image = gf.load_image('wall_up.png')
        else:
            self.image = gf.load_image('wall_down.png')
        if self.door and not self.door_open:
            self.image = gf.load_image('door_closed.png')
        elif self.door and self.door_open:
            self.image = gf.load_image('door_open.png')
        self.image = pygame.transform.scale(self.image, (
            int(float(self.image.get_width()) * 1.5), int(float(self.image.get_height()) * 1.5)))
        self.rect = self.image.get_rect()
        self.first = False
        self.end = False
        self.health = 100

    def update(self):
        if not self.door_open:
            self.image = gf.load_image('door_open.png')
            self.door_open = True
        else:
            self.image = gf.load_image('door_closed.png')
            self.door_open = False
        self.image = pygame.transform.scale(self.image, (
            int(float(self.image.get_width()) * 1.5), int(float(self.image.get_height()) * 1.5)))
