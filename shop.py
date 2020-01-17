import pygame
import game_functions as gf
from button import Button
import pygame.font


class Shop(pygame.sprite.Sprite):
    def __init__(self, screen, stats):
        self.stats = stats
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.SysFont('Brush Script MT', 350)
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer

        self.image = pygame.Surface((820, 410))
        self.image.fill((50, 50, 50))
        self.image_rect = self.screen.get_rect()
        self.text = "fix wall:"
        self.fix_wall_button = Button(self.screen, self.text, 100, 100, (100, 150, 50), 200, 200, True)
        self.text_hero = "heal:"
        self.heal_button = Button(self.screen, self.text, 310, 100, (100, 150, 50), 200, 200, True)
        self.text_up_wall = "up wall:"
        self.up_wall_button = Button(self.screen, self.text, 520, 100, (100, 150, 50), 200, 200, True)
        self.text_up_hero = "up hero:"
        self.up_hero_button = Button(self.screen, self.text, 730, 100, (100, 150, 50), 200, 200, True)
        self.shop_off_button = Button(self.screen, 'return', 100, 310, (100, 150, 50), 820, 200)
        self.point_wall_up = 1000
        self.point_hero_up = 1000
        self.point_wall_level = 1
        self.point_hero_up_level = 1

    def blit(self):
        point1 = self.stats.count_hp_wall - self.stats.hp_wall
        self.fix_wall_button.prep_msg(self.text, str(point1))
        point2 = self.stats.count_hp_hero - self.stats.hp_hero
        self.heal_button.prep_msg(self.text_hero, str(point2))
        self.up_wall_button.prep_msg(self.text_up_wall, str(self.point_wall_level * self.point_wall_up))
        self.up_hero_button.prep_msg(self.text_up_hero, str(self.point_hero_up_level * self.point_hero_up))

        self.screen.blit(self.image, (100, 100))
        self.fix_wall_button.draw_button()
        self.shop_off_button.draw_button()
        self.up_hero_button.draw_button()
        self.heal_button.draw_button()
        self.up_wall_button.draw_button()
        # self.quit_button.draw_button()

    def render(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.check_fix_wall_button(mouse_x, mouse_y)
        self.check_heal_button(mouse_x, mouse_y)
        self.check_up_wall_button(mouse_x, mouse_y)
        self.check_up_hero_button(mouse_x, mouse_y)
        self.check_shop_off_button(mouse_x, mouse_y)

    def check_fix_wall_button(self, mouse_x, mouse_y):
        point = self.stats.count_hp_wall - self.stats.hp_wall
        if self.stats.score >= point and self.fix_wall_button.rect.collidepoint(mouse_x, mouse_y):
            self.stats.score -= point
            self.stats.hp_wall = self.stats.count_hp_wall

    def check_shop_off_button(self, mouse_x, mouse_y):
        if self.shop_off_button.rect.collidepoint(mouse_x, mouse_y):
            self.stats.game_shop = False

    def check_heal_button(self, mouse_x, mouse_y):
        point = self.stats.count_hp_hero - self.stats.hp_hero
        if self.stats.score >= point and self.heal_button.rect.collidepoint(mouse_x, mouse_y):
            self.stats.score -= point
            self.stats.hp_hero = self.stats.count_hp_hero

    def check_up_wall_button(self, mouse_x, mouse_y):
        point = self.point_wall_level * self.point_wall_up
        if self.stats.score >= point and self.up_wall_button.rect.collidepoint(mouse_x, mouse_y) \
                and self.stats.max_up_hp_wall > self.stats.count_hp_wall:
            self.point_wall_level += 1
            self.stats.score -= point
            self.stats.count_hp_wall += 10
            self.stats.hp_wall = self.stats.count_hp_wall

    def check_up_hero_button(self, mouse_x, mouse_y):
        point = self.point_hero_up_level * self.point_wall_up
        if self.stats.score >= point and self.up_hero_button.rect.collidepoint(mouse_x, mouse_y) \
                and self.stats.max_up_hp_hero > self.stats.count_hp_hero:
            self.point_hero_up_level += 1
            self.stats.score -= point
            self.stats.count_hp_hero += 10
            self.stats.hp_hero = self.stats.count_hp_hero
