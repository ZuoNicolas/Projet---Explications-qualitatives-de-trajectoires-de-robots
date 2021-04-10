from enum import Enum

class Description(Enum):
    
    #Orientation
    NORD = 'nord'
    EST = 'est'
    SUD = 'sud'
    OUEST = 'ouest'
    
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
    
    #Explication Intersection
    BEAUCOUP_MOINS_SECURITE = 'le chemin est très peu sûr'
    MOINS_SECURITE = 'le chemin est un peu moins sûr'
    SECURITE = 'le chemin est aussi sûr'
    PLUS_SECURITE = 'le chemin est un peu plus sûr'
    BEAUCOUP_PLUS_SECURITE = 'le chemin est très sûr'
    
    BEAUCOUP_MOINS_RAPIDE = 'le chemin est très long'
    MOINS_RAPIDE = 'le chemin est un peu plus long'
    RAPIDE = 'le chemin est aussi court'
    PLUS_RAPIDE = 'le chemin est un peu plus court'
    BEAUCOU_PLUS_RAPIDE = 'le chemin est beaucoup plus court'
    
    #Objet 
    OBJECT = -60

