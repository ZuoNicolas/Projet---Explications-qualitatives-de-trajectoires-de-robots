# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 09:35:29 2021

@author: Nico
"""

import numpy as np
import time

class DescriptionTrajectoire():

    def __init__(self,map,path,label):
            self.map = map
            self.path = path
            self.label = label
            
    def descriptiontTrajectoireSimple(self, agent_rayon=None):
        """ list(list(int)) * list(int) * dict{int:dict{str:str}}
        Parcours le chemin path en regardant les objets au alentours,
        pour retourner la description contruite"""
        
        #Stockage de notre description
        desc = 'Initialisation :\n' 
    
        #créer une liste qui décris chaque case du path où les objets sont a porter d'intéraction de la case en question
        map_local = self.local_map(agent_rayon)
        print(map_local)
        
        old = None #Sauvegarde de l'ancienne orientation
        n_case = 0 #Compteur du nombre de case parcourus avant un événement
        old_res='' #Sauverade du dernier objet de passage pour évité le spam
        anti_spam=0 #Compteur du nombre d'itération du même événement de passage
        nb_de_case_anti_spam=2 #Nombre de case avant de pouvoir redécrire le même événement de passage
        
        #Parcours le chemin et contruit la description
        for i in range(len(self.path)):
            #Pour évité l'erreur de Out Of Bound, car on regarde notre case actuel et la case suivante,
            #pour savoir l'évolution du sens d'orientation actuel.
            if i == len(self.path)-1 :
                break
            
            desc += str(i)+" :" #Etape de notre avancement
            
            desc_temp = desc #Variable, pour savoir si notre description a évoluer ou non, si non on incrémente notre compteur d'anti-spam
            orientation = self.direction(self.path[i],self.path[i+1]) #Calcul de l'orientation de notre agent en regardant sa case actuel et la case suivante
            
            #Pour la première itération
            if old == None:
                old=orientation
    
            #Si l'orientation du case suivante est différente, alors on rajoute l'événement tourner
            if  old != orientation:
                #Pour évité les messages "j'avance de 0 case
                if n_case != 0:
                    desc += self.msg_avance_de(n_case)
            
                n_case=0 #Remise à 0 du compteur après un événement
                desc += self.msg_tourne(self.message_orientation(old, orientation)) #Ajout du bon message en fonction des orientations
                
            #Si il y a un événement sur la case
            if map_local[i] != [] :
                
                #if path[i] == map_local[i][0][1]: #Pour vérifié si on est bien sur la case, inutile ici
                
                #Calcul du message de passage à coté de ...
                res = self.msg_passage_a(self.calcul_position_objet(orientation, map_local[i][0][1],map_local[i][0][2]),map_local[i][0][0])
    
                #Pour évité le spam quand on passe a coté d'un objet qui a un rayon d'interraction sur plusieur case
                if res != old_res:
                    
                    if n_case != 0: #Pour évité les messages "j'avance de 0 case
                        desc += self.msg_avance_de(n_case)
                        
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
        desc +=str(i)+" :"+self.msg_avance_de(n_case) + "et je suis arrivé à destination !"
    
        print(desc)
        
        return desc
    
    def descriptiontTrajectoireActif(self, agent_rayon, saw=True, iterator=True):
        
        x = 0
        y = 0
        if iterator == None:
            t = len(self.path)
        else :
            t=1
        for i in range(t):
            if iterator == None :
                touch = input('Press enter to start/continue, q : for Quit\n')
            
                if touch == 'q' or touch =='Q':
                    break
            else:
                i = iterator
            
            msg=''
            if i == len(self.path)-1 :
                msg = 'Arrivé à destination !'
                break
            
            a,b = self.path[i]
            vision_area = []
            for xi in range(-agent_rayon, agent_rayon+1):
                for yi in range(-agent_rayon, agent_rayon+1):
                    x = xi + a
                    y = yi + b
                    if x > len(self.map)-1 or x < 0: 
                        continue
                    if y > len(self.map[0])-1 or y < 0: 
                        continue
                    
                    rayon = (a - x)**2 + (b - y)**2 #Formule de rayon au carré

                    if rayon <= int(agent_rayon)**2:
                        if self.label.get(self.map[x][y]).get('vision_area') != None :
                           vision_area.append((x,y,self.label.get(self.map[x][y]).get('name')))
                        else :
                            vision_area.append((x,y,None))
  
            for x, y, name in vision_area:
                if name != None : 
                     new_msg = self.msg_passage_a(self.calcul_position_objet( self.direction(self.path[i], self.path[i+1]) , (a,b), (x,y)), name)
                     
                     if name in msg :
                         continue

                     msg += new_msg
            
            if saw :
                self.affichageActif(i, vision_area, self.map.copy())
                if msg == '':
                    msg = 'Rien à signaler au alentour'
                    
                print('\n'+msg)
        
        if iterator == None : 
            print("\nArrivé à destination !")
            
        return msg
            
    def affichageActif(self,i,vision_area,map):
        print(i,":",vision_area)
            
        for o in vision_area:
            a1,b1, name=o
            map[a1][b1]=-1
            
        print('S = start    E = End     str = mur     chemin = *')
        for x in range(len(map)):
            print('[',end='')
            for y in range(len(map[x])):
                if map[x][y] == -1:
                    map[x][y] = self.map[x][y]
                    print(0,end='')
                elif not( self.label.get(self.map[x][y]).get('canPass') or 
                       self.label.get(self.map[x][y]).get('name') == 'start' or 
                       self.label.get(self.map[x][y]).get('name') == 'end' ):
                    print(self.label.get(self.map[x][y]).get('name')[0],end='')
                else:
                    b=True
                    for i,j in self.path:
                        if x == self.path[0][0] and y == self.path[0][1]:
                            print('S',end='')
                            b=False
                            break;
                        elif x == self.path[-1][0] and y == self.path[-1][1]:
                            print('E',end='')
                            b=False
                            break;
                        elif i==x and j==y:
                            print('*',end='')
                            b=False
                            break;
                    if b:
                        print(' ',end='')
                    
            print(']')
            
    def local_map(self, agent_rayon=None):
        """Retourne une liste de liste ou chaque indice correspond au case,*
        Chaque sous liste contient toute les événements entre les objets"""
        
        path_area = [ [] for x in range(len(self.path)) ]
        
        #Parcours de toute la map et on regarde le rayon d'action de chaque objet
        #Si l'objet est à porter d'une de nos case du path alors on le rajoute dans notre liste
        for x in range(len(self.map)):
            for y in range(len(self.map[0])):
                rayon_action = self.label.get(self.map[x][y]).get('vision_area') #Récupération du rayon d'action  
                
                if  rayon_action != None and int(rayon_action) > 0 : #Vérification de la présence d'un rayon
                    if  agent_rayon != None : #Vérification de la présence d'un rayon
                        #Parcours du path pour savoir si une de nos case est dans le rayon d'action de l'objet en question ou non
                        for i in range(len(self.path)): 
                            a,b = self.path[i]
                            rayon = (a - x)**2 + (b - y)**2 #Formule de rayon au carré
                            if rayon <= int(agent_rayon)**2 :
                                path_area[i].append((self.label.get(self.map[x][y]).get('name'),(a,b),(x,y)))
                                
                    else :
                        #Parcours du path pour savoir si une de nos case est dans le rayon d'action de l'objet en question ou non
                        for i in range(len(self.path)): 
                            a,b = self.path[i]
                            rayon = (a - x)**2 + (b - y)**2 #Formule de rayon au carré
                            if rayon <= int(rayon_action)**2 :
                                path_area[i].append((self.label.get(self.map[x][y]).get('name'),(a,b),(x,y)))
        
    
        return path_area
    
    def direction(self, case_present, case_suivante):
        """Calcul le sens de la direction et renvoie 0,1,2 ou 3, 
        mais ne marche, ici que pour deux case cote à cote"""
        vect_x = case_suivante[0] - case_present[0]
        vect_y = case_suivante[1] - case_present[1]
        
        if vect_x > 0 :
            return 2 
        elif vect_x < 0 :
            return 0 
        elif vect_x == 0:
            if vect_y > 0:
                return 1 
            elif vect_y < 0:
                return 3 
            else:
                print("Erreur dans le calcul de direction")
                return -1 #erreur
            
    def calcul_position_objet(self, d , point,point_objet):
        """         0 : Nord
        3 : Ouest               1 : Est
                    2 : Sud
        Prend la direction d : {0,1,2,3}
        et renvoie une phrase pour dire si depuis sont point actuel, 
        le point de l'objet est plutôt a droite, a gauche, devant ou derrire 
        (fonctionne meme sur deux points non cote a cote)
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
        
    def message_orientation(self, old, now):
        """         0 : Nord
        3 : Ouest               1 : Est
                    2 : Sud
        Prend deux direction : {0,1,2,3}  et renvoie un String pour dire dans quel sens on a tourné depuis la dernière orientation
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
        
    def msg_avance_de(self,m):
        return "/J'avance de "+ str(m) +" case(s) "
    
    def msg_tourne(self, m):
        return "/Je tourne à "+str(m)+" "
        
    def msg_passage_a(self, m,o):
        return "/Je "+str(m)+" l'objet "+str(o)+" "

