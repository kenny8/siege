import pygame
from pygame.sprite import Sprite
import game_functions as gf
import random


class Enemy(Sprite):
    """Класс, представляющий одного пришельца."""

    def __init__(self, screen):
        """Инициализирует пришельца и задает его начальную позицию."""
        super(Enemy, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Загрузка изображения пришельца и назначение атрибута rect.
        self.image = gf.load_image('orc_warrior.png', -1)
        self.image = pygame.transform.scale(self.image,
                                            (int(float(self.image.get_width()) * 2),
                                             int(float(self.image.get_height()) * 2)))
        self.rect = self.image.get_rect()
        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.post_x = self.rect.x
        self.post_y = self.rect.y
        self.post_down = False
        self.new_down = True

    def update_image(self, pos):
        if pos == 'down':
            if abs(self.post_y - self.rect.y) > 40 or self.new_down:
                self.new_down = False
                self.post_y = self.rect.y
                if self.post_down:
                    self.image = gf.load_image('orc_warrior2.png', -1)
                    self.post_down = False
                else:
                    self.post_down = True
                    self.image = gf.load_image('orc_warrior1.png', -1)
                self.image = pygame.transform.scale(self.image,
                                                    (int(float(self.image.get_width()) * 1.5),
                                                     int(float(self.image.get_height()) * 1.5)))

    def blitme(self):
        """Выводит врага в текущем положении."""
        self.screen.blit(self.image, self.rect)

    def update(self, wall_group_up, enemy_group_up):
        """Перемещает врага вправо."""
        if not pygame.sprite.spritecollideany(self, wall_group_up):
            self.update_image('down')
            self.rect.y += 1
