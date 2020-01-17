class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self):
        """Инициализирует статистику."""
        self.high_score = 0
        self.reset_stats()
        self.game_active = True
        self.game_intro = True
        self.game_over = False
        self.game_pause = False
        self.game_return = False
        self.game_shop = False
        self.count_hp_wall = 100
        self.count_hp_hero = 100
        self.max_up_hp_wall = 300
        self.max_up_hp_hero = 200

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.score = 0
        self.level = 1
        self.hp_wall = 100
        self.hp_hero = 100
