
import random
import Gun
import socket

MAX_X = 100
MAX_Y = 100

""" Class for controlling the main game. """
class FireController(object):

    def __init__(self, numPlayers):
        """ Constructor for the FireController class. Takes the
            number of players and grid size as arguments. 

            Preconditions:
                MIN_PLAYERS <= numPlayers <= MAX_PLAYERS
        """

        self.numPlayers = numPlayers;
        self.maxX, self.maxY = self.generate_grid_size()

        self.setup_guns()

    def setup_guns(self):
        """ Generates the guns with suitable starting conditions. """
        self.guns = []

        self.startingPositions = {}
        for i in range(0, self.numPlayers):
            x, y = self.generate_starting_positions()

            newGun = Gun.Gun(x, y)
            self.guns.append(newGun)

    def generate_starting_positions(self):
        """ Generates the ith player's starting positions. """
        x = random.randint(0, self.maxX)
        y = random.randint(0, self.maxY)

        # Check if key exists, regenerate if neccesary
        try:
            self.startingPositions[hash(x) * hash(y)]
        except KeyError:
            x = random.randint(0, self.maxX)
            y = random.randint(0, self.maxY)


        self.startingPositions[hash(x) * hash(y)] = x,y

        #Make sure starting positions are suitably distant

        return x, y 

    def generate_grid_size(self):
        """ Generates the grid size dynammically, based off the number
            of players. """
        return 100 + self.numPlayers * 10, 100 + self.numPlayers * 10 

    def play_game(self):
        """ Main game logic. """
        pass
