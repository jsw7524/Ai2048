import time
import unittest
from Board import Board
from Solver import Sovler2048
from WebOperator import WebOperator
from BoardOperator import BoardOperator

if __name__ == "__main__":
    webOperator = WebOperator()
    sovler=Sovler2048()
    while ("Game over!" not in webOperator.chrome.page_source):
        time.sleep(1)
        board=webOperator.GetBoardInfo()
        m=sovler.NextMove(board)
        webOperator.Move(m)
        print(m)
case=99999