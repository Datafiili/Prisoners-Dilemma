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

name = "Kova"

MyMoves = []
OpponentMoves = []

def GetInt():
    global MyMoves, OpponentMoves
    #Tämän funktion tulee palutaa 0, 1 tai 2.
    #Saat itse valita miten ohjelma sen päättää.
    #Käytössäsi on molempien pelaajien data aiemmilta kierroksilta.
    #SetData-funktio asettaa listat, joissa on molempien pelaajien aiemmat liikeet.
    if len(OpponentMoves) == 0:
        return 2
    
    kivi = 0
    paperi = 0
    sakset = 0
    if len(OpponentMoves) % 2 == 0:
        for i in range(len(OpponentMoves)):
            if OpponentMoves[-i] == 0:
                kivi += 1
            elif OpponentMoves[-i] == 1:
                paperi += 1
            elif OpponentMoves[-i] == 2:
                sakset += 1
        if sakset > kivi and sakset > paperi:
            return 0
        elif paperi > sakset and paperi > kivi:
            return 2
        elif kivi > sakset and kivi > paperi:
            return 1
    else:
        for i in range(len(MyMoves)):
            if MyMoves[-i] == 0:
                 kivi += 1
            elif MyMoves[-i] == 1:
                paperi += 1
            elif MyMoves[-i] == 2:
                 sakset += 1

        if sakset > kivi and sakset > paperi:
            return 1
        elif paperi > sakset and paperi > kivi:
            return 0
        elif kivi > sakset and kivi > paperi:
            return 2   



        

    return 0

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
