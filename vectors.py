import math


class Vector(object):
    '''
    Class to input a magnitude and direction and calculate x and y values
    '''
    def __init__(self, mag, angle):
        self.mag = mag
        self.angle = angle

    def getx(self):
        return self.mag * math.cos(math.radians(self.angle))

    def gety(self):
        return self.mag * math.sin(math.radians(self.angle))
