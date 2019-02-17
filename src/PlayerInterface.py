""" Class that handles client-side network interactions. """
import socket
import sys

GAME_PORT = 31415
SERVER_IP_ADDR = '10.0.0.101'

class PlayerInterface(object):
    """
        Class for handling player interactions with the server. Reads messages 
        from the server and displays them to the player. Also sends responses
        back to the server.
    """
    def __init__(self):
        self.client_socket = None

        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print('Failed to create socket.')
            sys.exit()

        self.client_socket.connect((SERVER_IP_ADDR, GAME_PORT))
        self.setup()

    def setup(self):
        """ Setup up the client-side game state. """
        try:
            grid_size = self.client_socket.recv(100)
            print(repr(grid_size))

            starting_position = self.client_socket.recv(100)
            print(repr(starting_position))
        except socket.error:    
            print('Receive failed.')       
            sys.exit()

player = PlayerInterface()

