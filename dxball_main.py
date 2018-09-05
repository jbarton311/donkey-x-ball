import donkey_ball as db
from donkey_ball.paddle import Paddle
from donkey_ball.scoreboard import Scoreboard
from donkey_ball.game_ball import GameBall
from donkey_ball.level import Level
import random

run = True
paddle = Paddle()
gb = GameBall()
level_1 = Level()
sb = Scoreboard(gb, level_1, paddle)


def redrawGameWindow():
    db.win.fill((0, 0, 0))
    paddle.draw_paddle()
    gb.draw_ball()
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

    # If the ball gets within 15 pixels of the bottom we are saying that's an L
    if gb.y >= db.window_height - 15:
        gb.level_status = "YOU BLEW IT (Sandler voice)"
        gb.lost_life()
        gb.ball_started = False
        gb.new_life = True

    # If the ball hits the paddle
    elif paddle.y < gb.y < paddle.y + paddle.height and paddle.x < gb.x < paddle.paddle_right_edge:
        ball_x_on_paddle = (gb.x - paddle.x) / paddle.width
        print(ball_x_on_paddle)

        if ball_x_on_paddle <= 0.5:
            gb.x_direction = -1
            gb.y_slope = 1 * (1 - ball_x_on_paddle)
            if ball_x_on_paddle <= 0.4:
                gb.y_slope = 2 * (1 - ball_x_on_paddle)
            elif ball_x_on_paddle <= 0.3:
                gb.y_slope = 3 * (1 - ball_x_on_paddle)
            elif ball_x_on_paddle <= 0.2:
                gb.y_slope = 4 * (1 - ball_x_on_paddle)
            elif ball_x_on_paddle <= 0.1:
                gb.y_slope = 5 * (1 - ball_x_on_paddle)

        elif ball_x_on_paddle > 0.5:
            gb.x_direction = 1
            gb.y_slope = 3 * ball_x_on_paddle
            if ball_x_on_paddle >= 0.6:
                gb.y_slope = 5 * (1 - ball_x_on_paddle)
            elif ball_x_on_paddle >= 0.7:
                gb.y_slope = 4 * (1 - ball_x_on_paddle)
            elif ball_x_on_paddle >= 0.8:
                gb.y_slope = 3 * (1 - ball_x_on_paddle)
            elif ball_x_on_paddle >= 0.9:
                gb.y_slope = 2 * (1 - ball_x_on_paddle)

        print("SOMETHING HIT!")
        gb.y_direction = gb.y_direction*-1

        if gb.x < paddle.paddle_mid:
            gb.x_direction = -1
        elif gb.x > paddle.paddle_mid:
            gb.x_direction = 1

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
