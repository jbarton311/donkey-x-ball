import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Donkey X Ball")


class Paddle(object):
    '''
    Main class for the paddle
    '''
    def __init__(self):
        self.x = 250
        self.y = 480
        self.height = 20
        self.width = 75
        self.vel = 5
        self.color = (0, 0, 255)

    def draw_paddle(self):
        pygame.draw.rect(win, self.color,
                        (self.x, self.y, self.width, self.height))


def redrawGameWindow():
    pygame.display.update()
    paddle.draw_paddle()


run = True
paddle = Paddle()

while run:
    pygame.time.delay(100)

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
