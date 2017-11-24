
from math import sin
from math import radians

EXIT_VELOCITY = 120
GRAVITY = 9.8

DEFAULT_ELEVATION = 45
DEFAULT_AZIMUTH = 45
DEFAULT_AMMO = 10

class Gun(object):
    """ Class for representing a particular artillery piece. """

    def __repr__(self):
        return "Gun with position x: " + str(self.x) + " y: " + str(self.y)

    def __init__(self, x, y, elevation=DEFAULT_ELEVATION, azimuth=DEFAULT_AZIMUTH,
                 ammo=DEFAULT_AMMO):
        """ Constructor for the gun class.

            Preconditons:
                0 < elevation < 90
                0 < azimuth < 360
                0 < ammo
        """
        self.x = x
        self.y = y
        self.elevation = elevation
        self.azimuth = azimuth
        self.ammo = ammo

    def get_azimuth(self):
        return self.azimuth

    def get_elevation(self):
        return self.elevation

    def calculate_range(self):
        """ Returns the linear range of the gun at the current elevation. """
        return EXIT_VELOCITY ** 2 * sin(2 * radians(self.elevation)) / GRAVITY 

    def set_azimuth(self, azimuth):
        """ Precondition: 0 <= azimuth < 360 """
        self.azimuth = azimuth	

    def set_elevation(self, elevation):
        """ Precondition: 0 < elevation < 90 """
        self.elevation = elevation

    def shoot_gun(self):
        """ Returns True if the gun has ammo and updates the ammo. Otherwise,
            False is returned. """
        if (self.ammo > 0 ):
            self.ammo -= 1
            return True
        else:
            return False

    def move(self, x, y):
        """ Precondition: 0 <= x <= MAX_X, 0 <= y <= MAX_Y """
        self.x = x
        self.y = y
