import pygame


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0
        self.past_x = 0
        self.past_y = 0
        self.new = True

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx * 2
        obj.rect.y += self.dy * 3

    def cheak_x(self, obj, w):
        if obj.first_x and obj.rect.x == 0 and self.dx > 0:
            return False
        if obj.end_x and obj.rect.x <= w and self.dx < 0:
            return False
        return True

    def cheak_y(self, obj, h):
        if obj.first_y and obj.rect.y >= - 10 and self.dy > 0:
            return False
        if obj.end_y and obj.rect.y <= h and self.dy < 0:
            return False
        return True

    # позиционировать камеру на объекте target
    def update(self, target):
        if self.new:
            self.past_x = target.rect.x
            self.past_y = target.rect.y
            self.new = False
            self.dx = 0
            self.dy = 0
        else:
            self.dx = (self.past_x - target.rect.x)
            self.past_x = target.rect.x
            self.dy = self.past_y - target.rect.y
            self.past_y = target.rect.y
