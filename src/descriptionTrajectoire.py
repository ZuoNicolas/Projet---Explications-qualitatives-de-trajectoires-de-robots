# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 09:35:29 2021

@author: Nico
"""

import numpy as np

def descriptiontTrajectoire(map,path,label):
    
    desc = 'Initialisation :\n'

    map_local = local_map(map, path, label)
    
    #print(map_local)
    old = None
    n_case = 0
    old_res=''
    anti_spam=0
    nb_de_case_anti_spam=2
    
    for i in range(len(path)):
        if i == len(path)-1 :
            break
        desc += str(i)+" :"
        
        desc_temp = desc
        orientation = direction(path[i],path[i+1])

        if old == None:
            old=orientation

        if orientation != old:
            if n_case != 0:
                desc += msg_avance_de(n_case)
            n_case=0
            desc += msg_tourne(message_orientation(old, orientation))
            
        
        if map_local[i] != [] :
            if path[i] == map_local[i][0][1]:
                res = msg_passage_a(calcul_position_objet(orientation, map_local[i][0][1],map_local[i][0][2]),map_local[i][0][0])
                #print(i,res)
                if res != old_res:
                    if n_case != 0:
                        desc += msg_avance_de(n_case)
                    n_case=0
                    desc += res
                    old_res = res
                    anti_spam=0
                    
        n_case+=1

        
        old = orientation
        
        if desc == desc_temp:
            anti_spam+=1
            if anti_spam > nb_de_case_anti_spam:
                old_res=''
                
        desc +='\n'
                
    desc +=str(i)+" :"+msg_avance_de(n_case) + "et je suis arrivé à destination !"


    print(desc)


def local_map(map ,path ,label):
    
    path_area = [ [] for x in range(len(path)) ]

    for x in range(len(map)):
        for y in range(len(map[0])):
            temp = label.get(map[x][y]).get('vision_area')
            if  temp != None and int(temp) > 0 :
                for i in range(len(path)):
                    a,b = path[i]
                    rayon = (a - x)**2 + (b - y)**2
                    if rayon <= int(temp)**2 :
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
    x, y = point
    xo, yo = point_objet
    
    if d == 0:
        if y < yo :
            return "passe à gauche de"
        elif y > yo  :
            return "passe à droite de"
        else :
            return "vais vers"
    if d == 1:
        if x < xo :
            return "passe à gauche de"
        elif x > xo :
            return "passe à droite de"
        else :
            return "vais vers"
        
    if d == 2:#check
        if y > yo :
            return "passe à gauche de"
        elif y < yo :
            return "passe à droite de"
        else :
            return "vais vers"
    if d == 3:
        if x > xo :
            return "passe à gauche de"
        elif x < xo :
            return "passe à droite de"
        else :
            return "vais vers"
    
def message_orientation(old, now):
    
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
    return "/J'avance de "+ str(m) +" case "

def msg_tourne(m):
    return "/Je tourne à "+str(m)+" "
    
def msg_passage_a(m,o):
    return "/Je "+str(m)+" l'objet "+str(o)+" "