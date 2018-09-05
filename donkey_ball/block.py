import donkey_ball as db

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
        db.pygame.draw.rect(db.win, self.color,
                         (self.x, self.y, self.width, self.height))

    def __str__(self):
        return f"Block at ({self.x}, {self.y})"
