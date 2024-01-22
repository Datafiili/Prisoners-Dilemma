import random
from typing import List

name = "Penabotti"

MyMoves: List[bool] = []
OpponentMoves: List[bool] = []

def GetBool() -> bool:
    if len(OpponentMoves) > 0:
        last_opponent_move = OpponentMoves[-1]
        return not last_opponent_move
    else:
        return random.choice([True, False])

def SetData(MyData: List[bool], OpponentData: List[bool]):
    global MyMoves, OpponentMoves
    MyMoves = MyData
    OpponentMoves = OpponentData

def Restart():
    global MyMoves, OpponentMoves
    MyMoves = []
    OpponentMoves = []
   
