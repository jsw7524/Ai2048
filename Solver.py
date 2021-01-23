from BoardOperator import BoardOperator
from Evaluater import EvaluateBoardSum, EvaluateBoardFirstRowFull, EvaluateBoardMaxCorner, EvaluateBoardFirstRowOrdered, \
    EvaluateBoardFirstColumnOrdered, EvaluateBoardTitleNumber


class Sovler2048(object):
    def __init__(self):
        self.boardOperator = BoardOperator()
        self.Evaluaters=[EvaluateBoardSum(),EvaluateBoardFirstRowFull(),EvaluateBoardFirstRowOrdered(),EvaluateBoardFirstColumnOrdered(),EvaluateBoardMaxCorner(),EvaluateBoardTitleNumber()]

    def NextMove(self,board):
        boardsFuture = [("UP",self.boardOperator.MoveUp(board)),("DOWN",self.boardOperator.MoveDown(board)),("LEFT",self.boardOperator.MoveLeft(board)),("RIGHT",self.boardOperator.MoveRight(board))]
        scores = []
        for b in boardsFuture:
            if self.boardOperator.AreSame(b[1], board):
                continue
            scores.append((self.DFS(b[1],0),b[0]))
        scores.sort(reverse=True)
        return scores[0][1]



    def DFS(self,board,depth):
        if (depth<2):
            boardsFuture = [self.boardOperator.MoveUp(board),self.boardOperator.MoveDown(board),self.boardOperator.MoveLeft(board),self.boardOperator.MoveRight(board)]
            scores=[]
            for b in boardsFuture:
                if self.boardOperator.AreSame(b,board):
                    continue
                for r in range(4):
                    for c in range(4):
                        if 0==b.title[r][c]:
                            b.title[r][c]=2
                            scores.append(self.DFS(b,depth+1))
                            b.title[r][c]=0
            if 0==len(scores):
                return 0
            return sum(scores) / len(scores)
        else:
            score=0
            for e in self.Evaluaters:
                score+=e.Evaluate(board)
            return score
