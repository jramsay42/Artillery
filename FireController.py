
import random
import Gun

NUM_PLAYERS = 10
MAX_X = 100
MAX_Y = 100


""" Class for controlling the main game. """
class FireController(object):

    def __init__(self, numPlayers=NUM_PLAYERS, maxX=MAX_X, maxY=MAX_Y):
        """ Constructor for the FireController class. Takes the
            number of players and grid size as arguments. 
        
            Preconditions:
                0 < numPlayers <= 30
                0 < maxX
                0 < maxY

        """
        self.numPlayers = numPlayers;
        self.maxX = maxX
        self.maxY = maxY

        self.setup_guns()

    def setup_guns(self):
        """ Generates the guns with suitable starting conditions. """
        self.guns = []

        for i in range(0, self.numPlayers):
            self.generate_start_positions(i)
            

    def generate_starting_positions(self, playerNum):
        """ Generates the ith player's starting positions. """
        random.seed(playerNum)
        x = random.randint(0, self.maxX)
        y = random.randint(0, self.maxY)

        #Make sure starting positions are suitably distant

        return x, y 

    def generate_grid_size(self):
        pass
         
    def play_game(self):
        """ Main game logic. """
        while(1):
            pass



""" MAIN LOOP """
if __name__ == "__main__":
    controller = FireController()
    controller.play_game()
