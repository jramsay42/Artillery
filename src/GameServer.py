""" Server which manages client interactions. """
import socket
import FireController

MIN_PLAYERS = 2
MAX_PLAYERS = 30
GAME_PORT = 31415

class GameServer(object):
    """ 
        Game server that offers clients a choice of action,
        then reads the response and updates its representation
        of the game accordingly. The other clients are then
        informed of the changes.
     """

    def __init__(self, num_players):
        self.sock = None
        self.num_players = num_players
        self.clients = list()
        self.controller = FireController.FireController(numPlayers)

    def create_server(self):
        """
            Creates the server for client players to connect to.
            Then waits until the requisite number of players are
            connected.
        """
        try:
            server_address = [ip for ip in \
                    socket.gethostbyname_ex(socket.gethostname())[2] if not \
                    ip.startswith("127.")][:1]
            print("Local IP Address is: ", server_address)

            self.sock = socket.socket()
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            port = GAME_PORT
            #socket.gethostname()
            self.sock.bind(('', port))

            print("Waiting for players...")
            num_connections = 0
            self.sock.listen(self.num_players)

            #Accept correct number of players
            while num_connections != self.num_players:
                conn, addr = self.sock.accept()
                print('Got connection from', addr)

                conn.send('Size {},{}'.format(self.controller.max_x, \
                        self.controller.max_y).encode('utf-8'))
                (x_start, y_start) = \
                        self.controller.starting_positions[num_connections]
                conn.send('Start {},{}'.format(x_start, y_start).encode('utf-8'))
                self.clients.append(conn)

                num_connections += 1
                

            print("All players connected.")

        except socket.error:
            print("There was a socket error.")

        self.controller.play_game()

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
    master = GameServer(numPlayers)
    master.create_server()