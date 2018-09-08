import donkey_ball as db
import pygame

class Block(pygame.sprite.Sprite):
    '''
    Main class for a standard block
    '''
    def __init__(self, x, y, color=(51, 101, 138)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("img/Blue Brick for Donk.png").convert_alpha(), [40, 20])
        self.mask = db.pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0, 0, 0))
        self.rect.left = x
        self.rect.top = y
        self.height = 20
        self.width = 40
        self.color = color

    def __str__(self):
        return f"Block at ({self.x}, {self.y})"

class RedBlock(Block):
    '''
    RedBlock
    '''
    def __init__(self, *args, **kwargs):
        super(RedBlock, self).__init__(*args, **kwargs)
        self.image = pygame.transform.scale(pygame.image.load("img/Red Brick for Donk.png").convert_alpha(), [40, 20])


class WhiteBlock(Block):
    '''
    RedBlock
    '''
    def __init__(self, *args, **kwargs):
        super(WhiteBlock, self).__init__(*args, **kwargs)
        self.image = pygame.transform.scale(pygame.image.load("img/White Brick for Donk.png").convert_alpha(), [40, 20])
