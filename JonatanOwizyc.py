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

name = "NiCE TRY"

MyMoves = []
OpponentMoves = []

def GetBool():
    global MyMoves, OpponentMoves
    round_number = len(MyMoves) + 1
    
    if round_number <= 100:

        return round_number % 10 != 0
    else:

        return round_number % 10 == 0 and round_number <= 200

def Restart():
    global MyMoves, OpponentMoves
    MyMoves = []
    OpponentMoves = []


## ----- ÄLÄ KOSKE ALUE ----- ##

#Älä muokkaa tai kutsu tätä funktiota.
def SetData(MyData,OpponentData):
    global MyMoves, OpponentMoves
    MyMoves = MyData
    OpponentMoves = OpponentData    
