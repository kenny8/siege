import pygame.font

class Button():
    def __init__(self, screen, msg, x, y, button_color, w=200, h=50, point_st=False):
        """Инициализирует атрибуты кнопки."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Назначение размеров и свойств кнопок.
        self.width, self.height = w, h
        self.button_color = button_color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.point_st = point_st
        # Построение объекта rect кнопки и выравнивание по центру экрана.
        self.rect = pygame.Rect(x, y, self.width, self.height)
        #self.rect.center = self.screen_rect.center
        #print(self.screen_rect.center)
        # Сообщение кнопки создается только один раз. 
        self.prep_msg(msg)

    def prep_msg(self, msg, point=''):
        """Преобразует msg в прямоугольник и выравнивает текст по центру."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.point_image = self.font.render(point, True, self.text_color,
                                            self.button_color)
        self.point_image_rect = self.point_image.get_rect()
        if len(point) > 0:
            self.msg_image_rect.x = self.rect.centerx - self.msg_image_rect.w // 2
            self.msg_image_rect.y = self.rect.centery - self.point_image_rect.h // 2
            self.point_image_rect.x = self.rect.centerx - self.point_image_rect.w // 2
            self.point_image_rect.y = self.rect.centery + self.point_image_rect.h // 2
        else:
            self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        if self.point_st:
            self.screen.blit(self.point_image, self.point_image_rect)


