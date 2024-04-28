import socket
from Game.GameConst import MYPORT


class Server(socket.socket):
    def __init__(self):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(('', MYPORT))
        self.listen(1)

    def start(self):
        self.conn, self.addr = self.accept()
        with self.conn:
            print(f"Connected by {self.addr}")
            while True:
                data = self.conn.recv(1024)
                if not data:
                    break
                # self.conn.sendall(data)
                print(data)
