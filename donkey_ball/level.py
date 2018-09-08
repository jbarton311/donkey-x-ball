from donkey_ball.block import Block, RedBlock, WhiteBlock
import pygame


class Level(object):
    '''
    Class to set up a level of blocks
    '''
    def __init__(self):
        self.blocks_hit = 0
        d1 = RedBlock(100, 100)
        d2 = RedBlock(100, 150)
        d3 = RedBlock(100, 200)
        d4 = RedBlock(100, 250)
        d5 = RedBlock(100, 300)
        d6 = RedBlock(100, 350)
        d7 = RedBlock(175, 350)
        d8 = RedBlock(250, 350)
        d9 = RedBlock(300, 300)
        d10 = RedBlock(300, 250)
        d11 = RedBlock(300, 200)
        d12 = RedBlock(300, 150)
        d13 = RedBlock(250, 100)
        d14 = RedBlock(175, 100)

        b1 = WhiteBlock(400, 100)
        b2 = WhiteBlock(400, 150)
        b3 = WhiteBlock(400, 200)
        b4 = WhiteBlock(400, 250)
        b5 = WhiteBlock(400, 300)
        b6 = WhiteBlock(400, 350)
        b7 = WhiteBlock(475, 350)
        b8 = WhiteBlock(550, 350)
        b9 = WhiteBlock(600, 300)
        b10 = WhiteBlock(600, 250)
        b11 = WhiteBlock(600, 200)
        b12 = WhiteBlock(600, 150)
        b13 = WhiteBlock(550, 100)
        b14 = WhiteBlock(475, 100)
        b15 = WhiteBlock(475, 225)
        b16 = WhiteBlock(550, 225)

        t1 = Block(850, 100)
        t2 = Block(850, 150)
        t3 = Block(850, 200)
        t4 = Block(850, 250)
        t5 = Block(850, 300)
        t6 = Block(850, 350)
        t7 = Block(730, 100)
        t8 = Block(790, 100)
        t9 = Block(910, 100)
        t10 = Block(970, 100)

        self.blocks = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14,
                       b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16,
                       t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]
        self.level_name = "DBT"

        self.brick_group = pygame.sprite.Group()
        for block in self.blocks:
            self.brick_group.add(block)


    def score_calc(self):
        self.blocks_hit = len(self.blocks) - len(self.brick_group)
        return self.blocks_hit


    def string_level_name(self):
        return f"LEVEL: {self.level_name}"


    def restart_level(self):
        self.__init__()
