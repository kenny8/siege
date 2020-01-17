import pygame
from pygame.sprite import Sprite
import game_functions as gf


class Bullet(Sprite):

    def __init__(self, screen, player):
        """Создает объект пули в текущей позиции корабля."""
        super(Bullet, self).__init__()
        self.screen = screen
        # Создание пули в позиции (0,0) и назначение правильной позиции.
        self.image = gf.load_image('arrow.png', -1)
        self.rect = self.image.get_rect()
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top
        # Позиция пули хранится в вещественном формате.
        self.y = float(self.rect.y)
        self.speed_factor = 3

    def update(self):
        """Перемещает пулю вверх по экрану."""
        self.y -= self.speed_factor
        # Обновление позиции прямоугольника.
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод пули на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)
