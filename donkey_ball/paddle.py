import donkey_ball as db


class Paddle(object):
    '''
    Main class for the paddle
    '''
    def __init__(self):
        self.y = db.window_height - 23
        self.x = 200
        self.height = 10
        self.width = 75
        self.vel = 20
        self.color = (193, 202, 214)

    def calc_mid_point(self):
        self.paddle_right_edge = self.x + self.width
        self.paddle_mid = ((self.paddle_right_edge - self.x) / 2) + self.x

    def draw_paddle(self):
        self.x, _ = db.pygame.mouse.get_pos()
        db.pygame.draw.rect(db.win, self.color,
                         (self.x, self.y, self.width, self.height))
