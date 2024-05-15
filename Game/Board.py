import pygame


class Board:
    COLOR_LINE = (255, 255, 255)
    COLOR_DAGGER = (255, 0, 0)
    COLOR_ZERO = (0, 0, 255)

    NONE = 0
    DAGGER = 1
    ZERO = 2
    counter = []
    WIN = 1
    LOOSE = 2
    iswin = NONE

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
        padd = cell_width * 0.1
        for i in range(1, self.size):
            line(sc, self.COLOR_LINE, (cell_width*i, 0), (cell_width*i, self.height))
            line(sc, self.COLOR_LINE, (0, cell_height*i), (self.width, cell_height*i))

        for j in range(self.size):
            for i in range(self.size):
                if self.board[i][j] == self.DAGGER:
                    line(sc, self.COLOR_DAGGER, (cell_width*i + padd, cell_height*j + padd), (cell_width*(i+1) - padd, cell_height*(j+1) - padd), 5)
                    line(sc, self.COLOR_DAGGER, (cell_width*(i+1) - padd, cell_height*j + padd), (cell_width*i + padd, cell_height*(j+1) - padd), 5)
                elif self.board[i][j] == self.ZERO:
                    circle(sc, self.COLOR_ZERO, (cell_width*i + cell_width//2, cell_height*j + cell_height//2), cell_height//2 - padd)
                    circle(sc, BACKGROUNDCOLOR, (cell_width*i + cell_width//2, cell_height*j + cell_height//2), cell_height//2 - padd - 5)
        pygame.display.flip()



    def click(self, pos, api, sc):
        x = pos[0] // (self.width // self.size)
        y = pos[1] // (self.height // self.size)
        if self.hod:
            if self.checkhod([x, y]):
                self.dohod([x, y], self.DAGGER, sc)
                api.Send(f'{x} {y}')
                from threading import Thread
                Thread(target=lambda: api.recv([self.dohod, sc])).start()
        else:
            print('NO!!!!!!')

    def dohod(self, data, znak, sc):
        self.board[data[0]][data[1]] = znak

        self.counter.append(data)
        if len(self.counter) >= 7:
            self.board[self.counter[0][0]][self.counter[0][1]] = self.NONE
            self.counter = self.counter[1::]

        self.print(sc)

        self.iswin = self.checkwin()


        self.hod = not self.hod

    def checkhod(self, data):
        return self.board[data[0]][data[1]] == self.NONE

    def checkwin(self):
        for i in range(self.size):
            if (self.board[0][i] == self.board[1][i] == self.board[2][i]) and self.board[0][i] == self.WIN:
                return self.WIN

        for i in range(self.size):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2]) and self.board[i][0] == self.WIN:
                return self.WIN

        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) and self.board[0][0] == self.WIN:
            return self.WIN
        if (self.board[0][2] == self.board[1][1] == self.board[2][0]) and self.board[0][2] == self.WIN:
            return self.WIN


        for i in range(self.size):
            if (self.board[0][i] == self.board[1][i] == self.board[2][i]) and self.board[0][i] == self.LOOSE:
                return self.LOOSE

        for i in range(self.size):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2]) and self.board[i][0] == self.LOOSE:
                return self.LOOSE

        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) and self.board[0][0] == self.LOOSE:
            return self.LOOSE
        if (self.board[0][2] == self.board[1][1] == self.board[2][0]) and self.board[0][2] == self.LOOSE:
            return self.LOOSE

        return self.NONE



