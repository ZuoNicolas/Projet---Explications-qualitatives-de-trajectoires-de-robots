# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 09:35:29 2021

@author: Nico
"""

import numpy as np

def descriptiontTrajectoire(map,path,label):
    """ list(list(int)) * list(int) * dict{int:dict{str:str}}
    Parcours le chemin path en regardant les objets au alentours,
    pour retourner la description contruite"""
    
    #Stockage de notre description
    desc = 'Initialisation :\n' 

    #créer une liste qui décris chaque case du path où les objets sont a porter d'intéraction de la case en question
    map_local = local_map(map, path, label)
    print(map_local)
    
    old = None #Sauvegarde de l'ancienne orientation
    n_case = 0 #Compteur du nombre de case parcourus avant un événement
    old_res='' #Sauverade du dernier objet de passage pour évité le spam
    anti_spam=0 #Compteur du nombre d'itération du même événement de passage
    nb_de_case_anti_spam=2 #Nombre de case avant de pouvoir redécrire le même événement de passage
    
    #Parcours le chemin et contruit la description
    for i in range(len(path)):
        #Pour évité l'erreur de Out Of Bound, car on regarde notre case actuel et la case suivante,
        #pour savoir l'évolution du sens d'orientation actuel.
        if i == len(path)-1 :
            break
        
        desc += str(i)+" :" #Etape de notre avancement
        
        desc_temp = desc #Variable, pour savoir si notre description a évoluer ou non, si non on incrémente notre compteur d'anti-spam
        orientation = direction(path[i],path[i+1]) #Calcul de l'orientation de notre agent en regardant sa case actuel et la case suivante
        
        #Pour la première itération
        if old == None:
            old=orientation

        #Si l'orientation du case suivante est différente, alors on rajoute l'événement tourner
        if  old != orientation:
            #Pour évité les messages "j'avance de 0 case
            if n_case != 0:
                desc += msg_avance_de(n_case)
        
            n_case=0 #Remise à 0 du compteur après un événement
            desc += msg_tourne(message_orientation(old, orientation)) #Ajout du bon message en fonction des orientations
            
        #Si il y a un événement sur la case
        if map_local[i] != [] :
            
            #if path[i] == map_local[i][0][1]: #Pour vérifié si on est bien sur la case, inutile ici
            
            #Calcul du message de passage à coté de ...
            res = msg_passage_a(calcul_position_objet(orientation, map_local[i][0][1],map_local[i][0][2]),map_local[i][0][0])

            #Pour évité le spam quand on passe a coté d'un objet qui a un rayon d'interraction sur plusieur case
            if res != old_res:
                
                if n_case != 0: #Pour évité les messages "j'avance de 0 case
                    desc += msg_avance_de(n_case)
                    
                #Mise à jour des variables
                n_case=0  
                desc += res
                old_res = res
                anti_spam=0
                    
        n_case+=1 #incrémentation
        
        old = orientation
        
        if desc == desc_temp: #Si il n'y a aucun changement on incrémente l'anti-spam
            anti_spam+=1
            if anti_spam > nb_de_case_anti_spam:
                old_res=''
                
        desc +='\n'
    
    #Ajout du dernier événement
    desc +=str(i)+" :"+msg_avance_de(n_case) + "et je suis arrivé à destination !"

    print(desc)
    
    return desc

def local_map(map ,path ,label):
    """Retourne une liste de liste ou chaque indice correspond au case,*
    Chaque sous liste contient toute les événements entre les objets"""
    
    path_area = [ [] for x in range(len(path)) ]
    
    #Parcours de toute la map et on regarde le rayon d'action de chaque objet
    #Si l'objet est à porter d'une de nos case du path alors on le rajoute dans notre liste
    for x in range(len(map)):
        for y in range(len(map[0])):
            rayon_action = label.get(map[x][y]).get('vision_area') #Récupération du rayon d'action
            
            if  rayon_action != None and int(rayon_action) > 0 : #Vérification de la présence d'un rayon
                #Parcours du path pour savoir si une de nos case est dans le rayon d'action de l'objet en question ou non
                for i in range(len(path)): 
                    a,b = path[i]
                    rayon = (a - x)**2 + (b - y)**2 #Formule de rayon au carré
                    if rayon <= int(rayon_action)**2 :
                        path_area[i].append((label.get(map[x][y]).get('name'),(a,b),(x,y)))


    return path_area

def direction(case_present, case_suivante):
    
    vect_x = case_suivante[0] - case_present[0]
    vect_y = case_suivante[1] - case_present[1]
    
    if vect_x > 0 :
        return 2 #Est
    elif vect_x < 0 :
        return 0 #Ouest
    elif vect_x == 0:
        if vect_y > 0:
            return 1 #Nord
        elif vect_y < 0:
            return 3 #Sud
        else:
            print("Erreur dans le calcul de direction")
            return -1 #erreur
        
def calcul_position_objet(d , point,point_objet):
    """         0 : Nord
    3 : Ouest               1 : Est
                2 : Sud
    """
    x, y = point
    xo, yo = point_objet
    
    if d == 0:
        if y < yo :
            return "passe à gauche de"
        elif y > yo  :
            return "passe à droite de"
        elif x > xo :
            return "vais vers"
        else :
            return "m'éloigne de"
    if d == 1:
        if x < xo :
            return "passe à gauche de"
        elif x > xo :
            return "passe à droite de"
        elif y < yo :
            return "vais vers"
        else :
            return "m'éloigne de"
        
    if d == 2:#check
        if y > yo :
            return "passe à gauche de"
        elif y < yo :
            return "passe à droite de"
        elif x < xo :
            return "vais vers"
        else :
            return "m'éloigne de"
    if d == 3:
        if x > xo :
            return "passe à gauche de"
        elif x < xo :
            return "passe à droite de"
        elif y > yo:
            return "vais vers"
        else :
            return "m'éloigne de"
    
def message_orientation(old, now):
    """         0 : Nord
    3 : Ouest               1 : Est
                2 : Sud
    """
    if old == 0:
        if now == 1:
            return "droite"
        if now == 2:
            return "derrière"
        if now == 3:
            return "gauche"
    if old == 1:
        if now == 2:
            return "droite"
        if now == 3:
            return "derrière"
        if now == 0:
            return "gauche"
    if old == 2:
        if now == 3:
            return "droite"
        if now == 0:
            return "derrière"
        if now == 1:
            return "gauche"
    if old == 3:
        if now == 0:
            return "droite"
        if now == 1:
            return "derrière"
        if now == 2:
            return "gauche"
    
def msg_avance_de(m):
    return "/J'avance de "+ str(m) +" case(s) "

def msg_tourne(m):
    return "/Je tourne à "+str(m)+" "
    
def msg_passage_a(m,o):
    return "/Je "+str(m)+" l'objet "+str(o)+" "

