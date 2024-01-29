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

name = "Vergilius"

MyMoves = []
OpponentMoves = []

def GetInt():
    global MyMoves, OpponentMoves
    # Tämän funktion tulee palautaa 0, 1 tai 2.
    # Pelaajan liikkeen valinta perustuu vastustajan aiempiin liikkeisiin.
    # Jos vastustajan liikkeet ovat tyhjät, palautetaan 1 (paperi).
    # Muussa tapauksessa lasketaan vastustajan aiempien liikkeiden määrät.
    # Palautetaan pelaajan liike sen perusteella, mikä vastustajan liikkeistä on yleisin.
    if len(OpponentMoves) == 0:
        return 1
    
    k = 0  # kivi
    p = 0  # paperi
    s = 0  # sakset
    
    if len(OpponentMoves) != 0:
        
        for i in range(len(OpponentMoves)):
            # Laskee vastustajan liikkeiden määrät.
            # k = kivi, p = paperi, s = sakset.
            # Jos vastustaja on valinnut kiven, lisätään k:n arvoa yhdellä.
            if OpponentMoves[i] == 0:
                k += 1
            # Jos vastustaja on valinnut paperin, lisätään p:n arvoa yhdellä.  
            elif OpponentMoves[i] == 1:
                p += 1
            # Jos vastustaja on valinnut sakset, lisätään s:n arvoa yhdellä.   
            elif OpponentMoves[i] == 2:
                s += 1
        # Jos k:n arvo on suurempi kuin p:n ja s:n arvot, palautetaan 0 (kivi).       
        if s > k and s > p:
            return 0  # sakset
        
        # Jos p:n arvo on suurempi kuin k:n ja s:n arvot, palautetaan 2 (paperi).
        elif p > s and p > k:
            return 2  # paperi
        # Jos k:n arvo on suurempi kuin p:n ja s:n arvot, palautetaan 1 (kivi).
        elif k > s and k > p:
            return 1  # kivi
    
    # Jos k:n, p:n ja s:n arvot ovat yhtä suuret, palautetaan 0 (Kivi).
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
