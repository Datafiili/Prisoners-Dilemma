## ----- Ohjeet ----- ##
#Jokaisen botti taistelee jokaista muuta bottia vastaan,
#tämä toistetaan viisi kertaa.
#Jokaisen botille lasketaan pisteet
#Lopuksi tarkastellaan, että kenen botilla on eniten pisteitä

#Millaisen botin saa rakentaa?
#Satunnaisluvut ovat kielletty ja botti ei saa lukea toisia koodeja.
#Muuten vapaat kädet, lisää ohjeita ExampleBot.py:ssä

#Jokainen lähettää Teams-kautta oman bottikoodinsa. Bottikoodin nimi tulee olla omanimesi.
#Esim: Aarni.py

## -------------------- Prisoners Dilemma -------------------- ##
import os


## ----- Osallistuja lista ----- ##
#Osallistuja lista eli kaikkien koodien nimet.
nimet = os.listdir()
for i in range(len(nimet)):
    nimet[i] = nimet[i][:-3]
nimet.remove("Prisoner")
print(nimet)

#Rakentaa oliot osallistujista
class Osallistuja:
    def __init__(self,name):
        self.name = name
        self.points = 0
        self.wins = 0
Osallistujat = []
for i in range(len(nimet)):
    Osallistujat.append(Osallistuja(nimet[i]))
    
Rounds = 200

## ----- Taistelu ----- ##
def Comparison(a, b): # 0 = kivi, 1 = paperi, 2 = Sakset
    if a == b:
        return [0,0]
    if a == 0 and b == 1:
        return [-1,1]
    if a == 0 and b == 2:
        return [1,-1]
    if a == 1 and b == 0:
        return [1,-1]
    if a == 1 and b == 2:
        return [-1,1]
    if a == 2 and b == 0:
        return [-1,1]
    if a == 2 and b == 1:
        return [1,-1]

A = ["Kivi","Paperi","Sakset"]
for i in range(len(A)):
    for k in range(len(A)):
        print(A[i],"vs",A[k],Comparison(i,k))

PrintRounds = False

MatchNmb = 0
#Jokainen jokaista vastaan kerran.
for l in range(5):
    for i in range(len(Osallistujat)): #Pelaaja A
        for k in range(i,len(Osallistujat)): #Pelaaja B
            if i != k: #Ei itseään vastaan
                MatchNmb += 1
                print("# -------------------- #")
                #Asettaa pelaajat muuttujiin
                A = __import__(Osallistujat[i].name)
                B = __import__(Osallistujat[k].name)
                print("Match:",MatchNmb, A.name, nimet[i],"vs",B.name,nimet[k])
                #Kierroksen aikaisemmat liikkeet.
                ActionsA = []
                ActionsB = []
                #Kierroksen pisteet.
                PointsA = 0
                PointsB = 0
                #Resetoidaan pelaajat ennen taistelua.
                A.Restart()
                B.Restart()
                RndNmb = 0 #Round number
                for j in range(Rounds):
                    RndNmb += 1
                    #Hakee liikkeet.
                    Adata = A.GetInt()
                    Bdata = B.GetInt()
                    #Tallentaa liikeet.
                    ActionsA.append(Adata)
                    ActionsB.append(Bdata)
                    #Taistelu.
                    RoundPoints = Comparison(Adata,Bdata)
                    #Lisää pisteet.
                    PointsA += RoundPoints[0]
                    PointsB += RoundPoints[1]
                    #Lähettää liikedatan.
                    A.SetData(ActionsA,ActionsB)
                    B.SetData(ActionsB,ActionsA)
                    if PrintRounds:
                        print("Round:", RndNmb, A.name,PointsA,B.name,PointsB)
                #Lisää lopulliset pisteet.
                Osallistujat[i].points += PointsA
                Osallistujat[k].points += PointsB
                #Lisää voittajan
                print("End of round", A.name,":",PointsA, B.name,":",PointsB)
                if PointsA > PointsB:
                    Osallistujat[i].wins += 1
                    print(A.name, nimet[i], "voitti!")
                if PointsA < PointsB:
                    Osallistujat[k].wins += 1
                    print(B.name, nimet[k], "voitti!")
                if PointsA == PointsB:
                    print("Tie!")

## ----- Lopputulostaulu ----- ##
print("## -------------------- Lopputulos -------------------- ##")
Osallistujat.sort(key=lambda x: x.points, reverse=True)
for i in range(len(Osallistujat)):
    print(Osallistujat[i].points, Osallistujat[i].name)  
    


