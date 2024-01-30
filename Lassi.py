## ----- Ohjeet ----- ##
#Koodin nimi tulee olla oma nimesi.
#Botin nimen saat keksiä itse, mutta sen tulee olla asiallinen.
#Botilla on kolme pakollista funktiota:
#1. GetBool() -> Oma funktiosi, joka palauttaa totuusarvon.
#Saat itse keksiä valinta perjaatteen.
#2. SetData(MyData,OpponentData) -> Saat dataa meneillään olevasta taistelusta.
#3. Restart() -> Resetoi saadun datan.
#Resetointi tapahtuu aina ennen kun saat uuden vastustajan.
#Resetoinnin tulee resetoida tiedot omista vanhoista liikkeistä ja vastustajan vanhoista liikkeista.
#Saat myös resetoida muita muuttujia, joita itse olet asettanut.

name = "Orange Rock"

MyMoves = []
OpponentMoves = []

def GetInt():
    global MyMoves, OpponentMoves
    
    if len(MyMoves) > 1:
        if len(OpponentMoves) == 1:
            if OpponentMoves[0] == 2:
                return 0
        
        #inspect if last move was a victory or loss
        #if the former, repeat the winning move
        LatestMove = MyMoves[len(MyMoves) - 1]
        LatestOppMove = OpponentMoves[len(OpponentMoves) - 1]
        
        while True:
            if LatestMove == LatestOppMove:
                break
            elif LatestMove == 0 and LatestOppMove == 1:
                break
            elif LatestMove == 0 and LatestOppMove == 2:
                return 0
            elif LatestMove == 1 and LatestOppMove == 0:
                return 1
            elif LatestMove == 1 and LatestOppMove == 2:
                break
            elif LatestMove == 2 and LatestOppMove == 0:
                break
            elif LatestMove == 2 and LatestOppMove == 1:
                return 2
        #if the last move was a loss, choose a new approach
        #depending on the two other options, whichever one the opponent has used more often; counter
        OppZeros = OpponentMoves.count(0)
        OppOnes = OpponentMoves.count(1)
        OppTwos = OpponentMoves.count(2)
        
        if LatestMove == 0:
            if OppOnes > OppTwos:
                return 2
            else:
                return 0

        elif LatestMove == 1:
            if OppZeros > OppTwos:
                return 1
            else:
                return 0
            
        elif LatestMove == 2:
            if OppZeros > OppOnes:
                return 1
            else:
                return 2
            
    #First move
    else:
        return 1

def Restart(): #Resets all the values for a new fight.
    global MyMoves, OpponentMoves
    MyMoves = []
    OpponentMoves = []
    #Jos jotain omaa resetoitavaa, niin laita se tähän.


## ----- ÄLÄ KOSKE ALUE ----- ##

#Älä muokkaa tai kutus tätä funktiota.
def SetData(MyData,OpponentData):
    MyMoves = MyData
    OpponentMoves = OpponentData    
