
import socket
import FireController

MIN_PLAYERS = 2
MAX_PLAYERS = 30
NUM_PLAYERS = 10

class ServerInterface(object):
    """ Class for managing client-server interactions. """
    
    def __init__(self, numPlayers):
        self.sock = None
        self.numPlayers = numPlayers
    
    def create_server(self):
        """ Creates the server for client players to connect to. """
        try:
            serverIPaddr = [ip for ip in \
                    socket.gethostbyname_ex(socket.gethostname())[2] if not \
                    ip.startswith("127.")][:1]
            print("Local IP Address is: ", serverIPaddr)

            self.sock = socket.socket()
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            host = 'localhost' #socket.gethostname()
            port = 31415

            self.sock.bind((host, port))

            print("Waiting for players...")
            numConnections = 0
            self.sock.listen(self.numPlayers)
            while True:
                conn, addr = self.sock.accept()
                numConnections += 1
                print('Got connection from', addr)

                if numConnections == self.numPlayers:
                    break
                #conn.close()
            
            print("All players connected.")

        except socket.error:
            print("There was a socket error.")

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
    master = ServerInterface(numPlayers)
    master.create_server()
    controller = FireController.FireController(numPlayers)
    controller.play_game()