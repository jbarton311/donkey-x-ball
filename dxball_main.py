import pygame
import donkey_ball as db
from donkey_ball.paddle import Paddle
from donkey_ball.scoreboard import Scoreboard
from donkey_ball.level import Level
from donkey_ball.game_ball import GameBall


run = True
paddle = Paddle()
gb = GameBall()
level_1 = Level()
sb = Scoreboard(gb, level_1, paddle)
paddle_group = db.pygame.sprite.Group()
paddle_group.add(paddle)

ball_group = db.pygame.sprite.Group()
ball_group.add(gb)

bg = pygame.image.load("img/space-2.jpg")

def redrawGameWindow():
    db.win.blit(bg, (0, 0))
    paddle_group.update()
    paddle_group.draw(db.win)

    ball_group.update()
    ball_group.draw(db.win)

    level_1.brick_group.update()
    level_1.brick_group.draw(db.win)

    sb.draw()
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
    if gb.y >= db.window_height - 5:
        gb.level_status = "YOU BLEW IT (Sandler voice)"
        gb.lost_life()
        gb.ball_started = False
        gb.new_life = True

    collide = pygame.sprite.spritecollide(gb, paddle_group, False, pygame.sprite.collide_mask)
    if collide:
        ball_x_on_paddle = (gb.x - paddle.x) / paddle.width
        print(ball_x_on_paddle)

        print("SOMETHING HIT!")
        gb.y_direction = gb.y_direction*-1

        print(f"paddle.paddle_mid = {paddle.rect.centerx}, gb.x = {gb.x}")

        if gb.x < paddle.rect.centerx:
            gb.x_direction = -1
        elif gb.x > paddle.rect.centerx:
            gb.x_direction = 1



    brick_collide = pygame.sprite.spritecollide(gb, level_1.brick_group, False, pygame.sprite.collide_mask)
    if brick_collide:
        hit_block = brick_collide[0]
        collide_dict = {}
        ball_x, ball_y = gb.x, gb.y
        print(f"Ball location: X={ball_x}, Y={ball_y}")
        print(hit_block.rect.left)
        print(hit_block.rect.right)
        print(hit_block.rect.top)
        print(hit_block.rect.bottom)

        collide_dict['left'] = abs(hit_block.rect.left - ball_x)
        collide_dict['right'] = abs(hit_block.rect.right - ball_x)

        collide_dict['top'] = abs(hit_block.rect.top - ball_y)
        collide_dict['bottom'] = abs(hit_block.rect.bottom - ball_y)

        print(f"FROM LEFT: {collide_dict['left']}")
        print(f"FROM RIGHT: {collide_dict['right']}")
        print(f"FROM TOP: {collide_dict['top']}")
        print(f"FROM BOTTOM: {collide_dict['bottom']}")

        hit_location = min(collide_dict, key=collide_dict.get)

        # i THINK WE NEED TO CHECK THE VELOCITY OF THE Ball
        # IF IT IS GOING RIGHT THEN IT CAN'T HIT THE RIGHT SIDE
        if hit_location == 'left' and gb.x_direction == 1 and collide_dict['left'] <= 8:
            gb.x_direction = gb.x_direction * -1
        elif hit_location == 'right' and gb.x_direction == -1 and collide_dict['right'] <= 8:
            gb.x_direction = gb.x_direction * -1

        elif hit_location == 'top' and gb.y_direction == 1:
            gb.y_direction = gb.y_direction * -1

        elif hit_location == 'bottom' and gb.y_direction == -1:
            gb.y_direction = gb.y_direction * -1

        elif hit_location in ['left','right']:
            gb.x_direction = gb.x_direction * -1
        else:
            gb.y_direction = gb.y_direction * -1

        level_1.brick_group.remove(brick_collide)

    '''
            if random.randint(1, 4) == 3:
                gb.special_power = random.choice(['Thru Ball', 'Fire Ball', 'Something bad'])
    '''
    redrawGameWindow()

print(f"Game ball hits: {gb.blocks_hit}")
db.pygame.quit()
