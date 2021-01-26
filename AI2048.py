import time
import unittest
from Board import Board
from Solver import Sovler2048
from WebOperator import WebOperator
from BoardOperator import BoardOperator

if __name__ == "__main__":
    webOperator = WebOperator()
    sovler=Sovler2048()
    i=0
    scores=[]
    while i < 10:
        print("start new game")
        while not webOperator.IsGameOver():
            time.sleep(0.1)
            board=webOperator.GetBoardInfo()
            webOperator.RandomMove()
            print(webOperator.GetScore())
            print("RandomMove")
#            m=sovler.NextMove(board)
#            webOperator.Move(m)
        scores.append(webOperator.GetScore())     
        time.sleep(1)
        print("END")
        webOperator.ResetGame()
        time.sleep(1)
        i+=1
    avg=sum(scores)/len(scores)
    print(avg)
case=99999