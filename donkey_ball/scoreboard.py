import donkey_ball as db


class Scoreboard():
    def __init__(self, game_ball, level, paddle):
        self.game_ball = game_ball
        self.level = level
        self.paddle = paddle
        self.score = 0

    def draw(self):
        blue_text = (36, 123, 160)
        red_text = (255, 107, 107)
        x_right_side_align = db.window_width - 150
        # Set up dividing bar between scoreboard and game
        db.pygame.draw.rect(db.win, (33, 131, 128),
                           (0, db.dividing_bar_y, db.window_width, db.dividing_bar_height))

        donkey_title = db.myfont.render("Donkey X Ball", 1, blue_text)
        db.win.blit(donkey_title, (db.window_width/2 - 50, 12))
        # Print Out Score
        scoretext = db.myfont.render(f"SCORE: {self.level.score_calc()}", 1, red_text)
        db.win.blit(scoretext, (5, 12))

        # Print Out Level Name
        level_text = db.small_font.render(self.level.string_level_name(), 1, blue_text)
        db.win.blit(level_text, (x_right_side_align, 5))

        if self.game_ball.still_alive_check() is False:
            level_situation = 'GAME OVER'
        elif self.game_ball.level_status:
            level_situation = self.game_ball.level_status
        else:
            level_situation = "Play the game, kid!"

        level_status = db.small_font.render(level_situation, 1, blue_text)
        db.win.blit(level_status, (x_right_side_align, 22))

        loggin_text = f"LIVES: {self.game_ball.lives}"
        loggin_print = db.myfont.render(loggin_text, 1, red_text)
        db.win.blit(loggin_print, (100, 12))

        random_power = db.small_font.render(f"Power Up: {self.game_ball.special_power}", 1, (253, 255, 252))
        db.win.blit(random_power, (200, 12))

        self.paddle.update()
        paddle_mid = db.small_font.render(f"Paddle-mid: {self.paddle.paddle_mid}", 1, (253, 255, 252))
        db.win.blit(paddle_mid, (650, 12))
