# ----- Ohjeet -----
# Koodin nimi tulee olla oma nimesi.
# Botin nimen saat keksiä itse, mutta sen tulee olla asiallinen.
# Botilla on kolme pakollista funktiota:
# 1. GetBool() -> Oma funktiosi, joka palauttaa totuusarvon.
# Saat itse keksiä valinta periaatteen.
# 2. SetData(MyData,OpponentData) -> Saat dataa meneillään olevasta taistelusta.
# 3. Restart() -> Resetoi saadun datan.
# Resetointi tapahtuu aina ennen kun saat uuden vastustajan.
# Resetoinnin tulee resetoida tiedot omista vanhoista liikkeistä ja vastustajan vanhoista liikkeista.
# Saat myös resetoida muita muuttujia, joita itse olet asettanut.

name = "Alcatraz"

MyMoves = []
OpponentMoves = []

def GetBool():
    global MyMoves, OpponentMoves

    # Cooperate in the first round
    if not MyMoves and not OpponentMoves:
        return True

    # If the opponent defected in the previous round, retaliate by cooperating
    if OpponentMoves and not OpponentMoves[-1]:
        return True

    # If the opponent has defected multiple times, cooperate to encourage cooperation
    if OpponentMoves.count(False) >= 2:
        return True

    # Otherwise, cooperate
    return True

def Restart():  # Resets all the values for a new fight.
    global MyMoves, OpponentMoves
    MyMoves = []
    OpponentMoves = []
    # Jos jotain omaa resetoitavaa, niin laita se tähän.

# ----- ÄLÄ KOSKE ALUE ----- #

# Älä muokkaa tai kutus tätä funktiota.
def SetData(MyData, OpponentData):
    global MyMoves, OpponentMoves
    MyMoves = MyData
    OpponentMoves = OpponentData
