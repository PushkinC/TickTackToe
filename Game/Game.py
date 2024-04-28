import pygame
import API.API
from Game.GameConst import *
from Game.Board import Board



pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tick Tack Toe")
clock = pygame.time.Clock()


board = Board(WIDTH, HEIGHT, 3)

running = True
while running:
    screen.fill(BACKGROUNDCOLOR)
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                board.click(event.pos)
    board.print(screen)

    pygame.display.flip()
pygame.quit()



