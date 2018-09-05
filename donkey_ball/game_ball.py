import donkey_ball as db


class GameBall(object):
    '''
    Main class for the game ball
    '''
    def __init__(self):
        self.x = 200
        self.y = db.window_height - 28
        self.x_direction = 1
        self.y_direction = 1
        self.y_slope = 0.5
        self.radius = 5
        self.vel = 0
        self.color = (32, 252, 143)
        self.ball_started = False
        self.still_alive = True
        self.new_life = False
        self.level_status = "Play the game, kid!"
        self.lives = 3
        self.blocks_hit = 0
        self.special_power = None

    def lost_life(self):
        '''Function to reduce lives when ball passes paddle'''
        if self.lives > 0:
            self.lives -= 1

    def still_alive_check(self):
        '''Check to see if we are still alive.'''
        if self.lives >= 1:
            return True
        else:
            return False

    def restart_game(self):
        self.lives = 4
        self.blocks_hit = 0

    def ready_new_life(self):
        '''Variables to set for a new life'''
        self.vel = 0
        self.x = db.pygame.mouse.get_pos()[0] + 37
        self.y = db.window_height - 28
        self.y_direction = -1

    def draw_ball(self):
        '''Figure out where to draw the ball on the screen'''

        # Do they still have lives left? If so, go to logic
        if self.still_alive_check():

            # Is this a new life? Initialize variables
            if self.new_life and not self.ball_started:
                self.ready_new_life()

            # If the ball is started make it move!
            if self.ball_started:
                self.level_status = "Play ball, bro!"
                self.vel = 5
            # If not, make it stay on the paddle
            else:
                self.x = db.pygame.mouse.get_pos()[0] + 37

            # Make sure ball stays within window
            if self.x <= 5:
                self.x_direction = 1
            elif self.x >= db.window_width - self.radius:
                self.x_direction = -1

            if self.y <= db.dividing_bar_y + db.dividing_bar_height:
                self.y_direction = 1
            elif self.y >= db.window_height - self.radius:
                self.y_direction = -1

            # Make the ball move in the correct direction
            self.x = self.x + (self.x_direction * self.vel)
            self.y = int(self.y + (self.y_direction * self.vel) * self.y_slope)
            db.pygame.draw.circle(db.win, self.color, (self.x, self.y), self.radius)
