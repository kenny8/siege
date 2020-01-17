import pygame
import game_functions as gf


class Player(pygame.sprite.Sprite):

    def __init__(self, screen, x, y):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen
        super(Player, self).__init__()
        self.image = gf.load_image('hero.png', -1)
        self.image = pygame.transform.scale(self.image,
                                            (int(float(self.image.get_width()) * 1.5),
                                             int(float(self.image.get_height()) * 1.5)))
        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.position_up = True
        self.position_on_ladder = False
        self.post_x = self.rect.x
        self.post_y = self.rect.y
        self.post_left = False
        self.post_right = False
        self.new_left = True
        self.new_right = True
        self.post_up = False
        self.new_up = True
        self.post_down = False
        self.new_down = True

    # анимация
    def update_image(self, pos):
        if pos == 'left':
            if abs(self.post_x - self.rect.x) > 40 or self.new_left:
                self.new_left = False
                self.post_x = self.rect.x
                if self.post_left:
                    self.image = gf.load_image('hero_left2.png', -1)
                    self.post_left = False
                else:
                    self.post_left = True
                    self.image = gf.load_image('hero_left.png', -1)
                self.image = pygame.transform.scale(self.image,
                                                    (int(float(self.image.get_width()) * 1.5),
                                                     int(float(self.image.get_height()) * 1.5)))
        elif pos == 'right':
            if abs(self.post_x - self.rect.x) > 40 or self.new_right:
                self.new_right = False
                self.post_x = self.rect.x
                if self.post_right:
                    self.image = gf.load_image('hero_right.png', -1)
                    self.post_right = False
                else:
                    self.post_right = True
                    self.image = gf.load_image('hero_right2.png', -1)
                self.image = pygame.transform.scale(self.image,
                                                    (int(float(self.image.get_width()) * 1.5),
                                                     int(float(self.image.get_height()) * 1.5)))
        elif pos == 'up':
            if abs(self.post_y - self.rect.y) > 40 or self.new_up:
                self.new_up = False
                self.post_y = self.rect.y
                if self.post_up:
                    self.image = gf.load_image('hero_up.png', -1)
                    self.post_up = False
                else:
                    self.post_up = True
                    self.image = gf.load_image('hero_up2.png', -1)
                self.image = pygame.transform.scale(self.image,
                                                    (int(float(self.image.get_width()) * 1.5),
                                                     int(float(self.image.get_height()) * 1.5)))
        elif pos == 'down':
            if abs(self.post_y - self.rect.y) > 40 or self.new_down:
                self.new_down = False
                self.post_y = self.rect.y
                if self.post_down:
                    self.image = gf.load_image('hero_down.png', -1)
                    self.post_down = False
                else:
                    self.post_down = True
                    self.image = gf.load_image('hero_down2.png', -1)
                self.image = pygame.transform.scale(self.image,
                                                    (int(float(self.image.get_width()) * 1.5),
                                                     int(float(self.image.get_height()) * 1.5)))

    def update(self, wall_group_up, wall_group_down, ladder, ground_group):
        """Обновляет позицию игрока ."""
        n = 2
        if not self.position_on_ladder:
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.update_image('right')
                self.rect.x += n
            if self.moving_left and self.rect.left > 0:
                self.update_image('left')
                self.rect.x -= n
            if self.position_up:
                if self.moving_up and (
                        pygame.sprite.spritecollideany(self, wall_group_up) or pygame.sprite.spritecollideany(self,
                                                                                                              ladder)):
                    self.update_image('up')
                    self.rect.y -= n
                elif self.moving_up and not pygame.sprite.spritecollideany(self, wall_group_up):
                    self.update_image('up')
                    self.rect.y += 10
                if self.moving_down and pygame.sprite.spritecollideany(self, wall_group_up) and \
                        not pygame.sprite.spritecollideany(self, wall_group_down):
                    self.update_image('down')
                    self.rect.y += n
            else:
                for sp in wall_group_down:
                    y = sp.rect.y + sp.rect.h - self.rect.h + 3
                if self.moving_up and self.rect.y > 0:
                    if not (pygame.sprite.spritecollideany(self, wall_group_down) and self.rect.y < y):
                        self.update_image('up')
                        self.rect.y -= n
                if self.moving_down and self.rect.y + self.rect.h < self.screen_rect.h \
                        and not pygame.sprite.spritecollideany(self, wall_group_up):
                    self.update_image('down')
                    self.rect.y += n
        else:
            if self.position_up:
                self.update_image('up')
                self.rect.y += 2
                if pygame.sprite.spritecollideany(self, ground_group) \
                        and not pygame.sprite.spritecollideany(self, wall_group_up) \
                        and not pygame.sprite.spritecollideany(self, wall_group_down):
                    self.position_on_ladder = False
                    self.position_up = False
            elif not self.position_up:
                self.rect.y -= 2
                self.update_image('up')
                if not pygame.sprite.spritecollideany(self, wall_group_down):
                    self.position_on_ladder = False
                    self.position_up = True

    def blitme(self):
        """Выводит пришельца в текущем положении."""
        self.screen.blit(self.image, self.rect)
