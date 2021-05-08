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
    COTE = 'à côté'
    
    #Direction Tourner
    A_GAUCHE = 'à gauche'
    A_DROITE = 'à droite'
    _DERRIERE = 'derrière'
    
    #Explication Intersection
    EXPLICATION = 'j\'ai pris ce chemin, car les autres chemins sont'
    
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
    
    BEAUCOUP_MOINS_PREFERE = 'très peu au goût de l\'utilisateur'
    MOINS_PREFERE = 'un peu moins au goût de l\'utilisateur'
    PREFERE = 'à la même niveau en terme d\'interêt de l\'utilisateur'
    PLUS_PREFERE = 'un peu plus au goût de l\'utilisateur'
    BEAUCOUP_PLUS_PREFERE = 'beaucoup plus au goût de l\'utilisateur'
    
    # ratio sécurité > X
    RATIO_BEAUCOUP_MOINS_SECURITE = 3
    RATIO_MOINS_SECURITE = 1
    RATIO_SECURITE = 1 # ratio sécurité == X
    RATIO_PLUS_SECURITE = 0.4
    
    # ratio radidité > X
    RATIO_BEAUCOUP_MOINS_RAPIDE = 3
    RATIO_MOINS_RAPIDE = 1
    RATIO_RAPIDE = 1# ratio radidité == X
    RATIO_PLUS_RAPIDE = 0.4 
    
    # ratio préférence < X
    RATIO_BEAUCOUP_MOINS_PREFERE = 0.4
    RATIO_MOINS_PREFERE = 1
    RATIO_PREFERE = 1# ratio préférence == X
    RATIO_PLUS_PREFERE = 2 

    MSG_NULL=''
    
    #Objet 
    OBJECT = 'Objet'

