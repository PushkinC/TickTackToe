import socket
from Game.GameConst import URL


class Client(socket.socket):
    def __init__(self):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        print(URL[:-5], int(URL[-4:]))
        self.connect((URL[:-5], int(URL[-4:])))

    def send(self, text_data):
        while True:
            self.sendall(bytes(text_data, encoding='utf-8'))
