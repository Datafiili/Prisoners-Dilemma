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

name = "ASD"

MyMoves = []
OpponentMoves = []

def GetInt():
    global MyMoves, OpponentMoves
    #Tämän funktion tulee palutaa 0, 1 tai 2.
    #Saat itse valita miten ohjelma sen päättää.
    #Käytössäsi on molempien pelaajien data aiemmilta kierroksilta.
    #SetData-funktio asettaa listat, joissa on molempien pelaajien aiemmat liikeet.
    # 0 = kivi, 1 = paperi, 2 = Sakset
    opKivi = 0
    opPaperi = 0
    opSakset = 0
    if len(OpponentMoves) == 0:
        return 0
    
    for i in OpponentMoves:
        if i == 0:
            opKivi += 1
        elif i == 1:
            opPaperi += 1
        elif i == 2:
            opSakset += 1

    if opKivi > opPaperi and opKivi > opSakset:
        return 1
    elif opPaperi > opKivi and opPaperi > opSakset:
        return 2
    elif opSakset > opKivi and opSakset > opPaperi:
        return 0
    else:
        if opKivi == opPaperi:
            return 1
        elif opKivi == opSakset:
            return 0
        elif opPaperi == opSakset:
            return 2

    


def Restart(): #Resets all the values for a new fight.
    global MyMoves, OpponentMoves, opKivi, opPaperi, opSakset
    MyMoves = []
    OpponentMoves = []
    opKivi = 0
    opPaperi = 0
    opSakset = 0
    #Jos jotain omaa resetoitavaa, niin laita se tähän.


## ----- ÄLÄ KOSKE ALUE ----- ##

#Älä muokkaa tai kutus tätä funktiota.
def SetData(MyData,OpponentData):
    global MyMoves, OpponentMoves
    MyMoves = MyData
    OpponentMoves = OpponentData    
