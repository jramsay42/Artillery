
import random
import Gun
import socket

MIN_PLAYERS = 2
MAX_PLAYERS = 30
NUM_PLAYERS = 10
MAX_X = 100
MAX_Y = 100

""" Class for controlling the main game. """
class FireController(object):

    def __init__(self, numPlayers=NUM_PLAYERS):
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
         
    def create_server(self):
        """ Creates the server for client players to connect to. """
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        host = 'localhost' #socket.gethostname()
        port = 31415

        self.sock.bind((host, port))

        print("Waiting for players...")
        numConnections = 0
        self.sock.listen(numPlayers)
        while True:
            conn, addr = self.sock.accept()
            numConnections += 1
            print('Got connection from', addr)

            if numConnections == numPlayers:
                break
            #conn.close()

        print("All players connected.")

    def play_game(self):
        """ Main game logic. """
        pass


""" MAIN LOOP """
if __name__ == "__main__":
    
    # Create new game
    while (1):
        try:
            numPlayers = int(input("Enter number of players: "))
            if (numPlayers < MIN_PLAYERS or numPlayers > MAX_PLAYERS):
                print("Invalid number of players. Must be between " + \
                str(MIN_PLAYERS) + " and " + str(MAX_PLAYERS) + ".")
            else:
                break
        except ValueError:
            print("Please enter a number.")

    # Setup game state
    controller = FireController(numPlayers)
    controller.create_server()
    controller.play_game()
