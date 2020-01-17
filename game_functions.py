import pygame
import os
from wall import Wall
from bullet import Bullet
from ground import Ground
from ladder import Ladder
from traider import Traider
from enemy import Enemy

pause = False
hp_wall = 100
camera_g = True
level_game = 1


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def create_fleet(width, height, wall_group_up, wall_group_down, ground_group, ladder_group, door_group, end_group,
                 traider_group,
                 size):
    numb_w = width / size
    numb_h = height / size
    if numb_w > int(numb_w):
        numb_w += 1
    numb_w = int(numb_w)
    if numb_h > int(numb_h):
        numb_h += 1
    numb_h = int(numb_h)
    n = 7
    for hig in range(numb_h):
        for wid in range(numb_w):
            if hig == 0:
                create_ground(end_group, 0, wid, numb_w, hig, numb_h, numb_h - size * (hig - n))
            if hig < 5 and hig != 0:
                create_ground(ground_group, 0, wid, numb_w, hig, numb_h, numb_h - size * (hig - n))
            if hig == 5:
                create_wall(wall_group_down, False, wid, numb_w, numb_h - size * (hig - n), ladder_group, door_group,
                            traider_group)
                create_ground(ground_group, 2, wid, numb_w, hig, numb_h, numb_h - size * (hig - n))
            if hig == 6:
                create_wall(wall_group_up, True, wid, numb_w, numb_h - size * (hig - n), ladder_group, door_group,
                            traider_group)
                create_ground(ground_group, 2, wid, numb_w, hig, numb_h, numb_h - size * (hig - n))
            if hig > 6:
                create_ground(ground_group, 1, wid, numb_w, hig, numb_h, numb_h - size * (hig - n))


def create_wall(wall_group, up_or_down_wall, numb, all_w, hight, ladder_group, door_group, traider_group):
    if numb % 3 == 0 and numb != 0 and not up_or_down_wall:
        wall = Wall(up_or_down_wall, True)
        wall_width = wall.rect.width
        wall.rect.x = wall_width * numb
        wall.rect.y = hight
        door_group.add(wall)
    else:
        wall = Wall(up_or_down_wall, False)
        wall_width = wall.rect.width
        wall.rect.x = wall_width * numb
        wall.rect.y = hight
    if numb == 1 and numb != 0 and not up_or_down_wall and not wall.door:
        traider = Traider()
        traider.rect.x = wall.rect.x + wall.rect.w // 2
        traider.rect.y = wall.rect.y + wall.rect.h - traider.rect.h + 20
        traider_group.add(traider)
    if numb % 4 == 0 and numb != 0 and not up_or_down_wall and not wall.door:
        ladder = Ladder()
        ladder.rect.x = wall.rect.x + 50
        ladder.rect.y = wall.rect.y - 35
        ladder_group.add(ladder)
    wall_group.add(wall)


def create_ground(ground_group, up_or_down_wall, numb, all_w, numb_h, all_h, hight):
    ground = Ground(up_or_down_wall)
    ground_width = ground.rect.width
    ground.rect.x = ground_width * numb
    ground.rect.y = hight
    if numb == 0:
        ground.first_x = True
    if numb == all_w - 1:
        ground.end_x = True
    if numb_h == all_h - 1:
        ground.first_y = True
    if numb_h == 1:
        ground.end_y = True
    ground_group.add(ground)


def key_evens(screen, player, bullets, ladder_group, door_group, play_button, game_over, camera, stats, intro,
              background, end_group, enemy_group, wall_group_down, wall_group_up, ground_group, quit_button,
              return_intro_button, traider_group, shop):
    global pause
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stats.game_active = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            shop.render()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)
            check_game_over_button(screen, background, end_group, enemy_group, wall_group_down, wall_group_up,
                                   ladder_group, ground_group, door_group, stats, player, game_over, camera, mouse_x,
                                   mouse_y, traider_group)
            check_quit_button(quit_button, stats, mouse_x, mouse_y)
            check_return_button(return_intro_button, stats, mouse_x, mouse_y)
            intro.render()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.moving_right = True
            if event.key == pygame.K_a:
                player.moving_left = True
            if event.key == pygame.K_w:
                player.moving_up = True
            if event.key == pygame.K_s:
                player.moving_down = True
            if event.key == pygame.K_SPACE:
                fire_bullet(screen, player, bullets)
            if event.key == pygame.K_ESCAPE:
                if stats.game_pause:
                    stats.game_pause = False
                else:
                    stats.game_pause = True
            if event.key == pygame.K_e:
                if pygame.sprite.spritecollideany(player, ladder_group):
                    player.position_on_ladder = True
                if pygame.sprite.spritecollideany(player, traider_group):
                    if not stats.game_shop:
                        stats.game_shop = True
                    else:
                        stats.game_shop = False
                for sprite in door_group:
                    w = sprite.rect.w
                    x = sprite.rect.x
                    y = sprite.rect.y
                    if not player.position_up and player.rect.x > x and player.rect.x < x + w \
                            and player.rect.y < y and player.rect.y > y - w * 2:
                        door_group.update()
                        camera.new = True
                        player.rect.y = y + w
                        break
                if not player.position_up and pygame.sprite.spritecollideany(player, door_group):
                    door_group.update()
                    camera.new = True
                    player.rect.y = y - w * 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.moving_right = False
            if event.key == pygame.K_a:
                player.moving_left = False
            if event.key == pygame.K_w:
                player.moving_up = False
            if event.key == pygame.K_s:
                player.moving_down = False


def check_play_button(stats, play_button, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and stats.game_pause:
        stats.game_pause = False


def check_quit_button(quit_button, stats, mouse_x, mouse_y):
    if (stats.game_pause or stats.game_over) and quit_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = False


def check_return_button(return_button, stats, mouse_x, mouse_y):
    if (stats.game_pause or stats.game_over) and return_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_return = True
        stats.game_intro = True


def check_game_over_button(screen, background, end_group, enemy_group, wall_group_down, wall_group_up, ladder,
                           ground_group, door_group, stats, player, game_over, camera, mouse_x, mouse_y, traider_group):
    button_clicked = game_over.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and stats.game_over:
        new_fleet(screen, background, end_group, enemy_group, wall_group_down, wall_group_up, ladder,
                  ground_group, door_group, stats, player, camera, traider_group)


def new_fleet(screen, background, end_group, enemy_group, wall_group_down, wall_group_up, ladder,
              ground_group, door_group, stats, player, camera, traider_group):
    wall_group_down.empty()
    wall_group_up.empty()
    ladder.empty()
    end_group.empty()
    ground_group.empty()
    enemy_group.empty()
    traider_group.empty()
    background_rect = background.get_rect()
    screen_rect = screen.get_rect()
    create_fleet(background_rect.w, background_rect.h, wall_group_up, wall_group_down, ground_group, ladder,
                 door_group, end_group, traider_group, Wall(False).rect.h)
    stats.reset_stats()
    stats.game_over = False
    for sprite in wall_group_up:
        nn = sprite.rect.y
        break
    if player.rect.y > nn:
        camera.new = True
    player.rect.x = screen_rect.centerx
    player.rect.y = nn
    player.position_up = True


def fire_bullet(screen, player, bullets):
    new_bullet = Bullet(screen, player)
    bullets.add(new_bullet)


def create_enemy(screen, enemy_group, enemy_number, row_number):
    """Создает пришельца и размещает его в ряду."""
    enemy = Enemy(screen)
    enemy_width = enemy.rect.width
    enemy.x = enemy_width + 2 * enemy_width * enemy_number
    enemy.rect.x = enemy.x
    enemy.rect.y = enemy.rect.height + 2 * enemy.rect.height * row_number - 500
    enemy_group.add(enemy)


def create_fleet_enemy(screen, enemy_group, level=1):
    """Создает флот пришельцев."""
    # Создание пришельца и вычисление количества пришельцев в ряду.
    enemy = Enemy(screen)
    screen_rect = screen.get_rect()
    number_max_x = screen_rect.right // (enemy.rect.width * 3)
    numb_enemy = level * number_max_x // 3
    number_enemy_x = (numb_enemy - numb_enemy // number_max_x)
    if number_enemy_x > 12:
        number_enemy_x = 12
    number_rows = numb_enemy // number_max_x
    if number_rows <= 1:
        number_rows = 2
    if number_rows <= 3:
        number_rows = 2
    for row_number in range(number_rows):
        for enemy_number in range(number_enemy_x):
            create_enemy(screen, enemy_group, enemy_number,
                         row_number)


def update_bullets(screen, enemy_group, bullets, stats):
    """Обновляет позиции пуль и уничтожает старые пули."""
    # Обновление позиций пуль.
    bullets.update()
    # Удаление пуль, вышедших за край экрана.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(screen, enemy_group, bullets, stats)


def check_bullet_alien_collisions(screen, enemy_group, bullets, stats):
    # Проверка попаданий в пришельцев.
    # При обнаружении попадания удалить пулю и пришельца.
    global level_game
    collisions = pygame.sprite.groupcollide(bullets, enemy_group, True, True)
    if collisions:
        stats.score += 100
        stats.high_score += 100
    if len(enemy_group) == 0:
        stats.level += 1
        bullets.empty()
        create_fleet_enemy(screen, enemy_group, stats.level)


def check_wall_enemy_collisions(wall_group_down, wall_group_up, ladder, enemy_group, player, stats, traider_group):
    if stats.hp_wall <= 0:
        player.position_up = False
        player.position_on_ladder = False
        wall_group_down.empty()
        wall_group_up.empty()
        ladder.empty()
        traider_group.empty()
    else:
        if pygame.sprite.groupcollide(wall_group_up, enemy_group, False, True):
            stats.hp_wall -= 5


def update_screen(screen, background, player, bullets, wall_group_down, wall_group_up, ground_group, enemy_group,
                  ladder_group, end_group, door_group, camera, stats, sb, player_group, traider_group):
    global camera_g
    player.update(wall_group_up, wall_group_down, ladder_group, ground_group)
    background.fill((0, 255, 50))
    camera.update(player)
    update_bullets(background, enemy_group, bullets, stats)
    check_wall_enemy_collisions(wall_group_down, wall_group_up, ladder_group, enemy_group, player, stats, traider_group)
    enemy_group.update(wall_group_up, enemy_group)
    check_bullet_alien_collisions(screen, enemy_group, bullets, stats)
    if pygame.sprite.groupcollide(player_group, enemy_group, False, True):
        stats.hp_hero -= 5
    check_win(end_group, enemy_group, stats)
    camera_mod(screen, wall_group_down, wall_group_up, camera, ground_group, enemy_group, ladder_group, bullets,
               end_group, traider_group)


def check_win(end_group, enemy_group, stats):
    collisions = pygame.sprite.groupcollide(end_group, enemy_group, False, True)
    if collisions or stats.hp_hero <= 0:
        stats.game_over = True


def camera_mod(screen, wall_group_down, wall_group_up, camera, ground_group, enemy_group, ladder_group, bullets,
               end_group, traider_group):
    n1 = True
    n2 = True
    screen_rect = screen.get_rect()
    for sprite in ground_group:
        if sprite.first_x or sprite.end_x:
            n1 = camera.cheak_x(sprite, screen_rect.w)
        if not n1:
            break
    for sprite in ground_group:
        if sprite.first_y or sprite.end_y:
            n2 = camera.cheak_y(sprite, screen_rect.h)
        if not n2:
            break
    if n1 and n2:
        for sprite in wall_group_down:
            camera.apply(sprite)
        for sprite in end_group:
            camera.apply(sprite)
        for sprite in wall_group_up:
            camera.apply(sprite)
        for sprite in ground_group:
            camera.apply(sprite)
        for sprite in ladder_group:
            camera.apply(sprite)
        for sprite in enemy_group:
            camera.apply(sprite)
        for sprite in bullets:
            camera.apply(sprite)
        for sprite in traider_group:
            camera.apply(sprite)
