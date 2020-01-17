import pygame
import game_functions as gf
from button import Button
import pygame.font


class Intro(pygame.sprite.Sprite):
    def __init__(self, screen, stats):
        self.stats = stats
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.SysFont('Brush Script MT', 350)
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = gf.load_image('intro.jpg')
        self.image = pygame.transform.scale(self.image, (self.screen_rect.w, self.screen_rect.h))
        self.start_game_button = Button(screen, "Play", self.screen_rect.centerx - 100, self.screen_rect.centery,
                                        (100, 150, 50))
        self.quit_button = Button(screen, "quit", self.screen_rect.centerx - 100, self.screen_rect.centery + 70,
                                  (100, 150, 50))

    def blit(self):
        self.print_image = self.font.render('Siege', True, (248, 23, 62))
        self.print_image_rect = self.print_image.get_rect()
        self.screen.blit(self.image, (0, 0))
        self.screen.blit(self.print_image, (
            self.screen_rect.centerx - self.print_image_rect.w // 2,
            self.screen_rect.centery - self.print_image_rect.h))
        self.start_game_button.draw_button()
        self.quit_button.draw_button()

    def render(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.check_start_game_button(mouse_x, mouse_y)
        self.check_quit_button(mouse_x, mouse_y)

    def check_start_game_button(self, mouse_x, mouse_y):
        if self.stats.game_intro and self.start_game_button.rect.collidepoint(mouse_x, mouse_y):
            self.stats.game_intro = False

    def check_quit_button(self, mouse_x, mouse_y):
        if self.quit_button.rect.collidepoint(mouse_x, mouse_y):
            self.stats.game_active = False
