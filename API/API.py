from API.server import Server
from API.client import Client
from threading import Thread


class API:
    def __init__(self):
        print('инит')

    def Send(self, text: str):
        print('Start thread...', end=' ')
        Thread(target=lambda: self.conn.send(text)).start()


    def recv(self, f):
        return self.conn.recv(f)

    def CreateLobby(self, btn):
        print('Создаю лобби')
        self.conn = Server()
        self.conn.start(btn)

    def ConnectToLobby(self, btn):
        print('Подключаюсь')
        self.conn = Client(btn)
        # thread = threading.Thread(target=lambda: conn.())
        # thread.start()
