import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 31415))
clientsocket.send('hello'.encode('utf-8'))