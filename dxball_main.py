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
        self.height = 30
        self.width = 50
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

    def draw_ball(self):

        if self.level_started:
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
    scoretext = myfont.render(f"Score: {score}", 1, (255, 0, 0))
    win.blit(scoretext, (5, 5))

    for block in level_1.blocks:
        block.draw()
    pygame.display.update()


class Level(object):
    '''
    Class to set up a level of blocks
    '''
    def __init__(self):
        self.blocks_hit = 0
        b1 = Block(300, 10)
        b2 = Block(100, 100)
        b3 = Block(200, 200)
        b4 = Block(300, 300)
        b5 = Block(400, 400)
        b6 = Block(500, 500)
        b7 = Block(600, 600)
        b8 = Block(600, 400)
        b9 = Block(600, 200)
        b10 = Block(700, 100)

        self.blocks = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10]

    def remove_block(self, block):
        self.blocks.remove(block)
        self.blocks_hit += 1
        print(f"HIT BLOCK {block}! Hit count at {self.blocks_hit}")



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
            gb.level_started = True

    keys = pygame.key.get_pressed()

    if gb.y >= window_height - 5:
        gb.vel = 0
    elif paddle.y < gb.y < paddle.y + paddle.height and paddle.x < gb.x < paddle.x + paddle.width:
        gb.y_direction = gb.y_direction*-1

    for block in level_1.blocks:
        if block.y < gb.y < block.y + block.height and block.x < gb.x < block.x + block.width:
            level_1.remove_block(block)

    redrawGameWindow()

pygame.quit()
