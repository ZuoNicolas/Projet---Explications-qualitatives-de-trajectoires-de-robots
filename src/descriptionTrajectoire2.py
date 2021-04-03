import numpy as np
import time
import myEnum

class DescriptionTrajectoire():

    def __init__(self,map,path,label):
            self.map = map
            self.path = path
            self.label = label
            self.description = []
            self.myEnum = myEnum.Description
            
    def descriptiontTrajectoireSimple(self, agent_rayon=None):
        """ list(list(int)) * list(int) * dict{int:dict{str:str}}
        Parcours le chemin path en regardant les objets au alentours,
        pour retourner la description contruite"""
        
        #Stockage de notre description
        #desc = 'Initialisation :\n'
    
        #créer une liste qui décris chaque case du path où les objets sont a porter d'intéraction de la case en question
        map_local = self.local_map(agent_rayon)
        print(map_local)
        
        old = None #Sauvegarde de l'ancienne orientation
        n_case = -1 #Compteur du nombre de case parcourus avant un événement
        old_res='' #Sauverade du dernier objet de passage pour évité le spam
        anti_spam=0 #Compteur du nombre d'itération du même événement de passage
        nb_de_case_anti_spam=2 #Nombre de case avant de pouvoir redécrire le même événement de passage
        
        #Parcours le chemin et contruit la description
        for i in range(len(self.path)):
            
            # n_case+=1 #incrémentation
            
            #Pour évité l'erreur de Out Of Bound, car on regarde notre case actuel et la case suivante,
            #pour savoir l'évolution du sens d'orientation actuel.
            if i == len(self.path)-1 :
                break
            
            #desc += str(i)+" :" #Etape de notre avancement

            description_temp = []
            orientation = self.direction(self.path[i],self.path[i+1]) #Calcul de l'orientation de notre agent en regardant sa case actuel et la case suivante
            
            description_temp.append(orientation)
            
            #Pour la première itération
            if old == None:
                old=orientation
                
            description_temp = description_temp + self.avancer_jusqu_a()
            sauvegarde = description_temp.copy()
    
            #Si l'orientation du case suivante est différente, alors on rajoute l'événement tourner
            if  old != orientation:
                #Pour évité les messages "j'avance de 0 case
                # if n_case != 0:
                #     desc += self.msg_avance_de(n_case)
            
                # n_case=0 #Remise à 0 du compteur après un événement
                description_temp.append(self.myEnum.INTERSECTION)
                description_temp += [self.myEnum.TOURNE, self.message_orientation(old, orientation) ]#Ajout du bon message en fonction des orientations
                
            #Si il y a un événement sur la case
            if map_local[i] != [] :
                
                #if path[i] == map_local[i][0][1]: #Pour vérifié si on est bien sur la case, inutile ici
                
                #Calcul du message de passage à coté de ...
                res = [self.calcul_position_objet(orientation, map_local[i][0][1],map_local[i][0][2]), map_local[i][0][0]]
    
                #Pour évité le spam quand on passe a coté d'un objet qui a un rayon d'interraction sur plusieur case
                if res != old_res:
                    
                    # if n_case != 0: #Pour évité les messages "j'avance de 0 case
                    #     desc += self.msg_avance_de(n_case)
                    
                    description_temp.append(self.myEnum.OBJECT)
                    description_temp += res
                    
                    #Mise à jour des variables
                    old_res = res
                    anti_spam=0
                        
            
            
            old = orientation
            
            if description_temp == sauvegarde: #Si il n'y a aucun changement on incrémente l'anti-spam
                description_temp = description_temp[:-1]
                anti_spam+=1
                if anti_spam > nb_de_case_anti_spam:
                    old_res=''
            
            self.description.append(description_temp)
        
        #Ajout du dernier événement
        description_temp = []
        description_temp.append(orientation)
        description_temp += self.avancer_jusqu_a() + [self.myEnum.ARRIVER]
        
        self.description.append(description_temp)
        
        print(self.description)
        
        return self.description
            
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
            return self.myEnum.SUD
        elif vect_x < 0 :
            return self.myEnum.NORD
        elif vect_x == 0:
            if vect_y > 0:
                return self.myEnum.EST
            elif vect_y < 0:
                return self.myEnum.OUEST
            
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
                return self.myEnum.GAUCHE
            elif y > yo  :
                return self.myEnum.DROITE
            elif x > xo :
                return self.myEnum.DEVANT
            else :
                return self.myEnum.DERRIERE
        if d == 1:
            if x < xo :
                return self.myEnum.GAUCHE
            elif x > xo :
                return self.myEnum.DROITE
            elif y < yo :
                return self.myEnum.DEVANT
            else :
                return self.myEnum.DERRIERE
            
        if d == 2:#check
            if y > yo :
                return self.myEnum.GAUCHE
            elif y < yo :
                return self.myEnum.DROITE
            elif x < xo :
                return self.myEnum.DEVANT
            else :
                return self.myEnum.DERRIERE
        if d == 3:
            if x > xo :
                return self.myEnum.GAUCHE
            elif x < xo :
                return self.myEnum.DROITE
            elif y > yo:
                return self.myEnum.DEVANT
            else :
                return self.myEnum.DERRIERE
        
    def message_orientation(self, old, now):
        """         0 : Nord
        3 : Ouest               1 : Est
                    2 : Sud
        Prend deux direction : {0,1,2,3}  et renvoie un String pour dire dans quel sens on a tourné depuis la dernière orientation
        """
        if old == self.myEnum.NORD:
            
            if now == self.myEnum.EST:
                return self.myEnum.DROITE
            
            if now == self.myEnum.SUD:
                return self.myEnum.DERRIERE
            
            if now == self.myEnum.OUEST:
                return self.myEnum.GAUCHE
            
        if old == self.myEnum.EST:
            
            if now == self.myEnum.SUD:
                return self.myEnum.DROITE
            
            if now == self.myEnum.OUEST:
                return self.myEnum.DERRIERE
            
            if now == self.myEnum.NORD:
                return self.myEnum.GAUCHE
            
        if old == self.myEnum.SUD:
            
            if now == self.myEnum.OUEST:
                return self.myEnum.DROITE
            
            if now == self.myEnum.NORD:
                return self.myEnum.DERRIERE
            
            if now == self.myEnum.EST:
                return self.myEnum.GAUCHE
            
        if old == self.myEnum.OUEST:
            
            if now == self.myEnum.NORD:
                return self.myEnum.DROITE
            
            if now == self.myEnum.EST:
                return self.myEnum.DERRIERE
            
            if now == self.myEnum.SUD:
                return self.myEnum.GAUCHE
        
    def avancer_jusqu_a(self):
        
        return [self.myEnum.AVANCE, self.myEnum.JUSQU_A]
        

