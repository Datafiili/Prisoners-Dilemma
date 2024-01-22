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

name = "DrEvilbot_V2"

MyMoves = []
OpponentMoves = []

def GetBool():
    global MyMoves, OpponentMoves
    
    # Katso onko tarpeeksi dataa tehdäksesi päätöksen
    if len(OpponentMoves) < 2:
        return True
    
    # Analysoi dataa ja tee päätös
    recent_moves = OpponentMoves[-2:]
    if recent_moves == [True, True]:
        return False
    elif recent_moves == [True, False]:
        return True
    elif recent_moves == [False, True]:
        return True
    elif recent_moves == [False, False]:
        return False
    
    # Jos vihollinen valitsee vain yhden vaihtoehdon, valitse vastakkainen
    if OpponentMoves[-1] == OpponentMoves[-2]:
        return not OpponentMoves[-1]
    
    # Jos ei ole tarpeeksi dataa, arvaa
    true_count = OpponentMoves[-10:].count(True)
    false_count = OpponentMoves[-10:].count(False)
    
    # Tee älykäs päätös
    if true_count > false_count:
        return False
    elif true_count < false_count:
        return True
    else:
        return not OpponentMoves[-1]


def Restart(): #Resets all the values for a new fight.
    global MyMoves, OpponentMoves
    MyMoves = []
    OpponentMoves = []
    #Jos jotain omaa resetoitavaa, niin laita se tähän.


## ----- ÄLÄ KOSKE ALUE ----- ##

#Älä muokkaa tai kutsu tätä funktiota.
def SetData(MyData,OpponentData):
    global MyMoves, OpponentMoves
    MyMoves = MyData
    OpponentMoves = OpponentData    
