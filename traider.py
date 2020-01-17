import pygame
import game_functions as gf


class Traider(pygame.sprite.Sprite):
    def __init__(self):
        super(Traider, self).__init__()
        self.image = gf.load_image('traider.png', -1)
        self.image = pygame.transform.scale(self.image, (
            int(float(self.image.get_width()) * 1.5), int(float(self.image.get_height()) * 1.5)))
        self.rect = self.image.get_rect()
