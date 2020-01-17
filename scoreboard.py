import pygame.font
from pygame.sprite import Group


class Scoreboard():
    """Класс для вывода игровой информации."""

    def __init__(self, screen, stats):
        """Инициализирует атрибуты подсчета очков."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        # Настройки шрифта для вывода счета.
        self.text_color = (255, 0, 100)
        self.font = pygame.font.SysFont(None, 48)
        # Подготовка исходного изображения.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_hp_wall()
        self.prep_hp_hero()
        self.high_score = 0

    def prep_level(self):
        """Преобразует уровень в графическое изображение."""
        self.level_image = self.font.render('Level: ' + str(self.stats.level), True,
                                            (255, 191, 0))
        # Уровень выводится под текущим счетом.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen_rect.left
        self.level_rect.top = 100

    def prep_hp_wall(self):
        """Преобразует уровень в графическое изображение."""
        self.name_image = self.font.render('hp стены', True, (255, 191, 0))
        self.hp_wall_image = pygame.Surface((self.stats.hp_wall * 2, 40))
        self.hp_wall_image.fill((255, 0, 0))
        self.hp_wall_image.blit(self.name_image, (0, 0))
        # Уровень выводится под текущим счетом.
        self.hp_wall_rect = self.hp_wall_image.get_rect()
        self.hp_wall_rect.right = self.screen_rect.right - 20
        self.hp_wall_rect.top = 100

    def prep_hp_hero(self):
        """Преобразует уровень в графическое изображение."""
        self.name_image = self.font.render('hp hero', True, (255, 191, 0))
        self.hp_hero_image = pygame.Surface((self.stats.hp_hero * 2, 40))
        self.hp_hero_image.fill((255, 0, 0))
        self.hp_hero_image.blit(self.name_image, (0, 0))
        # Уровень выводится под текущим счетом.
        self.hp_hero_rect = self.hp_hero_image.get_rect()
        self.hp_hero_rect.right = self.screen_rect.right - 20
        self.hp_hero_rect.top = 160

    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        """Преобразует текущий счет в графическое изображение."""
        self.score_image = self.font.render('Point: ' + score_str, True,
                                            (255, 215, 0))

        # Вывод счета в правой верхней части экрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Преобразует рекордный счет в графическое изображение."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render('Max point: ' + high_score_str, True,
                                                 (185, 242, 255))
        # Рекорд выравнивается по центру верхней стороны.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Выводит счет на экран."""
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_hp_wall()
        self.prep_hp_hero()
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.hp_wall_image, self.hp_wall_rect)
        self.screen.blit(self.hp_hero_image, self.hp_hero_rect)
