import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 31415))
clientsocket.send('hello'.encode('utf-8'))

class PlayerInterface(object):
    """
        Class for handling player interactions with the server. Reads messages 
        from the server and displays them to the player. Also sends responses
        back to the server.
    """
    pass