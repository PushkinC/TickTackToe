class Board:
    COLOR_LINE = (255, 255, 255)
    COLOR_DAGGER = (255, 0, 0)
    COLOR_ZERO = (0, 0, 255)

    NONE = 0
    DAGGER = 1
    ZERO = 2

    def __init__(self, width: int, height: int, size: int, hod: int):
        self.width = width
        self.height = height
        self.size = size
        self.hod = hod
        self.__create_board(size)

    def __create_board(self, size: int):
        self.board = []
        for i in range(size):
            self.board.append([self.NONE for j in range(size)])


    def print(self, sc):
        import pygame
        from pygame.draw import line, circle
        from Game.GameConst import BACKGROUNDCOLOR
        sc.fill(BACKGROUNDCOLOR)

        cell_width = self.width // self.size
        cell_height = self.height // self.size
        for i in range(1, self.size):
            line(sc, self.COLOR_LINE, (cell_width*i, 0), (cell_width*i, self.height))
            line(sc, self.COLOR_LINE, (0, cell_height*i), (self.width, cell_height*i))

        for j in range(self.size):
            for i in range(self.size):
                if self.board[i][j] == self.DAGGER:
                    line(sc, self.COLOR_DAGGER, (cell_width*i, cell_height*j), (cell_width*(i+1), cell_height*(j+1)))
                    line(sc, self.COLOR_DAGGER, (cell_width*(i+1), cell_height*j), (cell_width*i, cell_height*(j+1)))
                elif self.board[i][j] == self.ZERO:
                    circle(sc, self.COLOR_ZERO, (cell_width*i + cell_width//2, cell_height*j + cell_height//2), cell_height//2)
        pygame.display.flip()



    def click(self, pos, api, sc):
        x = pos[0] // (self.width // self.size)
        y = pos[1] // (self.height // self.size)
        if self.hod:
            self.dohod([x, y], self.DAGGER, sc)
            print('Start send...', end=' ')
            api.Send(f'{x} {y}')
            print('Sended')
            self.print(sc)
            from threading import Thread
            Thread(target=lambda: api.recv([self.dohod, sc])).start()
        else:
            print('NO!!!!!!')

    def dohod(self, data, znak, sc):
        self.board[data[0]][data[1]] = znak
        self.print(sc)
        self.hod = not self.hod


