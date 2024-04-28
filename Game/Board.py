class Board:
    COLOR_LINE = (255, 255, 255)
    COLOR_DAGGER = (255, 0, 0)
    COLOR_ZERO = (0, 0, 255)

    NONE = 0
    DAGGER = 1
    ZERO = 2

    def __init__(self, width: int, height: int, size: int):
        self.width = width
        self.height = height
        self.size = size
        self.__create_board(size)

    def __create_board(self, size: int):
        self.board = []
        for i in range(size):
            self.board.append([self.NONE for j in range(size)])


    def print(self, sc):
        from pygame.draw import line
        cell_width = self.width // self.size
        cell_height = self.height // self.size
        for i in range(1, self.size):
            line(sc, self.COLOR_LINE, (cell_width*i, 0), (cell_width*i, self.height))
            line(sc, self.COLOR_LINE, (0, cell_height*i), (self.width, cell_height*i))


    def click(self, pos):
        pass


