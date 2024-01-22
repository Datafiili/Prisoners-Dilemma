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

name = "Ikavalko"

MyMoves = []
OpponentMoves = []
laskuri = 1

def GetBool():
    global MyMoves, OpponentMoves,laskuri

    if not OpponentMoves:
        return True
    else:
        laskuri + 1
        if laskuri % 2 == 0:
            return True
        else:
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
