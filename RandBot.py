import random
name = "Aarni"
for i in range(8): #Random name... hehe
    name += chr(random.randint(33,127)) 

MyMoves = []
OpponentMoves = []

def SetData(MyData,OpponentData):
    MyMoves = MyData
    OpponentMoves = OpponentData

def Restart():
    global MyMoves, OpponentMoves
    MyMoves = []
    OpponentMoves = []

def GetInt():
    return random.randint(0,2)



    
