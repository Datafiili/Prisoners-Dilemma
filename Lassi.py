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

name = "ORANGE BOX"

MyMoves = []
OpponentMoves = []

def GetBool():
    global MyMoves, OpponentMoves
    #Tämän funktion tulee palauttaa True tai False.
    #Saat itse valita miten ohjelma sen päättää.
    #Käytössäsi on molempien pelaajien data aiemmilta kierroksilta.
    #SetData-funktio asettaa listat, joissa on molempien pelaajien aiemmat liikeet.
    
    #Ulostulo päättely.
    if len(MyMoves) > 1:
        
        #Kirjaa ylös omat viimeiset kaksi ja kolme liikettä.
        My2Moves = MyMoves[len(MyMoves) - 2:]
        if len(MyMoves) > 2:
            My3Moves = MyMoves[len(MyMoves) - 3:]
            
        #Ensin tarkista onko kaksi viimeisintä liikettä erit, jos viimeisin on True, palauta True, muuton False
        if MyMoves[len(MyMoves) - 1] != MyMoves[len(MyMoves) - 2]:
            if MyMoves[len(MyMoves) - 1] == True:
                return True
            else:
                return False
        
        #Jos entinen tarkistus epäonnistui, jatketaan laajempaan päättelyyn
        else:
            #Jos viimeiset kaksi ovat samoja, palauta sama vielä kerran
            if My2Moves[0] == My2Moves[1]:
                if My2Moves[0] == True:
                    return True
                else:
                    return False
                
            #Jos viimeiset kolme ovat samoja, palauta vastainen
            else:
                if My3Moves[1] == My3Moves[0] and My3Moves[1] == My3Moves[2]:
                    if My3Moves[0] == False:
                        return True
                    else:
                        return False
    
    else:
        #Aloitus liikkeet, juoksee vain kerran.
        if len(MyMoves) < 1:
            return True
        else:
            if len(MyMoves) < 2:
                return False
            
    #Varmuuden vuoksi
    return True

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
