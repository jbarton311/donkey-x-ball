import pygame
import random

import donkey_ball as db
from donkey_ball.paddle import Paddle
from donkey_ball.scoreboard import Scoreboard
from donkey_ball.game_ball import GameBall
from donkey_ball.level import Level

run = True
paddle = Paddle()
gb = GameBall()
level_1 = Level()
sb = Scoreboard(gb, level_1, paddle)
paddle_group = db.pygame.sprite.Group()
paddle_group.add(paddle)

ball_group = db.pygame.sprite.Group()
ball_group.add(gb)


def redrawGameWindow():
    db.win.fill((0, 0, 0))
    paddle_group.update()
    paddle_group.draw(db.win)

    ball_group.update()
    ball_group.draw(db.win)

    #gb.draw_ball()
    sb.draw()

    for block in level_1.blocks:
        block.draw()
    db.pygame.display.update()


while run:
    # pygame.time.delay(100)
    db.clock.tick(60)

    for event in db.pygame.event.get():
        if event.type == db.pygame.QUIT:
            run = False
        # Wait to start moving ball until a click
        if event.type == db.pygame.MOUSEBUTTONDOWN:
            if gb.still_alive and not gb.ball_started:
                gb.ball_started = True

    keys = db.pygame.key.get_pressed()

    if keys[db.pygame.K_SPACE] and gb.lives == 0:
        gb.restart_game()
        level_1.restart_level()

    collide = pygame.sprite.spritecollide(gb, paddle_group, False, pygame.sprite.collide_mask)
    if collide:
        gb.y_direction = gb.y_direction*-1
        #print("BOOOOOOOOM")

    # If the ball gets within 15 pixels of the bottom we are saying that's an L
    if gb.y >= db.window_height - 5:
        gb.level_status = "YOU BLEW IT (Sandler voice)"
        gb.lost_life()
        gb.ball_started = False
        gb.new_life = True

    # If the ball hits the paddle

    # Loop thru each block and figure out if it got hit
    for block in level_1.blocks:
        if block.y < gb.y < block.y + block.height and block.x < gb.x < block.x + block.width:
            if gb.y == block.y:
                print("Hit top of block")
            elif gb.y == block.y + block.height:
                print("Hit bottom of block")
            elif gb.x == block.x:
                print("Hit left of block")
            elif gb.x == block.x + block.width:
                print("Hit right of block")
            else:
                print(f"GB-x:{gb.x} GB-y:{gb.y} blockx:{block.x} blocky:{block.y} block-bottom:{block.y + block.height} ")
            # db.ball_hit_sound.play()
            level_1.remove_block(block)
            gb.blocks_hit += 1
            if random.randint(1, 4) == 3:
                gb.special_power = random.choice(['Thru Ball', 'Fire Ball', 'Something bad'])

    redrawGameWindow()

print(f"Game ball hits: {gb.blocks_hit}")
db.pygame.quit()
