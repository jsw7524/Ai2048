from Board import Board


class EvaluateBoardSum(object):
    def Evaluate(self, board):
        titleSum=0;
        return titleSum

class EvaluateBoardTitleNumber(object):
    def Evaluate(self, board):
        n=0
        for r in range(4):
            for c in range(4):
                if board.title[r][c] > 0:
                    n+=1
        return -1*pow(2,n)

class EvaluateBoardFirstRowFull(object):
    def Evaluate(self, board):
        v=board.title[0][0]+board.title[0][1]+board.title[0][2]+board.title[0][3]
        return v if board.title[0][0] >0 and board.title[0][1] >0 and board.title[0][2] >0 and board.title[0][3] > 0 else 0

class EvaluateBoardFirstRowOrdered(object):
    def Evaluate(self, board):
        penalty=0
        for r in range(4):
            for c in range(4):
                if board.title[r][c] > board.title[0][0]:
                    if not (r==0 and c==0):
                        return -(2**20)
        for r in range(4):
            for c in range(4):
                if board.title[r][c] > 0:
                    penalty+=10*(r+c)*abs(board.title[0][0]-board.title[r][c])
        return (-1)*penalty

class EvaluateBoardFirstColumnOrdered(object):
    def Evaluate(self, board):
        return 0
        # v=board.title[0][0]+board.title[1][0]+board.title[2][0]+board.title[3][0]
        # return (1)*v if board.title[0][0] > 0 and board.title[1][0] > 0 and board.title[2][0] > 0 and board.title[3][0] > 0 else 0

class EvaluateBoardMaxCorner(object):
    def Evaluate(self, board):
        titleMax=board.title[0][0]
        counter=0
        for r in range(4):
            for c in range(4):
                if titleMax < board.title[r][c]:
                    counter+=1
        return 2**20 if counter ==0 else -(2**20)

if __name__ == "__main__":
    case=1
    testBoard = Board()
    evaluateBoardSum=EvaluateBoardSum()
    result=evaluateBoardSum.Evaluate(testBoard)
    testBoard.SetBoard([[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 2, 0, 0],
                        [0, 2, 0, 0]])
    assert 4 == result
    case = 2
    testBoard = Board()
    testBoard.SetBoard([[0, 8, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]])
    evaluateBoardSum = EvaluateBoardSum()
    result = evaluateBoardSum.Evaluate(testBoard)
    assert 12 == result
    case = 3
    testBoard = Board()
    testBoard.SetBoard([[0, 8, 0, 0],
                        [0, 0, 0, 0],
                        [0, 2, 0, 64],
                        [0, 2, 0, 0]])
    evaluateBoardSum = EvaluateBoardSum()
    result = evaluateBoardSum.Evaluate(testBoard)
    assert 80 == result
    case = 4
    testBoard = Board()
    testBoard.SetBoard([[2, 0, 4, 2],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]])
    evaluateBoardFirstRowFull = EvaluateBoardFirstRowFull()
    result = evaluateBoardFirstRowFull.Evaluate(testBoard)
    assert 0 == result
    case = 5
    testBoard = Board()
    testBoard.SetBoard([[2, 4, 4, 2],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]])
    evaluateBoardFirstRowFull = EvaluateBoardFirstRowFull()
    result = evaluateBoardFirstRowFull.Evaluate(testBoard)
    assert 18 == result
    case = 6
    testBoard = Board()
    testBoard.SetBoard([[64, 4, 4, 2],
                        [0, 0, 0, 0],
                        [0, 0, 64, 0],
                        [0, 0, 0, 0]])
    evaluateBoardMaxCorner = EvaluateBoardMaxCorner()
    result = evaluateBoardMaxCorner.Evaluate(testBoard)
    assert 96 == result
    case = 6
    testBoard = Board()
    testBoard.SetBoard([[64, 4, 4, 0],
                        [0, 0, 0, 0],
                        [0, 0, 128, 0],
                        [0, 0, 0, 0]])
    evaluateBoardMaxCorner = EvaluateBoardMaxCorner()
    result = evaluateBoardMaxCorner.Evaluate(testBoard)
    assert 0 == result