name = "PenaBotti"

MyMoves = []
OpponentMoves = []

def GetInt():
    global MyMoves, OpponentMoves
   
    if OpponentMoves.count(1) > OpponentMoves.count(2):
        return 2
    elif OpponentMoves.count(0) >= 3:
        return 0
    else:
        return 1


def Restart():
    global MyMoves, OpponentMoves
    MyMoves = []
    OpponentMoves = []
   

# Älä muokkaa SetData-funktiota, koska se on yhteyspinta pelilogiikkaan.
def SetData(MyData, OpponentData):
    global MyMoves, OpponentMoves
    MyMoves = MyData
    OpponentMoves = OpponentData
