import pygame
from API.API import API
from API.server import Server
from Game.GameConst import *
from Game.Board import Board

class Game:
    def __init__(self, API: API):
        pygame.init()
        pygame.mixer.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tick Tack Toe")
        clock = pygame.time.Clock()
        hod = 1
        print(API.conn)
        if isinstance(API.conn, Server):
            hod = 0
        print(hod)
        board = Board(WIDTH, HEIGHT, 3, hod)
        board.print(screen)
        from threading import Thread
        Thread(target=lambda: API.recv([board.dohod, screen])).start()
        running = True
        while running:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        board.click(event.pos, API, screen)


        pygame.quit()



