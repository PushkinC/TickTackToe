import socket
from Game.GameConst import MYPORT
from threading import Thread


class Server(socket.socket):
    def __init__(self):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(('', MYPORT))
        self.listen(1)

    def start(self, btn):
        self.conn, self.addr = self.accept()
        print('Соединение установлено(сервер)')
        btn.pack()
        # with self.conn:
        #     print(f"Connected by {self.addr}")
        #     while True:
        #         data = self.conn.recv(1024)
        #         if data:
        #             print(data)
        #             break
        #         print(data)

    def recv(self, f):
        data = str(self.conn.recv(1024), encoding='UTF-8')
        f[0](list(map(int, data.split(' '))), 2, f[1])

    def send(self, text_data):
        self.conn.sendall(bytes(text_data, encoding='utf-8'))
