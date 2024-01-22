#BOTIN NIMI: Lena

MyMoves = []
OpponentMoves = []

def GetBool():
    global MyMoves, OpponentMoves
    if not OpponentMoves:
        return True 
    elif OpponentMoves.count("D") >= OpponentMoves.count("C"):
        return False
    else:
        return True  

def Restart():
    global MyMoves, OpponentMoves
    MyMoves = []
    OpponentMoves = []
   


def SetData(MyData, OpponentData):
    global MyMoves, OpponentMoves
    MyMoves = MyData
    OpponentMoves = OpponentData
