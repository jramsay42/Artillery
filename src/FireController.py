
import random
import Gun
import socket

MAX_X = 100
MAX_Y = 100

""" Class for controlling the main game. """
class FireController(object):

    def __init__(self, num_players):
        """ Constructor for the FireController class. Takes the
            number of players and grid size as arguments.

            Preconditions:
                MIN_PLAYERS <= num_players <= MAX_PLAYERS
        """

        self.num_players = num_players
        self.max_x, self.max_y = self.generate_grid_size()

        self.setup_guns()

    def setup_guns(self):
        """ Generates the guns with suitable starting conditions. """
        self.guns = []
        self.starting_positions = []

        for i in range(0, self.num_players):
            x_pos, y_pos = self.generate_starting_positions()
            self.starting_positions.append((x_pos, y_pos))

            new_gun = Gun.Gun(x_pos, y_pos)
            self.guns.append(new_gun)

    def generate_starting_positions(self):
        """ Generates the ith player's starting positions. """
        x_guess = random.randint(0, self.max_x)
        y_guess = random.randint(0, self.max_y)

        #Regenerate starting positions until they are unique
        while (x_guess, y_guess) in self.starting_positions:
            x_guess = random.randint(0, self.max_x)
            y_guess = random.randint(0, self.max_y)

        return x_guess, y_guess

    def generate_grid_size(self):
        """ Generates the grid size dynammically, based off the number
            of players. """
        return 100 + self.num_players * 10, 100 + self.num_players * 10 

    def play_game(self):
        """ Main game logic. """
        pass
