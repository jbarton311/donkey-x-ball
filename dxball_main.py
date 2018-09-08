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


def redrawGameWindow():
    db.win.fill((0, 0, 0))
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


    brick_collide = pygame.sprite.spritecollide(gb, level_1.brick_group, True, pygame.sprite.collide_mask)
    if brick_collide:
        print(brick_collide)
        print("Brick Collide")
    # Loop thru each block and figure out if it got hit
    '''
            if random.randint(1, 4) == 3:
                gb.special_power = random.choice(['Thru Ball', 'Fire Ball', 'Something bad'])
    '''
    redrawGameWindow()

print(f"Game ball hits: {gb.blocks_hit}")
db.pygame.quit()
