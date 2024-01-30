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

name = "Botti"

MyMoves = []
OpponentMoves = []

def GetInt():
    global MyMoves, OpponentMoves

    A = OpponentMoves.count(0) #Kivi
    B = OpponentMoves.count(1) #Paperi
    C = OpponentMoves.count(2) #Sakset
    
    
    Viimeisin = OpponentMoves[-1]
    Maara = 0
    for i in range(len(OpponentMoves)-2, -1, -1):
        if OpponentMoves[i] == Viimeisin:
            Maara += 1
        else:
            break
    
    if Maara >= 2:
        return (Viimeisin +1) % 3
        
    if A >= B and A >= C:
        return 1
    if B >= A and B >= C:
        return 2
    if C >= A and C >= B:
        return 0
        
    return 2
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