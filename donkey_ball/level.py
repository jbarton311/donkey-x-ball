from donkey_ball.block import Block


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
