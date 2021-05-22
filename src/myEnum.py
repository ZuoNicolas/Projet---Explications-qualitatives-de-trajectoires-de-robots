from enum import Enum

# =============================================================================
# VERSION FRANCAIS ORIGINAL
# =============================================================================

class Description(Enum):
    """
    Description de nos phrases
    """
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
    INTERSECTION = 'l\'intersection :'
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
    
    MAIS = 'mais'
    ET = 'et'
    LES = 'les'
    DES = 'des'
    
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
    
    TOUT_EST_MOIN_BON = "moins bon en terme de distance, sécurité et point d'interêt"
    TOUT_EST_MOIN_BON_USER = 'j\'ai pris ce chemin, car c\'est un des chemins choisi par l\'utilisateur, mais le chemin choisis n\'est pas meilleur en tout point avec le chemin comparer'
    
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

# =============================================================================
# VERSION FRANCAIS + FAMILIAL + EMOTION + EMOTE
# =============================================================================

# class Description(Enum):
#     """
#     Description de nos phrases
#     """
#     #Orientation
#     NORD = 'nord'
#     EST = 'est'
#     SUD = 'sud'
#     OUEST = 'ouest'
    
#     #Action
#     TOURNE = 'je tourne'
#     PASSE = 'je passe'
#     AVANCE = 'j\'avance'
    
#     #Precision Avancer
#     JUSQU_A = 'jusqu\'à'
    
#     #Description Avancer
#     INTERSECTION = 'l\'intersection :'
#     ARRIVER = 'l\'arriver'
    
#     #Precision Distance
#     PEU = -12
#     TRES = -13
    
#     #Distance
#     PROCHE = -15
#     LOIN = -16
    
#     #Direction Passe
#     GAUCHE = 'à gauche'
#     DROITE = 'à droite'
#     DEVANT = 'devant'
#     DERRIERE = 'derrière'
#     ENTRE = 'entre'
#     COTE = 'à côté'
    
#     #Direction Tourner
#     A_GAUCHE = 'à gauche'
#     A_DROITE = 'à droite'
#     _DERRIERE = 'derrière'
    
#     MAIS = 'mais surtout'
#     ET = 'et'
#     LES = 'les'
#     DES = 'des'
    
#     #Explication Intersection
#     EXPLICATION = 'j\'ai pris ce chemin, car les autres chemins sont'
    
#     BEAUCOUP_MOINS_SECURITE = 'trop dangereux, j\'ai peur :('
#     MOINS_SECURITE = 'un peu dangereux, j\'ai un peu peur :('
#     SECURITE = 'pas spécialement plus dangereux :)'
#     PLUS_SECURITE = 'un peu plus sécuriser, mais j\'ai pas peur :p'
#     BEAUCOUP_PLUS_SECURITE = 'beaucoup plus sécuriser, mais j\'ai pas peur :D'
    
#     BEAUCOUP_MOINS_RAPIDE = 'trop long, je suis fatigué :('
#     MOINS_RAPIDE = 'un peu trop long, je suis un peu fatigué :('
#     RAPIDE = 'pas spécialement plus long :)'
#     PLUS_RAPIDE = 'un peu plus rapide, mais je suis pas fatigué :)'
#     BEAUCOUP_PLUS_RAPIDE = 'plus rapide, mais je suis pas fatigué :D'
    
#     BEAUCOUP_MOINS_PREFERE = 'trop peu d\'intérêt, j\'aime pas du tout :('
#     MOINS_PREFERE = 'peu d\'intérêt, j\'aime pas :('
#     PREFERE = 'pas spécialement plus intéressant :)'
#     PLUS_PREFERE = 'un peu plus d\intérêt, mais pas assez pour moi :)'
#     BEAUCOUP_PLUS_PREFERE = 'beaucoup plus d\intérêt, mais pas assez pour moi :D'
    
#     TOUT_EST_MOIN_BON = 'moins bon en terme de distance, sécurité et point d\'interêt, je le fait pour toi :\'('
#     TOUT_EST_MOIN_BON_USER = 'j\'ai pris ce chemin, car c\'est un des chemins que tu a choisi, mais le chemin choisis n\'est pas meilleur en tout point avec le(s) chemin(s) comparer, je le fait pour toi :\'('
    
#     # ratio sécurité > X
#     RATIO_BEAUCOUP_MOINS_SECURITE = 3
#     RATIO_MOINS_SECURITE = 1
#     RATIO_SECURITE = 1 # ratio sécurité == X
#     RATIO_PLUS_SECURITE = 0.4
    
#     # ratio radidité > X
#     RATIO_BEAUCOUP_MOINS_RAPIDE = 3
#     RATIO_MOINS_RAPIDE = 1
#     RATIO_RAPIDE = 1# ratio radidité == X
#     RATIO_PLUS_RAPIDE = 0.4 
    
#     # ratio préférence < X
#     RATIO_BEAUCOUP_MOINS_PREFERE = 0.4
#     RATIO_MOINS_PREFERE = 1
#     RATIO_PREFERE = 1# ratio préférence == X
#     RATIO_PLUS_PREFERE = 2 

#     MSG_NULL=''
    
#     #Objet 
#     OBJECT = 'Objet'
    
# =============================================================================
# VERSION ANGLAIS (NEED TO CHANGE OBJECT NAME TO ENGLISH ON THE XML FILE)
# =============================================================================
# class Description(Enum):
#     """
#     Description de nos phrases
#     """
#     #Orientation
#     NORD = 'north'
#     EST = 'east'
#     SUD = 'south'
#     OUEST = 'west'
    
#     #Action
#     TOURNE = 'I turn'
#     PASSE = 'I pass'
#     AVANCE = 'I move forward'
    
#     #Precision Avancer
#     JUSQU_A = 'to'
    
#     #Description Avancer
#     INTERSECTION = 'l\'intersection :'
#     ARRIVER = 'l\'arriver'
    
#     #Precision Distance
#     PEU = -12
#     TRES = -13
    
#     #Distance
#     PROCHE = -15
#     LOIN = -16
    
#     #Direction Passe
#     GAUCHE = 'to the left'
#     DROITE = 'to the right'
#     DEVANT = 'in front of'
#     DERRIERE = 'behind'
#     ENTRE = 'between'
#     COTE = 'by'
    
#     #Direction Tourner
#     A_GAUCHE = 'to the left'
#     A_DROITE = 'to the right'
#     _DERRIERE = 'behind'
    
#     MAIS = 'but'
#     ET = 'and'
#     LES = 'the'
#     DES = ''
    
#     #Explication Intersection
#     EXPLICATION = 'I took this path, because the other paths are'
    
#     BEAUCOUP_MOINS_SECURITE = 'very unsafe in terms of security'
#     MOINS_SECURITE = 'a little less safe in terms of security'
#     SECURITE = 'also safe in terms of security'
#     PLUS_SECURITE = 'a little safer in terms of security'
#     BEAUCOUP_PLUS_SECURITE = 'much safer in terms of security'
    
#     BEAUCOUP_MOINS_RAPIDE = 'very long in terms of distance'
#     MOINS_RAPIDE = 'a little longer in terms of distance'
#     RAPIDE = 'also short in distance'
#     PLUS_RAPIDE = 'a little shorter in terms of distance'
#     BEAUCOUP_PLUS_RAPIDE = 'much shorter in terms of distance'
    
#     BEAUCOUP_MOINS_PREFERE = 'very little to the user\'s taste'
#     MOINS_PREFERE = 'a little less to the taste of the user'
#     PREFERE = 'at the same level in terms of user interest'
#     PLUS_PREFERE = 'a little more to the taste of the user'
#     BEAUCOUP_PLUS_PREFERE = 'much more to the taste of the user'
    
#     TOUT_EST_MOIN_BON = "less good in terms of distance, safety and point of interest"
#     TOUT_EST_MOIN_BON_USER = 'I took this path, because it is one of the paths chosen by the user, but the chosen path is not better in all points with the path compare'
    
#     # ratio sécurité > X
#     RATIO_BEAUCOUP_MOINS_SECURITE = 3
#     RATIO_MOINS_SECURITE = 1
#     RATIO_SECURITE = 1 # ratio sécurité == X
#     RATIO_PLUS_SECURITE = 0.4
    
#     # ratio radidité > X
#     RATIO_BEAUCOUP_MOINS_RAPIDE = 3
#     RATIO_MOINS_RAPIDE = 1
#     RATIO_RAPIDE = 1# ratio radidité == X
#     RATIO_PLUS_RAPIDE = 0.4 
    
#     # ratio préférence < X
#     RATIO_BEAUCOUP_MOINS_PREFERE = 0.4
#     RATIO_MOINS_PREFERE = 1
#     RATIO_PREFERE = 1# ratio préférence == X
#     RATIO_PLUS_PREFERE = 2 

#     MSG_NULL=''
    
#     #Objet 
#     OBJECT = 'Object'
