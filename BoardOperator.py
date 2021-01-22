from Board import Board

class MergingQueue(object):
    def __init__(self):
        self.buffer = []

    def Append(self, x):
        if 0 == x:
            return
        self.buffer.append(x)

    def Merging(self):
        self.FillZero(self.buffer,5)
        result=[]
        while len(self.buffer) >= 2:
            if self.buffer[0] == self.buffer[1]:
                result.append(2*self.buffer[0])
                self.buffer.pop(0)
                self.buffer.pop(0)
            else:
                result.append(self.buffer[0])
                self.buffer.pop(0)
        self.FillZero(result, 4)
        return result

    def FillZero(self,lst,n):
        while len(lst) < n:
            lst.append(0)

class BoardOperator(object):
    def AreSame(self, board1, board2):
        for r in range(4):
            for c in range(4):
                if board1.title[r][c] != board2.title[r][c]:
                    return False
        return True
    
    def MoveDown(self, board):
        return self.Move(board,{'c':[0,4,1],'r':[3, -1, -1]},False)

    def MoveUp(self, board):
        return self.Move(board,{'c':[0,4,1],'r':[0, 4, 1]},False)        

    def MoveLeft(self, board):
        return self.Move(board,{'c':[0,4,1],'r':[0, 4, 1]},True)           

    def MoveRight(self, board):
        return self.Move(board,{'c':[0,4,1],'r':[3, -1, -1]},True)                

    def Move(self, board, numberParameters, swap):
        newBoard = Board()
        for c in range(numberParameters['c'][0],numberParameters['c'][1],numberParameters['c'][2]):
            mergingQueue = MergingQueue()
            for r in range(numberParameters['r'][0], numberParameters['r'][1], numberParameters['r'][2]):
                x,y=r,c
                if True==swap:
                    x,y=c,r
                mergingQueue.Append(board.title[x][y])
            result=mergingQueue.Merging()
            for r in range(numberParameters['r'][0], numberParameters['r'][1], numberParameters['r'][2]):
                x,y=r,c
                if True==swap:
                    x,y=c,r
                newBoard.title[x][y] = result.pop(0)
        return newBoard

if __name__ == "__main__":
    case=1
    testBoard = Board()
    testBoard.SetBoard([[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 2, 0, 0],
                        [0, 2, 0, 0]])

    boardOperator=BoardOperator()
    result=boardOperator.MoveDown(testBoard)
    assert result.title==[[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 4, 0, 0]]
    case=2
    testBoard = Board()
    testBoard.SetBoard([[0, 0, 4, 0],
                        [0, 2, 0, 0],
                        [0, 0, 0, 0],
                        [0, 2, 0, 0]])

    boardOperator=BoardOperator()
    result=boardOperator.MoveDown(testBoard)
    assert result.title==[[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 4, 4, 0]]
    case=3
    testBoard = Board()
    testBoard.SetBoard([[0, 0, 4, 0],
                        [0, 2, 0, 0],
                        [0, 0, 2, 0],
                        [0, 2, 0, 0]])

    boardOperator=BoardOperator()
    result=boardOperator.MoveDown(testBoard)
    assert result.title==[[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 4, 0],[0, 4, 2, 0]]
    case=4
    testBoard = Board()
    testBoard.SetBoard([[0, 0, 4, 0],
                        [0, 2, 0, 0],
                        [0, 2, 2, 0],
                        [0, 2, 0, 0]])

    boardOperator=BoardOperator()
    result=boardOperator.MoveDown(testBoard)
    assert result.title==[[0, 0, 0, 0],[0, 0, 0, 0],[0, 2, 4, 0],[0, 4, 2, 0]]
    case=5
    testBoard = Board()
    testBoard.SetBoard([[0, 2, 0, 0],
                        [0, 2, 0, 0],
                        [0, 2, 0, 0],
                        [0, 2, 0, 0]])

    boardOperator=BoardOperator()
    result=boardOperator.MoveDown(testBoard)
    assert result.title==[[0, 0, 0, 0],[0, 0, 0, 0],[0, 4, 0, 0],[0, 4, 0, 0]]
    case=6
    testBoard = Board()
    testBoard.SetBoard([[0, 0, 4, 0],
                        [0, 0, 2, 0],
                        [0, 0, 2, 0],
                        [0, 0, 4, 0]])

    boardOperator=BoardOperator()
    result=boardOperator.MoveDown(testBoard)
    assert result.title==[[0, 0, 0, 0],
                          [0, 0, 4, 0],
                          [0, 0, 4, 0],
                          [0, 0, 4, 0]]
    case=7
    testBoard = Board()
    testBoard.SetBoard([[0, 0, 4, 0],
                        [0, 0, 2, 0],
                        [0, 0, 2, 0],
                        [0, 0, 4, 0]])

    boardOperator=BoardOperator()
    result=boardOperator.MoveUp(testBoard)
    assert result.title==[[0, 0, 4, 0],
                          [0, 0, 4, 0],
                          [0, 0, 4, 0],
                          [0, 0, 0, 0]]

    case=8
    testBoard = Board()
    testBoard.SetBoard([[0, 0, 0, 2],
                        [2, 0, 0, 0],
                        [2, 2, 0, 0],
                        [0, 0, 4, 0]])

    boardOperator=BoardOperator()
    result=boardOperator.MoveUp(testBoard)
    assert result.title==[[4, 2, 4, 2],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]]
    case=9
    testBoard = Board()
    testBoard.SetBoard([[0, 4, 0, 2],
                        [2, 4, 4, 8],
                        [2, 2, 8, 0],
                        [2, 2, 4, 0]])

    boardOperator=BoardOperator()
    result=boardOperator.MoveUp(testBoard)
    assert result.title==[[4, 8, 4, 2],
                          [2, 4, 8, 8],
                          [0, 0, 4, 0],
                          [0, 0, 0, 0]]
    case=10
    testBoard = Board()
    testBoard.SetBoard([[0, 0, 0, 2],
                        [2, 0, 0, 0],
                        [2, 2, 0, 0],
                        [0, 0, 4, 0]])

    boardOperator=BoardOperator()
    result=boardOperator.MoveLeft(testBoard)
    assert result.title==[[2, 0, 0, 0],
                          [2, 0, 0, 0],
                          [4, 0, 0, 0],
                          [4, 0, 0, 0]]

    case=11
    testBoard = Board()
    testBoard.SetBoard([[2, 2, 2, 2],
                        [2, 0, 2, 0],
                        [2, 2, 0, 2],
                        [0, 4, 4, 0]])

    boardOperator=BoardOperator()
    result=boardOperator.MoveLeft(testBoard)
    assert result.title==[[4, 4, 0, 0],
                          [4, 0, 0, 0],
                          [4, 2, 0, 0],
                          [8, 0, 0, 0]]
    case=12
    testBoard = Board()
    testBoard.SetBoard([[0, 0, 0, 2],
                        [2, 0, 0, 0],
                        [2, 2, 0, 0],
                        [0, 0, 4, 0]])

    boardOperator=BoardOperator()
    result=boardOperator.MoveRight(testBoard)
    assert result.title==[[0, 0, 0, 2],
                          [0, 0, 0, 2],
                          [0, 0, 0, 4],
                          [0, 0, 0, 4]]

    case=13
    testBoard = Board()
    testBoard.SetBoard([[2, 2, 2, 2],
                        [2, 0, 2, 0],
                        [2, 2, 0, 2],
                        [0, 4, 4, 0]])

    boardOperator=BoardOperator()
    result=boardOperator.MoveRight(testBoard)
    assert result.title==[[0, 0, 4, 4],
                          [0, 0, 0, 4],
                          [0, 0, 2, 4],
                          [0, 0, 0, 8]]
    case=14
    testBoard = Board()
    testBoard.SetBoard([[0, 0, 0, 2],
                        [0, 0, 0, 2],
                        [0, 0, 0, 4],
                        [0, 0, 0, 8]])

    boardOperator=BoardOperator()
    result=boardOperator.MoveRight(testBoard)
    assert result.title== [[0, 0, 0, 2],
                           [0, 0, 0, 2],
                           [0, 0, 0, 4],
                           [0, 0, 0, 8]] 
    case=15
    testBoard1 = Board()
    testBoard1.SetBoard([[2, 2, 2, 2],
                         [2, 0, 2, 0],
                         [2, 2, 0, 2],
                         [0, 4, 4, 0]])
    testBoard2 = Board()
    testBoard2.SetBoard([[2, 2, 2, 2],
                         [2, 0, 2, 0],
                         [2, 2, 0, 2],
                         [0, 4, 4, 0]])
    boardOperator=BoardOperator()
    result=boardOperator.AreSame(testBoard1,testBoard2)
    assert result==True
    case=16
    testBoard1 = Board()
    testBoard1.SetBoard([[2, 2, 2, 2],
                         [2, 0, 2, 0],
                         [2, 2, 8, 2],
                         [0, 4, 4, 0]])
    testBoard2 = Board()
    testBoard2.SetBoard([[2, 2, 2, 2],
                         [2, 0, 2, 0],
                         [2, 2, 0, 2],
                         [0, 4, 4, 0]])
    boardOperator=BoardOperator()
    result=boardOperator.AreSame(testBoard1,testBoard2)
    assert result==False
    case=99999