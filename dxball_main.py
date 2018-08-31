import pygame
import random

pygame.init()
pygame.font.init()

window_width = 1100
window_height = 600
dividing_bar_y = 36
dividing_bar_height = 6

win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Donkey X Ball")
clock = pygame.time.Clock()
myfont = pygame.font.SysFont('Arial Bold', 22)
small_font = pygame.font.SysFont('Arial Bold', 15)

ball_hit_sound = pygame.mixer.Sound('quick_fart_x.wav')
lost_ball_sound = pygame.mixer.Sound('toilet_flushing.wav')
music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)


class Paddle(object):
    '''
    Main class for the paddle
    '''
    def __init__(self):
        self.y = window_height - 23
        self.x = 200
        self.height = 10
        self.width = 75
        self.vel = 20
        self.color = (193, 202, 214)

    def calc_mid_point(self):
        self.paddle_right_edge = self.x + self.width
        self.paddle_mid = ((self.paddle_right_edge - self.x) / 2) + self.x

    def draw_paddle(self):
        self.x, _ = pygame.mouse.get_pos()
        pygame.draw.rect(win, self.color,
                         (self.x, self.y, self.width, self.height))


class Block(object):
    '''
    Main class for a standard block
    '''
    def __init__(self, x, y, color=(51, 101, 138)):
        self.x = x
        self.y = y
        self.height = 20
        self.width = 40
        self.color = color

    def draw(self):
        pygame.draw.rect(win, self.color,
                         (self.x, self.y, self.width, self.height))

    def __str__(self):
        return f"Block at ({self.x}, {self.y})"


class Scoreboard():
    def __init__(self, game_ball, level, paddle):
        self.game_ball = game_ball
        self.level = level
        self.paddle = paddle
        self.score = 0

    def draw(self):
        blue_text = (36, 123, 160)
        red_text = (255, 107, 107)
        x_right_side_align = window_width - 150
        # Set up dividing bar between scoreboard and game
        pygame.draw.rect(win, (33, 131, 128),
                         (0, dividing_bar_y, window_width, dividing_bar_height))



        donkey_title = myfont.render("Donkey X Ball", 1, blue_text)
        win.blit(donkey_title, (window_width/2 - 50, 12))
        # Print Out Score
        scoretext = myfont.render(f"SCORE: {self.game_ball.blocks_hit}", 1, red_text)
        win.blit(scoretext, (5, 12))



        # Print Out Level Name
        level_text = small_font.render(level_1.string_level_name(), 1, blue_text)
        win.blit(level_text, (x_right_side_align, 5))

        if self.game_ball.still_alive_check() == False:
            level_situation = 'GAME OVER'
        elif self.game_ball.level_status:
            level_situation = self.game_ball.level_status
        else:
            level_situation = "Play the game, kid!"

        level_status = small_font.render(level_situation, 1, blue_text)
        win.blit(level_status, (x_right_side_align, 22))

        loggin_text = f"LIVES: {self.game_ball.lives}"
        loggin_print = myfont.render(loggin_text, 1, red_text)
        win.blit(loggin_print, (100, 12))

        random_power = small_font.render(f"Power Up: {self.game_ball.special_power}", 1, (253, 255, 252))
        win.blit(random_power, (200, 12))

        paddle.calc_mid_point()
        paddle_mid = small_font.render(f"Paddle-mid: {self.paddle.paddle_mid}", 1, (253, 255, 252))
        win.blit(paddle_mid, (650, 12))

class GameBall(object):
    '''
    Main class for the game ball
    '''
    def __init__(self):
        self.x = 200
        self.y = window_height - 28
        self.x_direction = 1
        self.y_direction = 1
        self.y_slope = 1.0
        self.radius = 5
        self.vel = 0
        self.color = (32, 252, 143)
        self.ball_started = False
        self.still_alive = True
        self.new_life = False
        self.level_status = "Play the game, kid!"
        self.lives = 3
        self.blocks_hit = 0
        self.special_power = None

    def lost_life(self):
        '''Function to reduce lives when ball passes paddle'''
        if self.lives > 0:
            self.lives -= 1

    def still_alive_check(self):
        '''Check to see if we are still alive.'''
        if self.lives >= 1:
            return True
        else:
            return False

    def restart_game(self):
        self.lives = 4
        self.blocks_hit = 0

    def ready_new_life(self):
        '''Variables to set for a new life'''
        self.vel = 0
        self.x = pygame.mouse.get_pos()[0] + 37
        self.y = window_height - 28
        self.y_direction = -1

    def draw_ball(self):
        '''Figure out where to draw the ball on the screen'''

        # Do they still have lives left? If so, go to logic
        if self.still_alive_check():

            # Is this a new life? Initialize variables
            if self.new_life and not self.ball_started:
                self.ready_new_life()

            # If the ball is started make it move!
            if self.ball_started:
                self.level_status = "Play ball, bro!"
                self.vel = 5
            # If not, make it stay on the paddle
            else:
                self.x = pygame.mouse.get_pos()[0] + 37

            # Make sure ball stays within window
            if self.x <= 5:
                self.x_direction = 1
            elif self.x >= window_width - self.radius:
                self.x_direction = -1

            if self.y <= dividing_bar_y + dividing_bar_height:
                self.y_direction = 1
            elif self.y >= window_height - self.radius:
                self.y_direction = -1

            # Make the ball move in the correct direction
            self.x = self.x + (self.x_direction * self.vel)
            self.y = int(self.y + (self.y_direction * self.vel) * self.y_slope)
            pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redrawGameWindow():
    win.fill((0, 0, 0))
    paddle.draw_paddle()
    gb.draw_ball()
    sb.draw()

    for block in level_1.blocks:
        block.draw()
    pygame.display.update()


class Level(object):
    '''
    Class to set up a level of blocks
    '''
    def __init__(self):
        self.blocks_hit = 0
        d_color = (5, 130, 202)
        b_color = (253, 255, 252)
        t_color = (231, 29, 54)

        d1 = Block(100, 100, d_color)
        d2 = Block(100, 150, d_color)
        d3 = Block(100, 200, d_color)
        d4 = Block(100, 250, d_color)
        d5 = Block(100, 300, d_color)
        d6 = Block(100, 350, d_color)
        d7 = Block(175, 350, d_color)
        d8 = Block(250, 350, d_color)
        d9 = Block(300, 300, d_color)
        d10 = Block(300, 250, d_color)
        d11 = Block(300, 200, d_color)
        d12 = Block(300, 150, d_color)
        d13 = Block(250, 100, d_color)
        d14 = Block(175, 100, d_color)

        b1 = Block(400, 100, b_color)
        b2 = Block(400, 150, b_color)
        b3 = Block(400, 200, b_color)
        b4 = Block(400, 250, b_color)
        b5 = Block(400, 300, b_color)
        b6 = Block(400, 350, b_color)
        b7 = Block(475, 350, b_color)
        b8 = Block(550, 350, b_color)
        b9 = Block(600, 300, b_color)
        b10 = Block(600, 250, b_color)
        b11 = Block(600, 200, b_color)
        b12 = Block(600, 150, b_color)
        b13 = Block(550, 100, b_color)
        b14 = Block(475, 100, b_color)
        b15 = Block(475, 225, b_color)
        b16 = Block(550, 225, b_color)

        t1 = Block(850, 100, t_color)
        t2 = Block(850, 150, t_color)
        t3 = Block(850, 200, t_color)
        t4 = Block(850, 250, t_color)
        t5 = Block(850, 300, t_color)
        t6 = Block(850, 350, t_color)
        t7 = Block(730, 100, t_color)
        t8 = Block(790, 100, t_color)
        t9 = Block(910, 100, t_color)
        t10 = Block(970, 100, t_color)

        self.blocks = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14,
                       b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16,
                       t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]
        self.level_name = "DBT"

    def remove_block(self, block):
        ''' Will remove a block from the list. Will use when a block gets hit'''
        self.blocks.remove(block)
        self.blocks_hit += 1
        print(f"HIT BLOCK {block}! Hit count at {self.blocks_hit}")

    def string_level_name(self):
        return f"LEVEL: {self.level_name}"

    def restart_level(self):
        d_color = (5, 130, 202)
        b_color = (253, 255, 252)
        t_color = (231, 29, 54)

        d1 = Block(100, 100, d_color)
        d2 = Block(100, 150, d_color)
        d3 = Block(100, 200, d_color)
        d4 = Block(100, 250, d_color)
        d5 = Block(100, 300, d_color)
        d6 = Block(100, 350, d_color)
        d7 = Block(175, 350, d_color)
        d8 = Block(250, 350, d_color)
        d9 = Block(300, 300, d_color)
        d10 = Block(300, 250, d_color)
        d11 = Block(300, 200, d_color)
        d12 = Block(300, 150, d_color)
        d13 = Block(250, 100, d_color)
        d14 = Block(175, 100, d_color)

        b1 = Block(400, 100, b_color)
        b2 = Block(400, 150, b_color)
        b3 = Block(400, 200, b_color)
        b4 = Block(400, 250, b_color)
        b5 = Block(400, 300, b_color)
        b6 = Block(400, 350, b_color)
        b7 = Block(475, 350, b_color)
        b8 = Block(550, 350, b_color)
        b9 = Block(600, 300, b_color)
        b10 = Block(600, 250, b_color)
        b11 = Block(600, 200, b_color)
        b12 = Block(600, 150, b_color)
        b13 = Block(550, 100, b_color)
        b14 = Block(475, 100, b_color)
        b15 = Block(475, 225, b_color)
        b16 = Block(550, 225, b_color)

        t1 = Block(850, 100, t_color)
        t2 = Block(850, 150, t_color)
        t3 = Block(850, 200, t_color)
        t4 = Block(850, 250, t_color)
        t5 = Block(850, 300, t_color)
        t6 = Block(850, 350, t_color)
        t7 = Block(730, 100, t_color)
        t8 = Block(790, 100, t_color)
        t9 = Block(910, 100, t_color)
        t10 = Block(970, 100, t_color)

        self.blocks = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14,
                       b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16,
                       t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]


run = True
paddle = Paddle()
gb = GameBall()
level_1 = Level()
sb = Scoreboard(gb, level_1, paddle)

while run:
    # pygame.time.delay(100)
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Wait to start moving ball until a click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if gb.still_alive and not gb.ball_started:
                gb.ball_started = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and gb.lives == 0:
        gb.restart_game()
        level_1.restart_level()

    # If the ball gets within 15 pixels of the bottom we are saying that's an L
    if gb.y >= window_height - 15:
        gb.level_status = "YOU BLEW IT (Sandler voice)"
        gb.lost_life()
        gb.ball_started = False
        gb.new_life = True

    # If the ball hits the paddle
    elif paddle.y < gb.y < paddle.y + paddle.height and paddle.x < gb.x < paddle.paddle_right_edge:
        ball_x_on_paddle = (gb.x - paddle.x) / paddle.width
        '''
        if ball_x_on_paddle < 0.5:
            gb.x_direction = -1
            gb.y_slope = 5 * ball_x_on_paddle

        elif ball_x_on_paddle >= 0.5:
            gb.x_direction = 1
            gb.y_slope = 5 * (1 - ball_x_on_paddle)
        '''
        print("SOMETHING HIT!")
        gb.y_direction = gb.y_direction*-1
        if gb.x < paddle.paddle_mid:
            gb.x_direction = -1
        elif gb.x > paddle.paddle_mid:
            gb.x_direction = 1


    # Loop thru each block and figure out if it got hit
    for block in level_1.blocks:
        if block.y < gb.y < block.y + block.height and block.x < gb.x < block.x + block.width:
            ball_hit_sound.play()
            level_1.remove_block(block)
            gb.blocks_hit += 1
            if random.randint(1, 4) == 3:
                gb.special_power = random.choice(['Thru Ball', 'Fire Ball', 'Something bad'])

    redrawGameWindow()

print(f"Game ball hits: {gb.blocks_hit}")
pygame.quit()
