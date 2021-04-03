from enum import Enum

class Description(Enum):
    
    #Orientation
    NORD = -1
    EST = -2
    SUD = -3
    OUEST = -4
    
    #Action
    TOURNE = -5
    PASSE = -6
    AVANCE = -7
    
    #Precision Avancer
    JUSQU_A = -9
    
    #Description Avancer
    INTERSECTION = -10
    ARRIVER = -11
    
    #Precision Distance
    PEU = -12
    TRES = -13
    
    #Distance
    PROCHE = -15
    LOIN = -16
    
    #Direction Passe
    GAUCHE = -22
    DROITE = -23
    DEVANT = -24
    DERRIERE = -25
    ENTRE = -26
    
    #Direction Tourner
    A_GAUCHE = -30
    A_DROITE = -31
    _DERRIERE = -32
    
    #Objet 
    OBJECT = -60

