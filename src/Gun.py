""" Class representing a single artillery piece. """
from math import sin
from math import cos
from math import radians
from math import floor

EXIT_VELOCITY = 120
GRAVITY = 9.8

DEFAULT_ELEVATION = 45
DEFAULT_AZIMUTH = 45
DEFAULT_AMMO = 10

class Gun(object):
    """ Class for representing a particular artillery piece. """

    def __repr__(self):
        return "Gun with position x: " + str(self.x_pos) + " y: " + str(self.y_pos)

    def __init__(self, x, y, elevation=DEFAULT_ELEVATION, azimuth=DEFAULT_AZIMUTH,
                 ammo=DEFAULT_AMMO):
        """ Constructor for the gun class.

            Preconditons:
                0 < elevation < 90
                0 <= azimuth <= 360
                0 <= ammo
                0 <= x <= MAX_X
                0 <= y <= MAX_Y
        """
        self.x_pos = x
        self.y_pos = y
        self.elevation = elevation
        self.azimuth = azimuth
        self.ammo = ammo

    def get_azimuth(self):
        """ Returns the angle of orientation. """
        return self.azimuth

    def get_elevation(self):
        """ Returns the angle of elevation. """
        return self.elevation

    def calculate_range(self):
        """ Returns the linear range of the gun at the current elevation. """
        return EXIT_VELOCITY ** 2 * sin(2 * radians(self.elevation)) / GRAVITY 

    def calculate_trajectory(self):
        """ Returns the cell that the shell will land at as a tuple. """
        shell_range = self.calculate_range()
        new_x = self.x_pos + cos(radians(self.azimuth)) * shell_range
        new_y = self.y_pos + sin(radians(self.azimuth)) * shell_range
        return (floor(new_x), floor(new_y))

    def set_azimuth(self, azimuth):
        """ Precondition: 0 <= azimuth < 360 """
        self.azimuth = azimuth	

    def set_elevation(self, elevation):
        """ Precondition: 0 < elevation < 90 """
        self.elevation = elevation

    def shoot_gun(self):
        """ Returns True if the gun has ammo and updates the ammo. Otherwise,
            False is returned. """
        if self.ammo > 0:
            self.ammo -= 1
            return True
        return False

    def move(self, x, y):
        """ Precondition: 0 <= x <= MAX_X, 0 <= y <= MAX_Y """
        self.x_pos = x
        self.y_pos = y
