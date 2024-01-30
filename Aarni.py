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

name = "Opettaja"

MyMoves = []
OpponentMoves = []

def LaskeMahdollisuus(O): #Opponent moves, Liike
    L = O[-1]
    lista = [0,0,0]
    for i in range(len(O) - 1):
        
        if O[i] == L:
            if O[i + 1] == 0:
                lista[0] += 1
            if O[i + 1] == 1:
                lista[1] += 1
            if O[i + 1] == 2:
                lista[2] += 1
        
    return lista

def GetInt():
    global MyMoves, OpponentMoves
    if len(OpponentMoves) > 0:
        a = LaskeMahdollisuus(OpponentMoves)
        if a[0] < a[2] and a[1] < a[2]:
            return 0
        if a[0] < a[1] and a[2] < a[1]:
            return 2
        if a[1] < a[0] and a[2] < a[0]:
            return 1
    return 2

def Restart(): #Resets all the values for a new fight.
    global MyMoves, OpponentMoves
    MyMoves = []
    OpponentMoves = []
    #Jos jotain omaa resetoitavaa, niin laita se tähän.


## ----- ÄLÄ KOSKE ALUE ----- ##

#Älä muokkaa tai kutus tätä funktiota.
def SetData(MyData,OpponentData):
    global MyMoves,OpponentMoves
    MyMoves = MyData
    OpponentMoves = OpponentData    
