import numpy as np
import os
from sklearn.linear_model import LogisticRegression

# Luo logistinen regressiomalli
model = LogisticRegression()

name = "Dante Alighieri"

MyMoves = []
OpponentMoves = []

def TrainModel():
    global MyMoves, OpponentMoves
   
    # Muunna siirrot numpy-taulukoiksi
    X = np.array(MyMoves).reshape(-1, 1)
    y = np.array(OpponentMoves)

    # Kouluta malli
    model.fit(X, y)

def GetInt():
    global MyMoves, OpponentMoves
    # Kouluta malli, jos siirtoja on tarpeeksi
    if len(MyMoves) >= 10:
        TrainModel()

    # Analysoi vastustajan edelliset siirrot
    if len(OpponentMoves) > 0:
        last_move = OpponentMoves[-1]
        # Tee päätös vastustajan viimeisen siirron perusteella
        if last_move == 0:  # Vastustaja pelasi kiven
            return 1  # Pelaa paperi
        elif last_move == 1:  # Vastustaja pelasi paperin
            return 2  # Pelaa sakset
        elif last_move == 2:  # Vastustaja pelasi sakset
            return 0  # Pelaa kivi
    else:
        # Ei vastustajan siirtoja vielä, pelaa oletuksena kiveä
        return 2

def Restart():
    global MyMoves, OpponentMoves
    MyMoves = []
    OpponentMoves = []
    # Lisää mahdolliset lisäasetukset tähän.
    
    ## ----- ÄLÄ KOSKE ALUE ----- ##

# Älä muokkaa tai kutsu tätä funktiota.
def SetData(MyData,OpponentData):
    MyMoves = MyData
    OpponentMoves = OpponentData
