import pygame
pygame.init()
pygame.font.init()

window_width = 800
window_height = 600
win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Donkey X Ball")
clock = pygame.time.Clock()
myfont = pygame.font.SysFont('Arial Bold', 22)


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
        self.color = (0, 0, 255)

    def draw_paddle(self):
        self.x, _ = pygame.mouse.get_pos()
        pygame.draw.rect(win, self.color,
                         (self.x, self.y, self.width, self.height))


class Block(object):
    '''
    Main class for a standard block
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 20
        self.width = 40
        self.color = (123, 28, 255)

    def draw(self):
        pygame.draw.rect(win, self.color,
                         (self.x, self.y, self.width, self.height))


class GameBall(object):
    '''
    Main class for the game ball
    '''
    def __init__(self):
        self.x = 200
        self.y = window_height - 28
        self.x_direction = 1
        self.y_direction = 1
        self.radius = 5
        self.vel = 0
        self.color = (0, 255, 255)
        self.level_started = False
        self.still_alive = True

    def draw_ball(self):
        if self.still_alive:
            if self.level_started and self.still_alive:
                self.vel = 5
            else:
                self.x = pygame.mouse.get_pos()[0] + 37
            # Make sure ball stays within window
            if self.x <= 5:
                self.x_direction = 1
            elif self.x >= window_width - self.radius:
                self.x_direction = -1

            if self.y <= 5:
                self.y_direction = 1
            elif self.y >= window_height - self.radius:
                self.y_direction = -1

            self.x = self.x + (self.x_direction * self.vel)
            self.y = self.y + (self.y_direction * self.vel)
            pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redrawGameWindow():
    win.fill((0, 0, 0))
    paddle.draw_paddle()
    gb.draw_ball()
    score = level_1.blocks_hit

    # Print Out Score
    scoretext = myfont.render(f"Score: {score}", 1, (255, 0, 0))
    win.blit(scoretext, (5, 5))

    # Print Out Level Name
    level_text = myfont.render(level_1.string_level_name(), 1, (122, 122, 200))
    win.blit(level_text, (700, 5))

    if gb.level_started:
        level_situation = gb.level_started
    else:
        level_situation = "Play the game, kid!"

    level_status = myfont.render(level_situation, 1, (122, 122, 200))
    win.blit(level_status, (300, 5))

    #loggin_text = f"Ball Y: {gb.y}, Window Height: {window_height}"
    #loggin_print = myfont.render(loggin_text, 1, (122, 122, 200))
    #win.blit(loggin_print, (300, 50))

    for block in level_1.blocks:
        block.draw()
    pygame.display.update()


class Level(object):
    '''
    Class to set up a level of blocks
    '''
    def __init__(self):
        self.blocks_hit = 0

        d1 = Block(100, 100)
        d2 = Block(100, 150)
        d3 = Block(100, 200)
        d4 = Block(100, 250)
        d5 = Block(100, 300)
        d6 = Block(100, 350)
        d7 = Block(175, 350)
        d8 = Block(250, 350)
        d9 = Block(300, 300)
        d10 = Block(300, 250)
        d11 = Block(300, 200)
        d12 = Block(300, 150)
        d13 = Block(250, 100)
        d14 = Block(175, 100)

        b1 = Block(400, 100)
        b2 = Block(400, 150)
        b3 = Block(400, 200)
        b4 = Block(400, 250)
        b5 = Block(400, 300)
        b6 = Block(400, 350)
        b7 = Block(475, 350)
        b8 = Block(550, 350)
        b9 = Block(600, 300)
        b10 = Block(600, 250)
        b11 = Block(600, 200)
        b12 = Block(600, 150)
        b13 = Block(550, 100)
        b14 = Block(475, 100)
        b15 = Block(475, 225)
        b16 = Block(550, 225)



        self.blocks = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14,
                        b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16]
        self.level_name = "DBT"

    def remove_block(self, block):
        self.blocks.remove(block)
        self.blocks_hit += 1
        print(f"HIT BLOCK {block}! Hit count at {self.blocks_hit}")

    def string_level_name(self):
        return f"LEVEL: {self.level_name}"


run = True
paddle = Paddle()
gb = GameBall()
level_1 = Level()

while run:
    #pygame.time.delay(100)
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            gb.level_started = "Game on!"

    keys = pygame.key.get_pressed()

    if gb.y >= window_height - 15:
        print("FIRST CONDITION")
        gb.level_started = "BOTCH JOB HAHA"
        gb.still_alive = False
    elif paddle.y < gb.y < paddle.y + paddle.height and paddle.x < gb.x < paddle.x + paddle.width:
        print("SOMETHING HIT!")
        gb.y_direction = gb.y_direction*-1

    for block in level_1.blocks:
        if block.y < gb.y < block.y + block.height and block.x < gb.x < block.x + block.width:
            level_1.remove_block(block)

    redrawGameWindow()

pygame.quit()
