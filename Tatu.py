# Koodin nimi tulee olla oma nimesi.
# Botin nimen saat keksiä itse, mutta sen tulee olla asiallinen.
# Botilla on kolme pakollista funktiota:
# 1. GetBool() -> Oma funktiosi, joka palauttaa totuusarvon.
#    Saat itse keksiä valinta periaatteen.
# 2. SetData(MyData, OpponentData) -> Saat dataa meneillään olevasta taistelusta.
# 3. Restart() -> Resetoi saadun datan.
#    Resetointi tapahtuu aina ennen kun saat uuden vastustajan.
#    Resetoinnin tulee resetoida tiedot omista vanhoista liikkeistä ja vastustajan vanhoista liikkeistä.
#    Saat myös resetoida muita muuttujia, joita itse olet asettanut.

name = "Snitches get Bitcoins" #:D

MyMoves = []
OpponentMoves = []
MatchNmb = 0

def GetBool():
    global MyMoves, OpponentMoves, MatchNmb
    
    MatchNmb += 1
    
    if MatchNmb <= 5:
        return MatchNmb % 5 == 0
    else:
        return MatchNmb % 3 == 0

def Restart():
    # Resetaa kaikki arvot uutta taistelua varten.
    global MyMoves, OpponentMoves, MatchNmb
    MyMoves = []
    OpponentMoves = []
    MatchNmb = 0

# Älä muokkaa SetData-funktiota, se on tärkeä tietojen siirtämiseksi.
def SetData(MyData, OpponentData):
    global MyMoves, OpponentMoves
    MyMoves = MyData
    OpponentMoves = OpponentData
