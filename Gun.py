
from math import sin
from math import radians

EXIT_VELOCITY = 120
GRAVITY = 9.8

""" Class for representing a particular artillery piece. """
class Gun(object):

    def __repr__(self):
        return "Gun with position x: " + str(self.x) + " y: " + str(self.y)

    def __init__(self, x, y, elevation=45, azimuth=45, ammo=10):
        """ Constructor for the gun class.

            Preconditons:
                0 < elevation < 90
                0 < azimuth < 90
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
        return EXIT_VELOCITY ** 2 * sin(2 * radians(self.elevation)) / GRAVITY 

    def set_azimuth(self):
        self.azimuth = azimuth	

    def set_elevation(self):
        self.elevation = elevation

    def move(self, x, y):
        self.x = x
        self.y = y
