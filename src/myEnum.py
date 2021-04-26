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
    EXPLICATION = 'j\'ai pris ce chemin, car les autres chemins sont :'
    
    BEAUCOUP_MOINS_SECURITE = 'très peu sûr en terme de sécurité'
    MOINS_SECURITE = 'un peu moins sûr en terme de sécurité'
    SECURITE = 'aussi sûr en terme de sécurité'
    PLUS_SECURITE = 'un peu plus sûr en terme de sécurité'
    BEAUCOUP_PLUS_SECURITE = 'beaucoup plus sûr en terme de sécurité'
    
    BEAUCOUP_MOINS_RAPIDE = 'très long en terme de distance'
    MOINS_RAPIDE = 'un peu plus long en terme de distance'
    RAPIDE = 'aussi court en terme de distance'
    PLUS_RAPIDE = 'un peu plus court en terme de distance'
    BEAUCOUP_PLUS_RAPIDE = 'beaucoup plus court en terme de distance'
    
    BEAUCOUP_MOINS_PREFERE = 'la préférence n\'est pas du tout assez au goût de l\'utilisateur'
    MOINS_PREFERE = 'la préférence est un peu moins élevée au goût de l\'utilisateur'
    PREFERE = 'la préférence est à la même niveau'
    PLUS_PREFERE = 'la préférence est un peu plus élevée au goût de l\'utilisateur'
    BEAUCOUP_PLUS_PREFERE = 'la préférence est beaucoup plus élevée au goût de l\'utilisateur'
    
    #Objet 
    OBJECT = 'Objet'

