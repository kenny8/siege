import pygame
import game_functions as gf
from wall import Wall
from player import Player
from ground import Ground
from camera import Camera
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from intro import Intro
from shop import Shop

pygame.init()
size = 1500, 1000
width_screen, height_screen = size
width_background, height_background = 2500, 2500
screen = pygame.display.set_mode(size)
background = pygame.Surface((width_background, height_background))
background_rect = background.get_rect()
print(background_rect.w, background_rect.h)
screen_rect = screen.get_rect()
# стены крепости
wall_group_down = pygame.sprite.Group()
wall_group_up = pygame.sprite.Group()
# земля в крепости
ground_group = pygame.sprite.Group()
# лесница
ladder_group = pygame.sprite.Group()
# двери
door_group = pygame.sprite.Group()
# пули
bullets = pygame.sprite.Group()
end_group = pygame.sprite.Group()
# враги
enemy_group = pygame.sprite.Group()
# игрок
player_group = pygame.sprite.Group()
# торговец
traider_group = pygame.sprite.Group()
stats = GameStats()
sb = Scoreboard(screen, stats)
# создание поля
gf.create_fleet_enemy(background, enemy_group, stats.level)
gf.create_fleet(width_background, height_background, wall_group_up, wall_group_down, ground_group, ladder_group,
                door_group, end_group, traider_group, Wall(False).rect.h)
for sprite in wall_group_up:
    nn = sprite.rect.y
    break
player = Player(screen, screen_rect.centerx, nn)
player_group.add(player)
play_button = Button(screen, "Play", screen_rect.centerx - 100, screen_rect.centery, (100, 150, 50))
game_over_button = Button(screen, "New", screen_rect.centerx - 100, screen_rect.centery, (100, 150, 50))
quit_button = Button(screen, "quit", screen_rect.centerx - 100, screen_rect.centery + 70, (100, 150, 50))
return_intro_button = Button(screen, "return intro", screen_rect.centerx - 100, screen_rect.centery + 130,
                             (100, 150, 50))
camera = Camera()
intro = Intro(screen, stats)
shop = Shop(screen, stats)
help_image = gf.load_image('help.png')
while stats.game_active:
    # действия с квавиатуры и мыши
    gf.key_evens(screen, player, bullets, ladder_group, door_group, play_button, game_over_button, camera, stats, intro,
                 background, end_group, enemy_group, wall_group_down, wall_group_up, ground_group, quit_button,
                 return_intro_button, traider_group, shop)
    if stats.game_intro:
        # интро игры
        intro.blit()
    else:
        if stats.game_return:
            # переход через интро
            gf.new_fleet(screen, background, end_group, enemy_group, wall_group_down, wall_group_up, ladder_group,
                         ground_group, door_group, stats, player, camera, traider_group)
            stats.game_return = False
        # обновление останавлиывается если пауза или  магазин или окончание игры
        if not stats.game_over and not stats.game_pause and not stats.game_shop:
            gf.update_screen(screen, background, player, bullets, wall_group_down, wall_group_up, ground_group,
                             enemy_group,
                             ladder_group, end_group, door_group, camera, stats, sb, player_group, traider_group)
        # прорисовка поля
        ground_group.draw(background)
        end_group.draw(background)
        wall_group_down.draw(background)
        wall_group_up.draw(background)
        bullets.draw(background)
        ladder_group.draw(background)
        enemy_group.draw(background)
        traider_group.draw(background)
        screen.blit(background, (0, 0))
        sb.show_score()
        player.blitme()
        # прорисовка кнопок и магазина
        if stats.game_shop:
            shop.blit()
        if stats.game_pause:
            play_button.draw_button()
            quit_button.draw_button()
            return_intro_button.draw_button()
        if stats.game_over:
            game_over_button.draw_button()
            quit_button.draw_button()
            return_intro_button.draw_button()
        screen.blit(help_image, (screen_rect.w - 200, screen_rect.h - 100))
    pygame.display.flip()

pygame.quit()
