import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Donkey X Ball")
clock = pygame.time.Clock()

class Paddle(object):
    '''
    Main class for the paddle
    '''
    def __init__(self):
        self.y = 480
        self.x = 200

        self.height = 20
        self.width = 75
        self.vel = 20
        self.color = (0, 0, 255)

    def draw_paddle(self):
        self.x, _ = pygame.mouse.get_pos()
        pygame.draw.rect(win, self.color,
                         (self.x, self.y, self.width, self.height))


class GameBall(object):
    '''
    Main class for the game ball
    '''
    def __init__(self):
        self.x = 100
        self.y = 280
        self.x_direction = 1
        self.y_direction = 1
        self.radius = 5
        self.vel = 10
        self.color = (0, 255, 255)

    def draw_ball(self):
        if self.x <=5:
            self.x_direction = 1
        elif self.x >= 490:
            self.x_direction = -1

        if self.y <=5:
            self.y_direction = 1
        elif self.y >= 490:
            self.y_direction = -1

        self.x = self.x + (self.x_direction * self.vel)
        self.y = self.y + (self.y_direction * self.vel)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

def redrawGameWindow():
    win.fill((0, 0, 0))
    paddle.draw_paddle()
    gb.draw_ball()
    pygame.display.update()


run = True
paddle = Paddle()
gb = GameBall()

while run:
    #pygame.time.delay(100)
    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and paddle.x > paddle.vel:
        print(f"paddle width: {paddle.width}")
        paddle.x -= paddle.vel

    elif keys[pygame.K_RIGHT] and paddle.x < 500 - paddle.width - paddle.vel:
        print(f"paddle width: {paddle.width}")
        paddle.x += paddle.vel


    redrawGameWindow()

pygame.quit()
