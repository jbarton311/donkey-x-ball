import pygame
import logging
import random

import donkey_ball as db
from donkey_ball.paddle import Paddle
from donkey_ball.scoreboard import Scoreboard
from donkey_ball.level import Level
from donkey_ball.game_ball import GameBall

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter('%(asctime)s-%(levelname)s: %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# Initialize all of our donkey objects
run = True

# Have to set up sprite groups for pixel-perfect collision detection
paddle = Paddle()
paddle_group = db.pygame.sprite.Group()
paddle_group.add(paddle)

gb = GameBall()
level_1 = Level()
sb = Scoreboard(gb, level_1, paddle)

ball_group = db.pygame.sprite.Group()
ball_group.add(gb)

# Load background for the game
bg = pygame.image.load("img/space-2.jpg")
bg = pygame.transform.scale(bg, (db.window_width, db.window_height)).convert()

# Set up welcome screen data
donkey_pic = pygame.image.load('img/main_donkey_logo.png').convert()
before_game = True

# Hide the mouse on the screen
pygame.mouse.set_visible(False)


def pregame_window():
    '''
    Window to display before the player has started playing (welcome screen)
    '''
    db.win.fill((0, 0, 0))
    paddle_group.update()
    paddle_group.draw(db.win)

    font = pygame.font.Font(None, 36)
    db.win.blit(donkey_pic, [300, 60])

    donkey_title = font.render("Welcome to Donkey-X Ball!", 1, (100, 100, 100))
    db.win.blit(donkey_title, (370, 28))

    donkey_subtitle = font.render("Hit the space bar to start ya donk!", 1, (100, 100, 100))
    db.win.blit(donkey_subtitle, (330, 550))


def redrawGameWindow(brick_hit=False):
    '''
    Draw all of our blits on the window
    '''

    if before_game:
        pregame_window()
    else:
        db.win.blit(bg, (0, 0))
        paddle_group.update()
        paddle_group.draw(db.win)
        ball_group.update()
        ball_group.draw(db.win)

        if brick_hit:
            level_1.brick_group.update()

        level_1.brick_group.draw(db.win)

        sb.draw()
    db.pygame.display.update()


def collision_ball_paddle():
    '''
    Collision between ball and paddle
    '''

    collide = pygame.sprite.spritecollide(gb, paddle_group, False, pygame.sprite.collide_mask)
    if collide:

        # Determine where the ball lands on the paddle (%)
        ball_x_on_paddle = (gb.rect.left - paddle.rect.left) / paddle.width
        logger.info(f"gb.rect.left = {gb.rect.left}, paddle.x = {paddle.rect.left}, paddle.width = {paddle.width}")
        logger.info(f"Ball X on paddle: {ball_x_on_paddle}")

        # Move the ball up off the paddle
        gb.y_direction = gb.y_direction*-1

        logger.debug(f"paddle.paddle_mid = {paddle.rect.centerx}, gb.x = {gb.x}")

        # If it hits on the left send it to the left - same for right
        if gb.rect.centerx <= paddle.rect.centerx:
            logger.info(f"SLOPE FACTOR: {ball_x_on_paddle}")
            gb.x_direction = -1
        elif gb.rect.centerx > paddle.rect.centerx:
            ball_x_on_paddle = 1 - ball_x_on_paddle
            logger.info(f"SLOPE FACTOR: {ball_x_on_paddle}")
            gb.x_direction = 1

        # Control angle that ball leaves paddle with
        if ball_x_on_paddle <= 0.05:
            gb.angle = 25
        elif ball_x_on_paddle <= 0.20:
            gb.angle = 40
        elif ball_x_on_paddle <= 0.30:
            gb.angle = 55
        elif ball_x_on_paddle <= 0.40:
            gb.angle = 70
        else:
            gb.angle = 85

        logger.info(f"Leaving paddle with an angle of {gb.angle}")


def collision_ball_brick_standard(collide_dict):
    '''
    Check the direction of the ball
    we should limit options to only 2 logical options based on direction
    of ball
    '''
    if gb.x_direction == 1 and gb.y_direction == -1:
        # Only keep 2 logical values from dictionary
        trimmed_dict = {your_key: collide_dict[your_key] for your_key in ['left', 'bottom']}
        # Determine the min hit side
        hit = min(trimmed_dict, key=trimmed_dict.get)

        if hit == 'left':
            gb.x_direction *= -1
        elif hit == 'bottom':
            gb.y_direction *= -1

        # Helpful to see which clause it hit
        logger.info("BOOM 1")
    elif gb.x_direction == -1 and gb.y_direction == -1:
        trimmed_dict = {your_key: collide_dict[your_key] for your_key in ['right', 'bottom']}
        hit = min(trimmed_dict, key=trimmed_dict.get)
        if hit == 'right':
            gb.x_direction *= -1
        elif hit == 'bottom':
            gb.y_direction *= -1
        logger.info("BOOM 2")
    elif gb.x_direction == 1 and gb.y_direction == 1:
        trimmed_dict = {your_key: collide_dict[your_key] for your_key in ['left', 'top']}
        hit = min(trimmed_dict, key=trimmed_dict.get)
        if hit == 'left':
            gb.x_direction *= -1
        elif hit == 'top':
            gb.y_direction *= -1
            logger.info("BOOM 3")
    elif gb.x_direction == -1 and gb.y_direction == 1:
        trimmed_dict = {your_key: collide_dict[your_key] for your_key in ['right', 'top']}
        hit = min(trimmed_dict, key=trimmed_dict.get)
        if hit == 'right':
            gb.x_direction *= -1
        elif hit == 'top':
            gb.y_direction *= -1
        logger.info("BOOM 4")
    else:
        logger.debug("BAD COLLISION WHAT THE HELL")

    # Lot of debug statements here
    logger.debug(f"Collide Dict: {collide_dict}")
    logger.debug(f"Trimmed Dict: {trimmed_dict}")
    logger.debug(f"Hit: {hit}")

def collision_ball_brick():
    '''
    Collision between ball and a brick
    '''

    brick_collide = pygame.sprite.spritecollide(gb, level_1.brick_group, False, pygame.sprite.collide_mask)
    ball_x, ball_y = gb.x, gb.y
    if brick_collide:
        # This allows us to store the Block object in a variable
        hit_block = brick_collide[0]

        # Initialize a collide_dict to determine where it hit
        collide_dict = {}
        logger.debug(f"Ball location: X={ball_x}, Y={ball_y}")
        logger.debug(f"Ball DIRECTION: X={gb.x_direction}, Y={gb.y_direction}")

        collide_dict['left'] = abs(hit_block.rect.left - ball_x)
        collide_dict['right'] = abs(hit_block.rect.right - ball_x)
        collide_dict['top'] = abs(hit_block.rect.top - ball_y)
        collide_dict['bottom'] = abs(hit_block.rect.bottom - ball_y)

        if gb.special_power == 'Thru Ball':
            pass
        else:
            collision_ball_brick_standard(collide_dict)

        if gb.special_power == 'Fast Ball':
            # Increase velocity and then set power to none
            # we only want to increase speed once
            gb.vel *= 1.3
            gb.special_power = None

        if gb.special_power == 'Slow Ball':
            gb.vel *= 0.7
            gb.special_power = None
        level_1.brick_group.remove(brick_collide)
        logger.info(f"Level score: {level_1.score_calc()}")

        create_power()
        # Speed up the ball every other brick they hit
        if level_1.score_calc() % 2 == 0:
            logger.info("SPEEDING UP")
            logger.info(f"GB VEL: {gb.vel}")
            gb.vel += .02
            logger.info(f"GB VEL: {gb.vel}")
        else:
            logger.info("no speed")

        return True

def collision_ball_too_low():
    # If the ball gets within 5 pixels of the bottom we are saying that's an L
    if gb.y >= db.window_height - 5:
        gb.level_status = "YOU BLEW IT (Sandler voice)"
        gb.lost_life()
        gb.ball_started = False
        gb.new_life = True


def create_power():
    # Work on special powers
    if random.randint(1, 3) == 3:
        gb.special_power = random.choice(['Thru Ball', 'Slow Ball', 'Fast Ball'])
    return gb.special_power


while run:

    # pygame.time.delay(100)
    db.clock.tick(60)

    keys = db.pygame.key.get_pressed()

    # If they are on welcome screen and they hit space, set game to start
    if keys[db.pygame.K_SPACE] and before_game:
        before_game = False

    for event in db.pygame.event.get():
        if event.type == db.pygame.QUIT:
            run = False

        # Wait to start moving ball until a click
        if event.type == db.pygame.MOUSEBUTTONDOWN:
            if gb.still_alive and not gb.ball_started:
                gb.ball_started = True

    if keys[db.pygame.K_SPACE] and gb.lives == 0:
        gb.restart_game()
        level_1.restart_level()

    collision_ball_too_low()
    collision_ball_paddle()
    brick_hit = collision_ball_brick()

    redrawGameWindow(brick_hit)

logger.debug(f"Game ball hits: {gb.blocks_hit}")

db.pygame.quit()
