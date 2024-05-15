import pygame
from API.API import API
from API.server import Server
from Game.GameConst import *
from Game.Board import Board


def close(API):
    if API.typecon == API.SERVER:
        from time import sleep
        sleep(0.1)
    API.close()

class Game:
    def __init__(self, API: API):
        pygame.init()
        pygame.mixer.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tick Tack Toe")
        clock = pygame.time.Clock()
        hod = 0
        if API.typecon == API.SERVER:
            hod = 1
        board = Board(WIDTH, HEIGHT, 3, hod)
        board.print(screen)
        from threading import Thread
        Thread(target=lambda: API.recv([board.dohod, screen])).start()
        running = True
        while running:
            clock.tick(FPS)
            if board.iswin == 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            board.click(event.pos, API, screen)

            elif board.iswin == 1:
                screen.fill((0, 255, 0))
                pygame.display.flip()
                close(API)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            running = False

            elif board.iswin == 2:
                screen.fill((255, 0, 0))
                pygame.display.flip()
                close(API)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            running = False



        pygame.quit()



