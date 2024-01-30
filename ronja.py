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

name = ":D"

 # 0 = kivi, 1 = paperi, 2 = Sakset

MyMoves = []
OpponentMoves = []

def GetInt():
    global MyMoves, OpponentMoves
   
   
    answer = 1
   
    number_of_opponent_sakset = 0 #laskee kuinka monta kertaa vastustaja on laittanut sakset
    number_of_opponent_kivi = 0 #laskee kuinka monta kertaa vastustaja on laittanut kivi
    number_of_opponent_paperi = 0 #laskee kuinka monta kertaa vastustaja on laittanut paperi

    number_of_my_sakset = 0       #laskee kuinka monta kertaa pelaaja on laittanut sakset
    number_of_my_kivi = 0       #laskee kuinka monta kertaa pelaaja on laittanut kivi
    number_of_my_paperi = 0        #laskee kuinka monta kertaa pelaaja on laittanut paperi
           
    for x in OpponentMoves:
        if x == 0:
            number_of_opponent_kivi = number_of_opponent_kivi + 1
           
    for x in OpponentMoves:
        if x == 1:
            number_of_opponent_paperi = number_of_opponent_paperi + 1
           
    for x in OpponentMoves:
        if x == 2:
            number_of_opponent_sakset = number_of_opponent_sakset + 1
           
    for x in MyMoves:
        if x == 0:
            number_of_my_kivi = number_of_my_kivi + 1
           
    for x in MyMoves:
        if x == 1:
            number_of_my_paperi = number_of_my_paperi + 1
           
    for x in MyMoves:
        if x == 2:
            number_of_my_sakset = number_of_my_sakset + 1
           
           
           
    if number_of_my_sakset > number_of_opponent_sakset: #jos pelaaja on vastannut sakset enemmän kuin vastustaja, se vastaa paperi
        answer = 0
    
   
    if number_of_my_paperi > number_of_opponent_paperi: #jos pelaaja on vastannut paperi enemmän kuin vastustaja, se vastaa sakset
        answer = 2
   
   
    if number_of_my_kivi > number_of_opponent_kivi: #jos pelaaja on vastannut kivi enemmän kuin vastustaja, se vastaa paperi
        answer = 1
   
   
       
       
    if len(MyMoves) % 2 == 0: #joka toisella kerralla vastaa paperi
        answer = 1
           
           
    if len(MyMoves) % 3 == 0 and len(OpponentMoves) > 0: #joka kolmannella vastaa eritavalla kuin vastustaja edellisellä kerralla
        if OpponentMoves[len(OpponentMoves)-1] == 0:
            answer = 1
        elif OpponentMoves[len(OpponentMoves)-1] == 1:
            
            answer = 2
        else:
            answer = 0
   
    if len(OpponentMoves) >= 2:
        if OpponentMoves[len(OpponentMoves)-2] == OpponentMoves[len(OpponentMoves)-1]: #jos vastustaja on vastannut kahdella edellisellä kerralla saman, pelaaja vastaa voittajan
            if OpponentMoves[len(OpponentMoves)-1] == 0:
                answer = 1
            if OpponentMoves[len(OpponentMoves)-1] == 1:
                answer = 2
            if OpponentMoves[len(OpponentMoves)-1] == 2:
                answer = 0
               
#     if len(MyMoves) > 0:
#         if number_of_my_paperi / len(MyMoves) > 0.2: #lasketaan 80% pitää olla falsea
#             answer = 1
   
   
   
   
   
    #Tämän funktion tulee palutaa 0, 1 tai 2.
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
    MyMoves = MyData
    OpponentMoves = OpponentData    
