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

name = "k4dd1m4771"

MyMoves = []
OpponentMoves = []

def GetBool():
    global MyMoves, OpponentMoves
    #Tämän funktion tulee palauttaa True tai False.
    #Saat itse valita miten ohjelma sen päättää.
    #Käytössäsi on molempien pelaajien data aiemmilta kierroksilta.
    #SetData-funktio asettaa listat, joissa on molempien pelaajien aiemmat liikeet.
    falseCount = 0
    trueCount = 0
    for i in range(len(OpponentMoves)):
        if(OpponentMoves[i] == False):
            falseCount+=1
        if(OpponentMoves[i] == True):
            trueCount+=1
    if(falseCount >= trueCount):
        return False
    if(trueCount < falseCount):
        return True
    return False
    

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
