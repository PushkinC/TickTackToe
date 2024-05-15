from API.server import Server
from API.client import Client
from threading import Thread


class API:
    SERVER = 1
    CLIENT = 2
    def __init__(self):
        pass

    def Send(self, text: str):
        Thread(target=lambda: self.conn.send(text)).start()


    def recv(self, f):
        return self.conn.recv(f)

    def CreateLobby(self, btn):
        self.typecon = self.SERVER
        self.conn = Server()
        self.conn.start(btn)


    def ConnectToLobby(self, btn):
        self.typecon = self.CLIENT
        self.conn = Client(btn)


    def close(self):
        self.conn.close()
