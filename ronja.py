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

name = "Antares" 

MyMoves = []
OpponentMoves = []

def GetBool():
    global MyMoves, OpponentMoves
    
    answer = False
    
    number_of_opponent_trues = 0 #laskee kuinka monta trueta vastustaja on saanut
    number_of_my_trues = 0       #laskee kuinka monta trueta pelaaja on saanut
            
    for x in OpponentMoves:
        if x == True:
            number_of_opponent_trues = number_of_opponent_trues + 1 
            
    for x in MyMoves:
        if x == True: 
            number_of_my_trues = number_of_my_trues + 1
            
    if number_of_my_trues > number_of_opponent_trues: #jos pelaaja on vastannut true enemmän kuin vastustaja, se vastaa false
        answer = False
    else:
        answer = True
        
    if len(MyMoves) % 2 == 0: #joka toisella kerralla vastaa true
        answer = True
            
            
    if len(MyMoves) % 3 == 0 and len(OpponentMoves) > 0: #joka kolmannella vastaa eritavalla kuin vastustaja edellisellä kerralla
        if OpponentMoves[len(OpponentMoves)-1] == False:
            answer = True
        else:
            answer = False
    
    if len(OpponentMoves) >= 2:
        if OpponentMoves[len(OpponentMoves)-2] == OpponentMoves[len(OpponentMoves)-1]: #jos vastustaja on vastannut kahdella edellisellä kerralla true, pelaaja vastaa false ja toisinpäin
            if OpponentMoves[len(OpponentMoves)-1] == True:
                answer = False
            else:
                answer = True
                
    if len(MyMoves) > 0:
        if number_of_my_trues / len(MyMoves) > 0.2: #lasketaan 80% pitää olla falsea
            answer = False
            
    #Tämän funktion tulee palauttaa True tai False.
    #Saat itse valita miten ohjelma sen päättää.
    #Käytössäsi on molempien pelaajien data aiemmilta kierroksilta.
    #SetData-funktio asettaa listat, joissa on molempien pelaajien aiemmat liikeet.
    return answer

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

