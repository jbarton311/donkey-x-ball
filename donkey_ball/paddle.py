import donkey_ball as db
import pygame

class Paddle(pygame.sprite.Sprite):
    '''
    Main class for the paddle
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("img/glasspaddle2.png").convert_alpha(), [100, 12])
        self.mask = db.pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0, 0, 0))
        self.rect.center = (db.window_width / 2, db.window_height  - 15)
        self.y = db.window_height - 23
        self.x = 200
        self.height = 10
        self.width = 75
        self.vel = 20
        self.color = (193, 202, 214)

    def calc_mid_point(self):
        self.paddle_right_edge = self.x + self.width
        self.paddle_mid = ((self.paddle_right_edge - self.x) / 2) + self.x

    def update(self):
        self.rect.centerx, _ = db.pygame.mouse.get_pos()
