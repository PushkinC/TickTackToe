from API.server import Server
from API.client import Client
import threading



my = Server()
other = Client()

thread = threading.Thread(target=lambda: my.start())
thread.start()

# thread = threading.Thread(target=lambda: other)
# thread.start()