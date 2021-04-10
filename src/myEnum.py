from enum import Enum

class Description(Enum):
    
    #Orientation
    NORD = 'nord'
    EST = 'est'
    SUD = 'sud'
    OUEST = 'ouest'
    
    #Action
    TOURNE = 'je tourne'
    PASSE = 'je passe'
    AVANCE = 'j\'avance'
    
    #Precision Avancer
    JUSQU_A = 'jusqu\'à'
    
    #Description Avancer
    INTERSECTION = 'l\'intersection'
    ARRIVER = 'l\'arriver'
    
    #Precision Distance
    PEU = -12
    TRES = -13
    
    #Distance
    PROCHE = -15
    LOIN = -16
    
    #Direction Passe
    GAUCHE = 'à gauche'
    DROITE = 'à droite'
    DEVANT = 'devant'
    DERRIERE = 'derrière'
    ENTRE = 'entre'
    
    #Direction Tourner
    A_GAUCHE = 'à gauche'
    A_DROITE = 'à droite'
    _DERRIERE = 'derrière'
    
    #Explication Intersection
    EXPLICATION = 'j\'ai pris ce chemin, car les autres chemins sont'
    
    BEAUCOUP_MOINS_SECURITE = 'très peu sûr'
    MOINS_SECURITE = 'un peu moins sûr'
    SECURITE = 'aussi sûr'
    PLUS_SECURITE = 'un peu plus sûr'
    BEAUCOUP_PLUS_SECURITE = 'beaucoup plus sûr'
    
    BEAUCOUP_MOINS_RAPIDE = 'très long'
    MOINS_RAPIDE = 'un peu plus long'
    RAPIDE = 'aussi court'
    PLUS_RAPIDE = 'un peu plus court'
    BEAUCOUP_PLUS_RAPIDE = 'beaucoup plus court'
    
    #Objet 
    OBJECT = 'Objet'

