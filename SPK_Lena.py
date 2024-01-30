name = "Lena_BOTTI"

MyMoves = []
OpponentMoves = []

def GetInt():
    global MyMoves, OpponentMoves
    
    # Tarkistetaan, kuka voitti edellisen kierroksen, ja valitaan sen perusteella seuraava liike.
    if len(MyMoves) > 0 and len(OpponentMoves) > 0:
        my_last_move = MyMoves[-1]
        opponent_last_move = OpponentMoves[-1]

        if my_last_move == (opponent_last_move + 1) % 3:
            # Jos voitin edellisen kierroksen, valitsen vastaliikkeen.
            return (opponent_last_move + 2) % 3
        else:
            # Muuten valitsen satunnaisen liikkeen.
            return random.choice([0, 1, 2])
    else:
        # Ensimmäisellä kierroksella valitsen satunnaisen liikkeen.
        return random.choice([0, 1, 2])

def Restart(): 
    global MyMoves, OpponentMoves
    MyMoves = []
    OpponentMoves = []

## ----- ÄLÄ KOSKE ALUE ----- ##

# Älä muokkaa tai kutus tätä funktiota.
def SetData(MyData, OpponentData):
    global MyMoves, OpponentMoves
    MyMoves = MyData
    OpponentMoves = OpponentData
