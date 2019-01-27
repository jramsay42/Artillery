""" Class that handles client-side network interactions. """
import socket
import sys

GAME_PORT = 31415

class PlayerInterface(object):
    """
        Class for handling player interactions with the server. Reads messages 
        from the server and displays them to the player. Also sends responses
        back to the server.
    """
    def __init__(self):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print('Failed to create socket.')
            sys.exit()

        client_socket.connect(('10.0.0.101', GAME_PORT))
        
        try:
            client_socket.send('hello'.encode('utf-8'))
        except socket.error:
            print('Send failed.')

test = PlayerInterface()