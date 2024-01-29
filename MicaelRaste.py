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

name = "Counter"

MyMoves = []
OpponentMoves = []

def GetInt():
    global MyMoves, OpponentMoves

    if len(OpponentMoves) == 0:
        return 1  # Paperi

    # Anylysoi vihun liikkeet ja muuta omaa strategiaa sen mukaan.
    recent_moves = OpponentMoves[-5:]  # Katso viittä viimeisintä liikettä ja adaptoi

    # Jos vihu on toistanut liikkeen, valitse voittava liike.
    if len(set(recent_moves)) == 1:
        return (recent_moves[0] + 1) % 3

    # Jos vihulla on erilaisia liikkeitä, analysoi niiden frekvenssi ja valitse vastaliike.
    move_counts = [recent_moves.count(0), recent_moves.count(1), recent_moves.count(2)]

    # Valitse liike joka voittaa vihun eniten käyteytyn liikkeen.
    counter_move = (move_counts.index(max(move_counts)) + 1) % 3

    return counter_move


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