class Board(object):
    def __init__(self):
        self.title = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def SetBoard(self,b):
        self.title = b