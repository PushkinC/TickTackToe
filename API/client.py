import socket
from Game.GameConst import URL


class Client(socket.socket):
    def __init__(self, start):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        print(URL[:-5], int(URL[-4:]))
        self.connect((URL[:-5], int(URL[-4:])))
        print('соединение установлено(клиент)')
        start.pack()

    def send(self, text_data):
        self.sendall(bytes(text_data, encoding='utf-8'))

    def recv(self, f):
        data = str(super().recv(1024), encoding='UTF-8')
        print(data )
        f[0](list(map(int, data.split(' '))), 2, f[1])
