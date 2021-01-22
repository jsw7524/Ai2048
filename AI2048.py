import time
import unittest
from Board import Board
from WebOperator import WebOperator
from BoardOperator import BoardOperator

class EvaluateBoardSum(object):
    def Evaluate(self, board):
        titleSum=0;
        for r in range(4):
            for c in range(4):
                v=board.title[r][c]
                if v in [8,16,32]:
                    titleSum += (1.5)*v
                else:
                    titleSum += v                  
        return titleSum
        
class EvaluateBoardFirstRowFull(object):
    def Evaluate(self, board):
        v=board.title[0][0]+board.title[0][1]+board.title[0][2]+board.title[0][3]
        return (1.5)*v if board.title[0][0] > 0 and board.title[0][1] > 0 and board.title[0][2] > 0 and board.title[0][3] > 0 else 0        

class EvaluateBoardMaxCorner(object):
    def Evaluate(self, board):
        titleMax=board.title[0][0];
        for r in range(4):
            for c in range(4):
                if titleMax < board.title[r][c]:
                    return 0
        return (1.5)*titleMax

if __name__ == "__main__":
    case=1
    testBoard = Board()
    testBoard.SetBoard([[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 2, 0, 0],
                        [0, 2, 0, 0]])
    evaluateBoardSum=EvaluateBoardSum()
    result=evaluateBoardSum.Evaluate(testBoard)
    assert 4==result  
    case=2
    testBoard = Board()
    testBoard.SetBoard([[0, 8, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]])
    evaluateBoardSum=EvaluateBoardSum()
    result=evaluateBoardSum.Evaluate(testBoard)
    assert 12==result      
    case=3
    testBoard = Board()
    testBoard.SetBoard([[0, 8, 0, 0],
                        [0, 0, 0, 0],
                        [0, 2, 0, 64],
                        [0, 2, 0, 0]])
    evaluateBoardSum=EvaluateBoardSum()
    result=evaluateBoardSum.Evaluate(testBoard)
    assert 80==result  
    case=4
    testBoard = Board()
    testBoard.SetBoard([[2, 0, 4, 2],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]])
    evaluateBoardFirstRowFull=EvaluateBoardFirstRowFull()
    result=evaluateBoardFirstRowFull.Evaluate(testBoard)
    assert 0==result     
    case=5
    testBoard = Board()
    testBoard.SetBoard([[2, 4, 4, 2],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]])
    evaluateBoardFirstRowFull=EvaluateBoardFirstRowFull()
    result=evaluateBoardFirstRowFull.Evaluate(testBoard)
    assert 18==result 
    case=6
    testBoard = Board()
    testBoard.SetBoard([[64, 4, 4, 2],
                        [0, 0, 0, 0],
                        [0, 0, 64, 0],
                        [0, 0, 0, 0]])
    evaluateBoardMaxCorner=EvaluateBoardMaxCorner()
    result=evaluateBoardMaxCorner.Evaluate(testBoard)
    assert 96==result   
    case=6
    testBoard = Board()
    testBoard.SetBoard([[64, 4, 4, 0],
                        [0, 0, 0, 0],
                        [0, 0, 128, 0],
                        [0, 0, 0, 0]])
    evaluateBoardMaxCorner=EvaluateBoardMaxCorner()
    result=evaluateBoardMaxCorner.Evaluate(testBoard)
    assert 0==result      
    case=99999