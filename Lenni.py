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

name = "Smart bot"

MyMoves = []
OpponentMoves = []

def GetBool():
    global MyMoves, OpponentMoves
    c = len(OpponentMoves)-1
    if c < 1:

        return True
        
    else:
        if OpponentMoves[c] == False:
            return OpponentMoves[c]
        
        else:
            return OpponentMoves[c]
    

def Restart(): #Resets all the values for a new fight.
    global MyMoves, OpponentMoves
    MyMoves = []
    OpponentMoves = []
    #Jos jotain omaa resetoitavaa, niin laita se tähän.


## ----- ÄLÄ KOSKE ALUE ----- ##

#Älä muokkaa tai kutus tätä funktiota.
def SetData(MyData,OpponentData):
    global MyMoves, OpponentMoves
    MyMoves = MyData
    OpponentMoves = OpponentData    
